#include "simupdown.h"
#include "debug.h"
#include "sim_stats.hh"
#include "updown_config.h"
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <fcntl.h>
#include <sys/mman.h>
#include <utility>
#include <vector>

namespace UpDown {
  /**
   * @brief Construct a new SimUDRuntime_t object
   *
   * This constructor calls initMemoryArrays() to set the simulated memory
   * regions. Python will be disabled. Only simulating memory interactions.
   *
   */
  SimUDRuntime_t::SimUDRuntime_t() : UDRuntime_t(), python_enabled(false) {
    UPDOWN_INFOMSG("Initializing Simulated Runtime with default params");
    UPDOWN_WARNING("No python program. Python will be disabled, only "
                   "simulating memory interactions");
    UPDOWN_INFOMSG("Adding stats for %lu UDs", this->MachineConfig.NumUDs);
    #ifdef ASST_FASTSIM
    for (int i = 0;
         i < this->MachineConfig.NumUDs * this->MachineConfig.NumStacks;
         i++) {
      std::vector<struct SimStats> v(this->MachineConfig.NumLanes);
      this->simStats.push_back(v);
    }
    #else
    for (int i = 0;
         i < this->MachineConfig.NumUDs * this->MachineConfig.NumStacks *
                 this->MachineConfig.NumNodes;
         i++) {
      std::vector<struct SimStats> v(this->MachineConfig.NumLanes);
      this->simStats.push_back(v);
    }
    #endif
    initMemoryArrays();
    // Recalculate address map
    calc_addrmap();
  }

  /**
   * @brief Construct a new SimUDRuntime_t object
   *
   * This constructor calls initMemoryArrays() to set the simulated memory
   * regions. The pointers of ud_machine_t.MappedMemBase, ud_machine_t.UDbase
   * ud_machine_t.SPMemBase and ud_machine_t.ControlBase will be ignored and
   * overwritten in order to simulate the runtime.
   *
   * @param machineConfig Machine configuration
   */
  SimUDRuntime_t::SimUDRuntime_t(ud_machine_t machineConfig)
      : UDRuntime_t(machineConfig), python_enabled(false) {
    UPDOWN_INFOMSG("Initializing runtime with custom machineConfig");
    UPDOWN_WARNING("No python program. Python will be disabled, only "
                   "simulating memory interactions");
    UPDOWN_INFOMSG("Adding stats for %lu UDs", this->MachineConfig.NumUDs);
    #ifdef ASST_FASTSIM
    for (int i = 0;
         i < this->MachineConfig.NumUDs * this->MachineConfig.NumStacks;
         i++) {
      std::vector<struct SimStats> v(this->MachineConfig.NumLanes);
      this->simStats.push_back(v);
    }
    #else
    for (int i = 0;
         i < this->MachineConfig.NumUDs * this->MachineConfig.NumStacks *
                 this->MachineConfig.NumNodes;
         i++) {
      std::vector<struct SimStats> v(this->MachineConfig.NumLanes);
      this->simStats.push_back(v);
    }
    #endif
    initMemoryArrays();
    // Recalculate address map
    calc_addrmap();
    init_stats();
  }

  /**
   * @brief Construct a new SimUDRuntime_t object
   *
   * This constructor calls initMemoryArrays() to set the simulated memory
   * regions. The pointers of ud_machine_t.MappedMemBase, ud_machine_t.UDbase
   * ud_machine_t.SPMemBase and ud_machine_t.ControlBase will be ignored and
   * overwritten.
   *
   * @param machineConfig Machine configuration
   */
  SimUDRuntime_t::SimUDRuntime_t(std::string programFile, std::string programName,
                 std::string simulationDir,
                 EmulatorLogLevel printLvl)
      : UDRuntime_t(), programFile(programFile), programName(programName),
        simulationDir(simulationDir), python_enabled() {
    UPDOWN_INFOMSG("Initializing runtime with custom machineConfig");
    UPDOWN_INFOMSG("Adding stats for %lu UDs", this->MachineConfig.NumUDs);
    #ifdef ASST_FASTSIM
    for (int i = 0;
         i < this->MachineConfig.NumUDs * this->MachineConfig.NumStacks;
         i++) {
      std::vector<struct SimStats> v(this->MachineConfig.NumLanes);
      this->simStats.push_back(v);
    }
    #else
    for (int i = 0;
         i < this->MachineConfig.NumUDs * this->MachineConfig.NumStacks *
                 this->MachineConfig.NumNodes;
         i++) {
      std::vector<struct SimStats> v(this->MachineConfig.NumLanes);
      this->simStats.push_back(v);
    }
    #endif
    initMemoryArrays();
    UPDOWN_INFOMSG("Running file %s Program %s Dir %s", programFile.c_str(),
                   programName.c_str(), simulationDir.c_str());
    // Recalculate address map
    calc_addrmap();
    init_stats();
  }

