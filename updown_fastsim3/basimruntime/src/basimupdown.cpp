#include "basimupdown.h"
#include "debug.h"
#include "memorySegments.h"
#include "networkid.h"
#include "basim_stats.hh"
#include <cstddef>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <fcntl.h>
#include <ios>
#include <string>
#include <sys/mman.h>
#include <sys/types.h>
#include <utility>
#include <vector>
#include <omp.h>
#include <unistd.h>
#include "types.hh"
#include "lanetypes.hh"
#include "fstream"
#include "logging.hh"
#include "updown_config.h"
#include "util.hh"
#include "mmessage.hh"
#include "../../common/include/memorySegments.h"

namespace UpDown {

/*
  This is a hack as it is possible to have multiple instances of the runtime,
  but only one global logger is allowed. We need to know we are logging from
  which runtime instance.
*/
BASimUDRuntime_t *curRuntimeInstance = nullptr;

  /**
   * @brief Construct a new BASimUDRuntime_t object
   *
   * This constructor calls initMemoryArrays() to set the simulated memory
   * regions. Python will be disabled. Only simulating memory interactions.
   *
   */
BASimUDRuntime_t::BASimUDRuntime_t() : SimUDRuntime_t() {
    BASIM_INFOMSG("Initializing BASimulated Runtime with default params");
    BASIM_WARNING("No python program. Python will be disabled, only "
                   "simulating memory interactions");
    initialize(1);
}

  /**
   * @brief Construct a new BASimUDRuntime_t object
   *
   * This constructor calls initMemoryArrays() to set the simulated memory
   * regions. The pointers of ud_machine_t.MappedMemBase, ud_machine_t.UDbase
   * ud_machine_t.SPMemBase and ud_machine_t.ControlBase will be ignored and
   * overwritten in order to simulate the runtime.
   *
   * @param machineConfig Machine configuration
   */
BASimUDRuntime_t::BASimUDRuntime_t(ud_machine_t machineConfig)
      : SimUDRuntime_t(machineConfig){
    BASIM_INFOMSG("Initializing runtime with custom machineConfig");
    BASIM_WARNING("No python program. Python will be disabled, only "
                   "simulating memory interactions");
    BASIM_INFOMSG("Adding stats for %lu UDs", this->MachineConfig.NumUDs);
    
    initMPI();
    initialize(1);
  }

