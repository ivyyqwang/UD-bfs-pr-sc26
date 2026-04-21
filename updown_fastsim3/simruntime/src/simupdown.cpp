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
  initialize();
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
  this->nodesPerRuntime = this->MachineConfig.NumNodes;
  initialize();
}

SimUDRuntime_t::SimUDRuntime_t(std::string programFile, std::string programName,
               std::string simulationDir, EmulatorLogLevel printLvl)
    : UDRuntime_t(), programFile(programFile), programName(programName),
      simulationDir(simulationDir), python_enabled() {
  initialize();
}

SimUDRuntime_t::SimUDRuntime_t(ud_machine_t machineConfig, std::string programFile,
               std::string programName, std::string simulationDir,
               EmulatorLogLevel printLvl)
    : UDRuntime_t(machineConfig), programFile(programFile),
      programName(programName), simulationDir(simulationDir),
      python_enabled(true) {
  UPDOWN_INFOMSG("Initializing runtime with custom machineConfig");

  // nodesPerRuntime needs to be initialized after MPI is initialized
  this->nodesPerRuntime = -1;
}


SimUDRuntime_t::SimUDRuntime_t(ud_machine_t machineConfig, std::string programFile,
               std::string programName)
    : UDRuntime_t(machineConfig), programFile(programFile),
      programName(programName),
      python_enabled(false) {
  UPDOWN_INFOMSG("Initializing runtime with custom machineConfig");

  // nodesPerRuntime needs to be initialized after MPI is initialized
  this->nodesPerRuntime = -1;
}


SimUDRuntime_t::SimUDRuntime_t(ud_machine_t machineConfig, std::string programFile)
    : UDRuntime_t(machineConfig), programFile(programFile),
      python_enabled(false) {
  UPDOWN_INFOMSG("Initializing runtime with custom machineConfig");

  // nodesPerRuntime needs to be initialized after MPI is initialized
  this->nodesPerRuntime = -1;
}


SimUDRuntime_t::SimUDRuntime_t(std::string programFile)
    : UDRuntime_t(), programFile(programFile),
      python_enabled(false) {
}

uint32_t SimUDRuntime_t::getMPIUDNodesPerRank() {
  return this->nodesPerRuntime;
}


void SimUDRuntime_t::initialize() {
  uint64_t total_uds = this->nodesPerRuntime * this->MachineConfig.NumStacks * this->MachineConfig.NumUDs;
  
  UPDOWN_INFOMSG("Adding stats for %lu UDs", total_uds);
  for(int i=0; i < total_uds; i++) {
    std::vector<struct SimStats> v(this->MachineConfig.NumLanes);
    this->simStats.push_back(v);
  }
  UPDOWN_INFOMSG("Running file %s Program %s Dir %s", programFile.c_str(),
                 programName.c_str(), simulationDir.c_str());
  init_stats();
}