  /**
   * @brief Construct a new SimUDRuntime_t object
   *
   * This constructor calls initMemoryArrays() to set the simulated memory
   * regions. The pointers of ud_machine_t.MappedMemBase, ud_machine_t.UDbase
   * ud_machine_t.SPMemBase and ud_machine_t.ControlBase will be ignored and
   * overwritten.
   *
   * @param machineConfig Machine configuration
   */
  SimUDRuntime_t::SimUDRuntime_t(ud_machine_t machineConfig, std::string programFile,
                 std::string programName, std::string simulationDir,
                 EmulatorLogLevel printLvl)
      : UDRuntime_t(machineConfig), programFile(programFile),
        programName(programName), simulationDir(simulationDir),
        python_enabled(true) {
    UPDOWN_INFOMSG("Initializing runtime with custom machineConfig");
    UPDOWN_INFOMSG("Adding stats for %lu UDs", this->MachineConfig.NumUDs);
    #ifdef ASST_FASTSIM
    for (int i = 0;
         i < this->MachineConfig.NumUDs * this->MachineConfig.NumStacks;
         i++) {
      std::vector<struct SimStats> v(this->MachineConfig.NumLanes);
      this->simStats.push_back(v);
    }
    #else
    for (int i = 0;
         i < this->MachineConfig.NumUDs * this->MachineConfig.NumStacks *
                 this->MachineConfig.NumNodes;
         i++) {
      std::vector<struct SimStats> v(this->MachineConfig.NumLanes);
      this->simStats.push_back(v);
    }
    #endif
    initMemoryArrays();
    UPDOWN_INFOMSG("Running file %s Program %s Dir %s", programFile.c_str(),
                   programName.c_str(), simulationDir.c_str());
    // Recalculate address map
    calc_addrmap();
    init_stats();
  }

  /**
   * @brief Construct a new SimUDRuntime_t object
   *
   * This constructor calls initMemoryArrays() to set the simulated memory
   * regions. The pointers of ud_machine_t.MappedMemBase, ud_machine_t.UDbase
   * ud_machine_t.SPMemBase and ud_machine_t.ControlBase will be ignored and
   * overwritten. But No Python Interface is enabled
   *
   * @param machineConfig Machine configuration
   */
  SimUDRuntime_t::SimUDRuntime_t(ud_machine_t machineConfig, std::string programFile,
                 std::string programName)
      : UDRuntime_t(machineConfig), programFile(programFile),
        programName(programName),
        python_enabled(false) {
    UPDOWN_INFOMSG("Initializing runtime with custom machineConfig");
    UPDOWN_INFOMSG("Adding stats for %lu UDs", this->MachineConfig.NumUDs);
    #ifdef ASST_FASTSIM
    for (int i = 0;
         i < this->MachineConfig.NumUDs * this->MachineConfig.NumStacks;
         i++) {
      std::vector<struct SimStats> v(this->MachineConfig.NumLanes);
      this->simStats.push_back(v);
    }
    #else
    for (int i = 0;
         i < this->MachineConfig.NumUDs * this->MachineConfig.NumStacks *
                 this->MachineConfig.NumNodes;
         i++) {
      std::vector<struct SimStats> v(this->MachineConfig.NumLanes);
      this->simStats.push_back(v);
    }
    #endif
    initMemoryArrays();
    UPDOWN_INFOMSG("Running file Program %s Dir %s", programFile.c_str(),
                   programName.c_str());
    // Recalculate address map
    calc_addrmap();
    init_stats();
  }

