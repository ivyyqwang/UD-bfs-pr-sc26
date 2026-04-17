#include "dramalloc.hpp"
#include "bfs_udweave_exe.hpp"
#include <basim_stats.hh>
#include <basimupdown.h>
#include <cmath>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <sys/types.h>
#include <queue>
#include <vector>
#include <cmath>
#include <sys/time.h>

using namespace std;

// #define DEBUG
#define VALIDATE_RESULT

#ifdef GEM5_MODE
#include <gem5/m5ops.h>
#endif

#ifdef VALIDATE_RESULT
#include <fstream>
#include <iostream>
#endif

#define USAGE "USAGE: ./bfs_udweave_global <gv_bfs_bin> <nl_bin> <num_lanes> <num_control_lanes_per_level> <root_vid> "

#define TOP_FLAG_OFFSET 0


/* Vertex Structure */
typedef struct Vertex {
  uint64_t degree;
  uint64_t vid;
  uint64_t *neighbors;
  uint64_t orig_vid;
  uint64_t split_start;
  uint64_t split_end;
  uint64_t parent; // value in PR, default 0
  int64_t distance;  // padding in PR
}vertex_t;


/* Compare UpDown BFS with CPU BFS result */
int cpu_bfs(Vertex *g_v, uint64_t root_id, uint64_t n_vertices){
  queue<uint64_t> q;
  vector<uint64_t> cpu_distance(n_vertices, -1);
  Vertex *vertex = (Vertex *) (g_v + root_id);
  uint64_t distance = vertex->distance;
  root_id = vertex->orig_vid;
  if(distance != 0){
    return 1;
  }
  cpu_distance[root_id] = 0;
  q.push(root_id);
  uint64_t access_v = 0;

  uint64_t distance_level = 0;

  while (!q.empty()) {
    uint64_t vid = q.front();
    access_v++;
    // printf("vid = %lu, %lu\n", vid, n_vertices);
    // fflush(stdout);
    q.pop();
    vertex = (Vertex *)(g_v + vid);
    distance = vertex->distance;
    if(distance_level  < distance){
      // printf("distance = %lu\n", distance);
      // fflush(stdout);
      distance_level = distance;
    }
    // printf("distance = %lu\n", distance);
    // fflush(stdout);
    if(distance != cpu_distance[vid]){
      printf("vid = %lu, updown distance = %lu, updown parent = %lu, cpu distenace = %lu\n", vid, distance, vertex->parent, cpu_distance[vid]);
      return 1;
    }
    if(vertex->split_end == 0){
      uint64_t *neighbors = vertex->neighbors;
      for (int j = 0; j < vertex->degree; j++) {
        uint64_t *temp_neigh = (uint64_t *)(neighbors + j);
        uint64_t new_vid = temp_neigh[0];
        Vertex * new_vertex = (Vertex *)(g_v + new_vid);
        new_vid = new_vertex->orig_vid;
        if(cpu_distance[new_vid] == -1){
          cpu_distance[new_vid] = distance + 1;
          q.push(new_vid);
        }
      }
    }
    else{
      uint64_t split_vid = vertex->split_start;
      uint64_t split_bound = vertex->split_end;
      // printf("[%lu,%lu]\n", split_vid, split_bound);
      fflush(stdout);
      for(unsigned vid = split_vid; vid < split_bound; vid++){
        vertex = (Vertex *)(g_v + vid);
        uint64_t *neighbors = vertex->neighbors;
        for (int j = 0; j < vertex->degree; j++) {
          uint64_t *temp_neigh = (uint64_t *)(neighbors + j);
          uint64_t new_vid = temp_neigh[0];
          Vertex * new_vertex = (Vertex *)(g_v + new_vid);
          new_vid = new_vertex->orig_vid;
          if(cpu_distance[new_vid] == -1){
            cpu_distance[new_vid] = distance + 1;
            q.push(new_vid);
          }
        }
      }
    }
  }
  printf("Access num of v = %lu\n", access_v);
  return 0;
}