  /**
   * @brief Construct a new BASimUDRuntime_t object
   *
   * This constructor calls initMemoryArrays() to set the simulated memory
   * regions. The pointers of ud_machine_t.MappedMemBase, ud_machine_t.UDbase
   * ud_machine_t.SPMemBase and ud_machine_t.ControlBase will be ignored and
   * overwritten.
   *
   * @param machineConfig Machine configuration
   */
BASimUDRuntime_t::BASimUDRuntime_t(ud_machine_t machineConfig, std::string programFile,
                 std::string programName, basim::Addr pgbase, uint32_t numTicks)
      : SimUDRuntime_t(machineConfig, programFile, programName), NumTicks(numTicks)
        {
    BASIM_INFOMSG("Initializing runtime with custom machineConfig");
    BASIM_INFOMSG("Adding stats for %lu UDs", this->MachineConfig.NumUDs);
    BASIM_INFOMSG("Running file %s Program %s", programFile.c_str(),
                   programName.c_str());

    initMPI();
    initialize(1);
    initMachine(programFile, pgbase);
    init_stats();
    initOMP();
    initLogs(std::filesystem::path(programFile + ".rank" + std::to_string(this->getRank()) + ".logs").filename());
}


BASimUDRuntime_t::BASimUDRuntime_t(ud_machine_t machineConfig, std::string programFile,
                    basim::Addr pgbase, uint32_t numTicks, std::string log_subfolder_name) 
                    : SimUDRuntime_t(machineConfig, programFile), NumTicks(numTicks) {
    BASIM_INFOMSG("Initializing runtime with custom machineConfig");
    BASIM_INFOMSG("Adding stats for %lu UDs", this->MachineConfig.NumUDs);
    BASIM_INFOMSG("Running file %s Program %s", programFile.c_str(), programName.c_str());

    initMPI();
    initialize(1);
    initMachine(programFile, pgbase);
    init_stats();
    initOMP();
    initLogs(std::filesystem::path(programFile + ".rank" + std::to_string(this->getRank()) + ".logs").filename() / std::filesystem::path(log_subfolder_name));
}

void BASimUDRuntime_t::initialize(uint64_t topPerNode) {
    this->MachineConfig.CapControlPerLane = 0;
    SimUDRuntime_t::initialize();
    SimUDRuntime_t::initMemoryArrays(this->getRank(), this->getMPIProcesses());

    for (uint64_t i = 0; i < this->nodesPerRuntime * this->MachineConfig.NumUDs * this->MachineConfig.NumStacks; i++) {
        std::vector<struct BASimStats> v(this->MachineConfig.NumLanes);
        this->simStats.push_back(v);
    }

    // initialize across node traces    
    for(uint64_t i=0; i<this->nodesPerRuntime; ++i) {
        struct BASimNodeStats stats;
        stats.initialize(this->MachineConfig.NumNodes);
        this->simNodeStats.push_back(stats);
    }
    

    pthread_mutex_init(&mutex, nullptr);
    pthread_mutex_init(&top_lock, nullptr);
    pthread_cond_init(&condStart, nullptr);
    pthread_cond_init(&condTest, nullptr);
    #ifdef ASST_FASTSIM
      sem_init(&semStart, 0, 0);
      set_status(0);
    #endif
    
    python_enabled = false;
    this->topPerNode = topPerNode;
    set_barrier_times(this->nodesPerRuntime * this->topPerNode);
    
    this->startTime = std::chrono::high_resolution_clock::now();
    UpDown::curRuntimeInstance = this;
    
    pthread_mutex_init(&map_lock, nullptr);
    thread_num.store(0, std::memory_order_release);
    test_nwid = new networkid_t[this->topPerNode];
    test_offset = new uint32_t[this->topPerNode];
    test_expected = new word_t[this->topPerNode];
    
    #ifdef ASST_FASTSIM
        semSync = new sem_t[this->topPerNode];
        for(int i=0; i<this->topPerNode; i++)
            sem_init(&semSync[i], 0, 0);
        semTest = new sem_t[this->topPerNode];
        for(int i=0; i<this->topPerNode; i++)
            sem_init(&semTest[i], 0, 0);
        test_addr_flag = new int[this->topPerNode];
        for(int i=0; i<this->topPerNode; i++)
            test_addr_flag[i]=0;
    #endif
}

void BASimUDRuntime_t::extractSymbols(std::string progfile){
  std::ifstream instream(progfile.c_str(), std::ifstream::binary);
  uint64_t startofEventSymbols;
  uint32_t numEventSymbols, label, labelAddr;
  BASIM_ERROR_IF(!instream, "Could not load the binary: %s\n", progfile.c_str());

  instream.seekg(0, instream.end); 
  int length = instream.tellg();
  BASIM_INFOMSG("Program Size: %d Bytes", length);
  instream.seekg(0, instream.beg);
  instream.read(reinterpret_cast<char *>(&startofEventSymbols), sizeof(startofEventSymbols));
  instream.seekg(startofEventSymbols, instream.beg);
  instream.read(reinterpret_cast<char *>(&numEventSymbols), sizeof(numEventSymbols));
  BASIM_INFOMSG("Extracting %d EventLabels:Addresses from %s", numEventSymbols, progfile.c_str());
  for(auto i = 0; i < numEventSymbols; i++){
    instream.read(reinterpret_cast<char *>(&label), sizeof(label));
    instream.read(reinterpret_cast<char *>(&labelAddr), sizeof(labelAddr));
    symbolMap[label] = labelAddr; 
    //BASIM_INFOMSG("%d:%d", label, labelAddr);
  }
  instream.seekg(0, instream.beg);
}

void BASimUDRuntime_t::initMachine(std::string progfile, basim::Addr _pgbase){
  this->globalTick = 0;
  this->simTicks = 0;
  this->udsPerRuntime = this->MachineConfig.NumStacks * this->MachineConfig.NumUDs * this->nodesPerRuntime;
  this->uds.reserve(this->udsPerRuntime);
  network_output_limit = NumTicks * this->MachineConfig.InterNodeBandwidth / 2; // 2 is because of 2GHz

  // Create the default private segment, i.e., the entire memory mapped region
  private_segment_t default_segment(this->MachineConfig.MapMemBase, 
    this->MachineConfig.MapMemBase + this->MachineConfig.MapMemSize, this->MachineConfig.MapMemBase, 0b11);

  extractSymbols(progfile);

  this->uds.resize(this->udsPerRuntime);
  this->udMems.resize(this->nodesPerRuntime);
  
  #pragma omp parallel for
  for(uint64_t node=0; node<this->nodesPerRuntime; ++node) {
    basim::UDMemoryPtr udmptr = new basim::UDMemory(node, this->MachineConfig.NumStacks, this->MachineConfig.MemLatency, this->MachineConfig.MemBandwidth, this->MachineConfig.InterNodeLatency);
    udMems[node] = udmptr;

    uint32_t currentGlobalNodeID = this->nodesPerRuntime * this->getRank() + node;
    for (uint32_t stack = 0; stack < this->MachineConfig.NumStacks; stack++) {
      for (uint32_t udid = 0; udid < this->MachineConfig.NumUDs; udid++) {

        uint32_t nwid = ((currentGlobalNodeID << 11) & 0x07FFF800) | ((stack << 8) & 0x00000700) |
                  ((udid << 6) & 0x000000C0);

        basim::UDAcceleratorPtr udptr = new basim::UDAccelerator(MachineConfig.NumLanes, nwid, MachineConfig.LocalMemAddrMode, MachineConfig.InterNodeLatency);
        basim::Addr spBase = this->MachineConfig.SPMemBase + ((node * this->MachineConfig.NumStacks + stack) * this->MachineConfig.NumUDs + udid) * this->MachineConfig.NumLanes * this->MachineConfig.SPBankSize;
         
        udptr->initSetup(_pgbase, progfile, spBase, this->udsPerRuntime);
        
        // Add the translation for the default private local segment to the UpDown's translation memory
        udptr->insertLocalTrans(default_segment);

        int index = node * this->MachineConfig.NumStacks * this->MachineConfig.NumUDs + stack * this->MachineConfig.NumUDs + udid;
        this->uds[index] = udptr;
        UPDOWN_INFOMSG("Creating UpDown: Node: %ld, Stack: %d, UD: %d, nwid: %d, SPBase: 0x%lx\n", 
        currentGlobalNodeID, stack, udid, nwid, spBase);
      }
    }
  }

  
  // Get UPDOWN_SIM_ITERATIONS from env variable
  if (char *EnvStr = getenv("UPDOWN_SIM_ITERATIONS"))
    max_sim_iterations = std::stoi(EnvStr);
  UPDOWN_INFOMSG("Running with UPDOWN_SIM_ITERATIONS = %ld", max_sim_iterations);

}

void BASimUDRuntime_t::initOMP() {
  #ifndef GEM5_MODE
    int numThreads;
    int totalCores = sysconf(_SC_NPROCESSORS_ONLN);//omp_get_num_procs();
    int hardwareThreads = totalCores / this->getMPIProcessesPerHost();
    
    // A set environment variable always takes precedence
    if(!getenv("OMP_NUM_THREADS")) {
      numThreads = int(hardwareThreads < this->udsPerRuntime ? hardwareThreads : this->udsPerRuntime);
    } else {
      numThreads = std::atoi(getenv("OMP_NUM_THREADS"));
    }

    if(numThreads > this->udsPerRuntime) {
        numThreads = this->udsPerRuntime;
    }
    
    // enables or disables dynamic adjustment of the number of threads available for the execution of subsequent parallel regions
    omp_set_dynamic(0);
    omp_set_num_threads(numThreads);
    const int numMaxThreads = omp_get_max_threads();

    printf("OMP scheduler: Cores available: %d, Threads per MPI Process available: %d, running %d threads in parallel for %lu UDs, OMP reports maxThreads: %d\n",
              totalCores, hardwareThreads, numThreads, this->udsPerRuntime, numMaxThreads);
    
    if(!getenv("OMP_SCHEDULE")) {
      omp_set_schedule(omp_sched_static, 1);
    }
    omp_sched_t kind;
    int chunk_size;
    omp_get_schedule(&kind, &chunk_size);
    std::string kindStr;

    switch(kind) {
      case omp_sched_static:
        kindStr = "static";
        break;
      case omp_sched_dynamic:
        kindStr = "dynamic";
        break;
      case omp_sched_guided:
        kindStr = "guided";
        break;
      case omp_sched_auto:
        kindStr = "auto";
        break;
      default:
        kindStr = "other (implementation specific)";
        break;
    }
    UPDOWN_INFOMSG("OMP scheduler: %s, chunk size: %d", kindStr.c_str(), chunk_size);

    // initializing the conveyor
    uint32_t size = this->getMPIProcesses();
    for(int t=0; t<omp_get_max_threads(); ++t) {
        std::vector<std::vector<char>, AlignedAllocator<std::vector<char>>> vecPerThread;
        for(uint32_t i=0; i<size; i++) {
            vecPerThread.emplace_back();
        }
        this->conveyor_thread.emplace_back(std::move(vecPerThread));
    }
  #endif
}

void BASimUDRuntime_t::initMPI() {
  #ifndef GEM5_MODE

    MPI_Init(nullptr, nullptr);
    this->mpiRank = -1;
    this->numMpiRanks = -1;
    uint32_t rank = this->getRank();
    uint32_t size = this->getMPIProcesses();

    BASIM_ERROR_IF(this->MachineConfig.NumNodes % size != 0, "The number of nodes cannot be equally distributed among the MPI ranks. Num Nodes: %ld, MPI size: %d", this->MachineConfig.NumNodes, size);

    // distribute the UD nodes among the MPI processors
    this->nodesPerRuntime = this->MachineConfig.NumNodes / size;

    char processor_name[MPI_MAX_PROCESSOR_NAME];
    int name_len;
    MPI_Get_processor_name(processor_name, &name_len);
    BASIM_INFOMSG("MPI: Launching on %s, rank: %d/%d, handling UD nodes %d - %d", processor_name, rank, size, this->getMinNodeID(), this->getMaxNodeID());

    currentBufferSizeRecv = 0;
    mpibufferAllMessagesRecv = nullptr;
  #endif
}

void BASimUDRuntime_t::startMainLoop() {
    auto nwid = networkid_t(0, 0, 0, this->getMinNodeID());
    uint64_t data[MPI_ADMIN_PACKET_SIZE];
    const uint32_t myRank = this->getRank();
    MPI_Status status;

    // only rank 0 can start the simulation
    // TODO maybe that should be fixed later
    while(myRank != 0) {    // always true or always false for the ranks
        MPI_Recv(&data, MPI_ADMIN_PACKET_SIZE, MPI_UINT64_T, MPI_ANY_SOURCE, MPI_ANY_TAG, MPI_COMM_WORLD, &status);

        if(status.MPI_TAG == MPI_START_SIM) {
            printf("Received BC: starting SIM\n"); fflush(stdout);
            this->simLoop(nwid);
        } else if(status.MPI_TAG == MPI_EXIT_RT) {
            printf("Received BC: exiting RT\n"); fflush(stdout);
              break;
        } else if(status.MPI_TAG == MPI_TAG_PRINT_STATS) {
            printf("Received BC: print stats\n"); fflush(stdout);
            this->print_stats();
        } else if(status.MPI_TAG == MPI_TAG_PRINT_NODE_STATS) {
            printf("Received BC: print node stats\n"); fflush(stdout);
            this->print_node_stats();
        } else if(status.MPI_TAG == MPI_TAG_RESET_STATS) {
            printf("Received BC: reset stats\n"); fflush(stdout);
            this->reset_stats();
        } else if(status.MPI_TAG == MPI_TAG_RESET_NODE_STATS) {
            printf("Received BC: reset node stats\n"); fflush(stdout);
            this->reset_node_stats();
        } else if(status.MPI_TAG == MPI_TAG_RESET_CURR_CYCLE) {
            printf("Received BC: reset curr cycle\n"); fflush(stdout);
            this->reset_curr_cycle();
        } else if(status.MPI_TAG == MPI_TAG_T2DRAM) {
            // printf("Received BC: Preparing to receive DRAM packet\n"); fflush(stdout);
            common_addr dataSA = this->mapPA2SA(data[1], true);
            MPI_Recv(reinterpret_cast<char *>(dataSA.addr), data[0], MPI_CHAR, status.MPI_SOURCE, MPI_TAG_T2DRAM_DATA, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
            // printf("Received t2DRAM message: dataPA: 0x%lx, dataSA: 0x%lx, size: %d\n", data[1], dataSA.addr, data[0]); fflush(stdout);
        } else if(status.MPI_TAG == MPI_TAG_DRAM2T) {
            // printf("Received BC: Preparing to send DRAM packet\n"); fflush(stdout);
            common_addr dataSA = this->mapPA2SA(data[1], true);
            MPI_Send(reinterpret_cast<char *>(dataSA.addr), data[0], MPI_CHAR, 0, MPI_TAG_DRAM2T_DATA, MPI_COMM_WORLD);
        } else if(status.MPI_TAG == MPI_TAG_DB_WRITE_STATS) {
            char *label = new char[data[0]];
            MPI_Recv(label, data[0], MPI_CHAR, status.MPI_SOURCE, MPI_TAG_DB_WRITE_STATS_DATA, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
            printf("Received BC: db_write_stats: %s\n", label); fflush(stdout);
            this->db_write_stats(label);
            delete label;
        } else if(status.MPI_TAG == MPI_TAG_DB_EVENT_STATS) {
            char *label = new char[data[0]];
            MPI_Recv(label, data[0], MPI_CHAR, status.MPI_SOURCE, MPI_TAG_DB_EVENT_STATS_DATA, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
            printf("Received BC: db_write_event_stats: %s\n", label); fflush(stdout);
            this->db_write_event_stats(label);
            delete label;
        } else if(status.MPI_TAG == MPI_TAG_DB_NODE_STATS) {
            char *label = new char[data[0]];
            MPI_Recv(label, data[0], MPI_CHAR, status.MPI_SOURCE, MPI_TAG_DB_NODE_STATS_DATA, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
            printf("Received BC: db_write_node_stats: %s\n", label); fflush(stdout);
            this->db_write_node_stats(label);
            delete label;
        } else {
            BASIM_ERROR("Unknown MPI Message Tag: %d", status.MPI_TAG);
        }
    }
}

void BASimUDRuntime_t::terminateMainLoop() {
    if(this->getRank() == 0) {
        for(uint32_t rank=1; rank<this->getMPIProcesses(); ++rank) {
            MPI_Send(nullptr, 0, MPI_UINT64_T, rank, MPI_EXIT_RT, MPI_COMM_WORLD);
        }
    }
}

uint32_t BASimUDRuntime_t::getRank() {
    if(this->mpiRank == -1) {
        int rank;
        MPI_Comm_rank(MPI_COMM_WORLD, &rank);
        this->mpiRank = (uint32_t)rank;
    }
    return this->mpiRank;
}

uint32_t BASimUDRuntime_t::getMPIProcesses() {
    if(this->numMpiRanks == -1) {
        int size;
        MPI_Comm_size(MPI_COMM_WORLD, &size);
        this->numMpiRanks = (uint32_t)size;
    }
    return this->numMpiRanks;
}

uint32_t BASimUDRuntime_t::getMPIProcessesPerHost() {
    int local_comm_size;
    MPI_Comm local_comm;
    MPI_Comm_split_type(MPI_COMM_WORLD, MPI_COMM_TYPE_SHARED, 0, MPI_INFO_NULL, &local_comm);
    MPI_Comm_size(local_comm, &local_comm_size);
    MPI_Comm_free(&local_comm);
    return (uint32_t)local_comm_size;
}

uint32_t BASimUDRuntime_t::getMinNodeID() {
    uint32_t rank = this->getRank();
    return this->nodesPerRuntime*rank;
}

uint32_t BASimUDRuntime_t::getMaxNodeID() {
    uint32_t rank = this->getRank();
    return this->nodesPerRuntime*(rank+1)-1;
}

bool BASimUDRuntime_t::isRemoteNodeMPI(uint32_t otherNodeID) {
  return otherNodeID < this->getMinNodeID() || otherNodeID > this->getMaxNodeID();
}

void BASimUDRuntime_t::sendMPIData(void *data, size_t size, int sourceRank) {
    MPI_Bcast(data, size, MPI_BYTE, sourceRank, MPI_COMM_WORLD);
}

void BASimUDRuntime_t::receiveMPIData(void *data, size_t size, int sourceRank) {
    MPI_Bcast(data, size, MPI_BYTE, sourceRank, MPI_COMM_WORLD);
}

static void writeUpdownBasimPerflog(uint32_t network_id, uint32_t thread_id, // IDs
                             uint32_t event_label,     // event
                             uint32_t inc_exec_cycles, // incremental exec cycles
                             uint64_t total_exec_cycles, // total exec cycles
                             uint32_t msg_id, std::string &msg_str // message
) {
  uint64_t final_tick = UpDown::curRuntimeInstance->getCurTick();
  uint64_t sim_ticks = final_tick;
  double sim_sec = 0.0;
  double host_sec = std::chrono::duration<double>(std::chrono::high_resolution_clock::now() - UpDown::curRuntimeInstance->getStartTime()).count();
  uint64_t lane_exec_ticks = total_exec_cycles;

  basim::globalLogs.perflog.writeUpdown(host_sec, final_tick, sim_ticks, sim_sec, network_id, thread_id, event_label,
               lane_exec_ticks, msg_id, msg_str);
}

static void writeBasimTracelog(uint32_t inc_exec_cycles,  // incremental exec cycles
                               std::string &msg_type_str, // type of message
                               std::string &msg_str       // message
) {
  uint64_t final_tick = UpDown::curRuntimeInstance->getCurTick();
  uint64_t sim_ticks = final_tick;

  basim::globalLogs.tracelog.write(sim_ticks, msg_type_str, msg_str);
}

void BASimUDRuntime_t::initLogs(std::filesystem::path log_folder_path) {
  if (!std::filesystem::exists(log_folder_path)) {
    if (std::filesystem::create_directories(log_folder_path)) {
      UPDOWN_INFOMSG("CREATED LOG FOLDER: %s\n", log_folder_path.c_str());
    } else {
      UPDOWN_ERROR("COULD NOT CREATE LOG FOLDER: %s\n", log_folder_path.c_str());
    }
  } else {
    UPDOWN_INFOMSG("EXISTING LOG FOLDER: %s\n", log_folder_path.c_str());
  }

  // open perflog
  basim::globalLogs.perflog.open(log_folder_path / "perflog.tsv");
  basim::globalLogs.perflog.registerPerflogCallback(writeUpdownBasimPerflog);
  // open tracelog
  basim::globalLogs.tracelog.open(log_folder_path / "tracelog.log");
  basim::globalLogs.tracelog.registerTracelogCallback(writeBasimTracelog);

#if defined (ENABLE_SQLITE)
  char *errMsg = 0;
  std::remove((log_folder_path / "stats.db").c_str());
  auto rc = sqlite3_open((log_folder_path / "stats.db").c_str(), &(this->stats_db));
  BASIM_ERROR_IF(rc, "Cannot open database: %s", sqlite3_errmsg(this->stats_db));

  rc = sqlite3_exec(this->stats_db, "PRAGMA journal_mode=WAL;", 0, 0, &errMsg);
  if (rc != SQLITE_OK) {
    std::string error = errMsg;
    sqlite3_free(errMsg);
    BASIM_ERROR("Failed to enable WAL mode: %s", error.c_str());
  }
  std::cout << "SQLite3 thread safety: " << (sqlite3_threadsafe() == 1 ? "ENABLED" : "DISABLED") << std::endl;
#endif
}

void BASimUDRuntime_t::send_event(event_t ev) {

  auto netid = ev.get_NetworkId();
  uint32_t udid = this->get_globalUDNum(netid);

  // Update the label with the actual event label resolved address
  ev.set_EventLabel(symbolMap[ev.get_EventLabel()]);

  basim::eventword_t basimev = basim::EventWord(ev.get_EventWord());
  basim::operands_t op(ev.get_NumOperands(), basim::EventWord(ev.get_OperandsData()[0]));  // num operands + cont
  op.setData(&ev.get_OperandsData()[1]);
  basim::eventoperands_t eops(&basimev, &op);
  sendEventOperands(udid, &eops, (ev.get_NetworkId()).get_LaneId());
}

uint32_t BASimUDRuntime_t::getNodeIdx(basim::networkid_t nid) {
  uint64_t total_uds = this->MachineConfig.NumUDs * this->MachineConfig.NumStacks;
  return std::ceil(nid.getNodeID()*32.0/total_uds);
}

uint32_t BASimUDRuntime_t::getUDIdx(basim::networkid_t nid){
  uint32_t relNodeID = this->get_node_offset(nid.getNodeID());
  return relNodeID * this->MachineConfig.NumStacks * this->MachineConfig.NumUDs +
         nid.getStackID() * this->MachineConfig.NumUDs + 
         nid.getUDID();
}

uint32_t BASimUDRuntime_t::getUDIdxForAddr(basim::networkid_t nid, basim::Addr addr, bool isGlobal) {
  uint32_t random_number = std::rand() % this->MachineConfig.NumUDs;
  uint32_t node_id = isGlobal ? mapPA2SA(addr, isGlobal).node_id : this->get_node_offset(nid.getNodeID());
  uint32_t stack_id = getMemoryMessageTargetStackID(addr, isGlobal);
  return node_id * (this->MachineConfig.NumStacks * this->MachineConfig.NumUDs) +
         stack_id * (this->MachineConfig.NumUDs) + random_number;
}

uint32_t BASimUDRuntime_t::getMemoryMessageTargetStackID(uint64_t addr, bool isGlobal) {
    return (addr / this->MachineConfig.MemISegBlockSize) % this->MachineConfig.NumStacks;
}

#ifdef GEM5_MODE
  void BASimUDRuntime_t::postSimulate(uint32_t udid, uint32_t laneID) {
      // Cycle through the send buffers of each lane in the UDs
      while(uds[udid]->sendReady(laneID)){
          std::unique_ptr<basim::MMessage> m = uds[udid]->getSendMessage(laneID);
          switch(m->getType()){
              case basim::MType::M1Type:{
                    processMessageM1(std::move(m));
                    break;
              }
              case basim::MType::M2Type:{
                    processLoadStore(m.get());
                    processMessageM2(std::move(m), udid);
                    break;
              }
              case basim::MType::M3Type:{
                    processMessageM3(std::move(m));
                    break;
              }
              case basim::MType::M3Type_M:{
                    // Always a store (2 words)    
                    processLoadStore(m.get());
                    processMessageM3M(std::move(m));
                    break;
              }
              case basim::MType::M4Type:{
                    processMessageM4(std::move(m));
                    break;
              }
              case basim::MType::M4Type_M:{
                    // Always a store (2 words)
                    processLoadStore(m.get());
                    processMessageM4M(std::move(m));
                    break;
              }
              default:{
                    BASIM_ERROR("Undefined Message type in Send Buffer");
                    break;
              }
          }
      }
  }

#else // FASTSIM
    void BASimUDRuntime_t::postSimulate(uint32_t udid, uint32_t laneID) {
        // Cycle through the send buffers of each lane in the UDs
        while(uds[udid]->sendReady(laneID)){
            std::unique_ptr<basim::MMessage> m = uds[udid]->getSendMessage(laneID);

            // compute the global node ID
            uint32_t node_offset_mpi_rank = udid / (this->MachineConfig.NumUDs * this->MachineConfig.NumStacks);
            uint32_t srcNodeID = this->getRank() * this->nodesPerRuntime + node_offset_mpi_rank;
            common_addr destNodeID;
            switch(m->getType()){
                case basim::MType::M1Type:{
                    destNodeID.node_id = m->getXe().getNWID().getNodeID();
                    if(destNodeID.node_id != srcNodeID) {
                        #if defined(FASTSIM_NETWORK_TRACE)
                            basim::globalLogs.tracelog.write(UpDown::curRuntimeInstance->getCurTick(), "NETWORK_SEND_MSG",
                                "<NODE2NODE, " +
                                std::to_string(srcNodeID) +" -> " +
                                std::to_string(destNodeID.node_id) +", " +
                                std::to_string((m->getLen()+2) * WORDSIZE) + "B>"
                            );
                        #endif

                        #ifdef DETAIL_STATS
                            basim::LaneStats* loc_stats = uds[udid]->getLaneStats(laneID);
                            loc_stats->tran_count_other_node++;
                            loc_stats->tran_bytes_other_node += (m->getLen()+2) * WORDSIZE;

                            // Node to node statistics
                            (this->simNodeStats[node_offset_mpi_rank].tran_bytes_other_node[destNodeID.node_id])->fetch_add((m->getLen()+2) * WORDSIZE);
                            (this->simNodeStats[node_offset_mpi_rank].tran_count_other_node[destNodeID.node_id])->fetch_add(1);
                        #endif

                        uds[udid]->pushDelayedMessage(std::move(m));
                    } else {
                        processMessageM1(std::move(m));
                    }
                    break;
                }
                case basim::MType::M2Type:{
                    // Writes to memory
                    basim::Addr pAddr = m->getdestaddr();
                    destNodeID = mapPA2SA(pAddr, m->getIsGlobal());
                    if(!m->getIsGlobal()) {
                        destNodeID.node_id = srcNodeID;
                        destNodeID.node_offset = this->get_node_offset(srcNodeID);
                    }
                    if(destNodeID.node_id != srcNodeID) {
                        if(m->isStore()){
                            #if defined(FASTSIM_NETWORK_TRACE)
                                basim::globalLogs.tracelog.write(UpDown::curRuntimeInstance->getCurTick(), "NETWORK_SEND_MSG",
                                    "<NODE2DRAM_ST, " +
                                    std::to_string(srcNodeId) +" -> " +
                                    std::to_string(destNodeID.node_id) +", " +
                                    std::to_string((m->getLen()+2) * WORDSIZE) + "B>"
                                );
                            #endif
                            
                            #ifdef DETAIL_STATS
                                basim::LaneStats* loc_stats = uds[udid]->getLaneStats(laneID);
                                loc_stats->dram_store_count_other_node++;
                                loc_stats->dram_store_bytes_other_node += (m->getLen()+2) * WORDSIZE;

                                // Node to node statistics
                                this->simNodeStats[node_offset_mpi_rank].dram_store_bytes_other_node[destNodeID.node_id]->fetch_add((m->getLen()+2) * WORDSIZE);
                                this->simNodeStats[node_offset_mpi_rank].dram_store_count_other_node[destNodeID.node_id]->fetch_add(1);
                            #endif
                        } else {
                            #if defined(FASTSIM_NETWORK_TRACE)
                                basim::globalLogs.tracelog.write(UpDown::curRuntimeInstance->getCurTick(), "NETWORK_SEND_MSG",
                                    "<NODE2DRAM_LD, " +
                                    std::to_string(srcNodeID) +" -> " +
                                   std::to_string(destNodeID.node_id) +", " +
                                   std::to_string(2 * WORDSIZE) + "B>"
                                );
                            #endif

                            #ifdef DETAIL_STATS
                                basim::LaneStats* loc_stats = uds[udid]->getLaneStats(laneID);
                                loc_stats->dram_load_count_other_node++;
                                loc_stats->dram_load_bytes_other_node += (m->getLen()+2) * WORDSIZE;

                              
                                // Node to node statistics
                                this->simNodeStats[node_offset_mpi_rank].dram_load_bytes_other_node[destNodeID.node_id]->fetch_add(2 * WORDSIZE);
                                this->simNodeStats[node_offset_mpi_rank].dram_load_count_other_node[destNodeID.node_id]->fetch_add(1);
                            #endif
                        }
                        uds[udid]->pushDelayedMessage(std::move(m));
                    } else {
                        uint32_t target_stid = this->getMemoryMessageTargetStackID(pAddr, m->getIsGlobal());
                        this->udMems[destNodeID.node_offset]->pushMessage(std::move(m), target_stid);
                    }
                    break;
                }
                case basim::MType::M3Type:{
                    destNodeID.node_id = m->getXe().getNWID().getNodeID();
                    if(destNodeID.node_id != srcNodeID) {
                        #if defined(FASTSIM_NETWORK_TRACE)
                            basim::globalLogs.tracelog.write(UpDown::curRuntimeInstance->getCurTick(), "NETWORK_SEND_MSG",
                                "<NODE2NODE, " +
                                std::to_string(srcNodeID) +" -> " +
                                std::to_string(destNodeID.node_id) +", " +
                                std::to_string((m->getLen()+2) * WORDSIZE) + "B>"
                            );
                        #endif

                        #ifdef DETAIL_STATS
                            basim::LaneStats* loc_stats = uds[udid]->getLaneStats(laneID);
                            loc_stats->tran_count_other_node++;
                            loc_stats->tran_bytes_other_node += (m->getLen()+2) * WORDSIZE;

                            // Node to node statistics
                            this->simNodeStats[node_offset_mpi_rank].tran_bytes_other_node[destNodeID.node_id]->fetch_add((m->getLen()+2) * WORDSIZE);
                            this->simNodeStats[node_offset_mpi_rank].tran_count_other_node[destNodeID.node_id]->fetch_add(1);
                        #endif

                        uds[udid]->pushDelayedMessage(std::move(m));
                    } else {
                        processMessageM3(std::move(m));
                    }
                    break;
                }
                case basim::MType::M3Type_M:{
                    basim::Addr pAddr = m->getdestaddr();
                    destNodeID = mapPA2SA(pAddr, m->getIsGlobal());
                    if(!m->getIsGlobal()) {
                        destNodeID.node_id = srcNodeID;
                        destNodeID.node_offset = this->get_node_offset(srcNodeID);
                    }
                  
                    if(destNodeID.node_id != srcNodeID) {
                        #if defined(FASTSIM_NETWORK_TRACE)
                            basim::globalLogs.tracelog.write(UpDown::curRuntimeInstance->getCurTick(), "NETWORK_SEND_MSG",
                            "<NODE2DRAM_ST, " +
                            std::to_string(srcNodeID) +" -> " +
                            std::to_string(destNodeID.node_id) +", " +
                            std::to_string((m->getLen()+2) * WORDSIZE) + "B>"
                        );
                        #endif

                        #ifdef DETAIL_STATS
                            basim::LaneStats* loc_stats = uds[udid]->getLaneStats(laneID);
                            loc_stats->dram_store_count_other_node++;
                            loc_stats->dram_store_bytes_other_node += (m->getLen()+2) * WORDSIZE;

                            // Node to node statistics
                            this->simNodeStats[node_offset_mpi_rank].dram_store_bytes_other_node[destNodeID.node_id]->fetch_add((m->getLen()+2) * WORDSIZE);
                            this->simNodeStats[node_offset_mpi_rank].dram_store_count_other_node[destNodeID.node_id]->fetch_add(1);
                        #endif

                        uds[udid]->pushDelayedMessage(std::move(m));
                    } else {
                        uint32_t target_stid = this->getMemoryMessageTargetStackID(pAddr, m->getIsGlobal());
                        this->udMems[destNodeID.node_offset]->pushMessage(std::move(m), target_stid);
                    }
                    break;
                }
                case basim::MType::M4Type:{
                    destNodeID.node_id = m->getXe().getNWID().getNodeID();

                    if(destNodeID.node_id != srcNodeID) {
                        #if defined(FASTSIM_NETWORK_TRACE)
                            basim::globalLogs.tracelog.write(UpDown::curRuntimeInstance->getCurTick(), "NETWORK_SEND_MSG",
                                "<NODE2NODE, " +
                                std::to_string(srcNodeID) +" -> " +
                                std::to_string(destNodeID.node_id) +", " +
                                std::to_string((m->getLen()+2) * WORDSIZE) + "B>"
                            );
                        #endif

                        #ifdef DETAIL_STATS
                            basim::LaneStats* loc_stats = uds[udid]->getLaneStats(laneID);
                            loc_stats->tran_count_other_node++;
                            loc_stats->tran_bytes_other_node += (m->getLen()+2) * WORDSIZE;

                            // Node to node statistics
                            this->simNodeStats[node_offset_mpi_rank].tran_bytes_other_node[destNodeID.node_id]->fetch_add((m->getLen()+2) * WORDSIZE);
                            this->simNodeStats[node_offset_mpi_rank].tran_count_other_node[destNodeID.node_id]->fetch_add(1);
                        #endif

                        uds[udid]->pushDelayedMessage(std::move(m));
                    } else {
                        processMessageM4(std::move(m));
                    }
                    break;
                }
                case basim::MType::M4Type_M:{

                    basim::Addr pAddr = m->getdestaddr();
                    destNodeID = mapPA2SA(pAddr, m->getIsGlobal());
                    if(!m->getIsGlobal()) {
                        destNodeID.node_id = srcNodeID;
                        destNodeID.node_offset = this->get_node_offset(srcNodeID);
                    }
                  
                    if(destNodeID.node_id != srcNodeID) {
                        #if defined(FASTSIM_NETWORK_TRACE)
                        basim::globalLogs.tracelog.write(UpDown::curRuntimeInstance->getCurTick(), "NETWORK_SEND_MSG",
                            "<NODE2DRAM_ST, " +
                            std::to_string(srcNodeID) +" -> " +
                            std::to_string(destNodeID.node_id) +", " +
                            std::to_string((m->getLen()+2) * WORDSIZE) + "B>"
                        );
                        #endif

                        #ifdef DETAIL_STATS
                            basim::LaneStats* loc_stats = uds[udid]->getLaneStats(laneID);
                            loc_stats->dram_store_count_other_node++;
                            loc_stats->dram_store_bytes_other_node += (m->getLen()+2) * WORDSIZE;

                            // Node to node statistics
                            this->simNodeStats[node_offset_mpi_rank].tran_bytes_other_node[destNodeID.node_id]->fetch_add((m->getLen()+2) * WORDSIZE);
                            this->simNodeStats[node_offset_mpi_rank].tran_count_other_node[destNodeID.node_id]->fetch_add(1);
                        #endif

                        uds[udid]->pushDelayedMessage(std::move(m));
                    } else {
                        uint32_t target_stid = this->getMemoryMessageTargetStackID(pAddr, m->getIsGlobal());
                        this->udMems[destNodeID.node_offset]->pushMessage(std::move(m), target_stid);
                    }
                    break;
                }
                default: {
                    BASIM_ERROR("Undefined Message type in Send Buffer");
                    break;
                }
            }
        }
    }
#endif

bool BASimUDRuntime_t::popDelayedMessageUD(uint32_t udid) {
    #ifdef NETWORK_STATS
        const int network_stats_active = 1;
    #else 
        const int network_stats_active = 0;
    #endif
    bool popped = false;
    while(true) {
        uint32_t srcNodeID = udid / (this->MachineConfig.NumUDs * this->MachineConfig.NumStacks);
        if(network_output_limit > 0 && (this->simNodeStats[srcNodeID].output_bytes->load() + 88) >= network_output_limit){  // set network bandwidth and output network traffic on node nodeid is full
          return true;
        }

        std::unique_ptr<basim::MMessage> m = uds[udid]->popDelayedMessage();

        if (!m) {
          return popped;
        }
        popped = true;

        switch(m->getType()){
            case basim::MType::M1Type:{
                if(network_output_limit > 0 || network_stats_active)
                  this->simNodeStats[srcNodeID].output_bytes->fetch_add((m->getLen()+2) * WORDSIZE);
                
                uint32_t destNodeID = m->getXe().getNWID().getNodeID();
                if(this->isRemoteNodeMPI(destNodeID)) {
                    mpiSendMessage(std::move(m), destNodeID, MPI_TAG_MSG_UD_QUEUE, -1);
                } else {
                    processMessageM1(std::move(m));
                }
                break;
            }
            case basim::MType::M2Type: {
                if(network_output_limit > 0 || network_stats_active) {
                  if(m->isStore()) {
                      this->simNodeStats[srcNodeID].output_bytes->fetch_add((m->getLen()+2) * WORDSIZE);
                  } else {
                      this->simNodeStats[srcNodeID].output_bytes->fetch_add(2 * WORDSIZE);
                  }
                }

                basim::Addr pAddr = m->getdestaddr();
                common_addr sAddr = mapPA2SA(pAddr, m->getIsGlobal());
                if(!m->getIsGlobal()) {
                    sAddr.node_id = srcNodeID;
                    sAddr.node_offset = srcNodeID % this->nodesPerRuntime;
                }

                uint32_t target_stid = this->getMemoryMessageTargetStackID(pAddr, m->getIsGlobal());
                if(this->isRemoteNodeMPI(sAddr.node_id)) {
                    uint64_t userData = (((uint64_t)sAddr.node_offset) << 8) | (uint8_t)target_stid;
                    this->mpiSendMessage(std::move(m), sAddr.node_id, MPI_TAG_MSG_MEM_QUEUE, userData);
                } else {
                    this->udMems[sAddr.node_offset]->pushMessage(std::move(m), target_stid);
                }
                break;
            }
            case basim::MType::M3Type: {
                if(network_output_limit > 0 || network_stats_active)
                  this->simNodeStats[srcNodeID].output_bytes->fetch_add((m->getLen()+2) * WORDSIZE);
                
                uint32_t destNodeID = m->getXe().getNWID().getNodeID();
                if(this->isRemoteNodeMPI(destNodeID)) {
                    mpiSendMessage(std::move(m), destNodeID, MPI_TAG_MSG_UD_QUEUE, -1);
                } else {
                    processMessageM3(std::move(m));
                }
                break;
            }
            case basim::MType::M3Type_M: {
                if(network_output_limit > 0 || network_stats_active)
                  this->simNodeStats[srcNodeID].output_bytes->fetch_add((m->getLen()+2) * WORDSIZE);
                
                basim::Addr pAddr = m->getdestaddr();
                common_addr sAddr = mapPA2SA(pAddr, m->getIsGlobal());
                if(!m->getIsGlobal()) {
                    sAddr.node_id = srcNodeID;
                    sAddr.node_offset = srcNodeID % this->nodesPerRuntime;
                }

                uint32_t target_stid = this->getMemoryMessageTargetStackID(pAddr, m->getIsGlobal());
                if(this->isRemoteNodeMPI(sAddr.node_id)) {
                    uint64_t userData = (((uint64_t)sAddr.node_offset) << 8) | (uint8_t)target_stid;
                    this->mpiSendMessage(std::move(m), sAddr.node_id, MPI_TAG_MSG_MEM_QUEUE, userData);
                } else {
                    this->udMems[sAddr.node_offset]->pushMessage(std::move(m), target_stid);
                }
                break;
            }
            case basim::MType::M4Type:{
                if(network_output_limit > 0 || network_stats_active)
                  this->simNodeStats[srcNodeID].output_bytes->fetch_add((m->getLen()+2) * WORDSIZE);
                uint32_t destNodeID = m->getXe().getNWID().getNodeID();
                if(this->isRemoteNodeMPI(destNodeID)) {
                    mpiSendMessage(std::move(m), destNodeID, MPI_TAG_MSG_UD_QUEUE, -1);
                } else {
                    processMessageM4(std::move(m));
                }
                break;
            }
            case basim::MType::M4Type_M: {
                if(network_output_limit > 0 || network_stats_active)
                  this->simNodeStats[srcNodeID].output_bytes->fetch_add((m->getLen()+2) * WORDSIZE);
                
                basim::Addr pAddr = m->getdestaddr();
                common_addr sAddr = mapPA2SA(pAddr, m->getIsGlobal());
                if(!m->getIsGlobal()) {
                    sAddr.node_id = srcNodeID;
                    sAddr.node_offset = srcNodeID % this->nodesPerRuntime;
                }
                
                uint32_t target_stid = this->getMemoryMessageTargetStackID(pAddr, m->getIsGlobal());
                if(this->isRemoteNodeMPI(sAddr.node_id)) {
                    uint64_t userData = (((uint64_t)sAddr.node_offset) << 8) | (uint8_t)target_stid;
                    this->mpiSendMessage(std::move(m), sAddr.node_id, MPI_TAG_MSG_MEM_QUEUE, userData);
                } else {
                    this->udMems[sAddr.node_offset]->pushMessage(std::move(m), target_stid);
                }
                break;
            }
            default:{
                BASIM_ERROR("Undefined Message type in Delayed Buffer UD");
                break;
            }
        }
    }
}
    
bool BASimUDRuntime_t::popMemory(uint32_t nodeOffset, uint32_t stackID) {
    bool popped = false;
    while (true) {
        std::unique_ptr<basim::MMessage> m = this->udMems[nodeOffset]->popMessage(stackID);
        if (!m) {
          break;
        }
        popped = true;

        uint32_t destNodeID = m->getXc().getNWID().getNodeID();
        uint32_t currentNodeID = this->getRank() * this->nodesPerRuntime + nodeOffset;
        processLoadStore(m.get());
        switch(m->getType()) {
            case basim::MType::M2Type:
                if(destNodeID != currentNodeID) {
                    this->udMems[nodeOffset]->pushDelayedMessage(std::move(m), stackID);
                } else {
                    processMessageM2(std::move(m), nodeOffset);
                }
                break;
            case basim::MType::M3Type_M:
                if(destNodeID != currentNodeID) {
                    this->udMems[nodeOffset]->pushDelayedMessage(std::move(m), stackID);
                } else {
                    processMessageM3M(std::move(m));
                }
                break;
            case basim::MType::M4Type_M:
                if(destNodeID != currentNodeID) {
                    this->udMems[nodeOffset]->pushDelayedMessage(std::move(m), stackID);
                } else {
                    processMessageM4M(std::move(m));
                }
                break;
            default:
                BASIM_ERROR("Undefined Message type in MEM Buffer");
                break;
        }
    }
    return popped;
}

bool BASimUDRuntime_t::popDelayedMessageMEM(uint32_t srcNodeID, uint32_t stackID) {
    #ifdef NETWORK_STATS
        const int network_stats_active = 1;
    #else 
        const int network_stats_active = 0;
    #endif
    bool popped = false;
    while (true) {
        if(network_output_limit > 0 && (this->simNodeStats[srcNodeID].output_bytes->load() + 88) >= network_output_limit){  // set network bandwidth and output network traffic on node nodeid is full
         return true;
        }
        std::unique_ptr<basim::MMessage> m = this->udMems[srcNodeID]->popDelayedMessage(stackID);
        if (!m) {
            break;
        }

        uint32_t destNodeID = m->getXc().getNWID().getNodeID();
        if (this->isRemoteNodeMPI(destNodeID)) {
            mpiSendMessage(std::move(m), destNodeID, MPI_TAG_DELAY_MSG_MEM_QUEUE, srcNodeID);
            continue;
        }

        popped = true;
        switch(m->getType()) {
            case basim::MType::M2Type:
                if(network_output_limit > 0 || network_stats_active) {
                  if(m->isStore()) {
                      this->simNodeStats[srcNodeID].output_bytes->fetch_add(2 * WORDSIZE);
                  } else {
                      this->simNodeStats[srcNodeID].output_bytes->fetch_add((m->getLen()+2) * WORDSIZE);
                  }
                }
                processMessageM2(std::move(m), srcNodeID);
                break;
            case basim::MType::M3Type_M:
                if(network_output_limit > 0 || network_stats_active)
                  this->simNodeStats[srcNodeID].output_bytes->fetch_add(2 * WORDSIZE);
                processMessageM3M(std::move(m));
                break;
            case basim::MType::M4Type_M:
                if(network_output_limit > 0 || network_stats_active)
                  this->simNodeStats[srcNodeID].output_bytes->fetch_add(2 * WORDSIZE);
                processMessageM4M(std::move(m));
                break;
            default:
                std::cerr << *m << std::endl;
                BASIM_ERROR("Undefined Message type in Delayed Buffer MEM");
                break;
        }
    }
    return popped;
}



void BASimUDRuntime_t::processMessageM1(std::unique_ptr<basim::MMessage> m) {
    basim::eventword_t ev = m->getXe();
    // Send Message to another lane
    basim::operands_t op0(m->getLen(), m->getXc());  // num operands + cont
    //op0.setData((m->getpayload()).get());
    op0.setData((m->getpayload()));
    basim::eventoperands_t eops(&ev, &op0);
    uint32_t ud = getUDIdx(ev.getNWID());
    #ifndef SENDPOLICY
      sendEventOperands(ud, &eops, (ev.getNWID()).getLaneID());
    #else
      int policy = (ev.getNWID()).getSendPolicy();
      if(policy == 7) {
        basim::Addr addr = m->getdestaddr();
        ud = getUDIdxForAddr(ev.getNWID(), addr, m->getIsGlobal());
        int laneid = uds[ud]->getLanebyPolicy(ev.getNWID().getLaneID(), (ev.getNWID()).getSendPolicy());
        sendEventOperands(ud, &eops, laneid);
      }else{
        int laneid = uds[ud]->getLanebyPolicy(ev.getNWID().getLaneID(), policy);
        sendEventOperands(ud, &eops, laneid);
      }
    #endif
      #if defined(FASTSIM_TRACE_MSG)
      basim::globalLogs.tracelog.write(UpDown::curRuntimeInstance->getCurTick(), "MSG",
        "<LANE2LANE, " +
        std::to_string(m->getSrcEventWord().getNWID().getUDName()) + ":" +
        std::to_string(m->getSrcEventWord().getThreadID()) +" -> " +
        std::to_string(m->getXe().getNWID().getUDName()) + ":" +
        std::to_string(m->getXe().getThreadID()) +", " +
        std::to_string(m->getMsgSize()) + ">"
        );
      #endif
}

void BASimUDRuntime_t::processLoadStore(basim::MMessage* m) {
    basim::Addr pAddr = m->getdestaddr();
    common_addr sAddr = mapPA2SA(pAddr, m->getIsGlobal());

    if(m->isStore()) {
        word_t* dataptr = m->getpayload(); // get the data and store it in memory
        word_t* dst = reinterpret_cast<word_t*>(sAddr.addr);
        std::memcpy(dst, dataptr, m->getLen()*WORDSIZE);
    } else {
        // Reads from memory
        word_t* dataptr = reinterpret_cast<word_t*>(sAddr.addr);
        m->addpayload(dataptr);
    }
}

void BASimUDRuntime_t::processMessageM2(std::unique_ptr<basim::MMessage> m, uint32_t udORnode_id) {
  // Send to Memory
  basim::eventword_t* cont = new basim::EventWord();
  *cont = m->getXc();
  
  if(m->isStore()) {
    // Post store event push
    uint64_t noupdate_cont = 0x7fffffffffffffff;
    basim::operands_t op0(2, basim::EventWord(noupdate_cont));  // num operands + cont
    uint32_t ud = getUDIdx(cont->getNWID());
    uint64_t dest_va = getVirtualAddr(ud, m->getdestaddr(), m->getIsGlobal());
    op0.setDataWord(0, dest_va);
    op0.setDataWord(1, dest_va);
    basim::eventoperands_t eops(cont, &op0);
    sendEventOperands(ud, &eops, (cont->getNWID()).getLaneID());
    #if defined(FASTSIM_TRACE_MSG)
    basim::globalLogs.tracelog.write(UpDown::curRuntimeInstance->getCurTick(), "MSG",
      "<LANE2MEM_ST, " +
      std::to_string(m->getSrcEventWord().getNWID().getUDName()) + " -> " +
      basim::addr2HexString(reinterpret_cast<void *>(dest_va)) + ", " +
      std::to_string(m->getMsgSize()) + ">"
      );
    basim::globalLogs.tracelog.write(UpDown::curRuntimeInstance->getCurTick(), "MSG",
      "<MEM2LANE_ST, " +
      basim::addr2HexString(reinterpret_cast<void *>(dest_va)) + " -> " +
      std::to_string(m->getXc().getNWID().getUDName()) + ", " +
      std::to_string((2 /* DRAM Address */ + 1 /* Dst Event Word */ + 1 /* Continuation Word */) * WORDSIZE) + ">"
      );
    #endif
  } else {
    uint64_t noupdate_cont = 0x7fffffffffffffff;
    word_t* dst = m->getpayload();
    basim::operands_t op0(m->getLen() + 1, basim::EventWord(noupdate_cont));  // num operands + dram addr (cont added by constructor)
    for (int im = 0; im < m->getLen(); im++) {
      op0.setDataWord(im, dst[im]);
    }
    uint64_t dest_va = getVirtualAddr(udORnode_id, m->getdestaddr(), m->getIsGlobal());
    op0.setDataWord(m->getLen(), dest_va);
    basim::eventoperands_t eops(cont, &op0);
    uint32_t ud = getUDIdx(cont->getNWID());
    sendEventOperands(ud, &eops, (cont->getNWID()).getLaneID());
    // delete[] dst;
    #if defined(FASTSIM_TRACE_MSG)
    basim::globalLogs.tracelog.write(UpDown::curRuntimeInstance->getCurTick(), "MSG",
      "<LANE2MEM_LD, " +
      std::to_string(m->getSrcEventWord().getNWID().getUDName()) + " -> " +
      basim::addr2HexString(reinterpret_cast<void *>(dest_va)) + ", " +
      std::to_string(m->getMsgSize()) + ">"
      );
    basim::globalLogs.tracelog.write(UpDown::curRuntimeInstance->getCurTick(), "MSG",
      "<MEM2LANE_LD, " +
      basim::addr2HexString(reinterpret_cast<void *>(dest_va)) + " -> " +
      std::to_string(m->getXc().getNWID().getUDName()) + ", " +
      std::to_string((m->getLen() + 1 /* DRAM Address */ + 1 /* Dst Event Word */ + 1 /* Continuation Word */) * WORDSIZE) + ">"
      );
    #endif
  }
  delete cont;
}

void BASimUDRuntime_t::processMessageM3(std::unique_ptr<basim::MMessage> m) {
    // Send Message to another lane
    basim::eventword_t ev = m->getXe();
    basim::operands_t op0(m->getLen(), m->getXc());  // num operands + cont
    op0.setData((m->getpayload()));
    basim::eventoperands_t eops(&ev, &op0);
    uint32_t ud = getUDIdx(ev.getNWID());
    #ifndef SENDPOLICY
      sendEventOperands(ud, &eops, (ev.getNWID()).getLaneID());
    #else
      int policy = (ev.getNWID()).getSendPolicy();
      if(policy == 7){
        basim::Addr addr = m->getdestaddr();
        ud = getUDIdxForAddr(ev.getNWID(), addr, m->getIsGlobal());
        int laneid = uds[ud]->getLanebyPolicy(ev.getNWID().getLaneID(), (ev.getNWID()).getSendPolicy());
        sendEventOperands(ud, &eops, laneid);
      }else{
        int laneid = uds[ud]->getLanebyPolicy(ev.getNWID().getLaneID(), (ev.getNWID()).getSendPolicy());
        sendEventOperands(ud, &eops, laneid);
      }
    #endif
    #if defined(FASTSIM_TRACE_MSG)
    basim::globalLogs.tracelog.write(UpDown::curRuntimeInstance->getCurTick(), "MSG",
      "<LANE2LANE, " +
      std::to_string(m->getSrcEventWord().getNWID().getUDName()) + ":" +
      std::to_string(m->getSrcEventWord().getThreadID()) +" -> " +
      std::to_string(m->getXe().getNWID().getUDName()) + ":" +
      std::to_string(m->getXe().getThreadID()) +", " +
      std::to_string(m->getMsgSize()) + ">"
      );
    #endif
}

void BASimUDRuntime_t::processMessageM3M(std::unique_ptr<basim::MMessage> m) {
    basim::eventword_t cont = m->getXc();

    // Post store event push
    uint64_t noupdate_cont = 0x7fffffffffffffff;
    basim::operands_t op0(2, basim::EventWord(noupdate_cont));  // num opernads + cont
    uint32_t ud = getUDIdx(cont.getNWID());
    uint64_t dest_va = getVirtualAddr(ud, m->getdestaddr(), m->getIsGlobal());
    op0.setDataWord(0, dest_va);
    op0.setDataWord(1, dest_va);
    basim::eventoperands_t eops(&cont, &op0);
    sendEventOperands(ud, &eops, (cont.getNWID()).getLaneID());
    #if defined(FASTSIM_TRACE_MSG)
    basim::globalLogs.tracelog.write(UpDown::curRuntimeInstance->getCurTick(), "MSG",
      "<LANE2MEM_ST, " +
      std::to_string(m->getSrcEventWord().getNWID().getUDName()) + " -> " +
      basim::addr2HexString(reinterpret_cast<void *>(dest_va)) + ", " +
      std::to_string(m->getMsgSize()) + ">"
      );
    basim::globalLogs.tracelog.write(UpDown::curRuntimeInstance->getCurTick(), "MSG",
      "<MEM2LANE_ST, " +
      basim::addr2HexString(reinterpret_cast<void *>(dest_va)) + " -> " +
      std::to_string(m->getXc().getNWID().getUDName()) + ", " +
      std::to_string((2 /* DRAM Address */ + 1 /* Dst Event Word */ + 1 /* Continuation Word */) * WORDSIZE) + ">"
      );
    #endif
}

void BASimUDRuntime_t::processMessageM4(std::unique_ptr<basim::MMessage> m) {
    // Send Message to another lane
    // Merge this with M3Type
    basim::eventword_t ev = m->getXe();
    basim::operands_t op0(m->getLen(), m->getXc());  // num operands + cont
    op0.setData((m->getpayload()));
    basim::eventoperands_t eops(&ev, &op0);
    uint32_t ud = getUDIdx(ev.getNWID());
    #ifndef SENDPOLICY
        sendEventOperands(ud, &eops, (ev.getNWID()).getLaneID());
    #else
      int policy = (ev.getNWID()).getSendPolicy();
      if(policy == 7){
        basim::Addr addr = m->getdestaddr();
        ud = getUDIdxForAddr(ev.getNWID(), addr, m->getIsGlobal());
        int laneid = uds[ud]->getLanebyPolicy(ev.getNWID().getLaneID(), (ev.getNWID()).getSendPolicy());
        sendEventOperands(ud, &eops, laneid);
      }else{
        int laneid = uds[ud]->getLanebyPolicy(ev.getNWID().getLaneID(), (ev.getNWID()).getSendPolicy());
        sendEventOperands(ud, &eops, laneid);
      }
    #endif
    #if defined(FASTSIM_TRACE_MSG)
    basim::globalLogs.tracelog.write(UpDown::curRuntimeInstance->getCurTick(), "MSG",
      "<LANE2LANE, " +
      std::to_string(m->getSrcEventWord().getNWID().getUDName()) + ":" +
      std::to_string(m->getSrcEventWord().getThreadID()) +" -> " +
      std::to_string(m->getXe().getNWID().getUDName()) + ":" +
      std::to_string(m->getXe().getThreadID()) +", " +
      std::to_string(m->getMsgSize()) + ">"
      );
    #endif
}

void BASimUDRuntime_t::processMessageM4M(std::unique_ptr<basim::MMessage> m) {
    // @TODO Merge this with M3Type_M
    basim::eventword_t cont = m->getXc();

    // Post store event push
    uint64_t noupdate_cont = 0x7fffffffffffffff;
    basim::operands_t op0(2, basim::EventWord(noupdate_cont));  // num opernads + cont
    uint32_t ud = getUDIdx(cont.getNWID());
    uint64_t dest_va = getVirtualAddr(ud, m->getdestaddr(), m->getIsGlobal());
    op0.setDataWord(0, dest_va);
    op0.setDataWord(1, dest_va);
    basim::eventoperands_t eops(&cont, &op0);
    sendEventOperands(ud, &eops, (cont.getNWID()).getLaneID());
    #if defined(FASTSIM_TRACE_MSG)
    basim::globalLogs.tracelog.write(UpDown::curRuntimeInstance->getCurTick(), "MSG",
      "<LANE2MEM_ST, " +
      std::to_string(m->getSrcEventWord().getNWID().getUDName()) + " -> " +
      basim::addr2HexString(reinterpret_cast<void *>(dest_va)) + ", " +
      std::to_string(m->getMsgSize()) + ">"
      );
    basim::globalLogs.tracelog.write(UpDown::curRuntimeInstance->getCurTick(), "MSG",
      "<MEM2LANE_ST, " +
      basim::addr2HexString(reinterpret_cast<void *>(dest_va)) + " -> " +
      std::to_string(m->getXc().getNWID().getUDName()) + ", " +
      std::to_string((2 /* DRAM Address */ + 1 /* Dst Event Word */ + 1 /* Continuation Word */) * WORDSIZE) + ">"
      );
    #endif
}


void BASimUDRuntime_t::mpiSendMessage(std::unique_ptr<basim::MMessage> m, int targetNode, int tag, uint64_t userData) {
    int mpiNode = targetNode / this->nodesPerRuntime;
    // compressing tag ID and the udID/nodeID into the userData in the message
    m->setUserData((userData << 8) | static_cast<uint8_t>(tag));

    int tid = omp_get_thread_num();
    auto &c = conveyor_thread[tid][mpiNode];

    size_t oldSize = c.size();
    c.resize(oldSize + basim::MMessage::getMsgMaxSize());

    // serialize the message directly into the vector
    m->serializeInto(c.data() + oldSize);
}


void BASimUDRuntime_t::mpiBuildMessages(std::vector<int> &metaDataSend, std::vector<int> &metaDataRecv, bool *something_exec) {
    const uint32_t mpiRanks = this->getMPIProcesses();
    const uint32_t myRank = this->getRank();
    const int numThreads = omp_get_max_threads();
    bool hasData = false;

    std::fill(metaDataSend.begin(), metaDataSend.end(), 0);
    size_t totalConveyorSize = 0;

    // Determine the sizes of the messages in the conveyors
    for(int thread=0; thread<numThreads; ++thread) {
        for(uint32_t destination = 0; destination < mpiRanks; ++destination) {
            if(myRank != destination) {
                const size_t size = conveyor_thread[thread][destination].size();
                if(size > 0) {
                    // we use MPI_UINT64 to transmit the data (refer to branch fs3-large-scale-test)
                    metaDataSend[destination*2] += static_cast<int>(size / sizeof(uint64_t));
                    totalConveyorSize += size;
                    hasData = true;
                }
            }
        }
    }
    *something_exec |= hasData;

    if(hasData) {
        conveyor.reserve(totalConveyorSize);
        
        for(uint32_t destination = 0; destination < mpiRanks; ++destination) {
            for(int thread=0; thread<numThreads; ++thread) {
                if(metaDataSend[destination*2] != 0) {
                    conveyor.insert(conveyor.end(),
                        std::make_move_iterator(conveyor_thread[thread][destination].begin()),
                        std::make_move_iterator(conveyor_thread[thread][destination].end())
                    );
                    conveyor_thread[thread][destination].clear();
                }
            }
        }
    }

    if(*something_exec) {
        for(uint32_t destination = 0; destination < mpiRanks; ++destination) {
            metaDataSend[destination*2+1] = 1;
        }
    }

    // Tell all other MPI ranks what message sizes they are have to expect
    MPI_Alltoall(metaDataSend.data(), 2, MPI_INT, metaDataRecv.data(), 2, MPI_INT, MPI_COMM_WORLD);
}


void BASimUDRuntime_t::mpiCommitMessages(std::vector<int> &metaDataSend, std::vector<int> &metaDataRecv, bool *something_exec) {
    const size_t MSG_SIZE = basim::MMessage::getMsgMaxSize();

    const uint32_t mpiRanks = this->getMPIProcesses();
    std::vector<int> sdispls(mpiRanks);
    std::vector<int> rdispls(mpiRanks);
    int totalMessageSizeRecv = 0;
    int totalMessageSizeSend = 0;

    // Prepare the displacement arrays.
    // Essentially those arrays have an offset for each of the ranks in a single array.
    // For instance displs[2] = {0, 13} indicates, that rank 0 will write to the data
    // array starting at index 0 and rank 1 will fill the data array from index 13
    // onwords. To achieve this, you have to know the sizes, that the ranks are going
    // to send obviously. That is done in the method mpiBuildMessages (sizeToSend)
    // which communicates the sizes that the ranks are going to send to each other.
    for(uint32_t rank=0; rank<mpiRanks; ++rank) {
        metaDataSend[rank] = metaDataSend[rank*2];
        metaDataRecv[rank] = metaDataRecv[rank*2];
        sdispls[rank] = totalMessageSizeSend;
        rdispls[rank] = totalMessageSizeRecv;
        totalMessageSizeSend += metaDataSend[rank];
        totalMessageSizeRecv += metaDataRecv[rank];

        // TODO: Handle larger displacements (refer to branch fs3-large-scale-test)
        BASIM_ERROR_IF(totalMessageSizeSend < 0 || totalMessageSizeRecv < 0, "MPI cannot handle this displacement. The inter-rank messages are too large causing an integer overflow: totalMessageSizeSend: %d, totalMessageSizeRecv: %d", totalMessageSizeSend, totalMessageSizeRecv);

        *something_exec |= metaDataRecv[rank*2+1] != 0;
    }

    // Check, if the data array that holds the received data is large enough.
    // If not, reallocate a larger one.
    size_t totalMessageSizeRecvBytes = static_cast<size_t>(totalMessageSizeRecv)*sizeof(long);
    if(currentBufferSizeRecv < totalMessageSizeRecvBytes) {
        delete mpibufferAllMessagesRecv;
        const size_t newSize = std::max(totalMessageSizeRecvBytes, static_cast<size_t>(currentBufferSizeRecv * 1.2));
        mpibufferAllMessagesRecv = new char[newSize];
        currentBufferSizeRecv = newSize;
    }

    // Send AND Receive data to and from the other ranks
    MPI_Alltoallv(conveyor.data(), 
        metaDataSend.data(), sdispls.data(), MPI_UINT64_T, 
        mpibufferAllMessagesRecv, 
        metaDataRecv.data(), rdispls.data(), MPI_UINT64_T, 
        MPI_COMM_WORLD);
    conveyor.clear(); // Clear the conveyor after sending the data

    if(totalMessageSizeRecv == 0) return; // Nothing to process

    // Deserialize each message and process it
    #pragma omp parallel for
    for(size_t offset=0; offset<totalMessageSizeRecvBytes; offset+=MSG_SIZE) {
        char* ptr = mpibufferAllMessagesRecv + offset;
        std::unique_ptr<basim::MMessage> m = basim::MMessage::deserialize(ptr);

        uint64_t userData = m->getUserData();
        uint8_t tag = userData & 0xff;
        userData = userData >> 8;

        if(tag == MPI_TAG_MSG_UD_QUEUE) {
            switch(m->getType()){
                case basim::MType::M1Type:
                    processMessageM1(std::move(m));
                    break;
                case basim::MType::M3Type:
                    processMessageM3(std::move(m));
                    break;
                case basim::MType::M4Type:
                    processMessageM4(std::move(m));
                    break;
                default:
                    std::cerr << *m << std::endl;
                    BASIM_ERROR("Undefined Message type in Delayed Buffer MEM");
                    break;
            }
        } else if(tag == MPI_TAG_MSG_MEM_QUEUE) {
            uint8_t stackID = userData & 0xff;
            userData = userData >> 8;
            this->udMems[userData]->pushMessage(std::move(m), stackID);
        } else { // if(tag == MPI_TAG_DELAY_MSG_MEM_QUEUE) {
            switch(m->getType()) {
                case basim::MType::M2Type:
                    processMessageM2(std::move(m), userData);
                    break;
                case basim::MType::M3Type_M:
                    processMessageM3M(std::move(m));
                    break;
                case basim::MType::M4Type_M:
                    processMessageM4M(std::move(m));
                    break;
                default:
                    std::cerr << *m << std::endl;
                    BASIM_ERROR("Undefined Message type in Delayed Buffer MEM");
                    break;
            }
        }
    }
}

void BASimUDRuntime_t::sendEventOperands(uint32_t targetUDID, basim::eventoperands_t *eops, uint32_t targetLaneID) {
    uds[targetUDID]->pushEventOperands(*eops, targetLaneID);
}

uint64_t BASimUDRuntime_t::getVirtualAddr(int sourceUDID, uint64_t addr, bool isGlobal) {
    return uds[sourceUDID]->translate_pa2va(addr, isGlobal);
}


void BASimUDRuntime_t::start_exec(networkid_t nwid) {
    uint32_t myRank = this->getRank();
    BASIM_ERROR_IF(myRank != 0, "start_exec can only be called from MPI rank 0 at the moment!");

    for(uint32_t rank=1; rank<this->getMPIProcesses(); ++rank) {
        MPI_Send(nullptr, 0, MPI_UINT64_T, rank, MPI_START_SIM, MPI_COMM_WORLD);
    }
    this->simLoop(nwid);
}



void BASimUDRuntime_t::simLoop(networkid_t nwid) {

    // Then we do a round-robin execution of all the lanes while
    // there is something executing
    if(pthread_mutex_trylock(&mutex) == 0) {
        bool something_exec = true;
        uint64_t num_iterations = 0;
        const uint32_t mpiRanks = this->getMPIProcesses();
        std::vector<int> metaDataSend(mpiRanks*2);
        std::vector<int> metaDataRecv(mpiRanks*2);

        while(1) {
            // Determine sizes of message to be sent to other ranks and prepare conveyor.
            this->mpiBuildMessages(metaDataSend, metaDataRecv, &something_exec);
    
            // Send messages to the other MPI ranks
            this->mpiCommitMessages(metaDataSend, metaDataRecv, &something_exec);

            
            if(!something_exec) {
                break;
            }
            something_exec = false;

            /*------------------------ network initialization -------------------------*/
            // reset node tmp stats for max network bandwidth
            if(this->MachineConfig.InterNodeBandwidth > 0) {
                for(uint32_t nodeID = 0; nodeID < this->nodesPerRuntime; nodeID++){
                    this->simNodeStats[nodeID].reset_tmp();
                }
            }
            /*------------------------ network initialization end-------------------------*/

            for (uint32_t ud = 0; ud < this->udsPerRuntime; ud++) {
                uds[ud]->tock(NumTicks);
            }
            for (uint32_t node = 0; node < this->nodesPerRuntime; node++) {
                this->udMems[node]->tick(NumTicks);
            }

            // Do computations
            #pragma omp parallel for schedule(runtime) reduction(|| : something_exec) // ud level parallelism
            for (uint32_t ud = 0; ud < this->udsPerRuntime; ud++) {
                for (uint32_t ln = 0; ln < this->MachineConfig.NumLanes; ln++) {
                    if (!uds[ud]->isIdle(ln)) {
                        something_exec = true;
                        uds[ud]->simulate(ln, NumTicks, globalTick);
                    }
                }
            }
            // OMP: implicit barrier

            // Send messages
            bool something_popped = false;
            #pragma omp parallel for schedule(runtime) reduction(|| : something_popped)
            for (uint32_t ud = 0; ud < this->udsPerRuntime; ud++) {
                if(something_exec) {
                    for (uint32_t ln = 0; ln < this->MachineConfig.NumLanes; ln++) {
                        postSimulate(ud, ln);
                    }
                }
                something_popped |= popDelayedMessageUD(ud);
            }
            // OMP: implicit barrier

            something_exec |= something_popped;

            // Memory operations
            #pragma omp parallel for schedule(runtime) reduction(|| : something_exec)
                for (uint32_t st = 0; st < this->MachineConfig.NumStacks; st++) {
                    for (uint32_t node = 0; node < this->nodesPerRuntime; node++) {
                        something_exec |= popMemory(node, st) | popDelayedMessageMEM(node, st);
                    }
                }
            // OMP: implicit barrier


            for (uint32_t node = 0; node < this->nodesPerRuntime; node++) {
              for (uint32_t st = 0; st < this->MachineConfig.NumStacks; st++) {
                this->udMems[node]->updateStats(st);
              }
            }
            


            // #if defined(NETWORK_STATS)
            //     for (uint32_t node = 0; node < this->nodesPerRuntime; node++) {
            //         for (uint32_t dstNodeID = 0; dstNodeID < this->MachineConfig.NumNodes; dstNodeID++) {
            //             uint64_t node_stats_tmp = std::max(this->simNodeStats[node].max_total_count_other_node[dstNodeID]->load(), this->simNodeStats[node].max_total_count_other_node_tmp[dstNodeID]->load());
            //             this->simNodeStats[node].max_total_count_other_node[dstNodeID]->store(node_stats_tmp);
            //             node_stats_tmp = std::max(this->simNodeStats[node].max_total_bytes_other_node[dstNodeID]->load(), this->simNodeStats[node].max_total_bytes_other_node_tmp[dstNodeID]->load());
            //             this->simNodeStats[node].max_total_bytes_other_node[dstNodeID]->store(node_stats_tmp);
            //             node_stats_tmp = std::max(this->simNodeStats[node].max_tran_count_other_node[dstNodeID]->load(), this->simNodeStats[node].max_tran_count_other_node_tmp[dstNodeID]->load());
            //             this->simNodeStats[node].max_tran_count_other_node[dstNodeID]->store(node_stats_tmp);
            //             node_stats_tmp = std::max(this->simNodeStats[node].max_tran_bytes_other_node[dstNodeID]->load(), this->simNodeStats[node].max_tran_bytes_other_node_tmp[dstNodeID]->load());
            //             this->simNodeStats[node].max_tran_bytes_other_node[dstNodeID]->store(node_stats_tmp);
            //             node_stats_tmp = std::max(this->simNodeStats[node].max_dram_store_count_other_node[dstNodeID]->load(), this->simNodeStats[node].max_dram_store_count_other_node_tmp[dstNodeID]->load());
            //             this->simNodeStats[node].max_dram_store_count_other_node[dstNodeID]->store(node_stats_tmp);
            //             node_stats_tmp = std::max(this->simNodeStats[node].max_dram_load_count_other_node[dstNodeID]->load(), this->simNodeStats[node].max_dram_load_count_other_node_tmp[dstNodeID]->load());
            //             this->simNodeStats[node].max_dram_load_count_other_node[dstNodeID]->store(node_stats_tmp);
            //             node_stats_tmp = std::max(this->simNodeStats[node].max_dram_store_bytes_other_node[dstNodeID]->load(), this->simNodeStats[node].max_dram_store_bytes_other_node_tmp[dstNodeID]->load());
            //             this->simNodeStats[node].max_dram_store_bytes_other_node[dstNodeID]->store(node_stats_tmp);
            //             node_stats_tmp = std::max(this->simNodeStats[node].max_dram_load_bytes_other_node[dstNodeID]->load(), this->simNodeStats[node].max_dram_load_bytes_other_node_tmp[dstNodeID]->load());
            //             this->simNodeStats[node].max_dram_load_bytes_other_node[dstNodeID]->store(node_stats_tmp);
            //             node_stats_tmp = std::max(this->simNodeStats[node].max_dram_store_ack_count_other_node[dstNodeID]->load(), this->simNodeStats[node].max_dram_store_ack_count_other_node_tmp[dstNodeID]->load());
            //             this->simNodeStats[node].max_dram_store_ack_count_other_node[dstNodeID]->store(node_stats_tmp);
            //             node_stats_tmp = std::max(this->simNodeStats[node].max_dram_load_ack_count_other_node[dstNodeID]->load(), this->simNodeStats[node].max_dram_load_ack_count_other_node_tmp[dstNodeID]->load());
            //             this->simNodeStats[node].max_dram_load_ack_count_other_node[dstNodeID]->store(node_stats_tmp);
            //             node_stats_tmp = std::max(this->simNodeStats[node].max_dram_store_ack_bytes_other_node[dstNodeID]->load(), this->simNodeStats[node].max_dram_store_ack_bytes_other_node_tmp[dstNodeID]->load());
            //             this->simNodeStats[node].max_dram_store_ack_bytes_other_node[dstNodeID]->store(node_stats_tmp);
            //             node_stats_tmp = std::max(this->simNodeStats[node].max_dram_load_ack_bytes_other_node[dstNodeID]->load(), this->simNodeStats[node].max_dram_load_ack_bytes_other_node_tmp[dstNodeID]->load());
            //             this->simNodeStats[node].max_dram_load_ack_bytes_other_node[dstNodeID]->store(node_stats_tmp);

            //         }
            //         uint64_t node_stats_tmp = std::max(this->simNodeStats[node].max_bytes[0]->load(), this->simNodeStats[node].output_bytes->load());
            //         this->simNodeStats[node].max_bytes[0]->store(node_stats_tmp);
            //         node_stats_tmp = std::max(this->simNodeStats[node].max_counts[0]->load(), this->simNodeStats[node].output_counts[0]->load());
            //         this->simNodeStats[node].max_counts[0]->store(node_stats_tmp);
            //         uint64_t len = 0;
            //         for(uint32_t j = 0; j < MachineConfig.NumUDs * MachineConfig.NumStacks; j++){
            //             uint64_t udid = node * MachineConfig.NumUDs * MachineConfig.NumStacks + j;
            //             len = len + uds[udid]->DelayedMessageLen();
            //         }
            //         this->simNodeStats[node].total_queue_size[0]->fetch_add(len);
            //         node_stats_tmp = std::max(this->simNodeStats[node].max_queue_size[0]->load(), len);
            //         this->simNodeStats[node].max_queue_size[0]->store(node_stats_tmp);
            //     }
            // #endif
            
            globalTick += NumTicks;
            simTicks += NumTicks;
        }
        printf("Exiting simLoop\n"); fflush(stdout);
        pthread_mutex_unlock(&mutex);
    }
}


void BASimUDRuntime_t::memcpyTop2DRAM(void *dataPA, void *dataLocal, size_t size, bool useMPI) {
  if(this->MachineConfig.NumNodes == 1){
    memcpy(dataPA, dataLocal, size);
    return;
  }
  // get the nodeID of the address
  common_addr dataSA = mapPA2SA((basim::Addr)dataPA, true);
  if(useMPI && this->isRemoteNodeMPI(dataSA.node_id)) {
    uint64_t destMPIRank = dataSA.node_id / this->nodesPerRuntime;

    // ready the receiver
    uint64_t data[MPI_ADMIN_PACKET_SIZE] = {size, (uint64_t)dataPA};
    MPI_Send(data, MPI_ADMIN_PACKET_SIZE, MPI_UINT64_T, destMPIRank, MPI_TAG_T2DRAM, MPI_COMM_WORLD);

    // printf("Sending t2DRAM message: dataPA: 0x%lx, dataSA: 0x%lx, size: %lu, dest MPI rank: %d\n", (uint64_t)dataPA, dataSA.addr, size, destMPIRank);
    MPI_Send(reinterpret_cast<char *>(dataLocal), size, MPI_CHAR, destMPIRank, MPI_TAG_T2DRAM_DATA, MPI_COMM_WORLD);
  } else {
    //printf("Local Memcpy: dataPA: 0x%lx, dataSA: 0x%lx, size: %lu\n", (uint64_t)dataPA, dataSA.addr, size);
    memcpy(reinterpret_cast<void *>(dataSA.addr), dataLocal, size);
  }
}


void BASimUDRuntime_t::memcpyDRAM2Top(void *dataPA, void *dataLocal, uint64_t size, bool useMPI) {
  if(this->MachineConfig.NumNodes == 1){
    memcpy(dataLocal, dataPA, size);
    return;
  }
  // get the nodeID of the address
  common_addr dataSA = mapPA2SA((basim::Addr)dataPA, true);
  if(useMPI && this->isRemoteNodeMPI(dataSA.node_id)) {
    uint64_t destMPIRank = dataSA.node_id / this->nodesPerRuntime;

    // ready the receiver
    uint64_t data[MPI_ADMIN_PACKET_SIZE] = {size, (uint64_t)dataPA};
    MPI_Send(data, MPI_ADMIN_PACKET_SIZE, MPI_UINT64_T, destMPIRank, MPI_TAG_DRAM2T, MPI_COMM_WORLD);

    // Expect a data transfer from the remote rank
    MPI_Recv(reinterpret_cast<char *>(dataLocal), size, MPI_CHAR, destMPIRank, MPI_TAG_DRAM2T_DATA, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
    // printf("Received DRAM2T message: dataLocal: 0x%lx, dataPA: 0x%lx, size: %lu, dest MPI rank: %d\n", (uint64_t)dataLocal, (uint64_t)dataPA, size, destMPIRank);
    
  } else {
    // printf("Local Memcpy: dataPA: 0x%lx, dataSA: 0x%lx, size: %lu\n", (uint64_t)dataPA, dataSA.addr, size);
    memcpy(dataLocal, reinterpret_cast<void *>(dataSA.addr), size);
  }
}

void BASimUDRuntime_t::t2ud_memcpy(void *data, uint64_t size, networkid_t nwid,
                                 uint32_t offset) {
  // TODO MPI: If the nwid is not part of this BASIMRuntime, send a message to the
  // target BASUMRuntime and start_exec there.
  if(this->isRemoteNodeMPI(nwid.get_NodeId())) {
    return;
  }

  uint32_t ud_num = this->get_globalUDNum(nwid);
  uint64_t addr = UDRuntime_t::get_lane_physical_memory(nwid, offset); 
  uint8_t* data_ptr = reinterpret_cast<uint8_t *>(data);
  for (uint64_t i = 0; i < size / sizeof(word_t); i++) {
    // Address is local
    uds[ud_num]->writeScratchPad(sizeof(word_t), addr, reinterpret_cast<uint8_t *>(data_ptr));
    addr += sizeof(word_t);
    data_ptr += sizeof(word_t);
  }
}

void BASimUDRuntime_t::ud2t_memcpy(void *data, uint64_t size, networkid_t nwid,
                                 uint32_t offset) {

  // TODO MPI: If the nwid is not part of this BASIMRuntime, send a message to the
  // target BASUMRuntime and start_exec there.
  if(this->isRemoteNodeMPI(nwid.get_NodeId())) {
    return;
  }

  uint32_t ud_num = this->get_globalUDNum(nwid);
  uint64_t addr = UDRuntime_t::get_lane_physical_memory(nwid, offset);
  uint64_t apply_offset = UDRuntime_t::get_lane_aligned_offset(nwid, offset);
  apply_offset /= sizeof(word_t);
  ptr_t base = BaseAddrs.spaddr + apply_offset;
  UPDOWN_INFOMSG("Actual addr: 0x%lX , base: 0x%lX", addr, (unsigned long)base);
  UPDOWN_ASSERT(
      base + size / sizeof(word_t) <
          BaseAddrs.spaddr + MachineConfig.SPSize() / sizeof(word_t),
      "ud2t_memcpy: memory access to 0x%lX out of scratchpad memory bounds "
      "with offset %lu bytes and size %lu bytes. Scratchpad memory Base "
      "Address 0x%lX scratchpad memory size %lu bytes",
      (unsigned long)(base), (unsigned long)(apply_offset * sizeof(word_t)),
      (unsigned long)size, (unsigned long)BaseAddrs.spaddr,
      (unsigned long)MachineConfig.SPSize());
  //if (python_enabled)
  //  upstream_pyintf[ud_num]->read_scratch(
  //      addr, reinterpret_cast<uint8_t *>(base), size);
  uds[ud_num]->readScratchPad(sizeof(word_t), addr, reinterpret_cast<uint8_t*>(base));
  UDRuntime_t::ud2t_memcpy(data, size, nwid, offset);
}

bool BASimUDRuntime_t::test_addr(networkid_t nwid, uint32_t offset, word_t expected) {

  // TODO MPI: If the nwid is not part of this BASIMRuntime, send a message to the
  // target BASUMRuntime and start_exec there.
  if(this->isRemoteNodeMPI(nwid.get_NodeId())) {
    return true;
  }

  uint32_t ud_num = this->get_globalUDNum(nwid);
  uint64_t addr = UDRuntime_t::get_lane_physical_memory(nwid, offset);
  uint64_t apply_offset = UDRuntime_t::get_lane_aligned_offset(nwid, offset);
  apply_offset /= sizeof(word_t);
  ptr_t base = BaseAddrs.spaddr + apply_offset;
  UPDOWN_ASSERT(
      base < BaseAddrs.spaddr + MachineConfig.SPSize() / sizeof(word_t),
      "test_addr: memory access to 0x%lX out of scratchpad memory bounds "
      "with offset %lu bytes and size 4 bytes. Scratchpad memory Base Address "
      "0x%lX scratchpad memory size %lu bytes",
      (unsigned long)(base), (unsigned long)(apply_offset * sizeof(word_t)),
      (unsigned long)BaseAddrs.spaddr, (unsigned long)MachineConfig.SPSize());
  uds[ud_num]->readScratchPad(sizeof(word_t), addr, reinterpret_cast<uint8_t*>(base));
  return UDRuntime_t::test_addr(nwid, offset, expected);
}

bool BASimUDRuntime_t::test_addr_without_exec(networkid_t nwid, uint32_t offset,
                               word_t expected) {

  uint32_t ud_num = this->get_globalUDNum(nwid);
  uint64_t addr = UDRuntime_t::get_lane_physical_memory(nwid, offset);
  uint64_t apply_offset = UDRuntime_t::get_lane_aligned_offset(nwid, offset);
  apply_offset /= sizeof(word_t);
  ptr_t base = BaseAddrs.spaddr + apply_offset;
  UPDOWN_ASSERT(
      base < BaseAddrs.spaddr + MachineConfig.SPSize() / sizeof(word_t),
      "test_addr: memory access to 0x%lX out of scratchpad memory bounds "
      "with offset %lu bytes and size 4 bytes. Scratchpad memory Base Address "
      "0x%lX scratchpad memory size %lu bytes",
      (unsigned long)(base), (unsigned long)(apply_offset * sizeof(word_t)),
      (unsigned long)BaseAddrs.spaddr, (unsigned long)MachineConfig.SPSize());
  uds[ud_num]->readScratchPad(sizeof(word_t), addr, reinterpret_cast<uint8_t*>(base));
  bool end = UDRuntime_t::test_addr(nwid, offset, expected);
  return end;
}

void BASimUDRuntime_t::test_wait_addr(networkid_t nwid, uint32_t offset,
                                    word_t expected) {


    // TODO MPI: If the nwid is not part of this BASIMRuntime, send a message to the
    // target BASUMRuntime and start_exec there.
  if(this->isRemoteNodeMPI(nwid.get_NodeId())) {
    return;
  }

#ifdef ASST_FASTSIM
    pthread_mutex_lock(&map_lock);
    pthread_t tid = pthread_self();
    int id1 = 0;
    auto it1 = thread_map.find(tid);
    if (it1 != thread_map.end()) {
        id1 = it1->second;
    }else{
        id1 = thread_num.load(std::memory_order_relaxed);
        thread_num.store(id1+1, std::memory_order_release);
        thread_map[tid] = id1;
    }
    pthread_mutex_unlock(&map_lock);


    assert(nwid.get_NodeId() == nodeID && "Error, nwid is not current UpDown node");
    networkid_t nwid2(nwid.get_LaneId(), nwid.get_UdId(), nwid.get_StackId(), 0);
    while(test_addr_flag[id1] != 0)
        fflush(stdout);
    test_nwid[id1] = nwid2;
    test_offset[id1] = offset;
    test_expected[id1] = expected;
    test_addr_flag[id1] = 1;
    sem_wait(&(semTest[id1]));
    // The bottom call will never hold since we're holding here
    UDRuntime_t::test_wait_addr(nwid2, offset, expected);
#else
    while (!test_addr(nwid, offset, expected));
    // The bottom call will never hold since we're holding here
    UDRuntime_t::test_wait_addr(nwid, offset, expected);
#endif
}


size_t BASimUDRuntime_t::dumpMemoryTranslation(std::string filename, uint64_t nodeID) {
    size_t storedBytes;
    filename += std::to_string(this->getRank()) + ".dram.dat";
    FILE* mem_file = fopen(filename.c_str(), "wb");
    UPDOWN_ERROR_IF(!mem_file, "DRAM Dump: MPI Rank %d: Could not open %s", this->getRank(), filename.c_str());

    fseek(mem_file, 0, SEEK_SET);
    // Write 'F' to indicate dump by Fastsim
    storedBytes = fwrite("F", sizeof(char), 1, mem_file);
    // Write 'D' to indicate DRAM dump
    storedBytes += fwrite("D", sizeof(char), 1, mem_file);

    // include a version number for format changes (it also makes the file easier to read in hex editors, since the values are aligned now)
    uint16_t version = 1;
    storedBytes += fwrite(&version, sizeof(uint16_t), 1, mem_file);
    BASIM_INFOMSG("DRAM Dump: MPI Rank %d: file version: %d", this->getRank(), version);

    // Get access to the translation memory. We should always have at least 1 UD.
    basim::TranslationMemoryPtr transmem = uds[0]->getTranslationMem();
    transmem->dumpSegments();

    // number of private segments in the dump file
    // TODO we do not dump them for the time being
    size_t nPrivateSegments = transmem->private_segments.size();
    storedBytes += fwrite(&nPrivateSegments, sizeof(size_t), 1, mem_file);
    BASIM_INFOMSG("DRAM Dump: MPI Rank %d: number of private segments: %ld", this->getRank(), nPrivateSegments);

    // number of global segments in the dump file
    size_t nGlobalSegments = transmem->global_segments.size();
    storedBytes += fwrite(&nGlobalSegments, sizeof(size_t), 1, mem_file);
    BASIM_INFOMSG("DRAM Dump: MPI Rank %d: number of global segments: %ld", this->getRank(), nGlobalSegments);

    // basim::Addr pAddr;
    // for(uint64_t i=0; i<size/8; i+=0x1'0000) {
    //   pAddr = transmem->translate_va2pa((basim::Addr)((uint64_t)vaddr + i*8), 1);
    //   printf("vAddr: %p, pAddr: %p\n", (uint64_t)vaddr + i*8, (uint64_t)pAddr);
    // }

    for (auto seg : transmem->global_segments) {

        BASIM_INFOMSG("DRAM Dump: MPI Rank %d: Current segment:", this->getRank());
        seg.print_info();

        // position of the metadata of the current segment in the file
        uint64_t metaPos = ftell(mem_file);
        BASIM_INFOMSG("DRAM Dump: MPI Rank %d: Metadata position: %ld (0x%lx)", this->getRank(), metaPos, metaPos);
        BASIM_INFOMSG("DRAM Dump: MPI Rank %d: Stored metadata: vBase: 0x%lx, vLimit: 0x%lx, swizzleMask: 0x%lx, pAddr: 0x%lx, blockSize: %ld, accessFlags: %d", this->getRank(), seg.virtual_base, seg.virtual_limit, seg.swizzle_mask.getMask(), seg.physical_base.getCompressed(), seg.block_size, seg.access_flags);

        // store the meta data
        storedBytes += fwrite(&(seg.virtual_base), sizeof(uint64_t), 1, mem_file);
        storedBytes += fwrite(&(seg.virtual_limit), sizeof(uint64_t), 1, mem_file);
        uint64_t tempValue = seg.swizzle_mask.getMask();
        storedBytes += fwrite(&tempValue, sizeof(uint64_t), 1, mem_file);
        storedBytes += fwrite(&(seg.block_size), sizeof(uint64_t), 1, mem_file);
        tempValue = seg.physical_base.getCompressed();
        storedBytes += fwrite(&tempValue, sizeof(uint64_t), 1, mem_file);
        storedBytes += fwrite(&(seg.access_flags), sizeof(uint8_t), 1, mem_file);
        
        // add some padding after the metadata, so that debugging gets easier as the blocks are aligned.
        tempValue = 0xcafecafecafecafe;
        storedBytes += fwrite(&tempValue, sizeof(uint8_t)*3, 1, mem_file);

        for(uint64_t vAddr=seg.virtual_base; vAddr < seg.virtual_limit; vAddr += seg.block_size) {
            // translating the virtual address
            physical_addr_t pa = seg.getPhysicalAddr(vAddr);

            // Dump only data, that is of this node
            // Other node's addresses are inaccessible from this node. Hence, the TOP program of their nodes,
            // have to initialize their own dumpMemory.
            if(this->isRemoteNodeMPI(pa.getNodeId())) {
            BASIM_INFOMSG("DRAM Dump: MPI Rank %d: skipping: vAddr: 0x%lx, pAddr 0x%lx, nodeID: %ld", this->getRank(), (uint64_t)vAddr, pa.getCompressed(), pa.getNodeId());
                continue;
            }

            // Translate the physical address of the simulator to the host address, where we can actually find the data
            uint64_t pAddr = pa.getCompressed();
            common_addr hostAddr = mapPA2SA(pAddr, 1);
            auto dst = reinterpret_cast<word_t*>(hostAddr.addr);
            BASIM_INFOMSG("DRAM Dump: MPI Rank %ld: vAddr: 0x%lx, pAddr 0x%lx, hostAddr: %p, block_size: %ld", this->getRank(), (uint64_t)vAddr, pAddr, dst, seg.block_size);

            // store the data in the file
            storedBytes += fwrite(dst, sizeof(uint8_t), std::min(seg.block_size, seg.virtual_limit-vAddr), mem_file);
        }
    }
    fclose(mem_file);
    BASIM_INFOMSG("DRAM Dump: MPI Rank %d: Dump complete. Stored %ld Bytes", this->getRank(), storedBytes);
    return storedBytes;
}

size_t BASimUDRuntime_t::loadMemoryTranslation(std::string filename, uint64_t nodeID, void* dumpVA) {

    size_t loadedBytes;
    filename += std::to_string(this->getRank()) + ".dram.dat";
    FILE* mem_file = fopen(filename.c_str(), "rb");
    UPDOWN_ERROR_IF(!mem_file, "DRAM Load: MPI Rank %d: Could not open %s", this->getRank(), filename.c_str());

    // Read 'F' to indicate dump by Fastsim
    char dump_type;
    loadedBytes = fread(&dump_type, sizeof(char), 1, mem_file);
    UPDOWN_ERROR_IF(dump_type != 'F', "DRAM dump load failed! Not a FastSim dump file!\n");

    // Read 'D' to indicate DRAM dump
    loadedBytes += fread(&dump_type, sizeof(char), 1, mem_file);
    UPDOWN_ERROR_IF(dump_type != 'D', "DRAM dump load failed! Not a DRAM dump file!\n");

    // Read version number
    uint16_t version;
    loadedBytes += fread(&version, sizeof(uint16_t), 1, mem_file);
    UPDOWN_ERROR_IF(version != 1, "DRAM dump load failed! Incorrect format version!\n");

    // Read number of entries for the private and global segments
    size_t nPrivateSegments, nGlobalSegments;
    loadedBytes = fread(&nPrivateSegments, sizeof(size_t), 1, mem_file);
    loadedBytes = fread(&nGlobalSegments, sizeof(size_t), 1, mem_file);

    for(uint64_t seg=0; seg<nGlobalSegments; ++seg) {
        uint64_t metaPos = ftell(mem_file);
        BASIM_INFOMSG("DRAM Load: MPI Rank %d: Metadata position: %ld (0x%lx)", this->getRank(), metaPos, metaPos);

        // Read the metadata
        basim::Addr vBase, vLimit, pBase;
        uint64_t swizzleMask, blockSize;
        uint8_t accessFlags;
        loadedBytes += fread(&vBase, sizeof(basim::Addr), 1, mem_file);
        loadedBytes += fread(&vLimit, sizeof(basim::Addr), 1, mem_file);
        loadedBytes += fread(&swizzleMask, sizeof(uint64_t), 1, mem_file);
        loadedBytes += fread(&blockSize, sizeof(uint64_t), 1, mem_file);
        loadedBytes += fread(&pBase, sizeof(basim::Addr), 1, mem_file);
        loadedBytes += fread(&accessFlags, sizeof(uint8_t), 1, mem_file);

        // skip over the padding fields (The coffee from above)
        fseek(mem_file, 3, SEEK_CUR);
        BASIM_INFOMSG("DRAM Load: MPI Rank %d: Found metadata: vBase: 0x%lx, vLimit: 0x%lx, swizzleMask: 0x%lx, pAddr: 0x%lx, blockSize: %ld, accessFlags: %d", this->getRank(), vBase, vLimit, swizzleMask, pBase, blockSize, accessFlags);

        
        if(vBase != reinterpret_cast<basim::Addr>(dumpVA)) {
            BASIM_INFOMSG("DRAM Load: MPI Rank %d: Skipping segment at VA 0x%lx", this->getRank(), vBase);
            fseek(mem_file, vLimit-vBase, SEEK_CUR);
            continue;
        }

        // get access to the translation memory
        basim::TranslationMemoryPtr transmem = this->uds[0]->getTranslationMem();

        for(basim::Addr vAddr=vBase; vAddr<vLimit; vAddr+=blockSize) {

            // translating the virtual address to the host's address
            uint64_t translationSize = std::min(blockSize, vLimit-vAddr);

            if(vBase > reinterpret_cast<basim::Addr>(dumpVA)) {
                BASIM_INFOMSG("DRAM Load: Returning early as we find unallocated blocks");
                fclose(mem_file);

                return loadedBytes;
            }

            uint64_t pAddr = transmem->translate_va2pa_global(vAddr, translationSize/sizeof(UpDown::word_t));
            UPDOWN_ERROR_IF(pAddr == transmem->INVALID_ADDR, "DRAM Load: MPI Rank: %d: Could not translate vAddr: 0x%lx, vLimit: 0x%lx, translationSize: %ld Bytes", this->getRank(), vAddr, vLimit, translationSize);
            auto pa = physical_addr_t(pAddr);

            // Read only data, that is for this node
            // Other node's addresses are inaccessible from this node. Hence, the TOP program of their nodes,
            // have to initialize their own dumpRead.
            if(isRemoteNodeMPI(pa.getNodeId())) {
                BASIM_INFOMSG("DRAM Load: MPI Rank %ld: skipping: vAddr: 0x%lx, vLimit: 0x%lx, pAddr 0x%lx, nodeID: %ld", this->getRank(), (uint64_t)vAddr, vLimit, pa.getCompressed(), pa.getNodeId());
                continue;
            }

            // translate the physical address to the host's address
            auto sAddr = reinterpret_cast<word_t*>(mapPA2SA(pa.getCompressed(), 1).addr);

            BASIM_INFOMSG("DRAM Load: MPI Rank %d: vAddr: 0x%lx, pAddr 0x%lx, hostAddr: %p, block_size: %ld", this->getRank(), (uint64_t)vAddr, pa.getCompressed(), sAddr, blockSize);

            // read 1 block from the file
            loadedBytes += fread(sAddr, sizeof(uint8_t), translationSize, mem_file);
        }
    }
    BASIM_INFOMSG("DRAM Load: MPI Rank %d: Dump loading complete. Loaded %ld Bytes", this->getRank(), loadedBytes);
    return loadedBytes;
}

  
void BASimUDRuntime_t::dumpMemory(const char* filename, void* vaddr, uint64_t size){
  FILE* mem_file = fopen(filename, "wb");
  UPDOWN_ERROR_IF(!mem_file, "Could not open %s", filename);

  // Use API to access mm_malloced area
  uint64_t offset = reinterpret_cast<uint64_t>(vaddr) - reinterpret_cast<uint64_t>(BaseAddrs.mmaddr);
  auto *data = (uint8_t*)malloc(size * sizeof(uint8_t));
  this->mm2t_memcpy(offset, data, size);

  fseek(mem_file, 0, SEEK_SET);
  // Write 'F' to indicate dump by Fastsim
  fwrite("F", sizeof(char), 1, mem_file);
  // Write 'D' to indicate DRAM dump
  fwrite("D", sizeof(char), 1, mem_file);
  // Write dump start file offset
  //                                F   D dump_start_file_offset  vaddr  size
  uint64_t dump_start_file_offset = 1 + 1     + 8 +                8     + 8;
  fwrite(&dump_start_file_offset, sizeof(uint64_t), 1, mem_file);
  BASIM_INFOMSG("DRAM Dump start file offset: %lu", dump_start_file_offset);
  // Write dump vaddr
  fwrite(&vaddr, sizeof(uint64_t), 1, mem_file);
  BASIM_INFOMSG("DRAM Dump vaddr: %p", vaddr);
  // Write dump size
  fwrite(&size, sizeof(uint64_t), 1, mem_file);
  BASIM_INFOMSG("DRAM Dump size: %lu", size);
  // Write size bytes into mem_file
  fwrite(data, sizeof(uint8_t), size, mem_file);

  fclose(mem_file);
  free(data);
}

std::pair<void *, uint64_t> BASimUDRuntime_t::loadMemory(const char* filename, void* vaddr, uint64_t size) {
  size_t loadedBytes; // to prevent compiler warnings


  FILE* mem_file = fopen(filename, "rb");
  UPDOWN_ERROR_IF(!mem_file, "Could not open %s", filename);

  fseek(mem_file, 0, SEEK_SET);
  // Read 'F' to indicate dump by Fastsim
  char dump_type;
  loadedBytes = fread(&dump_type, sizeof(char), 1, mem_file);
  UPDOWN_ERROR_IF(dump_type != 'F', "DRAM dump load failed! Not a FastSim dump file!\n");
  // Read 'D' to indicate DRAM dump
  loadedBytes = fread(&dump_type, sizeof(char), 1, mem_file);
  UPDOWN_ERROR_IF(dump_type != 'D', "DRAM dump load failed! Not a DRAM dump file!\n");
  // Read dump start file offset
  uint64_t dump_start_file_offset;
  loadedBytes = fread(&dump_start_file_offset, sizeof(uint64_t), 1, mem_file);
  BASIM_INFOMSG("DRAM Dump start file offset: %lu", dump_start_file_offset);
  // Read dump vaddr
  uint64_t dump_vaddr;
  loadedBytes = fread(&dump_vaddr, sizeof(uint64_t), 1, mem_file);
  if (vaddr == nullptr) {
    vaddr = reinterpret_cast<void *>(dump_vaddr);
    BASIM_INFOMSG("DRAM Dump vaddr (from dump file): %p", vaddr);
  } else {
    BASIM_INFOMSG("DRAM Dump vaddr (user specified): %p", vaddr);
  }
  // Read dump size
  uint64_t dump_size;
  loadedBytes = fread(&dump_size, sizeof(uint64_t), 1, mem_file);
  if (vaddr == nullptr || size == 0) {
    size = dump_size;
    BASIM_INFOMSG("DRAM Dump size (from dump file): %lu", size);
  } else {
    BASIM_INFOMSG("DRAM Dump size (user specified): %lu", size);
  }
  // Read size bytes into mem_file
  fseek(mem_file, dump_start_file_offset, SEEK_SET);
  uint8_t *data = (uint8_t*)malloc(size * sizeof(uint8_t));
  loadedBytes = fread(data, sizeof(uint8_t), size, mem_file);

  // Use API to access mm_malloced area
  if (this->mm_malloc_at_addr(vaddr, size) == nullptr) { // allocate memory
    BASIM_ERROR("DRAM dump load failed! Cannot allocate memory at (%p, %lu)", vaddr, size);
  }
  uint64_t offset = reinterpret_cast<uint64_t>(vaddr) - reinterpret_cast<uint64_t>(BaseAddrs.mmaddr);
  this->t2mm_memcpy(offset, data, size);

  fclose(mem_file);
  free(data);

  return std::make_pair(vaddr, size);
}

void BASimUDRuntime_t::dumpLocalMemory(const char* filename, networkid_t start_nwid, uint64_t num_lanes) {
  BASIM_ERROR_IF(this->isRemoteNodeMPI(start_nwid.get_NodeId()), "Only local nodes have access to the local memory.");

  FILE* spd_file = fopen(filename, "wb");
  BASIM_ERROR_IF(!spd_file, "Could not open %s\n", filename);

  uint64_t lane_lm_size = DEF_SPMEM_BANK_SIZE;
  uint64_t total_lm_size;
  if (start_nwid.get_NetworkId_UdName() == 0 && num_lanes == 0) {
    // all LMs
    total_lm_size = lane_lm_size * this->MachineConfig.NumLanes * this->MachineConfig.NumUDs * this->MachineConfig.NumStacks * this->MachineConfig.NumNodes;
    num_lanes = this->MachineConfig.NumLanes * this->MachineConfig.NumUDs * this->MachineConfig.NumStacks * this->MachineConfig.NumNodes;
  } else {
    // selected LMs
    total_lm_size = lane_lm_size * num_lanes;
  }
  uint8_t *data = (uint8_t*)malloc(total_lm_size * sizeof(uint8_t));
  basim::Addr start_addr = (uint64_t)BaseAddrs.spaddr;
  uint64_t lm_offset = 0;

  for (uint32_t i = start_nwid.get_NetworkId_UdName(); i < start_nwid.get_NetworkId_UdName() + num_lanes; i++) {
    uds[i / DEF_NUM_LANES]->readScratchPadBank(i % DEF_NUM_LANES, &data[lm_offset]);
    lm_offset += DEF_SPMEM_BANK_SIZE;
  }

  fseek(spd_file, 0, SEEK_SET);
  // Write 'F' to indicate dump by Fastsim
  fwrite("F", sizeof(char), 1, spd_file);
  // Write 'L' to indicate LM dump
  fwrite("L", sizeof(char), 1, spd_file);
  // Write dump start file offset
  uint64_t dump_start_file_offset = 1 + 1 + 8 + 8 + 8 + 8;
  fwrite(&dump_start_file_offset, sizeof(uint64_t), 1, spd_file);
  BASIM_INFOMSG("LM Dump start file offset: %lu", dump_start_file_offset);
  // Write dump start nwid (ud_name only)
  uint64_t dump_nwid = start_nwid.get_NetworkId_UdName();
  fwrite(&dump_nwid, sizeof(uint64_t), 1, spd_file);
  BASIM_INFOMSG("LM Dump start nwid: %lu", dump_nwid);
  // Write num lanes dumped
  if (start_nwid.get_NetworkId_UdName() == 0 && num_lanes == 0) {
    num_lanes = this->MachineConfig.NumLanes * this->MachineConfig.NumUDs * this->MachineConfig.NumStacks * this->MachineConfig.NumNodes;
  }
  fwrite(&num_lanes, sizeof(uint64_t), 1, spd_file);
  BASIM_INFOMSG("LM Dump num lanes: %lu", num_lanes);
  // Write LM size per lane
  fwrite(&lane_lm_size, sizeof(uint64_t), 1, spd_file);
  BASIM_INFOMSG("LM Dump size per lane: %lu", lane_lm_size);
  // Write size bytes into mem_file
  fwrite(data, sizeof(uint8_t), total_lm_size, spd_file);
  fclose(spd_file);

  free(data);
}

std::pair<networkid_t, uint64_t> BASimUDRuntime_t::loadLocalMemory(const char* filename, networkid_t start_nwid, uint64_t num_lanes) {

  BASIM_ERROR_IF(this->isRemoteNodeMPI(start_nwid.get_NodeId()), "Only local nodes have access to the local memory.");

  size_t loadedBytes; // just to prevent compiler warnings
  FILE* spd_file = fopen(filename, "rb");
  BASIM_ERROR_IF(!spd_file, "Could not open %s\n", filename);

  fseek(spd_file, 0, SEEK_SET);
  // Read 'F' to indicate dump by Fastsim
  char dump_type;
  loadedBytes = fread(&dump_type, sizeof(char), 1, spd_file);
  UPDOWN_ERROR_IF(dump_type != 'F', "DRAM dump load failed! Not a FastSim dump file!\n");
  // Read 'L' to indicate LM dump
  loadedBytes = fread(&dump_type, sizeof(char), 1, spd_file);
  UPDOWN_ERROR_IF(dump_type != 'L', "DRAM dump load failed! Not a LM dump file!\n");
  // Read dump start file offset
  uint64_t dump_start_file_offset;
  loadedBytes = fread(&dump_start_file_offset, sizeof(uint64_t), 1, spd_file);
  BASIM_INFOMSG("LM Dump start file offset: %lu", dump_start_file_offset);
  // Read dump start nwid (ud_name only)
  uint64_t dump_start_nwid_raw;
  loadedBytes = fread(&dump_start_nwid_raw, sizeof(uint64_t), 1, spd_file);
  networkid_t dump_start_nwid(dump_start_nwid_raw, false, 0);
  BASIM_INFOMSG("LM Dump start nwid (from dump file): %lu", dump_start_nwid_raw);
  // Read num lanes dumped
  uint64_t dump_num_lanes;
  loadedBytes = fread(&dump_num_lanes, sizeof(uint64_t), 1, spd_file);
  BASIM_INFOMSG("LM Dump num lanes (from dump file): %lu", dump_num_lanes);
  // Read LM size per lane
  uint64_t lane_lm_size;
  loadedBytes = fread(&lane_lm_size, sizeof(uint64_t), 1, spd_file);
  BASIM_INFOMSG("LM Dump size per lane (from dump file): %lu", lane_lm_size);

  // Copy it lm by lm
  fseek(spd_file, dump_start_file_offset, SEEK_SET);
  uint8_t *data = nullptr;
  if (start_nwid.get_NetworkId_UdName() == 0 && num_lanes == 0) {
    // LM specified from the dump
    uint64_t total_lm_size = dump_num_lanes * lane_lm_size;
    data = (uint8_t*)malloc(total_lm_size * sizeof(uint8_t));
    loadedBytes = fread(data, sizeof(uint8_t), total_lm_size, spd_file);
    uint64_t lm_offset = 0;
    for (uint32_t i = dump_start_nwid.get_NetworkId_UdName(); i < dump_start_nwid.get_NetworkId_UdName() + dump_num_lanes; i++) {
      uds[i / DEF_NUM_LANES]->writeScratchPadBank(i % DEF_NUM_LANES, &data[lm_offset]);
      lm_offset += DEF_SPMEM_BANK_SIZE;
    }
  } else {
    // all LMs
    uint64_t total_lm_size = num_lanes * DEF_SPMEM_BANK_SIZE;
    data = (uint8_t*)malloc(total_lm_size * sizeof(uint8_t));
    loadedBytes = fread(data, sizeof(uint8_t), total_lm_size, spd_file);
    uint64_t lm_offset = 0;
    for (uint32_t i = start_nwid.get_NetworkId_UdName(); i < start_nwid.get_NetworkId_UdName() + num_lanes; i++) {
      uds[i / DEF_NUM_LANES]->writeScratchPadBank(i % DEF_NUM_LANES, &data[lm_offset]);
      lm_offset += DEF_SPMEM_BANK_SIZE;
    }
  }

  fclose(spd_file);
  free(data);

  if (start_nwid.get_NetworkId_UdName() == 0 && num_lanes == 0) {
    return std::make_pair(dump_start_nwid, dump_num_lanes);
  } else {
    return std::make_pair(start_nwid, num_lanes);
  }
}

void BASimUDRuntime_t::reset_stats(uint32_t ud_id, uint8_t lane_id){
  this->uds[ud_id]->resetStats(lane_id);
}

void BASimUDRuntime_t::reset_stats(uint32_t ud_id){
  this->uds[ud_id]->resetStats();
}

void BASimUDRuntime_t::reset_stats(){
  if(this->getRank() == 0) {
    // send the request to the other MPI instances
    for(uint32_t rank=1; rank<this->getMPIProcesses(); ++rank) {
      MPI_Send(nullptr, 0, MPI_UINT64_T, rank, MPI_TAG_RESET_STATS, MPI_COMM_WORLD);
    }
  }

  #ifndef GEM5_MODE
    #pragma omp parallel for // ud level parallelism
    for (int ud = 0; ud < this->udsPerRuntime; ud++)
      this->uds[ud]->resetStats();
  #else
    for (int ud = 0; ud < this->udsPerRuntime; ud++)
      this->uds[ud]->resetStats();
  #endif
}

void BASimUDRuntime_t::update_stats(uint32_t lane_num) {
  uint8_t lane_id = lane_num % 64;
  uint32_t ud_id = lane_num / 64;
  this->update_stats(ud_id, lane_id);
}

void BASimUDRuntime_t::update_stats(uint32_t ud_id, uint8_t lane_num) {

  const basim::LaneStats* loc_stats = uds[ud_id]->getLaneStats(lane_num);
  uint32_t lane_id = lane_num; 
  this->simStats[ud_id][lane_id].cycle_count = loc_stats->cycle_count;
  this->simStats[ud_id][lane_id].inst_count = loc_stats->inst_count;  
  this->simStats[ud_id][lane_id].tran_count = loc_stats->tran_count;
  this->simStats[ud_id][lane_id].thread_count = loc_stats->thread_count;
  this->simStats[ud_id][lane_id].max_thread_count = loc_stats->max_thread_count;
  this->simStats[ud_id][lane_id].cycles_gt128th = loc_stats->cycles_gt128th;
  this->simStats[ud_id][lane_id].inst_count_atomic = loc_stats->inst_count_atomic;
  this->simStats[ud_id][lane_id].inst_count_bitwise = loc_stats->inst_count_bitwise;
  this->simStats[ud_id][lane_id].inst_count_ctrlflow = loc_stats->inst_count_ctrlflow;
  this->simStats[ud_id][lane_id].inst_count_datmov = loc_stats->inst_count_datmov; 
  this->simStats[ud_id][lane_id].inst_count_ev = loc_stats->inst_count_ev;
  this->simStats[ud_id][lane_id].inst_count_fparith = loc_stats->inst_count_fparith;
  this->simStats[ud_id][lane_id].inst_count_hash = loc_stats->inst_count_hash;
  this->simStats[ud_id][lane_id].inst_count_intarith = loc_stats->inst_count_intarith;
  this->simStats[ud_id][lane_id].inst_count_intcmp = loc_stats->inst_count_intcmp;
  this->simStats[ud_id][lane_id].inst_count_msg = loc_stats->inst_count_msg;
  this->simStats[ud_id][lane_id].inst_count_threadctrl = loc_stats->inst_count_threadctrl;
  this->simStats[ud_id][lane_id].inst_count_tranctrl = loc_stats->inst_count_tranctrl;
  this->simStats[ud_id][lane_id].inst_count_vec = loc_stats->inst_count_vec;
  this->simStats[ud_id][lane_id].tran_count_basic = loc_stats->tran_count_basic;
  this->simStats[ud_id][lane_id].tran_count_majority = loc_stats->tran_count_majority;
  this->simStats[ud_id][lane_id].tran_count_default = loc_stats->tran_count_default;
  this->simStats[ud_id][lane_id].tran_count_epsilon = loc_stats->tran_count_epsilon;
  this->simStats[ud_id][lane_id].tran_count_common = loc_stats->tran_count_common;
  this->simStats[ud_id][lane_id].tran_count_flagged = loc_stats->tran_count_flagged;
  this->simStats[ud_id][lane_id].tran_count_refill = loc_stats->tran_count_refill;
  this->simStats[ud_id][lane_id].tran_count_event = loc_stats->tran_count_event;
  this->simStats[ud_id][lane_id].tran_count_other_node = loc_stats->tran_count_other_node;
  this->simStats[ud_id][lane_id].tran_bytes_other_node = loc_stats->tran_bytes_other_node;
  this->simStats[ud_id][lane_id].dram_store_count_other_node = loc_stats->dram_store_count_other_node;
  this->simStats[ud_id][lane_id].dram_load_count_other_node = loc_stats->dram_load_count_other_node;
  this->simStats[ud_id][lane_id].dram_store_bytes_other_node = loc_stats->dram_store_bytes_other_node;
  this->simStats[ud_id][lane_id].dram_load_bytes_other_node = loc_stats->dram_load_bytes_other_node;
  this->simStats[ud_id][lane_id].dram_store_ack_count_other_node = loc_stats->dram_store_ack_count_other_node;
  this->simStats[ud_id][lane_id].dram_load_ack_count_other_node = loc_stats->dram_load_ack_count_other_node;
  this->simStats[ud_id][lane_id].dram_store_ack_bytes_other_node = loc_stats->dram_store_ack_bytes_other_node;
  this->simStats[ud_id][lane_id].dram_load_ack_bytes_other_node = loc_stats->dram_load_ack_bytes_other_node;
#ifdef DETAIL_STATS
  this->simStats[ud_id][lane_id].max_inst_count_per_event = loc_stats->max_inst_per_event;
  this->simStats[ud_id][lane_id].max_inst_count_per_tx = loc_stats->max_inst_per_tx;
#endif
  this->simStats[ud_id][lane_id].lm_load_bytes = loc_stats->lm_load_bytes;
  this->simStats[ud_id][lane_id].lm_store_bytes = loc_stats->lm_store_bytes;
  this->simStats[ud_id][lane_id].lm_load_count = loc_stats->lm_load_count;
  this->simStats[ud_id][lane_id].lm_store_count = loc_stats->lm_store_count;
  this->simStats[ud_id][lane_id].dram_load_bytes = loc_stats->dram_load_bytes;
  this->simStats[ud_id][lane_id].dram_store_bytes = loc_stats->dram_store_bytes;
  this->simStats[ud_id][lane_id].dram_load_count = loc_stats->dram_load_count;
  this->simStats[ud_id][lane_id].dram_store_count = loc_stats->dram_store_count;
  this->simStats[ud_id][lane_id].eventq_len_max = loc_stats->eventq_len_max;
  this->simStats[ud_id][lane_id].opbuff_len_max = loc_stats->opbuff_len_max;
  //for (int i = 0; i < 16; i++) {
  //  this->simStats[ud_id][lane_num].user_counter[i] = loc_stats->user_counter[i];
  //}
}

struct BASimStats& BASimUDRuntime_t::get_stats(uint32_t ud_id, uint8_t lane_num){
  update_stats(ud_id, lane_num);
  return this->simStats[ud_id][lane_num];
}

struct BASimStats& BASimUDRuntime_t::get_stats(uint32_t lane_num){
  uint8_t lane_id = lane_num % 64;
  uint32_t ud_id = lane_num / 64;
  return this->get_stats(ud_id, lane_id);
}

void BASimUDRuntime_t::print_stats() {
  if(this->getRank() == 0) {
    // send the request to the other MPI instances
    for(uint32_t rank=1; rank<this->getMPIProcesses(); ++rank) {
      MPI_Send(nullptr, 0, MPI_UINT64_T, rank, MPI_TAG_PRINT_STATS, MPI_COMM_WORLD);
    }
  }

  // We use a barrier here to pretty print the statistics and to prevent that multiple
  // ranks output interleaved text. It might be slow, but it makes analysis so much easier,
  // when the text is not jumbled up, right?
  for(uint32_t rank=0; rank<this->getMPIProcesses(); ++rank) {
    MPI_Barrier(MPI_COMM_WORLD);
    if(rank == this->getRank()) {
      for(uint32_t i=0; i<this->udsPerRuntime*this->MachineConfig.NumLanes; ++i) {
        print_stats(i);
      }
    }
  }
}

void BASimUDRuntime_t::print_stats(uint32_t nwid){
  uint8_t lane_id = nwid % 64;
  uint32_t ud_id = nwid / 64;
  print_stats(ud_id, lane_id);
}

void BASimUDRuntime_t::print_stats(uint32_t ud_id, uint8_t lane_num) {
  const int wid = 10;
  const basim::LaneStats* lnstats = uds[ud_id]->getLaneStats(lane_num);
  
  ud_id += this->getRank() * this->udsPerRuntime;

  printf("[BASIM_GLOBAL]: Curr_Sim_Cycle:%lu\n", this->simTicks);
  printf("[UD%d-L%d] Cycles               =%lu\n", ud_id, lane_num, static_cast<uint64_t>(lnstats->cycle_count));
  printf("[UD%d-L%d] InstructionCount     =%lu\n", ud_id, lane_num, lnstats->inst_count); 
  printf("[UD%d-L%d] TransitionCount      =%lu\n", ud_id, lane_num, lnstats->tran_count);
  printf("[UD%d-L%d] ThreadCount          =%lu\n", ud_id, lane_num, lnstats->thread_count);
  printf("[UD%d-L%d] MaxThreadCount       =%lu\n", ud_id, lane_num, lnstats->max_thread_count);
  printf("[UD%d-L%d] Cycles (>128threads) =%lu\n", ud_id, lane_num, lnstats->cycles_gt128th);
  printf("[UD%d-L%d] AtomicInstructions   =%lu\n", ud_id, lane_num, lnstats->inst_count_atomic);
  printf("[UD%d-L%d] BitWiseInstructions  =%lu\n", ud_id, lane_num, lnstats->inst_count_bitwise);
  printf("[UD%d-L%d] CtrlFlowInstructions =%lu\n", ud_id, lane_num, lnstats->inst_count_ctrlflow);
  printf("[UD%d-L%d] DataMovInstructions  =%lu\n", ud_id, lane_num, lnstats->inst_count_datmov);
  printf("[UD%d-L%d] EvInstructions       =%lu\n", ud_id, lane_num, lnstats->inst_count_ev);
  printf("[UD%d-L%d] FPArithInstructions  =%lu\n", ud_id, lane_num, lnstats->inst_count_fparith);
  printf("[UD%d-L%d] HashInstructions     =%lu\n", ud_id, lane_num, lnstats->inst_count_hash);
  printf("[UD%d-L%d] IntArithInstructions =%lu\n", ud_id, lane_num, lnstats->inst_count_intarith);
  printf("[UD%d-L%d] IntCompInstructions  =%lu\n", ud_id, lane_num, lnstats->inst_count_intcmp);
  printf("[UD%d-L%d] MsgInstructions      =%lu\n", ud_id, lane_num, lnstats->inst_count_msg);
  printf("[UD%d-L%d] MsgInstructions(Mem) =%lu\n", ud_id, lane_num, lnstats->inst_count_msg_mem);
  printf("[UD%d-L%d] MsgInstructions(Lane)=%lu\n", ud_id, lane_num, lnstats->inst_count_msg_lane);
  printf("[UD%d-L%d] ThrdCtrlInstructions =%lu\n", ud_id, lane_num, lnstats->inst_count_threadctrl);
  printf("[UD%d-L%d] TranCtrlInstructions =%lu\n", ud_id, lane_num, lnstats->inst_count_tranctrl);
  printf("[UD%d-L%d] VectorInstructions   =%lu\n", ud_id, lane_num, lnstats->inst_count_vec);
  printf("[UD%d-L%d] BasicTransitions     =%lu\n", ud_id, lane_num, lnstats->tran_count_basic);
  printf("[UD%d-L%d] MajorityTransitions  =%lu\n", ud_id, lane_num, lnstats->tran_count_majority);
  printf("[UD%d-L%d] DefaultTransitions   =%lu\n", ud_id, lane_num, lnstats->tran_count_default);
  printf("[UD%d-L%d] EpsilonTransitions   =%lu\n", ud_id, lane_num, lnstats->tran_count_epsilon);
  printf("[UD%d-L%d] CommonTransitions    =%lu\n", ud_id, lane_num, lnstats->tran_count_common);
  printf("[UD%d-L%d] FlaggedTransitions   =%lu\n", ud_id, lane_num, lnstats->tran_count_flagged);
  printf("[UD%d-L%d] RefillTransitions    =%lu\n", ud_id, lane_num, lnstats->tran_count_refill);
  printf("[UD%d-L%d] EventTransitions     =%lu\n", ud_id, lane_num, lnstats->tran_count_event);
  printf("[UD%d-L%d] MessagesNodeCount    =%lu\n", ud_id, lane_num, lnstats->tran_count_other_node);
  printf("[UD%d-L%d] MessagesNodeBytes    =%lu\n", ud_id, lane_num, lnstats->tran_bytes_other_node);
  printf("[UD%d-L%d] DRAMStoreNodeCount   =%lu\n", ud_id, lane_num, lnstats->dram_store_count_other_node);
  printf("[UD%d-L%d] DRAMStoreNodeBytes   =%lu\n", ud_id, lane_num, lnstats->dram_store_bytes_other_node);
  printf("[UD%d-L%d] DRAMLoadNodeCount    =%lu\n", ud_id, lane_num, lnstats->dram_load_count_other_node);
  printf("[UD%d-L%d] DRAMLoadNodeBytes    =%lu\n", ud_id, lane_num, lnstats->dram_load_bytes_other_node);
  printf("[UD%d-L%d] DRAMStoreNodeAckCount   =%lu\n", ud_id, lane_num, lnstats->dram_store_ack_count_other_node);
  printf("[UD%d-L%d] DRAMStoreNodeAckBytes   =%lu\n", ud_id, lane_num, lnstats->dram_store_ack_bytes_other_node);
  printf("[UD%d-L%d] DRAMLoadNodeAckCount    =%lu\n", ud_id, lane_num, lnstats->dram_load_ack_count_other_node);
  printf("[UD%d-L%d] DRAMLoadNodeAckBytes    =%lu\n", ud_id, lane_num, lnstats->dram_load_ack_bytes_other_node);
#ifdef DETAIL_STATS
  printf("[UD%d-L%d] MaxInstCountPerEvent =%lu\n", ud_id, lane_num, lnstats->max_inst_per_event);
  printf("[UD%d-L%d] MaxInstCountPerTx    =%lu\n", ud_id, lane_num, lnstats->max_inst_per_tx);
#endif
  printf("[UD%d-L%d] LMLoadBytes          =%lu\n", ud_id, lane_num, lnstats->lm_load_bytes);
  printf("[UD%d-L%d] LMStoreBytes         =%lu\n", ud_id, lane_num, lnstats->lm_store_bytes);
  printf("[UD%d-L%d] LMLoadCount          =%lu\n", ud_id, lane_num, lnstats->lm_load_count);
  printf("[UD%d-L%d] LMStoreCount         =%lu\n", ud_id, lane_num, lnstats->lm_store_count);
  printf("[UD%d-L%d] DRAMLoadBytes        =%lu\n", ud_id, lane_num, lnstats->dram_load_bytes);
  printf("[UD%d-L%d] DRAMStoreBytes       =%lu\n", ud_id, lane_num, lnstats->dram_store_bytes);
  printf("[UD%d-L%d] DRAMLoadCount        =%lu\n", ud_id, lane_num, lnstats->dram_load_count);
  printf("[UD%d-L%d] DRAMStoreCount       =%lu\n", ud_id, lane_num, lnstats->dram_store_count);
  printf("[UD%d-L%d] MessageBytes         =%lu\n", ud_id, lane_num, lnstats->message_bytes);
  printf("[UD%d-L%d] EventQLenMax         =%lu\n", ud_id, lane_num, lnstats->eventq_len_max);
  printf("[UD%d-L%d] OperandQueueLenMax   =%lu\n", ud_id, lane_num, lnstats->opbuff_len_max);


  //for (int i = 0; i < 16; i++) {
  //  std::printf("[UD%d-L%d] user_counter%2d      = %*ld\n", ud_id, lane_num, i,
  //              wid, this->simStats[ud_id][lane_num].user_counter[i]);
  //}
}

/* Print the current simulation time in cycles  */
void BASimUDRuntime_t::print_curr_cycle(void){
  printf("[BASIM_GLOBAL]: Curr_Sim_Cycle:%lu\n", this->simTicks);
}

/* Reset the current simulation time to 0 cycles  */
void BASimUDRuntime_t::reset_curr_cycle(void){
  if(this->getRank() == 0) {
    for(uint32_t rank=1; rank<this->getMPIProcesses(); ++rank) {
      MPI_Send(nullptr, 0, MPI_UINT64_T, rank, MPI_TAG_RESET_CURR_CYCLE, MPI_COMM_WORLD);
    }
  }
  
  if(pthread_mutex_trylock(&mutex) == 0) {
    this->simTicks = 0;
    this->num_start_exe = 0;
  }
  pthread_mutex_unlock(&mutex);
  printf("[BASIM_GLOBAL]: Reset Curr_Sim_Cycle: %lu\n", this->simTicks);
}


void BASimUDRuntime_t::print_node_stats() {

  if(this->getRank() == 0) {
    for(uint32_t rank=1; rank<this->getMPIProcesses(); ++rank) {
      MPI_Send(nullptr, 0, MPI_UINT64_T, rank, MPI_TAG_PRINT_NODE_STATS, MPI_COMM_WORLD);
    }
  }

  // We use a barrier here to pretty print the statistics and to prevent that multiple
  // ranks output interleaved text. It might be slow, but it makes analysis so much easier,
  // when the text is not jumbled up, right?
  for(uint32_t rank=0; rank<this->getMPIProcesses(); ++rank) {
    MPI_Barrier(MPI_COMM_WORLD);
    if(rank == this->getRank()) {
      for(uint32_t srcNodeID=0; srcNodeID<this->nodesPerRuntime; ++srcNodeID) {
        this->print_node_stats(srcNodeID);
      }
    }
  }
}


void BASimUDRuntime_t::print_node_stats(uint32_t srcNodeID) {
    uint32_t srcNodeIDText = srcNodeID + this->getRank() * this->nodesPerRuntime;
    #ifdef DETAIL_STATS

        printf("[Node%d] PeakTotalCrossNodeCount  = %lu\n", srcNodeIDText, this->simNodeStats[srcNodeID].max_counts[0]->load());
        printf("[Node%d] PeakTotalCrossNodeBytes  = %lu\n", srcNodeIDText, this->simNodeStats[srcNodeID].max_bytes[0]->load());
        printf("[Node%d] MaxQueueSize  = %lu\n", srcNodeIDText, this->simNodeStats[srcNodeID].max_queue_size[0]->load());
        printf("[Node%d] AvgQueueSize  = %.2f\n", srcNodeIDText, this->simNodeStats[srcNodeID].total_queue_size[0]->load()/num_start_exe);

        for(uint32_t dstNodeID=0; dstNodeID<this->MachineConfig.NumNodes; ++dstNodeID) {

            if(srcNodeID == dstNodeID) {
                continue;
            }

            printf("[Node%d->%d] TotalNodeCount  = %lu\n", srcNodeIDText, dstNodeID, this->simNodeStats[srcNodeID].total_count_other_node[dstNodeID]->load());
            printf("[Node%d->%d] TotalNodeBytes  = %lu\n", srcNodeIDText, dstNodeID, this->simNodeStats[srcNodeID].total_bytes_other_node[dstNodeID]->load());
            printf("[Node%d->%d] MessagesNodeCount  = %lu\n", srcNodeIDText, dstNodeID, this->simNodeStats[srcNodeID].tran_count_other_node[dstNodeID]->load());
            printf("[Node%d->%d] MessagesNodeBytes  = %lu\n", srcNodeIDText, dstNodeID, this->simNodeStats[srcNodeID].tran_bytes_other_node[dstNodeID]->load());
            printf("[Node%d->%d] DRAMStoreNodeCount = %lu\n", srcNodeIDText, dstNodeID, this->simNodeStats[srcNodeID].dram_store_count_other_node[dstNodeID]->load());
            printf("[Node%d->%d] DRAMStoreNodeBytes = %lu\n", srcNodeIDText, dstNodeID, this->simNodeStats[srcNodeID].dram_store_bytes_other_node[dstNodeID]->load());
            printf("[Node%d->%d] DRAMLoadNodeCount  = %lu\n", srcNodeIDText, dstNodeID, this->simNodeStats[srcNodeID].dram_load_count_other_node[dstNodeID]->load());
            printf("[Node%d->%d] DRAMLoadNodeBytes  = %lu\n", srcNodeIDText, dstNodeID, this->simNodeStats[srcNodeID].dram_load_bytes_other_node[dstNodeID]->load());
            printf("[Node%d->%d] DRAMStoreNodeAckCount = %lu\n", srcNodeIDText, dstNodeID, this->simNodeStats[srcNodeID].dram_store_ack_count_other_node[dstNodeID]->load());
            printf("[Node%d->%d] DRAMStoreNodeAckBytes = %lu\n", srcNodeIDText, dstNodeID, this->simNodeStats[srcNodeID].dram_store_ack_bytes_other_node[dstNodeID]->load());
            printf("[Node%d->%d] DRAMLoadNodeAckCount  = %lu\n", srcNodeIDText, dstNodeID, this->simNodeStats[srcNodeID].dram_load_ack_count_other_node[dstNodeID]->load());
            printf("[Node%d->%d] DRAMLoadNodeAckBytes  = %lu\n", srcNodeIDText, dstNodeID, this->simNodeStats[srcNodeID].dram_load_ack_bytes_other_node[dstNodeID]->load());

            printf("[Node%d->%d] PeakTotalNodeCount  = %lu\n", srcNodeIDText, dstNodeID, this->simNodeStats[srcNodeID].max_total_count_other_node[dstNodeID]->load());
            printf("[Node%d->%d] PeakTotalNodeBytes  = %lu\n", srcNodeIDText, dstNodeID, this->simNodeStats[srcNodeID].max_total_bytes_other_node[dstNodeID]->load());
            printf("[Node%d->%d] PeakMessagesNodeCount  = %lu\n", srcNodeIDText, dstNodeID, this->simNodeStats[srcNodeID].max_tran_count_other_node[dstNodeID]->load());
            printf("[Node%d->%d] PeakMessagesNodeBytes  = %lu\n", srcNodeIDText, dstNodeID, this->simNodeStats[srcNodeID].max_tran_bytes_other_node[dstNodeID]->load());
            printf("[Node%d->%d] PeakDRAMStoreNodeCount = %lu\n", srcNodeIDText, dstNodeID, this->simNodeStats[srcNodeID].max_dram_store_count_other_node[dstNodeID]->load());
            printf("[Node%d->%d] PeakDRAMStoreNodeBytes = %lu\n", srcNodeIDText, dstNodeID, this->simNodeStats[srcNodeID].max_dram_store_bytes_other_node[dstNodeID]->load());
            printf("[Node%d->%d] PeakDRAMLoadNodeCount  = %lu\n", srcNodeIDText, dstNodeID, this->simNodeStats[srcNodeID].max_dram_load_count_other_node[dstNodeID]->load());
            printf("[Node%d->%d] PeakDRAMLoadNodeBytes  = %lu\n", srcNodeIDText, dstNodeID, this->simNodeStats[srcNodeID].max_dram_load_bytes_other_node[dstNodeID]->load());
            printf("[Node%d->%d] PeakDRAMStoreNodeAckCount = %lu\n", srcNodeIDText, dstNodeID, this->simNodeStats[srcNodeID].max_dram_store_ack_count_other_node[dstNodeID]->load());
            printf("[Node%d->%d] PeakDRAMStoreNodeAckBytes = %lu\n", srcNodeIDText, dstNodeID, this->simNodeStats[srcNodeID].max_dram_store_ack_bytes_other_node[dstNodeID]->load());
            printf("[Node%d->%d] PeakDRAMLoadNodeAckCount  = %lu\n", srcNodeIDText, dstNodeID, this->simNodeStats[srcNodeID].max_dram_load_ack_count_other_node[dstNodeID]->load());
            printf("[Node%d->%d] PeakDRAMLoadNodeAckBytes  = %lu\n", srcNodeIDText, dstNodeID, this->simNodeStats[srcNodeID].max_dram_load_ack_bytes_other_node[dstNodeID]->load());

            printf("[Node%d->%d] TotalPacketSizeHistogram  = [%lu, %lu, %lu, %lu, %lu, %lu, %lu, %lu, %lu, %lu, %lu, %lu]\n", srcNodeIDText, dstNodeID, this->simNodeStats[srcNodeID].total_packet_size_other_node_histogram[dstNodeID][0]->load(), this->simNodeStats[srcNodeID].total_packet_size_other_node_histogram[dstNodeID][1]->load(), this->simNodeStats[srcNodeID].total_packet_size_other_node_histogram[dstNodeID][2]->load(), this->simNodeStats[srcNodeID].total_packet_size_other_node_histogram[dstNodeID][3]->load(), this->simNodeStats[srcNodeID].total_packet_size_other_node_histogram[dstNodeID][4]->load(), this->simNodeStats[srcNodeID].total_packet_size_other_node_histogram[dstNodeID][5]->load(), this->simNodeStats[srcNodeID].total_packet_size_other_node_histogram[dstNodeID][6]->load(), this->simNodeStats[srcNodeID].total_packet_size_other_node_histogram[dstNodeID][7]->load(), this->simNodeStats[srcNodeID].total_packet_size_other_node_histogram[dstNodeID][8]->load(), this->simNodeStats[srcNodeID].total_packet_size_other_node_histogram[dstNodeID][9]->load(), this->simNodeStats[srcNodeID].total_packet_size_other_node_histogram[dstNodeID][10]->load(), this->simNodeStats[srcNodeID].total_packet_size_other_node_histogram[dstNodeID][11]->load());
            printf("[Node%d->%d] TranPacketSizeHistogram  = [%lu, %lu, %lu, %lu, %lu, %lu, %lu, %lu, %lu, %lu, %lu, %lu]\n", srcNodeIDText, dstNodeID, this->simNodeStats[srcNodeID].tran_packet_size_other_node_histogram[dstNodeID][0]->load(), this->simNodeStats[srcNodeID].tran_packet_size_other_node_histogram[dstNodeID][1]->load(), this->simNodeStats[srcNodeID].tran_packet_size_other_node_histogram[dstNodeID][2]->load(), this->simNodeStats[srcNodeID].tran_packet_size_other_node_histogram[dstNodeID][3]->load(), this->simNodeStats[srcNodeID].tran_packet_size_other_node_histogram[dstNodeID][4]->load(), this->simNodeStats[srcNodeID].tran_packet_size_other_node_histogram[dstNodeID][5]->load(), this->simNodeStats[srcNodeID].tran_packet_size_other_node_histogram[dstNodeID][6]->load(), this->simNodeStats[srcNodeID].tran_packet_size_other_node_histogram[dstNodeID][7]->load(), this->simNodeStats[srcNodeID].tran_packet_size_other_node_histogram[dstNodeID][8]->load(), this->simNodeStats[srcNodeID].tran_packet_size_other_node_histogram[dstNodeID][9]->load(), this->simNodeStats[srcNodeID].tran_packet_size_other_node_histogram[dstNodeID][10]->load(), this->simNodeStats[srcNodeID].tran_packet_size_other_node_histogram[dstNodeID][11]->load());
            printf("[Node%d->%d] DramLoadPacketSizeHistogram  = [%lu, %lu, %lu, %lu, %lu, %lu, %lu, %lu, %lu, %lu, %lu, %lu]\n", srcNodeIDText, dstNodeID, this->simNodeStats[srcNodeID].dram_load_packet_size_other_node_histogram[dstNodeID][0]->load(), this->simNodeStats[srcNodeID].dram_load_packet_size_other_node_histogram[dstNodeID][1]->load(), this->simNodeStats[srcNodeID].dram_load_packet_size_other_node_histogram[dstNodeID][2]->load(), this->simNodeStats[srcNodeID].dram_load_packet_size_other_node_histogram[dstNodeID][3]->load(), this->simNodeStats[srcNodeID].dram_load_packet_size_other_node_histogram[dstNodeID][4]->load(), this->simNodeStats[srcNodeID].dram_load_packet_size_other_node_histogram[dstNodeID][5]->load(), this->simNodeStats[srcNodeID].dram_load_packet_size_other_node_histogram[dstNodeID][6]->load(), this->simNodeStats[srcNodeID].dram_load_packet_size_other_node_histogram[dstNodeID][7]->load(), this->simNodeStats[srcNodeID].dram_load_packet_size_other_node_histogram[dstNodeID][8]->load(), this->simNodeStats[srcNodeID].dram_load_packet_size_other_node_histogram[dstNodeID][9]->load(), this->simNodeStats[srcNodeID].dram_load_packet_size_other_node_histogram[dstNodeID][10]->load(), this->simNodeStats[srcNodeID].dram_load_packet_size_other_node_histogram[dstNodeID][11]->load());
            printf("[Node%d->%d] DramLoadAckPacketSizeHistogram  = [%lu, %lu, %lu, %lu, %lu, %lu, %lu, %lu, %lu, %lu, %lu, %lu]\n", srcNodeIDText, dstNodeID, this->simNodeStats[srcNodeID].dram_load_ack_packet_size_other_node_histogram[dstNodeID][0]->load(), this->simNodeStats[srcNodeID].dram_load_ack_packet_size_other_node_histogram[dstNodeID][1]->load(), this->simNodeStats[srcNodeID].dram_load_ack_packet_size_other_node_histogram[dstNodeID][2]->load(), this->simNodeStats[srcNodeID].dram_load_ack_packet_size_other_node_histogram[dstNodeID][3]->load(), this->simNodeStats[srcNodeID].dram_load_ack_packet_size_other_node_histogram[dstNodeID][4]->load(), this->simNodeStats[srcNodeID].dram_load_ack_packet_size_other_node_histogram[dstNodeID][5]->load(), this->simNodeStats[srcNodeID].dram_load_ack_packet_size_other_node_histogram[dstNodeID][6]->load(), this->simNodeStats[srcNodeID].dram_load_ack_packet_size_other_node_histogram[dstNodeID][7]->load(), this->simNodeStats[srcNodeID].dram_load_ack_packet_size_other_node_histogram[dstNodeID][8]->load(), this->simNodeStats[srcNodeID].dram_load_ack_packet_size_other_node_histogram[dstNodeID][9]->load(), this->simNodeStats[srcNodeID].dram_load_ack_packet_size_other_node_histogram[dstNodeID][10]->load(), this->simNodeStats[srcNodeID].dram_load_ack_packet_size_other_node_histogram[dstNodeID][11]->load());
            printf("[Node%d->%d] DramStorePacketSizeHistogram  = [%lu, %lu, %lu, %lu, %lu, %lu, %lu, %lu, %lu, %lu, %lu, %lu]\n", srcNodeIDText, dstNodeID, this->simNodeStats[srcNodeID].dram_store_packet_size_other_node_histogram[dstNodeID][0]->load(), this->simNodeStats[srcNodeID].dram_store_packet_size_other_node_histogram[dstNodeID][1]->load(), this->simNodeStats[srcNodeID].dram_store_packet_size_other_node_histogram[dstNodeID][2]->load(), this->simNodeStats[srcNodeID].dram_store_packet_size_other_node_histogram[dstNodeID][3]->load(), this->simNodeStats[srcNodeID].dram_store_packet_size_other_node_histogram[dstNodeID][4]->load(), this->simNodeStats[srcNodeID].dram_store_packet_size_other_node_histogram[dstNodeID][5]->load(), this->simNodeStats[srcNodeID].dram_store_packet_size_other_node_histogram[dstNodeID][6]->load(), this->simNodeStats[srcNodeID].dram_store_packet_size_other_node_histogram[dstNodeID][7]->load(), this->simNodeStats[srcNodeID].dram_store_packet_size_other_node_histogram[dstNodeID][8]->load(), this->simNodeStats[srcNodeID].dram_store_packet_size_other_node_histogram[dstNodeID][9]->load(), this->simNodeStats[srcNodeID].dram_store_packet_size_other_node_histogram[dstNodeID][10]->load(), this->simNodeStats[srcNodeID].dram_store_packet_size_other_node_histogram[dstNodeID][11]->load());
            printf("[Node%d->%d] DramStoreAckPacketSizeHistogram  = [%lu, %lu, %lu, %lu, %lu, %lu, %lu, %lu, %lu, %lu, %lu, %lu]\n", srcNodeIDText, dstNodeID, this->simNodeStats[srcNodeID].dram_store_ack_packet_size_other_node_histogram[dstNodeID][0]->load(), this->simNodeStats[srcNodeID].dram_store_ack_packet_size_other_node_histogram[dstNodeID][1]->load(), this->simNodeStats[srcNodeID].dram_store_ack_packet_size_other_node_histogram[dstNodeID][2]->load(), this->simNodeStats[srcNodeID].dram_store_ack_packet_size_other_node_histogram[dstNodeID][3]->load(), this->simNodeStats[srcNodeID].dram_store_ack_packet_size_other_node_histogram[dstNodeID][4]->load(), this->simNodeStats[srcNodeID].dram_store_ack_packet_size_other_node_histogram[dstNodeID][5]->load(), this->simNodeStats[srcNodeID].dram_store_ack_packet_size_other_node_histogram[dstNodeID][6]->load(), this->simNodeStats[srcNodeID].dram_store_ack_packet_size_other_node_histogram[dstNodeID][7]->load(), this->simNodeStats[srcNodeID].dram_store_ack_packet_size_other_node_histogram[dstNodeID][8]->load(), this->simNodeStats[srcNodeID].dram_store_ack_packet_size_other_node_histogram[dstNodeID][9]->load(), this->simNodeStats[srcNodeID].dram_store_ack_packet_size_other_node_histogram[dstNodeID][10]->load(), this->simNodeStats[srcNodeID].dram_store_ack_packet_size_other_node_histogram[dstNodeID][11]->load());
        }
    #endif

    // print memory stack stats
    for(uint32_t stid = 0; stid < this->MachineConfig.NumStacks; stid++){
      const basim::StackStats* ststats = udMems[srcNodeID]->getStackStats(stid);
      printf("[Node%d-S%d] DRAMStackLoadBytes        =%lu\n", srcNodeIDText, stid, ststats->dram_load_bytes);
      printf("[Node%d-S%d] DRAMStackStoreBytes       =%lu\n", srcNodeIDText, stid, ststats->dram_store_bytes);
      printf("[Node%d-S%d] DRAMStackLoadCount        =%lu\n", srcNodeIDText, stid, ststats->dram_load_count);
      printf("[Node%d-S%d] DRAMStackStoreCount       =%lu\n", srcNodeIDText, stid, ststats->dram_store_count);
      printf("[Node%d-S%d] DRAMStackPeakLoadBytes    =%lu\n", srcNodeIDText, stid, ststats->peak_dram_load_bytes);
      printf("[Node%d-S%d] DRAMStackPeakStoreBytes   =%lu\n", srcNodeIDText, stid, ststats->peak_dram_store_bytes);
      printf("[Node%d-S%d] DRAMStackPeakLoadCount    =%lu\n", srcNodeIDText, stid, ststats->peak_dram_load_count);
      printf("[Node%d-S%d] DRAMStackPeakStoreCount   =%lu\n", srcNodeIDText, stid, ststats->peak_dram_store_count);
      printf("[Node%d-S%d] DRAMStackPeakLoadStoreCount  =%lu\n", srcNodeIDText, stid, ststats->peak_dram_load_store_count);
    }
}

void BASimUDRuntime_t::reset_node_stats() {
    if(this->getRank() == 0) {
        for(uint32_t rank=1; rank<this->getMPIProcesses(); ++rank) {
            MPI_Send(nullptr, 0, MPI_UINT64_T, rank, MPI_TAG_RESET_NODE_STATS, MPI_COMM_WORLD);
        }
    }

    for(uint32_t nodeID = 0; nodeID < this->nodesPerRuntime; nodeID++){
        #ifdef DETAIL_STATS
           this->simNodeStats[nodeID].reset();
        #endif
      
        // reset memory stack stats
        for(uint32_t stid = 0; stid < this->MachineConfig.NumStacks; stid++){
            basim::StackStats* ststats = udMems[nodeID]->getStackStats(stid);
            ststats->reset();
        }
    }
}

void BASimUDRuntime_t::reset_all_stats() {
    this->reset_stats();  // reset lane stats
    this->reset_node_stats(); // reset node and dram stack stats
    this->reset_curr_cycle(); // reset ticks
}



#ifdef INST_HIST
void BASimUDRuntime_t::print_inst_hist(const char* filename){
  std::ofstream csvfile;
  csvfile.open (filename);
  // sum up all lanes and report
  for (uint32_t ud = 0; ud < this->total_uds; ud++) {
    for (int ln = 0; ln < this->MachineConfig.NumLanes; ln++) {
      uint32_t* instCounts_loc = uds[ud]->getInstCount(ln);
      for(uint32_t inst = 0; inst < static_cast<uint32_t>(basim::InstMap::COUNT); inst++){
        instCounts[inst] += instCounts_loc[inst];
      }
    }
  }
  for(uint32_t inst = 0; inst < static_cast<uint32_t>(basim::InstMap::COUNT); inst++){
    csvfile << InstNames[inst] << "," << instCounts[inst] << "\n";
  }
  csvfile.close();
}
#endif


void BASimUDRuntime_t::db_exec(std::string sql) {
  #if defined (ENABLE_SQLITE)
  
  // Lock mutex only if SQLite is not thread-safe
  // Lock is automatically released, when lock is destructed (at the end of the method)
  std::unique_lock<std::mutex> lock(db_mutex, std::defer_lock);
  if(sqlite3_threadsafe() != 1) {
    lock.lock();
  }
  char* errMsg = 0;
  int rc = sqlite3_exec(this->stats_db, sql.c_str(), 0, 0, &errMsg);
  if (rc != SQLITE_OK) {
    std::string error = errMsg;
    sqlite3_exec(this->stats_db, "ROLLBACK;", 0, 0, &errMsg);
    sqlite3_free(errMsg);
    BASIM_ERROR("SQL error: %s (error code: %d)", error.c_str(), rc);
  }
  #else
    std::cerr << "ENABLE_SQLITE flag not set. Ignore exec database." << std::endl;
  #endif
}

int BASimUDRuntime_t::db_write_label(const char label[]) {
  #if defined (ENABLE_SQLITE)
    std::string table_name;
    std::string sql;
    
    // Create the labels table
    table_name = "labels";
    sql = "CREATE TABLE IF NOT EXISTS " + table_name + " ("
          "id INTEGER PRIMARY KEY AUTOINCREMENT, "
          "label TEXT NOT NULL UNIQUE, "
          "final_tick INTEGER, "
          "sim_ticks INTEGER"
          ");";
    db_exec(sql);

    // Insert the label into the labels table if it doesn't already exist
    sql = "INSERT OR IGNORE INTO " + table_name + " (label, final_tick, sim_ticks) VALUES ('" + std::string(label) + "', " + std::to_string(this->globalTick) + ", " + std::to_string(this->simTicks) + ");";
    db_exec(sql);
    

    // Update the final_tick and sim_ticks values if the label already exists
    sql = "UPDATE " + table_name + " SET final_tick = " + std::to_string(this->globalTick) + ", sim_ticks = " + std::to_string(this->simTicks) + " WHERE label = '" + std::string(label) + "';";
    db_exec(sql);

    // Get the ID of the label
    int label_id;
    sql = "SELECT id FROM " + table_name + " WHERE label = '" + std::string(label) + "';";
    char* errMsg = 0;
    int rc = sqlite3_exec(this->stats_db, sql.c_str(), [](void* data, int argc, char** argv, char** colName) -> int {
        *static_cast<int*>(data) = std::stoi(argv[0]);
        return 0;
    }, &label_id, &errMsg);
    if (rc != SQLITE_OK) {
      std::string error = errMsg;
      sqlite3_exec(this->stats_db, "ROLLBACK;", 0, 0, &errMsg);
      sqlite3_free(errMsg);
      BASIM_ERROR("SQL error: %s", error.c_str());
    }
    return label_id;
  #else
    std::cerr << "ENABLE_SQLITE flag not set. Ignore writing stats to database." << std::endl;
    return 0;
  #endif
}


void BASimUDRuntime_t::db_write_stats(const char label[]) {
    #if defined (ENABLE_SQLITE)
        if(this->getRank() == 0) {
            uint64_t len = strlen(label)+1;
            // send the request to the other MPI instances
            for(uint32_t rank=1; rank<this->getMPIProcesses(); ++rank) {
                MPI_Send(&len, 1, MPI_UINT64_T, rank, MPI_TAG_DB_WRITE_STATS, MPI_COMM_WORLD);
                MPI_Send(label, len, MPI_CHAR, rank, MPI_TAG_DB_WRITE_STATS_DATA, MPI_COMM_WORLD);
            }
        }

        db_write_stats(0, this->udsPerRuntime * this->MachineConfig.NumLanes, label);
    #endif
}


void BASimUDRuntime_t::db_write_stats(uint32_t start_nwid, uint32_t num_lanes, const char label[]) {

#if defined (ENABLE_SQLITE)
  std::string table_name;
  std::string sql;

  db_exec("BEGIN TRANSACTION;");
  int label_id = db_write_label(label);

  // Create the stats table
  table_name = "stats";
  sql = "CREATE TABLE IF NOT EXISTS " + table_name + " ("
        "id INTEGER PRIMARY KEY AUTOINCREMENT, "
        "label_id INTEGER NOT NULL, "
        "nwid INTEGER NOT NULL,"
        "Cycles INTEGER, "
        "InstructionCount INTEGER, "
        "TransitionCount INTEGER, "
        "ThreadCount INTEGER, "
        "MaxThreadCount INTEGER, "
        "Cycles_gt128th INTEGER, "
        "AtomicInstructions INTEGER, "
        "BitWiseInstructions INTEGER, "
        "CtrlFlowInstructions INTEGER, "
        "DataMovInstructions INTEGER, "
        "EvInstructions INTEGER, "
        "FPArithInstructions INTEGER, "
        "HashInstructions INTEGER, "
        "IntArithInstructions INTEGER, "
        "IntCompInstructions INTEGER, "
        "MsgInstructions INTEGER, "
        "MsgInstructionsMem INTEGER, "
        "MsgInstructionsLane INTEGER, "
        "ThrdCtrlInstructions INTEGER, "
        "TranCtrlInstructions INTEGER, "
        "VectorInstructions INTEGER, "
        "BasicTransitions INTEGER, "
        "MajorityTransitions INTEGER, "
        "DefaultTransitions INTEGER, "
        "EpsilonTransitions INTEGER, "
        "CommonTransitions INTEGER, "
        "FlaggedTransitions INTEGER, "
        "RefillTransitions INTEGER, "
        "EventTransitions INTEGER, "
        "MaxInstCountPerEvent INTEGER, "
        "MaxInstCountPerTx INTEGER, "
        "MessagesNodeCount INTEGER, "
        "MessagesNodeBytes INTEGER, "
        "DRAMStoreNodeCount INTEGER, "
        "DRAMStoreNodeBytes INTEGER, "
        "DRAMLoadNodeCount INTEGER, "
        "DRAMLoadNodeBytes INTEGER, "
        "DRAMStoreAckNodeCount INTEGER, "
        "DRAMStoreAckNodeBytes INTEGER, "
        "DRAMLoadAckNodeCount INTEGER, "
        "DRAMLoadAckNodeBytes INTEGER, "
        "LMLoadBytes INTEGER, "
        "LMStoreBytes INTEGER, "
        "LMLoadCount INTEGER, "
        "LMStoreCount INTEGER, "
        "DRAMLoadBytes INTEGER, "
        "DRAMStoreBytes INTEGER, "
        "DRAMLoadCount INTEGER, "
        "DRAMStoreCount INTEGER, "
        "MessageBytes INTEGER, "
        "EventQLenMax INTEGER, "
        "OperandQueueLenMax INTEGER, "
        "FOREIGN KEY(label_id) REFERENCES labels(id)"
        ");";
  db_exec(sql);

  #pragma omp parallel for
  for (uint32_t nwid = start_nwid; nwid < start_nwid + num_lanes; nwid++) {
    auto lnstats = uds[nwid/64]->getLaneStats(nwid%64);

    uint32_t nwidText = nwid + this->getRank() * this->udsPerRuntime * this->MachineConfig.NumLanes;

    // Construct the INSERT statement
    std::string sqlInsert = "INSERT INTO " + table_name + " (label_id, nwid, Cycles, InstructionCount, TransitionCount, ThreadCount, MaxThreadCount, "
          " Cycles_gt128th, AtomicInstructions, BitWiseInstructions, CtrlFlowInstructions, DataMovInstructions, EvInstructions, "
          "FPArithInstructions, HashInstructions, IntArithInstructions, IntCompInstructions, MsgInstructions, "
          "MsgInstructionsMem, MsgInstructionsLane, ThrdCtrlInstructions, TranCtrlInstructions, VectorInstructions, "
          "BasicTransitions, MajorityTransitions, DefaultTransitions, EpsilonTransitions, CommonTransitions, "
          "FlaggedTransitions, RefillTransitions, EventTransitions, "
          "MaxInstCountPerEvent, MaxInstCountPerTx, "
          "MessagesNodeCount, MessagesNodeBytes, "
          "DRAMStoreNodeCount, DRAMStoreNodeBytes, DRAMLoadNodeCount, DRAMLoadNodeBytes, "
          "DRAMStoreAckNodeCount, DRAMStoreAckNodeBytes, DRAMLoadAckNodeCount, DRAMLoadAckNodeBytes, "
          "LMLoadBytes, LMStoreBytes, LMLoadCount, LMStoreCount, DRAMLoadBytes, DRAMStoreBytes, DRAMLoadCount, "
          "DRAMStoreCount, MessageBytes, EventQLenMax, OperandQueueLenMax) VALUES ("
          + std::to_string(label_id) + ", " + std::to_string(nwidText) + ", " +
          std::to_string(lnstats->cycle_count) + ", " +
          std::to_string(lnstats->inst_count) + ", " +
          std::to_string(lnstats->tran_count) + ", " +
          std::to_string(lnstats->thread_count) + ", " +
          std::to_string(lnstats->max_thread_count) + ", " +
          std::to_string(lnstats->cycles_gt128th) + ", " +
          std::to_string(lnstats->inst_count_atomic) + ", " +
          std::to_string(lnstats->inst_count_bitwise) + ", " +
          std::to_string(lnstats->inst_count_ctrlflow) + ", " +
          std::to_string(lnstats->inst_count_datmov) + ", " +
          std::to_string(lnstats->inst_count_ev) + ", " +
          std::to_string(lnstats->inst_count_fparith) + ", " +
          std::to_string(lnstats->inst_count_hash) + ", " +
          std::to_string(lnstats->inst_count_intarith) + ", " +
          std::to_string(lnstats->inst_count_intcmp) + ", " +
          std::to_string(lnstats->inst_count_msg) + ", " +
          std::to_string(lnstats->inst_count_msg_mem) + ", " +
          std::to_string(lnstats->inst_count_msg_lane) + ", " +
          std::to_string(lnstats->inst_count_threadctrl) + ", " +
          std::to_string(lnstats->inst_count_tranctrl) + ", " +
          std::to_string(lnstats->inst_count_vec) + ", " +
          std::to_string(lnstats->tran_count_basic) + ", " +
          std::to_string(lnstats->tran_count_majority) + ", " +
          std::to_string(lnstats->tran_count_default) + ", " +
          std::to_string(lnstats->tran_count_epsilon) + ", " +
          std::to_string(lnstats->tran_count_common) + ", " +
          std::to_string(lnstats->tran_count_flagged) + ", " +
          std::to_string(lnstats->tran_count_refill) + ", " +
          std::to_string(lnstats->tran_count_event) + ", " +
          #ifdef DETAIL_STATS
            std::to_string(lnstats->max_inst_per_event) + ", " +
            std::to_string(lnstats->max_inst_per_tx) + ", " +
          #else
            "NULL, NULL, " +
          #endif
          std::to_string(lnstats->tran_count_other_node) + ", " +
          std::to_string(lnstats->tran_bytes_other_node) + ", " +
          std::to_string(lnstats->dram_store_count_other_node) + ", " +
          std::to_string(lnstats->dram_store_bytes_other_node) + ", " +
          std::to_string(lnstats->dram_load_count_other_node) + ", " +
          std::to_string(lnstats->dram_load_bytes_other_node) + ", " +
          std::to_string(lnstats->dram_store_ack_count_other_node) + ", " +
          std::to_string(lnstats->dram_store_ack_bytes_other_node) + ", " +
          std::to_string(lnstats->dram_load_ack_count_other_node) + ", " +
          std::to_string(lnstats->dram_load_ack_bytes_other_node) + ", " +
          std::to_string(lnstats->lm_load_bytes) + ", " +
          std::to_string(lnstats->lm_store_bytes) + ", " +
          std::to_string(lnstats->lm_load_count) + ", " +
          std::to_string(lnstats->lm_store_count) + ", " +
          std::to_string(lnstats->dram_load_bytes) + ", " +
          std::to_string(lnstats->dram_store_bytes) + ", " +
          std::to_string(lnstats->dram_load_count) + ", " +
          std::to_string(lnstats->dram_store_count) + ", " +
          std::to_string(lnstats->message_bytes) + ", " +
          std::to_string(lnstats->eventq_len_max) + ", " +
          std::to_string(lnstats->opbuff_len_max) + ");";

    db_exec(sqlInsert);
  }

  // Commit transaction
  db_exec("COMMIT;");
  int rc = sqlite3_wal_checkpoint(this->stats_db, NULL);
  if (rc != SQLITE_OK) {
      std::cerr << "Checkpoint failed: " << sqlite3_errmsg(this->stats_db) << std::endl;
  }
#else
  std::cerr << "ENABLE_SQLITE flag not set. Ignore writing stats to database." << std::endl;
#endif
}

void BASimUDRuntime_t::print_histograms(uint32_t ud_id, uint8_t lane_num) {
  #ifdef DETAIL_STATS
  const basim::LaneStats* lnstats = uds[ud_id]->getLaneStats(lane_num);
  printf("[UD%d-L%d] Inst_Per_Event_Histogram   =[",ud_id, lane_num);
  uint64_t loc_count;
  for(int i = 0; i < MAX_BINS/BUCKET_SIZE; i++){
    loc_count = 0;
    for(int j = i * BUCKET_SIZE; j < (i + 1)*BUCKET_SIZE; j++)
      loc_count += lnstats->inst_per_event[j];
    if (loc_count == 0) {
      continue;
    }
    printf("%d:%lu, ", i*BUCKET_SIZE, loc_count);
  }
  printf("]\n");
  printf("[UD%d-L%d] LM_Count_Per_Event_Histogram   =[",ud_id, lane_num);
  for(int i = 0; i < MAX_COUNT_BINS/COUNT_BUCKET_SIZE; i++){
    loc_count = 0;
    for(int j = i * COUNT_BUCKET_SIZE; j < (i + 1)*COUNT_BUCKET_SIZE; j++)
      loc_count += lnstats->lm_load_count_per_event[j] + lnstats->lm_store_count_per_event[j];
    if (loc_count == 0) {
      continue;
    }
    printf("%d:%lu, ", i*COUNT_BUCKET_SIZE, loc_count);
  }
  printf("]\n");
  printf("[UD%d-L%d] LM_Bytes_Per_Event_Histogram   =[",ud_id, lane_num);
  for(int i = 0; i < MAX_BYTES_BINS/BYTES_BUCKET_SIZE; i++){
    loc_count = 0;
    for(int j = i * BYTES_BUCKET_SIZE; j < (i + 1)*BYTES_BUCKET_SIZE; j++)
      loc_count += lnstats->lm_load_bytes_per_event[j] + lnstats->lm_store_bytes_per_event[j];
    if (loc_count == 0) {
      continue;
    }
    printf("%d:%lu, ", i*BYTES_BUCKET_SIZE, loc_count);
  }
  printf("]\n");
  printf("[UD%d-L%d] DRAM_Count_Per_Event_Histogram   =[",ud_id, lane_num);
  for(int i = 0; i < MAX_COUNT_BINS/COUNT_BUCKET_SIZE; i++){
    loc_count = 0;
    for(int j = i * COUNT_BUCKET_SIZE; j < (i + 1)*COUNT_BUCKET_SIZE; j++)
      loc_count += lnstats->dram_load_count_per_event[j] + lnstats->dram_store_count_per_event[j];
    if (loc_count == 0) {
      continue;
    }
    printf("%d:%lu, ", i*COUNT_BUCKET_SIZE, loc_count);
  }
  printf("]\n");
  printf("[UD%d-L%d] DRAM_Bytes_Per_Event_Histogram   =[",ud_id, lane_num);
  for(int i = 0; i < MAX_BYTES_BINS/BYTES_BUCKET_SIZE; i++){
    loc_count = 0;
    for(int j = i * BYTES_BUCKET_SIZE; j < (i + 1)*BYTES_BUCKET_SIZE; j++)
      loc_count += lnstats->dram_load_bytes_per_event[j] + lnstats->dram_store_bytes_per_event[j];
    if (loc_count == 0) {
      continue;
    }
    printf("%d:%lu, ", i*BYTES_BUCKET_SIZE, loc_count);
  }
  printf("]\n");
  #else
    std::cerr << "DETAIL_STATS flag not set. Ignore printing statistics." << std::endl;
  #endif
}

void BASimUDRuntime_t::print_histograms(uint32_t nwid) {
  print_histograms(nwid/64, nwid%64);
}

/**
  * Print the event stats for a given network id
  * Each line:
  * NWID,EventName,EventCycleCount,EventActivationCount,EventAvgCycleCount
  */
void BASimUDRuntime_t::print_event_stats(uint32_t nwid) {
  #ifdef DETAIL_STATS
  auto lnstats = uds[nwid/64]->getLaneStats(nwid%64);
  auto sym_map = uds[nwid/64]->getSymbolNameMap();
  for (auto &sym : lnstats->event_cycle_count) {
    if (sym.second == 0) {
      continue;
    }
    uint64_t cycle_count = sym.second;
    uint64_t activation_count = lnstats->event_activation_count.at(sym.first);
    uint64_t avg_cycle_count = static_cast<uint64_t>((static_cast<long double>(sym.second) / lnstats->event_activation_count.at(sym.first)));
    printf("%u,%s,%lu,%lu,%lu\n", nwid, sym_map[sym.first].c_str(), cycle_count, activation_count, avg_cycle_count);
  }
  #else
    std::cerr << "DETAIL_STATS flag not set. Ignore printing statistics." << std::endl;
  #endif
}

/**
  * Print the event stats for a given UD and lane
  * Each line:
  * NWID,EventName,EventCycleCount,EventActivationCount,EventAvgCycleCount
  */
void BASimUDRuntime_t::print_event_stats(uint32_t ud_id, uint8_t lane_num) {
  #ifdef DETAIL_STATS
  auto lnstats = uds[ud_id]->getLaneStats(lane_num);
  auto sym_map = uds[ud_id]->getSymbolNameMap();
  for (auto &sym : lnstats->event_cycle_count) {
    if (sym.second == 0) {
      continue;
    }
    uint64_t cycle_count = sym.second;
    uint64_t activation_count = lnstats->event_activation_count.at(sym.first);
    uint64_t avg_cycle_count = static_cast<uint64_t>((static_cast<long double>(sym.second) / lnstats->event_activation_count.at(sym.first)));
    printf("%u,%u,%s,%lu,%lu,%lu\n", ud_id, lane_num, sym_map[sym.first].c_str(), cycle_count, activation_count, avg_cycle_count);
  }
  #else
    std::cerr << "DETAIL_STATS flag not set. Ignore printing statistics." << std::endl;
  #endif
}


void BASimUDRuntime_t::db_write_event_stats(const char label[]) {
    #if defined (ENABLE_SQLITE) && defined(DETAIL_STATS)
        if(this->getRank() == 0) {
            uint64_t len = strlen(label)+1;
            // send the request to the other MPI instances
            for(uint32_t rank=1; rank<this->getMPIProcesses(); ++rank) {
                MPI_Send(&len, 1, MPI_UINT64_T, rank, MPI_TAG_DB_EVENT_STATS, MPI_COMM_WORLD);
                MPI_Send(label, len, MPI_CHAR, rank, MPI_TAG_DB_EVENT_STATS_DATA, MPI_COMM_WORLD);
            }
        }

        db_write_event_stats(0, this->udsPerRuntime * this->MachineConfig.NumLanes, label);
    #endif
}

void BASimUDRuntime_t::db_write_event_stats(uint32_t start_nwid, uint32_t num_lanes, const char label[]) {
#if defined (ENABLE_SQLITE) && defined(DETAIL_STATS)
  std::string table_name;
  std::string sql;

  // Begin transaction
  db_exec("BEGIN TRANSACTION;");
  int label_id = db_write_label(label);

  // Create the events table
  table_name = "events";
  sql = "CREATE TABLE IF NOT EXISTS " + table_name + " ("
        "id INTEGER PRIMARY KEY AUTOINCREMENT, "
        "event_name TEXT NOT NULL UNIQUE"
        ");";
  db_exec(sql);

  // Get the symbol name map and insert all event names into the events table
  auto sym_map = uds[start_nwid/64]->getSymbolNameMap();
  for (const auto &sym : sym_map) {
    sql = "INSERT OR IGNORE INTO events (event_name) VALUES ('" + sym.second + "');";
    db_exec(sql);
  }

  // Create the event_stats table
  table_name = "event_stats";
  sql = "CREATE TABLE IF NOT EXISTS " + table_name + " ("
        "id INTEGER PRIMARY KEY AUTOINCREMENT, "
        "label_id INTEGER NOT NULL, "
        "nwid INTEGER NOT NULL, "
        "event_name_id INTEGER NOT NULL, "
        "cycle_count INTEGER, "
        "activation_count INTEGER, "
        "avg_cycle_count INTEGER, "
        "FOREIGN KEY(label_id) REFERENCES labels(id), "
        "FOREIGN KEY(event_name_id) REFERENCES events(id)"
        ");";
  db_exec(sql);

  for (uint32_t nwid = start_nwid; nwid < start_nwid + num_lanes; nwid++) {
    auto lnstats = uds[nwid/64]->getLaneStats(nwid%64);

    uint32_t nwidText = nwid + this->getRank() * this->udsPerRuntime * this->MachineConfig.NumLanes;

    for (auto &sym : lnstats->event_cycle_count) {
      if (sym.second == 0) {
        continue;
      }
      uint64_t cycle_count = sym.second;
      uint64_t activation_count = lnstats->event_activation_count.at(sym.first);
      uint64_t avg_cycle_count = static_cast<uint64_t>((static_cast<long double>(sym.second) / lnstats->event_activation_count.at(sym.first)));

      // Get the ID of the event_name
      int event_name_id;
      sql = "SELECT id FROM events WHERE event_name = '" + sym_map[sym.first] + "';";
      char *errMsg = 0;
      int rc = sqlite3_exec(this->stats_db, sql.c_str(), [](void* data, int argc, char** argv, char** colName) -> int {
          *static_cast<int*>(data) = std::stoi(argv[0]);
          return 0;
      }, &event_name_id, &errMsg);
      if (rc != SQLITE_OK) {
        std::string error = errMsg;
        sqlite3_exec(this->stats_db, "ROLLBACK;", 0, 0, &errMsg);
        sqlite3_free(errMsg);
        BASIM_ERROR("SQL error 12: %s", error.c_str());
      }

      // Construct the INSERT statement for event_stats
      sql = "INSERT INTO " + table_name + " (label_id, nwid, event_name_id, cycle_count, activation_count, avg_cycle_count) VALUES ("
            + std::to_string(label_id) + ", " + std::to_string(nwidText) + ", " + std::to_string(event_name_id) + ", "
            + std::to_string(cycle_count) + ", "
            + std::to_string(activation_count) + ", "
            + std::to_string(avg_cycle_count) + ");";

      db_exec(sql);
    }
  }

  // Commit transaction
  db_exec("COMMIT;");
  int rc = sqlite3_wal_checkpoint(this->stats_db, NULL);
  if (rc != SQLITE_OK) {
      std::cerr << "Checkpoint failed: " << sqlite3_errmsg(this->stats_db) << std::endl;
  }
#else
  std::cerr << "ENABLE_SQLITE and DETAIL_STATS flags not set. Ignore writing event stats to database." << std::endl;
#endif
}

void BASimUDRuntime_t::db_write_node_stats(const char label[]) {
    if(this->getRank() == 0) {
        uint64_t len = strlen(label)+1;
        // send the request to the other MPI instances
        for(uint32_t rank=1; rank<this->getMPIProcesses(); ++rank) {
            MPI_Send(&len, 1, MPI_UINT64_T, rank, MPI_TAG_DB_NODE_STATS, MPI_COMM_WORLD);
            MPI_Send(label, len, MPI_CHAR, rank, MPI_TAG_DB_NODE_STATS_DATA, MPI_COMM_WORLD);
        }
    }

    db_write_node_stats(0, this->nodesPerRuntime, label);
}

void BASimUDRuntime_t::db_write_node_stats(uint32_t start_node, uint32_t num_nodes, const char label[]) {
#if defined(ENABLE_SQLITE)

  std::string table_name;
  std::string sql;
  db_exec("BEGIN TRANSACTION;");
  std::string label_id = std::to_string(db_write_label(label));

  #if defined(DETAIL_STATS)
  // Create the node_stats table
  table_name = "node_stats";
  sql = "CREATE TABLE IF NOT EXISTS " + table_name + " ("
        "id INTEGER PRIMARY KEY AUTOINCREMENT, "
        "label_id INTEGER NOT NULL, "
        "srcNode INTEGER NOT NULL, "
        "dstNode INTEGER, "
        // "PeakTotalCrossNodeCount INTEGER, "
        // "PeakTotalCrossNodeBytes INTEGER, "
        // "MaxQueueSize INTEGER, "
        // "AvgQueueSize INTEGER, "
        "TotalNodeCount INTEGER, "
        "TotalNodeBytes INTEGER, "
        "MessagesNodeCount INTEGER, "
        "MessagesNodeBytes INTEGER, "
        "DRAMStoreNodeCount INTEGER, "
        "DRAMStoreNodeBytes INTEGER, "
        "DRAMLoadNodeCount INTEGER, "
        "DRAMLoadNodeBytes INTEGER, "
        "DRAMStoreAckNodeCount INTEGER, "
        "DRAMStoreAckNodeBytes INTEGER, "
        "DRAMLoadAckNodeCount INTEGER, "
        "DRAMLoadAckNodeBytes INTEGER, "
        "PeakTotalNodeCount INTEGER, "
        "PeakTotalNodeBytes INTEGER, "
        "PeakMessagesNodeCount INTEGER, "
        "PeakMessagesNodeBytes INTEGER, "
        "PeakDRAMStoreNodeCount INTEGER, "
        "PeakDRAMStoreNodeBytes INTEGER, "
        "PeakDRAMLoadNodeCount INTEGER, "
        "PeakDRAMLoadNodeBytes INTEGER, "
        "PeakDRAMStoreNodeAckCount INTEGER, "
        "PeakDRAMStoreNodeAckBytes INTEGER, "
        "PeakDRAMLoadNodeAckCount INTEGER, "
        "PeakDRAMLoadNodeAckBytes INTEGER, "
        "FOREIGN KEY(label_id) REFERENCES labels(id)"
        ");";
  db_exec(sql);

  #pragma omp parallel for
  for(uint32_t srcNodeID=0; srcNodeID<this->nodesPerRuntime; ++srcNodeID) {
    std::string srcNodeIDText = std::string(std::to_string(srcNodeID + this->getRank() * this->nodesPerRuntime));
    for(uint32_t dstNodeID=0; dstNodeID<this->MachineConfig.NumNodes; ++dstNodeID) {
      // Construct the INSERT statement for event_stats
      std::string sqlInsert = "INSERT INTO " + table_name + " (label_id, srcNode, dstNode, TotalNodeCount, TotalNodeBytes, MessagesNodeCount, MessagesNodeBytes, DRAMStoreNodeCount, DRAMStoreNodeBytes, DRAMLoadNodeCount, DRAMLoadNodeBytes, DRAMStoreAckNodeCount, DRAMStoreAckNodeBytes, DRAMLoadAckNodeCount, DRAMLoadAckNodeBytes, PeakTotalNodeCount, PeakTotalNodeBytes, PeakMessagesNodeCount, PeakMessagesNodeBytes, PeakDRAMStoreNodeCount, PeakDRAMStoreNodeBytes, PeakDRAMLoadNodeCount, PeakDRAMLoadNodeBytes, PeakDRAMStoreNodeAckCount, PeakDRAMStoreNodeAckBytes, PeakDRAMLoadNodeAckCount, PeakDRAMLoadNodeAckBytes) VALUES ("
            + label_id + ", " + srcNodeIDText + ", " + std::to_string(dstNodeID) + ", "
            + std::to_string(this->simNodeStats[srcNodeID].total_count_other_node[dstNodeID]->load()) + ", "
            + std::to_string(this->simNodeStats[srcNodeID].total_bytes_other_node[dstNodeID]->load()) + ", "
            + std::to_string(this->simNodeStats[srcNodeID].tran_count_other_node[dstNodeID]->load()) + ", "
            + std::to_string(this->simNodeStats[srcNodeID].tran_bytes_other_node[dstNodeID]->load()) + ", "
            + std::to_string(this->simNodeStats[srcNodeID].dram_store_count_other_node[dstNodeID]->load()) + ", "
            + std::to_string(this->simNodeStats[srcNodeID].dram_store_bytes_other_node[dstNodeID]->load()) + ", "
            + std::to_string(this->simNodeStats[srcNodeID].dram_load_count_other_node[dstNodeID]->load()) + ", "
            + std::to_string(this->simNodeStats[srcNodeID].dram_load_bytes_other_node[dstNodeID]->load()) + ", "
            + std::to_string(this->simNodeStats[srcNodeID].dram_store_ack_count_other_node[dstNodeID]->load()) + ", "
            + std::to_string(this->simNodeStats[srcNodeID].dram_store_ack_bytes_other_node[dstNodeID]->load()) + ", "
            + std::to_string(this->simNodeStats[srcNodeID].dram_load_ack_count_other_node[dstNodeID]->load()) + ", "
            + std::to_string(this->simNodeStats[srcNodeID].dram_load_ack_bytes_other_node[dstNodeID]->load()) + ", "
            + std::to_string(this->simNodeStats[srcNodeID].max_total_count_other_node[dstNodeID]->load()) + ", "
            + std::to_string(this->simNodeStats[srcNodeID].max_total_bytes_other_node[dstNodeID]->load()) + ", "
            + std::to_string(this->simNodeStats[srcNodeID].max_tran_count_other_node[dstNodeID]->load()) + ", "
            + std::to_string(this->simNodeStats[srcNodeID].max_tran_bytes_other_node[dstNodeID]->load()) + ", "
            + std::to_string(this->simNodeStats[srcNodeID].max_dram_store_count_other_node[dstNodeID]->load()) + ", "
            + std::to_string(this->simNodeStats[srcNodeID].max_dram_store_bytes_other_node[dstNodeID]->load()) + ", "
            + std::to_string(this->simNodeStats[srcNodeID].max_dram_load_count_other_node[dstNodeID]->load()) + ", "
            + std::to_string(this->simNodeStats[srcNodeID].max_dram_load_bytes_other_node[dstNodeID]->load()) + ", "
            + std::to_string(this->simNodeStats[srcNodeID].max_dram_store_ack_count_other_node[dstNodeID]->load()) + ", "
            + std::to_string(this->simNodeStats[srcNodeID].max_dram_store_ack_bytes_other_node[dstNodeID]->load()) + ", "
            + std::to_string(this->simNodeStats[srcNodeID].max_dram_load_ack_count_other_node[dstNodeID]->load()) + ", "
            + std::to_string(this->simNodeStats[srcNodeID].max_dram_load_ack_bytes_other_node[dstNodeID]->load())
            + ");";

      db_exec(sqlInsert);
    }
  }
#endif // DETAILED_STATS

  // Adding per stack stats for each node
  table_name = "node_stack_stats";
  sql = "CREATE TABLE IF NOT EXISTS " + table_name + " ("
        "id INTEGER PRIMARY KEY AUTOINCREMENT, "
        "label_id INTEGER NOT NULL, "
        "node INTEGER NOT NULL, "
        "stack INTEGER NOT NULL, "
        "DRAMStackLoadBytes INTEGER, "
        "DRAMStackStoreBytes INTEGER, "
        "DRAMStackLoadCount INTEGER, "
        "DRAMStackStoreCount INTEGER, "
        "DRAMStackPeakLoadBytes INTEGER, "
        "DRAMStackPeakStoreBytes INTEGER, "
        "DRAMStackPeakLoadCount INTEGER, "
        "DRAMStackPeakStoreCount INTEGER, "
        "DRAMStackPeakLoadStoreCount INTEGER, "
        "FOREIGN KEY(label_id) REFERENCES labels(id)"
  ");";
  db_exec(sql);

  for (uint32_t nodeID = start_node; nodeID < num_nodes; ++nodeID) {
    std::string nodeIDText = std::to_string(nodeID + this->getRank() * this->nodesPerRuntime);
    // Construct the INSERT statement for event_stats
    for(int stid = 0; stid < this->MachineConfig.NumStacks; stid++) {
      const basim::StackStats* ststats = udMems[nodeID]->getStackStats(stid);
      sql = "INSERT INTO " + table_name + " (label_id, node, stack, DRAMStackLoadBytes, DRAMStackStoreBytes, DRAMStackLoadCount, DRAMStackStoreCount, DRAMStackPeakLoadBytes, DRAMStackPeakStoreBytes, DRAMStackPeakLoadCount, DRAMStackPeakStoreCount, DRAMStackPeakLoadStoreCount) VALUES ("
          + label_id + ", " + nodeIDText + ", " + std::to_string(stid) + ", "
          + std::to_string(ststats->dram_load_bytes) + ", "
          + std::to_string(ststats->dram_store_bytes) + ", "
          + std::to_string(ststats->dram_load_count) + ", "
          + std::to_string(ststats->dram_store_count) + ", "
          + std::to_string(ststats->peak_dram_load_bytes) + ", "
          + std::to_string(ststats->peak_dram_store_bytes) + ", "
          + std::to_string(ststats->peak_dram_load_count) + ", "
          + std::to_string(ststats->peak_dram_store_count) + ", "
          + std::to_string(ststats->peak_dram_load_store_count)
          + ");";
      db_exec(sql);
    }
  }

  // Commit transaction
  db_exec("COMMIT;");
  int rc = sqlite3_wal_checkpoint(this->stats_db, NULL);
  if(rc != SQLITE_OK) {
      std::cerr << "Checkpoint failed: " << sqlite3_errmsg(this->stats_db) << std::endl;
  }
#else
  std::cerr << "ENABLE_SQLITE flag not set. Ignore writing event stats to database." << std::endl;
#endif // ENABLE_SQLITE
}


BASimUDRuntime_t::~BASimUDRuntime_t() {

#ifndef GEM5_MODE
  uint32_t myRank = this->getRank();

  // Inform the other ranks about the destruction, so that they can exit gracefully.
  this->terminateMainLoop();

  MPI_Finalize();
#endif


  // close perflog
  basim::globalLogs.perflog.close();
  // close tracelog
  basim::globalLogs.tracelog.close();
#if defined (ENABLE_SQLITE)
  // close db
  sqlite3_close(this->stats_db);
#endif

  // Delete the uds Aaaah we do not care, let the OS handle that, it is much more efficient in this.
  // #pragma omp parallel for
  // for (auto &ud : uds) {
  //   delete ud;
  // }
  // uds.clear();
}

bool BASimUDRuntime_t::isIdle(uint32_t udid, uint32_t laneID){
  return uds[udid]->isIdle(laneID);
}

void BASimUDRuntime_t::simulate(uint32_t udid, uint32_t laneID, uint64_t numTicks, uint64_t timestamp){
  uds[udid]->simulate(laneID, NumTicks, timestamp);
}


common_addr BASimUDRuntime_t::mapSA2PA(basim::Addr mm_addr, uint8_t isGlobal){
    common_addr final_addr;
    final_addr.isGlobal = isGlobal;

    // local memory
    if(isGlobal == 0){
        final_addr.node_id = 0;
        final_addr.addr = mm_addr;
    } else { // global memory
        uint64_t memSize = this->MachineConfig.GMapMemSize / this->nodesPerRuntime;
        basim::Addr offset = mm_addr - this->MachineConfig.PhysGMapMemBase;
        uint64_t node_id = offset / memSize;
        offset = offset % memSize;
        final_addr.addr = (node_id << 37) | offset;
        final_addr.node_id = node_id;
        final_addr.node_offset = this->get_node_offset(node_id);
    }

    return final_addr;
}

uint32_t BASimUDRuntime_t::get_PA_nodeID(basim::Addr ud_addr) {
  return ((ud_addr >> 37) & 0x3FFFULL);
}

uint64_t BASimUDRuntime_t::get_PA_offset(basim::Addr ud_addr) {
  return ud_addr & 0x1F'FFFF'FFFFULL;
}

uint32_t BASimUDRuntime_t::get_node_offset(uint32_t node_id) {
  return node_id % this->nodesPerRuntime;
}


basim::Addr BASimUDRuntime_t::construct_PA(uint64_t node_id, basim::Addr offset){
  return (node_id << 37) | (offset & 0x1F'FFFF'FFFFULL);
}

common_addr BASimUDRuntime_t::mapPA2SA(basim::Addr ud_addr, uint8_t isGlobal){
    common_addr final_addr;
    final_addr.isGlobal = isGlobal;
    
    // local memory
    if(isGlobal == 0){    
        final_addr.node_id = 0;
        final_addr.node_offset = 0;
        final_addr.addr = ud_addr;
    } else {   // global memory
        uint64_t node_id = get_PA_nodeID(ud_addr);
        final_addr.node_id = node_id;
        basim::Addr offset = get_PA_offset(ud_addr);
        
        uint64_t memPerNode = this->MachineConfig.GMapMemSize / this->MachineConfig.NumNodes;
        final_addr.node_offset = get_node_offset(node_id);
        final_addr.addr = this->MachineConfig.PhysGMapMemBase + (memPerNode * final_addr.node_offset) + offset;
            
        //printf("mapPA2SA: udpa_addr = 0x%lx, isGlobal = %d, node_id = %ld, node_offset: %d, memPerNode = 0x%lx, offset = 0x%lx, simulator_addr = 0x%lx\n", ud_addr, isGlobal, node_id, final_addr.node_offset, memPerNode, offset, final_addr.addr); fflush(stdout);
    }
    
    return final_addr;
}

uint64_t BASimUDRuntime_t::mapVA2SA(uint64_t virt, uint64_t virt_base, uint64_t phy_base, uint64_t blockSize, uint64_t numNodes){
  // Check for single node allocation
  if (numNodes == 1) {
    return virt;
  }

  // Check for bounds
  UpDown::word_t offset = virt - virt_base;

  // Convert the swizzle mask to the parameters
  uint64_t C = log2(blockSize);
  uint64_t B = log2(numNodes);
  uint64_t F = 37 - C;
  uint64_t P = 64 - C - B - F;

  // Calculate the physical address
  uint64_t blockNumber = (offset >> C) & ((1ULL << (B + F)) - 1);
  uint64_t nodeOffset = blockNumber % numNodes;
  uint64_t blockNumberInNode = blockNumber / numNodes;
  uint64_t blockOffset = offset & ((1ULL << C) - 1);

  uint64_t swizzledAddress = (offset & ~(~0ULL >> P)) | nodeOffset << 37 | blockNumberInNode * blockSize + blockOffset;
  uint64_t physicalAddress = (physical_addr_t(phy_base)+physical_addr_t(swizzledAddress)).getCompressed();
  uint64_t pa2sa = mapPA2SA((basim::Addr)physicalAddress, 1).addr;
  return pa2sa;
}

uint64_t BASimUDRuntime_t::get_status(){
    return status.load(std::memory_order_relaxed);
}
void BASimUDRuntime_t::set_status(uint64_t _status){
    status.store(_status, std::memory_order_release);
}


uint64_t BASimUDRuntime_t::get_barrier_times(){
    return barrier_times_atomic.load(std::memory_order_relaxed);
}
void BASimUDRuntime_t::set_barrier_times(uint64_t _barrier_times){
    barrier_times_atomic.store(_barrier_times, std::memory_order_release);
}

void BASimUDRuntime_t::barrier(uint64_t barrier_id){
#ifdef ASST_FASTSIM
    pthread_mutex_lock(&map_lock);
    pthread_t tid = pthread_self();
    int id1 = 0;
    auto it1 = thread_map.find(tid);
    if (it1 != thread_map.end()) {
        id1 = it1->second;
    }else{
        id1 = thread_num.load(std::memory_order_relaxed);
        thread_num.store(id1+1, std::memory_order_release);
        thread_map[tid] = id1;
    }
    pthread_mutex_unlock(&map_lock);
    while(get_status() != 0){
        fflush(stdout);
    }
    set_status(10+id1);
    sem_wait(&semSync[id1]);
#else
   uint64_t barrier_times = get_barrier_times();
    while(get_status() != barrier_id){
        fflush(stdout);
    }
    set_status(barrier_id+1);
    if(get_status() == (barrier_times)){
        set_status(barrier_times - 1);
    }
    while(get_status() != barrier_id){
        fflush(stdout);
    }
    if(barrier_id > 0)
        set_status(barrier_id-1);
#endif
}

void BASimUDRuntime_t::barrier(){
#ifdef ASST_FASTSIM
    pthread_mutex_lock(&map_lock);
    pthread_t tid = pthread_self();
    int id1 = 0;
    auto it1 = thread_map.find(tid);
    if (it1 != thread_map.end()) {
        id1 = it1->second;
    }else{
        id1 = thread_num.load(std::memory_order_relaxed);
        thread_num.store(id1+1, std::memory_order_release);
        thread_map[tid] = id1;
    }
    pthread_mutex_unlock(&map_lock);
    while(get_status() != 0){
        fflush(stdout);
    }
    set_status(10+id1);
    sem_wait(&semSync[id1]);
#else
    uint64_t barrier_id = this->getMinNodeID();
    uint64_t barrier_times = get_barrier_times();
    while(get_status() != barrier_id){
        fflush(stdout);
    }
    set_status(barrier_id+1);
    if(get_status() == (barrier_times)){
        set_status(barrier_times - 1);
    }
    while(get_status() != barrier_id){
        fflush(stdout);
    }
    if(barrier_id > 0)
        set_status(barrier_id-1);
#endif
}

void BASimUDRuntime_t::lock(){
    pthread_mutex_lock(&top_lock);
}

void BASimUDRuntime_t::unlock(){
    pthread_mutex_unlock(&top_lock);
}

void BASimUDRuntime_t::reorder_freetids(){
    for (int ud = 0; ud < this->udsPerRuntime; ud++)
        this->uds[ud]->reorder_freetids();
}


} // namespace UpDown