void SimUDRuntime_t::initMemoryArrays(uint32_t myRank, uint32_t runtime_instances) {
  this->runtime_instances = runtime_instances;

  size_t size_mapMem = this->MachineConfig.MapMemSize;
  MappedMemory = (uint8_t *)mmap(nullptr, size_mapMem, PROT_READ | PROT_WRITE, MAP_ANONYMOUS | MAP_PRIVATE, -1, 0);
  UPDOWN_ERROR_IF(MappedMemory == MAP_FAILED, "Failed to allocate mapped memory with size %lu", size_mapMem);
  
  size_t size_gmapMem = this->MachineConfig.GMapMemSize / runtime_instances;
  GMappedMemory = (uint8_t *)mmap(nullptr, size_gmapMem, PROT_READ | PROT_WRITE, MAP_ANONYMOUS | MAP_PRIVATE, -1, 0);
  UPDOWN_ERROR_IF(GMappedMemory == MAP_FAILED, "Failed to allocate mapped global memory with size %lu", 
    size_gmapMem);
  
  size_t size_spMem = this->MachineConfig.SPSize() / runtime_instances;
  ScratchpadMemory = (uint8_t *)mmap(nullptr, size_spMem, PROT_READ | PROT_WRITE, MAP_ANONYMOUS | MAP_PRIVATE, -1, 0);
  UPDOWN_ERROR_IF(ScratchpadMemory == NULL, "Failed to allocate mapped memory with size %lu for LM",
     size_spMem);
  memset(ScratchpadMemory, 0, size_spMem);


  // Control Memory is not required in Fastsim3
  size_t size_control = this->MachineConfig.ControlSize();
  if(size_control != 0) {
    ControlMemory = new uint8_t[size_control];
    UPDOWN_ERROR_IF(ControlMemory == NULL, "Failed to allocate mapped memory with size %lu for Control Memory", size_control);
  } else {
    ControlMemory = nullptr;
  }

  // Changing the base locations for the simulated memory regions
  UPDOWN_INFOMSG("Runtime instances: %d", runtime_instances);
  this->MachineConfig.MapMemBase = reinterpret_cast<uint64_t>(MappedMemory);
  printf("MapMemBase:\tstart: %p, end: %p, size: 0x%lx (total: 0x%lx)\n", 
    (void *)this->MachineConfig.MapMemBase, 
    (void *)((uint64_t)this->MachineConfig.MapMemBase+size_mapMem-sizeof(uint64_t)), 
    size_mapMem,
    this->MachineConfig.MapMemSize * this->runtime_instances);

  this->MachineConfig.PhysGMapMemBase = reinterpret_cast<uint64_t>(GMappedMemory);
  printf("PhysGMapMemBase:\tstart: %p, end: %p, size: 0x%lx (total: 0x%lx)\n", 
    (void *)this->MachineConfig.PhysGMapMemBase,
    (void *)((uint64_t)this->MachineConfig.PhysGMapMemBase+size_gmapMem-sizeof(uint64_t)),
    size_gmapMem,
    this->MachineConfig.GMapMemSize);

  this->MachineConfig.UDbase = reinterpret_cast<uint64_t>(ScratchpadMemory);
  this->MachineConfig.SPMemBase = reinterpret_cast<uint64_t>(ScratchpadMemory);
  printf("SPMemBase/UDbase:\tstart: %p, end: %p, size: 0x%lx (total: 0x%lx)\n", 
    (void *)this->MachineConfig.SPMemBase,
    (void *)((uint64_t)this->MachineConfig.SPMemBase+size_spMem-sizeof(uint64_t)),
    size_spMem,
    this->MachineConfig.SPSize());
  
  this->MachineConfig.ControlBase = reinterpret_cast<uint64_t>(ControlMemory);
  printf("ControlBase:\tstart: %p, end: %p, size: 0x%lx\n", 
    (void *)this->MachineConfig.ControlBase,
    (void *)((uint64_t)this->MachineConfig.ControlBase+size_control-sizeof(uint64_t)),
    size_control);

  // ReInit Memory Manager with new machine configuration
  reset_memory_manager();
}


void SimUDRuntime_t::init_stats() {
  for (uint64_t ud_id=0; ud_id<this->MachineConfig.NumStacks * this->MachineConfig.NumUDs * this->nodesPerRuntime; ++ud_id) {
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

void SimUDRuntime_t::t2ud_memcpy(void *data, uint64_t size, networkid_t nwid,
                                 uint32_t offset) {
  UDRuntime_t::t2ud_memcpy(data, size, nwid, offset);
  uint32_t ud_num = this->get_globalUDNum(nwid);
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

  munmap(MappedMemory, this->MachineConfig.MapMemSize/this->runtime_instances);
  munmap(GMappedMemory, this->MachineConfig.GMapMemSize/this->runtime_instances);
  munmap(ScratchpadMemory, this->MachineConfig.SPSize() / runtime_instances);
  
  delete[] ControlMemory;
}
} // namespace UpDown