/* UpDown BFS */
uint64_t bfs_main_updown_iter(UpDown::UDRuntime_t *rt, Vertex* gv, uint64_t* queue, uint64_t queue_length, uint64_t num_lanes, uint64_t num_control_lanes_per_level) {

  UpDown::word_t ops_data[8];
  UpDown::operands_t ops(8, ops_data);

  uint64_t log2_num_control_lanes_per_level = std::log2(num_control_lanes_per_level);

  ops.set_operand(0, (uint64_t)num_lanes);
  ops.set_operand(1, (uint64_t)gv);
  ops.set_operand(2, (uint64_t)queue);
  ops.set_operand(3, (uint64_t)queue_length);
  ops.set_operand(4, (uint64_t)0);
  ops.set_operand(5, (uint64_t)num_lanes);
  ops.set_operand(6, (uint64_t)log2_num_control_lanes_per_level);
  ops.set_operand(7, (uint64_t)0);


  UpDown::networkid_t nwid(0, false, 0);
  UpDown::event_t event_ops(bfs_udweave_exe::main_master__init /*Event Label*/, nwid, UpDown::CREATE_THREAD /*Thread ID*/, &ops /*Operands*/);
  rt->send_event(event_ops);
  uint64_t val = 0;
  rt->t2ud_memcpy(&val, sizeof(uint64_t), nwid, TOP_FLAG_OFFSET);

#ifdef GEM5_MODE
  m5_reset_stats(0, 0);
#else
  ((UpDown::BASimUDRuntime_t *)rt)->reset_all_stats();
  ((UpDown::BASimUDRuntime_t *)rt)->reset_sim_ticks();
#endif

  rt->start_exec(nwid);

  rt->test_wait_addr(nwid, TOP_FLAG_OFFSET, 1);

#ifdef GEM5_MODE
  m5_dump_reset_stats(0, 0);
#endif

  return val;
}

/* Cpoy between local and global, only work on Fastsim2 */
size_t CopyLocal2Global(dramalloc::DramAllocator* allocator, uint64_t chunck_size, uint64_t local_addr, uint64_t global_addr, uint64_t copy_size){
    uint64_t current_copy_size = 0;
    uint64_t current_global_addr = global_addr;
    uint64_t current_local_addr = local_addr;
    while(current_copy_size < copy_size){
      uint64_t size = chunck_size;
      if((copy_size - current_copy_size) < size)
        size = copy_size - current_copy_size;
      void *current_global_addr_sa = allocator->translate_udva2sa(current_global_addr);
      memcpy(current_global_addr_sa, reinterpret_cast<void *>(current_local_addr), size);
      current_copy_size = current_copy_size + size;
      current_global_addr = current_global_addr + size;
      current_local_addr = current_local_addr + size;
    }
    return current_copy_size;
}

size_t CopyGlobal2Local(dramalloc::DramAllocator* allocator, uint64_t chunck_size, uint64_t global_addr, uint64_t local_addr, uint64_t copy_size){
    uint64_t current_copy_size = 0;
    uint64_t current_global_addr = global_addr;
    uint64_t current_local_addr = local_addr;
    while(current_copy_size < copy_size){
      uint64_t size = chunck_size;
      if((copy_size - current_copy_size) < size)
        size = copy_size - current_copy_size;
      void *current_global_addr_sa = allocator->translate_udva2sa(current_global_addr);
      memcpy(reinterpret_cast<void *>(current_local_addr), current_global_addr_sa, size);
      current_copy_size = current_copy_size + size;
      current_global_addr = current_global_addr + size;
      current_local_addr = current_local_addr + size;
    }
    return current_copy_size;
}

uint64_t next_power_of_2(uint64_t n) {
    if (n == 0) return 1;
    n--;
    n |= n >> 1;
    n |= n >> 2;
    n |= n >> 4;
    n |= n >> 8;
    n |= n >> 16;
    n |= n >> 32;
    return n + 1;
}

bool is_power_of_2(uint64_t x) {
    return x && !(x & (x - 1));
}


uint64_t next_power_of_2_or_same(uint64_t n) {
    if (n == 0) return 1;
    if (is_power_of_2(n)) return n;
    return next_power_of_2(n);
}


size_t getMemoryUsageKB() {
    std::ifstream status("/proc/self/status");
    std::string line;
    while (std::getline(status, line)) {
        if (line.rfind("VmRSS:", 0) == 0) {
            std::istringstream iss(line);
            std::string key, value, unit;
            iss >> key >> value >> unit;
            return std::stoul(value); // VmRSS is in KB
        }
    }
    return 0;
}