  /**
   * @brief Construct a new SimUDRuntime_t object
   *
   * This constructor calls initMemoryArrays() to set the simulated memory
   * regions. The pointers of ud_machine_t.MappedMemBase, ud_machine_t.UDbase
   * ud_machine_t.SPMemBase and ud_machine_t.ControlBase will be ignored and
   * overwritten. But No Python Interface is enabled
   *
   * @param machineConfig Machine configuration
   */
  SimUDRuntime_t::SimUDRuntime_t(ud_machine_t machineConfig, std::string programFile)
      : UDRuntime_t(machineConfig), programFile(programFile),
        python_enabled(false) {
    UPDOWN_INFOMSG("Initializing runtime with custom machineConfig");
    UPDOWN_INFOMSG("Adding stats for %lu UDs", this->MachineConfig.NumUDs);
    #ifdef ASST_FASTSIM
    for (int i = 0;
         i < this->MachineConfig.NumUDs * this->MachineConfig.NumStacks;
         i++) {
      std::vector<struct SimStats> v(this->MachineConfig.NumLanes);
      this->simStats.push_back(v);
    }
    #else
    for (int i = 0;
         i < this->MachineConfig.NumUDs * this->MachineConfig.NumStacks *
                 this->MachineConfig.NumNodes;
         i++) {
      std::vector<struct SimStats> v(this->MachineConfig.NumLanes);
      this->simStats.push_back(v);
    }
    #endif
    initMemoryArrays();
    UPDOWN_INFOMSG("Running Program %s ", programFile.c_str());
    // Recalculate address map
    calc_addrmap();
    init_stats();
  }

void SimUDRuntime_t::initMemoryArrays() {
  // Initializing arrays containning mapped memory
  UPDOWN_INFOMSG("Allocating %lu bytes for mapped memory",
                 this->MachineConfig.MapMemSize);

  // Old way of allocating simulation memory
  // MappedMemory = new uint8_t[this->MachineConfig.MapMemSize];

  // Use mmap to allocate memory to make sure the allocated address is consistent
  MappedMemory = (uint8_t *) mmap(reinterpret_cast<void *>(BASE_MAPPED_ADDR), this->MachineConfig.MapMemSize, PROT_READ | PROT_WRITE, MAP_FIXED_NOREPLACE | MAP_ANONYMOUS | MAP_PRIVATE, -1, 0);
  UPDOWN_ERROR_IF(MappedMemory == MAP_FAILED, "Failed to allocate mapped memory at 0x%llX with size %lu", BASE_MAPPED_ADDR, this->MachineConfig.MapMemSize);

  #ifdef ASST_FASTSIM
    UPDOWN_INFOMSG("Allocating %lu bytes for mapped global memory",
                   this->MachineConfig.GMapMemSize/MachineConfig.NumNodes);
    GMappedMemory = new uint8_t[this->MachineConfig.GMapMemSize/MachineConfig.NumNodes];
    this->MachineConfig.PhysGMapMemBase = reinterpret_cast<uint64_t>(GMappedMemory);
    UPDOWN_ERROR_IF(GMappedMemory == NULL, "Failed to allocate mapped global memory with size %lu", this->MachineConfig.GMapMemSize/MachineConfig.NumNodes);
  //   printf("allocate mapped global memory at 0x%llX with size %lu\n", this->MachineConfig.PhysGMapMemBase, this->MachineConfig.GMapMemSize/nnodes);
    // Use mmap to allocate memory to make sure the allocated address is consistent
  //   GMappedMemory = (uint8_t *) mmap(reinterpret_cast<void *>(BASE_MAPPED_GLOBAL_ADDR), this->MachineConfig.GMapMemSize/nnodes, PROT_READ | PROT_WRITE, MAP_FIXED_NOREPLACE | MAP_ANONYMOUS | MAP_PRIVATE, -1, 0);
  //   UPDOWN_ERROR_IF(GMappedMemory == MAP_FAILED, "Failed to allocate mapped global memory at 0x%llX with size %lu", this->MachineConfig.PhysGMapMemBase, this->MachineConfig.GMapMemSize/MachineConfig.NumNodes);
  #else
    UPDOWN_INFOMSG("Allocating %lu bytes for mapped global memory",
                   this->MachineConfig.GMapMemSize);
    GMappedMemory = new uint8_t[this->MachineConfig.GMapMemSize];
    this->MachineConfig.PhysGMapMemBase = reinterpret_cast<uint64_t>(GMappedMemory);
    UPDOWN_ERROR_IF(GMappedMemory == NULL, "Failed to allocate mapped global memory with size %lu", this->MachineConfig.GMapMemSize);
  //   printf("allocate mapped global memory at 0x%llX with size %lu\n", this->MachineConfig.PhysGMapMemBase, this->MachineConfig.GMapMemSize);
    // Use mmap to allocate memory to make sure the allocated address is consistent
  //   GMappedMemory = (uint8_t *) mmap(reinterpret_cast<void *>(BASE_MAPPED_GLOBAL_ADDR), this->MachineConfig.GMapMemSize, PROT_READ | PROT_WRITE, MAP_FIXED_NOREPLACE | MAP_ANONYMOUS | MAP_PRIVATE, -1, 0);
  //   UPDOWN_ERROR_IF(GMappedMemory == MAP_FAILED, "Failed to allocate mapped global memory at 0x%llX with size %lu", this->MachineConfig.PhysGMapMemBase, this->MachineConfig.GMapMemSize);
  #endif



  UPDOWN_INFOMSG("Allocating %lu bytes for Scratchpad memory", this->MachineConfig.SPSize());
  // Old way of allocating simulation LM memory
  ScratchpadMemory = new uint8_t[this->MachineConfig.SPSize()];
  UPDOWN_ERROR_IF(ScratchpadMemory == NULL, "Failed to allocate mapped memory with size %lu for LM", this->MachineConfig.SPSize());
  // Use mmap to allocate memory to make sure the allocated address is consistent
//   ScratchpadMemory = (uint8_t *) mmap(reinterpret_cast<void *>(BASE_SPMEM_ADDR), this->MachineConfig.SPSize(), PROT_READ | PROT_WRITE, MAP_FIXED_NOREPLACE | MAP_ANONYMOUS | MAP_PRIVATE, -1, 0);
//   UPDOWN_ERROR_IF(ScratchpadMemory == MAP_FAILED, "Failed to allocate mapped memory at 0x%llX with size %lu for LM", BASE_SPMEM_ADDR, this->MachineConfig.SPSize());

  uint64_t size_control =
      this->MachineConfig.CapNumNodes * this->MachineConfig.CapNumStacks *
      this->MachineConfig.CapNumUDs * this->MachineConfig.CapNumLanes *
      this->MachineConfig.CapControlPerLane;
  UPDOWN_INFOMSG("Allocating %lu bytes for control", size_control);
  ControlMemory = new uint8_t[size_control];
  UPDOWN_ERROR_IF(ControlMemory == NULL, "Failed to allocate mapped memory with size %lu for Control Memory", size_control);

  // Changing the base locations for the simulated memory regions
  this->MachineConfig.MapMemBase = reinterpret_cast<uint64_t>(MappedMemory);
  UPDOWN_INFOMSG("MapMemBase changed to 0x%lX", this->MachineConfig.MapMemBase);
//   this->MachineConfig.GMapMemBase = reinterpret_cast<uint64_t>(GMappedMemory);
//   UPDOWN_INFOMSG("GMapMemBase changed to 0x%lX", this->MachineConfig.GMapMemBase);
  this->MachineConfig.UDbase = reinterpret_cast<uint64_t>(ScratchpadMemory);
  this->MachineConfig.SPMemBase = reinterpret_cast<uint64_t>(ScratchpadMemory);
  UPDOWN_INFOMSG("SPMemBase and UDbase changed to 0x%lX",
                 this->MachineConfig.SPMemBase);
  this->MachineConfig.ControlBase = reinterpret_cast<uint64_t>(ControlMemory);
  UPDOWN_INFOMSG("ControlBase changed to 0x%lX",
                 this->MachineConfig.ControlBase);
  // ReInit Memory Manager with new machine configuration
  reset_memory_manager();
}


void SimUDRuntime_t::init_stats() {
  uint64_t upperLimit = this->MachineConfig.NumUDs * this->MachineConfig.NumStacks;
  #ifndef ASST_FASTSIM
    upperLimit *= this->MachineConfig.NumNodes;
  #endif

  for (uint64_t ud_id=0; ud_id<upperLimit; ++ud_id) {
    for (uint64_t lane_num=0; lane_num<this->MachineConfig.NumLanes; ++lane_num) {
      this->simStats[ud_id][lane_num].cur_num_sends = 0;
      this->simStats[ud_id][lane_num].num_sends = 0;
      this->simStats[ud_id][lane_num].exec_cycles = 0;
      this->simStats[ud_id][lane_num].idle_cycles = 0;
      this->simStats[ud_id][lane_num].lm_write_bytes = 0;
      this->simStats[ud_id][lane_num].lm_read_bytes = 0;
      this->simStats[ud_id][lane_num].transition_cnt = 0;
      this->simStats[ud_id][lane_num].total_inst_cnt = 0;
      this->simStats[ud_id][lane_num].send_inst_cnt = 0;
      this->simStats[ud_id][lane_num].move_inst_cnt = 0;
      this->simStats[ud_id][lane_num].branch_inst_cnt = 0;
      this->simStats[ud_id][lane_num].alu_inst_cnt = 0;
      this->simStats[ud_id][lane_num].yield_inst_cnt = 0;
      this->simStats[ud_id][lane_num].compare_inst_cnt = 0;
      this->simStats[ud_id][lane_num].cmp_swp_inst_cnt = 0;
      this->simStats[ud_id][lane_num].event_queue_max = 0;
      this->simStats[ud_id][lane_num].event_queue_mean = 0.0;
      this->simStats[ud_id][lane_num].operand_queue_max = 0;
      this->simStats[ud_id][lane_num].operand_queue_mean = 0.0;
      for (uint64_t i=0; i<16; ++i) {
        this->simStats[ud_id][lane_num].user_counter[i] += 0;
      }
    }
  }
}

void SimUDRuntime_t::send_event(event_t ev) {
  // Perform the regular access. This will have no effect
  UDRuntime_t::send_event(ev);
  
}

void SimUDRuntime_t::start_exec(networkid_t nwid) {
  // Perform the regular access. This will have no effect
  UDRuntime_t::start_exec(nwid);
}

void SimUDRuntime_t::t2ud_memcpy(void *data, uint64_t size, networkid_t nwid,
                                 uint32_t offset) {
  UDRuntime_t::t2ud_memcpy(data, size, nwid, offset);
}

void SimUDRuntime_t::ud2t_memcpy(void *data, uint64_t size, networkid_t nwid,
                                 uint32_t offset) {
  uint32_t ud_num = this->get_globalUDNum(nwid);
  uint64_t addr = UDRuntime_t::get_lane_physical_memory(nwid, offset) -
                  UDRuntime_t::get_ud_physical_memory(nwid);
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
  UDRuntime_t::ud2t_memcpy(data, size, nwid, offset);
}

bool SimUDRuntime_t::test_addr(networkid_t nwid, uint32_t offset,
                               word_t expected) {
  uint32_t ud_num = this->get_globalUDNum(nwid);
  uint64_t addr = UDRuntime_t::get_lane_physical_memory(nwid, offset) -
                  UDRuntime_t::get_ud_physical_memory(nwid);
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

  return UDRuntime_t::test_addr(nwid, offset, expected);
}

void SimUDRuntime_t::test_wait_addr(networkid_t nwid, uint32_t offset,
                                    word_t expected) {

  while (!test_addr(nwid, offset, expected))
    ;
  // The bottom call will never hold since we're holding here
  UDRuntime_t::test_wait_addr(nwid, offset, expected);
}

void SimUDRuntime_t::update_stats(struct SimStats &loc_stats, uint32_t ud_id,
                                  uint8_t lane_num) {
  this->simStats[ud_id][lane_num].cur_num_sends = loc_stats.cur_num_sends;
  this->simStats[ud_id][lane_num].num_sends += loc_stats.num_sends;
  this->simStats[ud_id][lane_num].exec_cycles += loc_stats.exec_cycles;
  this->simStats[ud_id][lane_num].idle_cycles += loc_stats.idle_cycles;
  this->simStats[ud_id][lane_num].lm_write_bytes += loc_stats.lm_write_bytes;
  this->simStats[ud_id][lane_num].lm_read_bytes += loc_stats.lm_read_bytes;
  this->simStats[ud_id][lane_num].transition_cnt += loc_stats.transition_cnt;
  this->simStats[ud_id][lane_num].total_inst_cnt += loc_stats.total_inst_cnt;
  this->simStats[ud_id][lane_num].send_inst_cnt += loc_stats.send_inst_cnt;
  this->simStats[ud_id][lane_num].move_inst_cnt += loc_stats.move_inst_cnt;
  this->simStats[ud_id][lane_num].branch_inst_cnt += loc_stats.branch_inst_cnt;
  this->simStats[ud_id][lane_num].alu_inst_cnt += loc_stats.alu_inst_cnt;
  this->simStats[ud_id][lane_num].yield_inst_cnt += loc_stats.yield_inst_cnt;
  this->simStats[ud_id][lane_num].compare_inst_cnt +=
      loc_stats.compare_inst_cnt;
  this->simStats[ud_id][lane_num].cmp_swp_inst_cnt +=
      loc_stats.cmp_swp_inst_cnt;
  this->simStats[ud_id][lane_num].event_queue_max = loc_stats.event_queue_max;
  this->simStats[ud_id][lane_num].event_queue_mean = loc_stats.event_queue_mean;
  this->simStats[ud_id][lane_num].operand_queue_max =
      loc_stats.operand_queue_max;
  this->simStats[ud_id][lane_num].operand_queue_mean =
      loc_stats.operand_queue_mean;
  for (int i = 0; i < 16; i++) {
    this->simStats[ud_id][lane_num].user_counter[i] +=
        loc_stats.user_counter[i];
  }
}

void SimUDRuntime_t::print_stats(uint32_t ud_id, uint8_t lane_num) {
  const int wid = 10;
  std::printf("[UD%d-L%d] num_sends           = %*lu\n", ud_id, lane_num, wid,
              this->simStats[ud_id][lane_num].num_sends);
  std::printf("[UD%d-L%d] exec_cycles         = %*lu\n", ud_id, lane_num, wid,
              this->simStats[ud_id][lane_num].exec_cycles);
  std::printf("[UD%d-L%d] idle_cycles         = %*lu\n", ud_id, lane_num, wid,
              this->simStats[ud_id][lane_num].idle_cycles);
  std::printf("[UD%d-L%d] lm_write_bytes      = %*lu\n", ud_id, lane_num, wid,
              this->simStats[ud_id][lane_num].lm_write_bytes);
  std::printf("[UD%d-L%d] lm_read_bytes       = %*lu\n", ud_id, lane_num, wid,
              this->simStats[ud_id][lane_num].lm_read_bytes);
  std::printf("[UD%d-L%d] transition_cnt      = %*lu\n", ud_id, lane_num, wid,
              this->simStats[ud_id][lane_num].transition_cnt);
  std::printf("[UD%d-L%d] total_inst_cnt      = %*lu\n", ud_id, lane_num, wid,
              this->simStats[ud_id][lane_num].total_inst_cnt);
  std::printf("[UD%d-L%d] send_inst_cnt       = %*lu\n", ud_id, lane_num, wid,
              this->simStats[ud_id][lane_num].send_inst_cnt);
  std::printf("[UD%d-L%d] move_inst_cnt       = %*lu\n", ud_id, lane_num, wid,
              this->simStats[ud_id][lane_num].move_inst_cnt);
  std::printf("[UD%d-L%d] branch_inst_cnt     = %*lu\n", ud_id, lane_num, wid,
              this->simStats[ud_id][lane_num].branch_inst_cnt);
  std::printf("[UD%d-L%d] alu_inst_cnt        = %*lu\n", ud_id, lane_num, wid,
              this->simStats[ud_id][lane_num].alu_inst_cnt);
  std::printf("[UD%d-L%d] yield_inst_cnt      = %*lu\n", ud_id, lane_num, wid,
              this->simStats[ud_id][lane_num].yield_inst_cnt);
  std::printf("[UD%d-L%d] compare_inst_cnt    = %*lu\n", ud_id, lane_num, wid,
              this->simStats[ud_id][lane_num].compare_inst_cnt);
  std::printf("[UD%d-L%d] cmp_swp_inst_cnt    = %*lu\n", ud_id, lane_num, wid,
              this->simStats[ud_id][lane_num].cmp_swp_inst_cnt);
  std::printf("[UD%d-L%d] event_queue_max     = %*lu\n", ud_id, lane_num, wid,
              this->simStats[ud_id][lane_num].event_queue_max);
  std::printf("[UD%d-L%d] event_queue_mean    = %*.2lf\n", ud_id, lane_num, wid,
              this->simStats[ud_id][lane_num].event_queue_mean);
  std::printf("[UD%d-L%d] operand_queue_max   = %*lu\n", ud_id, lane_num, wid,
              this->simStats[ud_id][lane_num].operand_queue_max);
  std::printf("[UD%d-L%d] operand_queue_mean  = %*.2lf\n", ud_id, lane_num, wid,
              this->simStats[ud_id][lane_num].operand_queue_mean);
  for (int i = 0; i < 16; i++) {
    std::printf("[UD%d-L%d] user_counter%2d      = %*ld\n", ud_id, lane_num, i,
                wid, this->simStats[ud_id][lane_num].user_counter[i]);
  }
}

SimUDRuntime_t::~SimUDRuntime_t() {
  // delete[] MappedMemory;
  delete[] ScratchpadMemory;
  munmap(MappedMemory, this->MachineConfig.MapMemSize);
//   munmap(ScratchpadMemory, this->MachineConfig.SPSize());
  delete[] GMappedMemory;
  delete[] ControlMemory;
}
} // namespace UpDown