int main(int argc, char *argv[]) {
  timeval start,end;
  timeval start1,end1;
  double time;

  #if not defined GEM5_MODE
  gettimeofday(&start,NULL);
  #endif
/*---------------------------- Input Parameter ----------------------------*/
  uint64_t blockSize = 1UL * 32 * 1024; // 32KB
  if (argc < 6) {
    printf("Insufficient Input Params\n");
    printf("%s\n", USAGE);
    exit(1);
  }
  char* filename = argv[1];
  char* filename2 = argv[2];
  uint64_t num_lanes = atoi(argv[3]);
  uint64_t num_control_lanes_per_level = atoi(argv[4]);
  uint64_t root_vertex_id = atoi(argv[5]);
  uint64_t network_latency = 1100;
  uint64_t network_bandwidth = 0;
  
  if (argc >= 7) {
    network_latency = atoi(argv[6]);
  }

  if (argc >= 8) {
    network_bandwidth = atoi(argv[7]);
  }

  printf("network_latency = %lu, network_bandwidth = %lu\n", network_latency, network_bandwidth);
  fflush(stdout);

  if(!is_power_of_2(num_lanes)){
    printf("The number of lanes to be a power of 2!!!\n");
    exit(1);
  }
  printf("Num Lanes:%ld\n", num_lanes); fflush(stdout);

  /*---------------------------- read input files ----------------------------*/
  printf("File Name:%s , ", filename);
  FILE* in_file_gv = fopen(filename, "rb");
  if (!in_file_gv) {
    printf("Error when openning file, exiting.\n");
    exit(EXIT_FAILURE);
  }
  printf("File Name:%s , ", filename2);
  FILE* in_file_nl = fopen(filename2, "rb");
  if (!in_file_nl) {
    printf("Error when openning file, exiting.\n");
    exit(EXIT_FAILURE);
  }

  uint64_t num_verts, num_split_verts, num_edges, nlist_size;
  size_t n;
  fseek(in_file_gv, 0, SEEK_SET);
  fseek(in_file_nl, 0, SEEK_SET);
  n = fread(&num_verts, sizeof(num_verts),1, in_file_gv);
  n = fread(&num_split_verts, sizeof(num_split_verts),1, in_file_gv);
  n = fread(&num_edges, sizeof(num_edges), 1, in_file_nl);
  n = fread(&nlist_size, sizeof(nlist_size), 1, in_file_nl);
  printf("num_verts = %lu, num_split_verts = %lu\n", num_verts, num_split_verts);
  printf("num_edges = %lu, nlist_size = %lu\n", num_edges, nlist_size);  fflush(stdout);


  /*---------------------------- compute memory size ----------------------------*/
  uint64_t g_v_bin_size = num_split_verts * sizeof(vertex_t);
  uint64_t nlist_beg_size = nlist_size * sizeof(uint64_t);
  uint64_t avg_deg = num_edges / num_split_verts * 1.8;
  uint64_t queue_length = (num_split_verts * avg_deg / num_lanes) / 2 * 2;
  if(queue_length < 1024)
    queue_length = 1024;
  uint64_t queue_size = (queue_length * 2 + 2) * num_lanes * sizeof(uint64_t);
  
  uint64_t localDRAMRequirement = blockSize + queue_size;
  uint64_t globalDRAMRequirement = g_v_bin_size + nlist_beg_size;
  #ifdef VALIDATE_RESULT
  localDRAMRequirement = g_v_bin_size + nlist_beg_size + blockSize + queue_size;
  printf("\tPrivate DRAM: g_v_bin_size: %lu\n\tnlist_beg_size: %lu\n\tfrontier_size: %lu\n\tblockSize: %lu\n\tSum: %lu\n", g_v_bin_size, nlist_beg_size, queue_size, blockSize, localDRAMRequirement);
  printf("\tGlobal DRAM: g_v_bin_size: %lu\n\tnlist_beg_size: %lu\n\tfrontier_size: %lu\n\tSum: %lu\n", g_v_bin_size, nlist_beg_size, globalDRAMRequirement);
  #else
  printf("\tPrivate DRAM: blockSize: %lu\n\tfrontier_size: %lu\n\tSum: %lu\n", blockSize, queue_size, localDRAMRequirement);
  printf("\tGlobal DRAM: g_v_bin_size: %lu\n\tnlist_beg_size: %lu\n\tfrontier_size: %lu\n\tSum: %lu\n", g_v_bin_size, nlist_beg_size, globalDRAMRequirement);
  #endif

  localDRAMRequirement = next_power_of_2_or_same(localDRAMRequirement);
  globalDRAMRequirement = next_power_of_2_or_same(globalDRAMRequirement);
  printf("Local DRAM Size: %lu, Global DRAM Size: %lu\n", localDRAMRequirement, globalDRAMRequirement); fflush(stdout);

  /*---------------------------- UpDown Machine Configuration ----------------------------*/

  // Set up machine parameters
  UpDown::ud_machine_t machine;
  uint64_t num_nodes = std::ceil(num_lanes / (64.0 * 4 * 8));

  /* A smaller memory configuration for testing */
  if(num_lanes <= 2048){
     machine.MapMemSize = next_power_of_2_or_same(localDRAMRequirement+globalDRAMRequirement);
     machine.GMapMemSize = 1UL << 30; // 1GB
  }else{
    machine.MapMemSize = localDRAMRequirement;
    machine.GMapMemSize = globalDRAMRequirement;
  }

  machine.LocalMemAddrMode = 1;
  machine.NumLanes = num_lanes > 64 ? 64 : num_lanes;
  machine.NumUDs = std::ceil(num_lanes / 64.0) > 4 ? 4 : std::ceil(num_lanes / 64.0);
  machine.NumStacks = std::ceil(num_lanes / (64.0 * 4)) > 8 ? 8 : std::ceil(num_lanes / (64.0 * 4));
  machine.NumNodes = std::ceil(num_lanes / (64.0 * 4 * 8));
  machine.InterNodeLatency = network_latency;
  machine.InterNodeBandwidth = network_bandwidth;

  printf("Machine Local DRAM Size: %lu, Global DRAM Size: %lu\n", machine.MapMemSize, machine.GMapMemSize); fflush(stdout);
  printf("Current memory consumption: %lu KB\n", getMemoryUsageKB()); fflush(stdout);


#ifdef GEM5_MODE
  UpDown::UDRuntime_t *rt = new UpDown::UDRuntime_t(machine);
#else
  // UpDown::BASimUDRuntime_t* rt = new UpDown::BASimUDRuntime_t(machine, "bfs_udweave_exe.bin", 0, 100);
  UpDown::BASimUDRuntime_t* rt = new UpDown::BASimUDRuntime_t(machine, "bfs_udweave_exe.bin", 0, 100, std::string("bfs") + "_" + std::to_string(num_lanes) + "nds");
#endif

#ifdef DEBUG
  printf("=== Base Addresses ===\n");
  bfs_rt->dumpBaseAddrs();
  printf("\n=== Machine Config ===\n");
  bfs_rt->dumpMachineConfig();
#endif

  /*---------------------------- Initialize DramAllocator ----------------------------*/
  printf("Initialize DRAMalloc\n");  fflush(stdout);
#ifdef GEM5_MODE
  dramalloc::DramAllocator *allocator = new dramalloc::DramAllocator(rt, bfs_udweave_exe::DRAMalloc__global_broadcast /*eventlabel*/, blockSize);
#else
  dramalloc::DramAllocator *allocator = new dramalloc::DramAllocator(rt, bfs_udweave_exe::DRAMalloc__global_broadcast /*eventlabel*/);
#endif
  printf("Finish initialize DRAMalloc\n");  fflush(stdout);

  if((blockSize % sizeof(vertex_t)) != 0){
    fprintf(stderr, "blockSize must be an integer multiple of sizeof(vertex_t)!\n");
    return 1;
  }
  if((blockSize % sizeof(uint64_t)) != 0){
    fprintf(stderr, "blockSize must be an integer multiple of sizeof(uint64_t)!\n");
    return 1;
  }

  vertex_t * g_v_bin_global_va = reinterpret_cast<vertex_t *>(allocator->mm_malloc_global(g_v_bin_size, blockSize, num_nodes, 0));
  uint64_t* nlist_beg_global_va = reinterpret_cast<uint64_t*>(allocator->mm_malloc_global(nlist_beg_size, blockSize, num_nodes, 0));
  // uint64_t *frontier_global_va = reinterpret_cast<uint64_t *>(allocator->mm_malloc_global(queue_size, blockSize, num_nodes, 0));
  uint64_t *frontier_va = reinterpret_cast<uint64_t *>(rt->mm_malloc(queue_size));
  /*---------------------------- Load g_v_bin ----------------------------*/
  printf("Load g_v_bin_global.\n"); fflush(stdout);
  #if not defined GEM5_MODE
  gettimeofday(&start1,NULL);
  #endif

  uint64_t va1 = reinterpret_cast<uint64_t>(g_v_bin_global_va);
  uint64_t va1_end = reinterpret_cast<uint64_t>(g_v_bin_global_va) + g_v_bin_size;

  while(va1 < va1_end){
    vertex_t * sa1 = reinterpret_cast<vertex_t *>(allocator->translate_udva2sa(va1));
    int64_t len = blockSize;
    if((va1 + len) > va1_end){
      len = va1_end - va1;
    }
    fread(sa1, sizeof(vertex_t), len/sizeof(vertex_t), in_file_gv); // read in all vertices 
    for(int64_t j = 0; j < len/sizeof(vertex_t); j++){
        int64_t offset = (uint64_t)(sa1[j].neighbors);
        uint64_t *loc_nlist = nlist_beg_global_va + offset;
        sa1[j].neighbors = loc_nlist;
        sa1[j].parent = 0;
        sa1[j].distance = -1;

        // if(sa1[j].vid < 10){
        //   printf("vid = %lu, deg = %lu, orig_vid = %lu, distance = %ld", sa1[j].vid, sa1[j].degree, sa1[j].orig_vid, sa1[j].distance);
        //   fflush(stdout);
        // }
      }
      va1 = va1 + len;
  }

  fclose(in_file_gv);
  #if not defined GEM5_MODE
  gettimeofday(&end1,NULL);
  time = (end1.tv_sec-start1.tv_sec) + (end1.tv_usec-start1.tv_usec) / 1000000.0;
  printf("Loading g_v_bin_global time:%lf s\n", time); fflush(stdout);
  #endif


  /*---------------------------- Load nlist_bin ----------------------------*/
  printf("Load nlist_beg_global.\n"); fflush(stdout);
  #if not defined GEM5_MODE
  gettimeofday(&start1,NULL);
  #endif

  va1 = reinterpret_cast<uint64_t>(nlist_beg_global_va);
  va1_end = reinterpret_cast<uint64_t>(nlist_beg_global_va) + nlist_beg_size;

  while(va1 < va1_end){
    uint64_t * sa1 = reinterpret_cast<uint64_t *>(allocator->translate_udva2sa(va1));
    int64_t len = blockSize;
    if((va1 + len) > va1_end){
      len = va1_end - va1;
    }
    fread(sa1, sizeof(int64_t), len/sizeof(int64_t), in_file_nl); // read in all edges
    va1 = va1 + len;
  }

  fclose(in_file_nl);
  #if not defined GEM5_MODE
  gettimeofday(&end1,NULL);
  time = (end1.tv_sec-start1.tv_sec) + (end1.tv_usec-start1.tv_usec) / 1000000.0;
  printf("Loading nlist_beg_global time:%lf s\n", time); fflush(stdout);
  #endif

  /*---------------------------- Initialize frontier ----------------------------*/
  printf("Initialize frontier.\n"); fflush(stdout);
  #if not defined GEM5_MODE
  gettimeofday(&start1,NULL);
  #endif

  va1 = reinterpret_cast<uint64_t>(frontier_va);
  va1_end = reinterpret_cast<uint64_t>(frontier_va) + queue_size;

  while(va1 < va1_end){
    uint64_t * sa1 = reinterpret_cast<uint64_t *>(va1);
    int64_t len = blockSize;
    if((va1 + len) > va1_end){
      len = va1_end - va1;
    }
    memset(sa1, 0, len);
    if(va1 == reinterpret_cast<uint64_t>(frontier_va)){
      sa1[0] = 2;
      sa1[1] = 0;
      sa1[2] = root_vertex_id;
      sa1[3] = root_vertex_id;
    }
    va1 = va1 + len;
  }
  #if not defined GEM5_MODE
  gettimeofday(&end1,NULL);
  time = (end1.tv_sec-start1.tv_sec) + (end1.tv_usec-start1.tv_usec) / 1000000.0;
  printf("Initialize frontier time:%lf s\n", time); fflush(stdout);
  #endif

  #if not defined GEM5_MODE
  gettimeofday(&end,NULL);
  time = (end.tv_sec-start.tv_sec) + (end.tv_usec-start.tv_usec) / 1000000.0;
  printf("Loading time:%lf s\n", time); fflush(stdout);
  #endif

  /*---------------------------- Start UpDown ----------------------------*/
  printf("Finish DRAM loading, start running BFS.\n");
  fflush(stdout);

  #ifdef GEM5_MODE
  m5_switch_cpu();
  #else
  rt->reset_all_stats();
  #endif

  printf("Starting UD now\n");
  fflush(stdout);
  #if not defined GEM5_MODE
  gettimeofday(&start,NULL);
  #endif

  UpDown::word_t ops_data[8];
  UpDown::operands_t ops(8, ops_data);

  uint64_t log2_num_control_lanes_per_level = std::log2(num_control_lanes_per_level);

  ops.set_operand(0, (uint64_t)num_lanes);
  ops.set_operand(1, (uint64_t)g_v_bin_global_va);
  ops.set_operand(2, (uint64_t)frontier_va);
  ops.set_operand(3, (uint64_t)queue_length);
  ops.set_operand(4, (uint64_t)0);
  ops.set_operand(5, (uint64_t)num_lanes);
  ops.set_operand(6, (uint64_t)log2_num_control_lanes_per_level);
  ops.set_operand(7, (uint64_t)0);


  UpDown::networkid_t nwid(0, false, 0);
  UpDown::event_t event_ops(bfs_udweave_exe::main_master__init /*Event Label*/, nwid, UpDown::CREATE_THREAD /*Thread ID*/, &ops /*Operands*/);
  rt->send_event(event_ops);
  uint64_t flag = 0;
  rt->t2ud_memcpy(&flag, sizeof(uint64_t), nwid, TOP_FLAG_OFFSET);

  #if defined GEM5_MODE
  m5_dump_reset_stats(0,0);
  #endif
  rt->start_exec(nwid);
  rt->test_wait_addr(nwid, TOP_FLAG_OFFSET, 1);
  
  #if not defined GEM5_MODE
  gettimeofday(&end,NULL);
  time = (end.tv_sec-start.tv_sec) + (end.tv_usec-start.tv_usec) / 1000000.0;
  printf("BFS UpDown time:%lf s\n", time); fflush(stdout);
  #endif

  #if not defined GEM5_MODE
	for(int j=0; j<num_lanes; j++)
	{
		printf("UD = %d, Lane = %d\n",(j / 64) , j%64);
		rt->print_stats((j / 64) , j%64);
		#ifdef DETAIL_STATS
		rt->print_histograms(j / 64 , j%64);
		#endif
	}
	#endif


  /*---------------------------- Validate ----------------------------*/
  #ifdef VALIDATE_RESULT
  vertex_t *g_v_bin = reinterpret_cast<vertex_t *>(malloc(g_v_bin_size));
  uint64_t* nlist_beg = reinterpret_cast<uint64_t*>(malloc(nlist_beg_size));
  int64_t nlist_offset = reinterpret_cast<int64_t>(nlist_beg) - reinterpret_cast<int64_t>(nlist_beg_global_va);

  if(g_v_bin == NULL || nlist_beg == NULL){
    printf("Error, malloc failed\n"); fflush(stdout);
    exit(1);
  }
 
  va1 = reinterpret_cast<uint64_t>(g_v_bin_global_va);
  va1_end = reinterpret_cast<uint64_t>(g_v_bin_global_va) + g_v_bin_size;

  uint64_t va2 = reinterpret_cast<uint64_t>(g_v_bin);

  while(va1 < va1_end){
    vertex_t * sa1 = reinterpret_cast<vertex_t *>(allocator->translate_udva2sa(va1));
    int64_t len = blockSize;
    if((va1 + len) > va1_end){
      len = va1_end - va1;
    }
    vertex_t * sa2 = reinterpret_cast<vertex_t *>(va2);
    memcpy(sa2, reinterpret_cast<vertex_t *>(sa1), len);
    for(int64_t j = 0; j < len/sizeof(vertex_t); j++){
        int64_t offset = (uint64_t)(sa2[j].neighbors);
        uint64_t *loc_nlist = reinterpret_cast<uint64_t *>(offset + nlist_offset);
        sa2[j].neighbors = loc_nlist;
      }
      va1 = va1 + len;
      va2 = va2 + len;
  }

  in_file_nl = fopen(filename2, "rb");
  if (!in_file_nl) {
    printf("Error when openning file, exiting.\n");
    exit(EXIT_FAILURE);
  }
  fseek(in_file_nl, 0, SEEK_SET);
  n = fread(&num_edges, sizeof(num_edges), 1, in_file_nl);
  n = fread(&nlist_size, sizeof(nlist_size), 1, in_file_nl);
  n = fread(nlist_beg, sizeof(int64_t), nlist_size, in_file_nl); // read in all edges
  fclose(in_file_nl);
  #endif

  delete rt;

  /*---------------------------- Validate ----------------------------*/
  #ifdef VALIDATE_RESULT
  printf("start validate \n"); fflush(stdout);
  if(cpu_bfs(g_v_bin, root_vertex_id, num_split_verts) == 0)
    printf("Validate Pass\n");
  else
    printf("Validate Fail\n");
  #endif

}
