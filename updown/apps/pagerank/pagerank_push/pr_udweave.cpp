#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <random>
#include <string>
#include <sys/time.h>
#include "./utils.hpp"

#ifndef DRAMALLOC
#define DRAMALLOC
#include "dramalloc.hpp"
#endif

#ifdef BASIM
#include <basimupdown.h>
#endif

#ifdef GEM5_MODE
 #include <gem5/m5ops.h>
#endif

#define VALIDATE_RESULT
#define DEBUG


#include "out/pr_exe.hpp"

#define USAGE "USAGE: ./pr_udweave <graph_file_gv.bin> <graph_file_nl.bin> <num_nodes> \n\
  graph_file_gv.bin: \tpath to the graph vertices file.\n\
  graph_file_nl.bin: \tpath to the graph edges file.\n\
  num_nodes: \tnumber of nodes, minimum is 1.\n"

#define NUM_LANE_PER_UD 64
#define NUM_UD_PER_CLUSTER 4
#define NUM_CLUSTER_PER_NODE 8
#define TOP_FLAG_OFFSET 0

#define PART_PARM 1
// #define SHUFFLE_PARTITIONS

typedef struct Vertex{
  uint64_t deg;
  uint64_t id;
  uint64_t* neighbors;
  uint64_t orig_vid;
  uint64_t split_start;
  uint64_t split_bound;
  double val;
  uint64_t gv_bin;
}vertex_t;

struct Iterator {
  Vertex* begin;
  Vertex* end;
};

struct Value{
  double val;
};

void pagerank_top(Vertex *g_v, Value *val_array, uint64_t num_vertices){
  uint64_t vid = 0;
  uint64_t deg, uid;
  double old_val, new_val;
  uint64_t* edge_list;
  while (vid < num_vertices) {
    deg = g_v[vid].deg;
    old_val = g_v[vid].val;

    if (deg == 0) {
      vid ++;
      continue;
    }

    if(g_v[vid].id != g_v[vid].orig_vid){
    // if (deg == 0) {
      uint64_t new_deg = 0;
      double old_val = 0;
      for(uint64_t tmp_id = g_v[vid].split_start; tmp_id < g_v[vid].split_bound; tmp_id++){
        new_deg += g_v[tmp_id].deg;
        old_val += g_v[tmp_id].val;
      }
      new_val = old_val / new_deg;
    }else{
      new_val = old_val / deg;
    }
    
    edge_list = g_v[vid].neighbors;
    for (uint64_t j = 0; j < deg; j++) {
      uid = edge_list[j];
      val_array[uid].val += new_val;
      uint64_t* ptr = (uint64_t*)(&new_val);
      // if(uid == 57){
      //   printf("vid 57, add %lf (%llu) from %lu, now %lf\n", new_val, *ptr, vid, val_array[uid].val);
      // }
    }
    vid ++;
  }
}

bool compare(Value *val_array0, Value *val_array1, uint64_t num_vertices){
  bool return_value = true;
  for(uint64_t i=0; i<num_vertices; i++){
    if(!almostEqual(val_array0[i].val, val_array1[i].val)){
      printf("index %lu not match, %lf != %lf\n", i, val_array0[i].val, val_array1[i].val);
      return_value = false;
      return return_value;
    }
  }
  return return_value;
}


int main(int argc, char* argv[]) {
  timeval start,end;
  timeval start1,end1;
  double time;
  uint64_t blockSize = 1UL * 32 * 1024; // 32KB

  #if not defined GEM5_MODE
  gettimeofday(&start,NULL);
  #endif
/*---------------------------- Input Parameter ----------------------------*/

  if (argc < 4) {
    printf("Insufficient Input Params\n");
    printf("%s\n", USAGE);
    exit(1);
  }
  
  char* filename = argv[1];
  char* filename2 = argv[2];
  uint64_t num_nodes = atoi(argv[3]);
  uint64_t num_uds_per_node = NUM_UD_PER_CLUSTER * NUM_CLUSTER_PER_NODE;
  uint64_t num_lanes_per_ud = NUM_LANE_PER_UD;
  uint64_t network_latency = 1100;
  uint64_t network_bandwidth = 0;

  if (argc >= 5) {
    network_latency = atoi(argv[4]);
  }

  if (argc >= 6) {
    network_bandwidth = atoi(argv[5]);
  }

  printf("network_latency = %lu, network_bandwidth = %lu\n", network_latency, network_bandwidth);
  fflush(stdout);

  printf("Test configurations: \n\tnum_nodes = %ld, \n\tnum_uds_per_node = %ld, \n\tnum_lanes_per_ud = %ld, ", num_nodes, num_uds_per_node, num_lanes_per_ud);
  fflush(stdout);
  uint64_t num_lanes = num_nodes * num_uds_per_node * num_lanes_per_ud;

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
  uint64_t g_v_val_size = num_split_verts * sizeof(Value);
  uint64_t num_partitions = num_lanes * PART_PARM;
  uint64_t num_pairs_per_part = ceil((num_split_verts + 0.0) / num_partitions);
  uint64_t partitions_size = (num_partitions) * sizeof(Iterator);

  uint64_t localDRAMRequirement = blockSize;
  uint64_t globalDRAMRequirement = g_v_bin_size + nlist_beg_size + g_v_val_size + partitions_size;
  #ifdef VALIDATE_RESULT
  localDRAMRequirement = g_v_bin_size + nlist_beg_size + g_v_val_size;
  printf("\tPrivate DRAM: g_v_bin_size: %lu\n\tnlist_beg_size: %lu\n\tg_v_val_size: %lu\n\tSum: %lu\n", g_v_bin_size, nlist_beg_size, g_v_val_size, localDRAMRequirement);
  printf("\tGlobal DRAM: g_v_bin_size: %lu\n\tnlist_beg_size: %lu\n\tg_v_val_size: %lu\n\tpartitions_size: %lu\n\tSum: %lu\n", g_v_bin_size, nlist_beg_size, g_v_val_size, partitions_size, globalDRAMRequirement);
  #else
  printf("\tPrivate DRAM: blockSize: %lu\n\tSum: %lu\n", blockSize, localDRAMRequirement);
  printf("\tGlobal DRAM: g_v_bin_size: %lu\n\tnlist_beg_size: %lu\n\tg_v_val_size: %lu\n\tpartitions_size: %lu\n\tSum: %lu\n", g_v_bin_size, nlist_beg_size, g_v_val_size, partitions_size, globalDRAMRequirement);
  #endif

  localDRAMRequirement = next_power_of_2_or_same(localDRAMRequirement);
  globalDRAMRequirement = next_power_of_2_or_same(globalDRAMRequirement);
  printf("Local DRAM Size: %lu, Global DRAM Size: %lu\n", localDRAMRequirement, globalDRAMRequirement); fflush(stdout);


  /*---------------------------- UpDown Machine Configuration ----------------------------*/
  // Set up machine parameters
  UpDown::ud_machine_t machine;

  /* A smaller memory configuration for testing */
  if(num_lanes <= 2048){
     machine.MapMemSize = globalDRAMRequirement;
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
#elif BASIM
  UpDown::BASimUDRuntime_t* rt = new UpDown::BASimUDRuntime_t(machine, "pr_exe.bin", 0);
#endif

#ifdef DEBUG
  printf("=== Base Addresses ===\n");
  rt->dumpBaseAddrs();
  printf("\n=== Machine Config ===\n");
  rt->dumpMachineConfig();
#endif

  /*---------------------------- Initialize DramAllocator ----------------------------*/
  printf("Initialize DRAMalloc\n");
  #ifdef GEM5_MODE
  dramalloc::DramAllocator *allocator = new dramalloc::DramAllocator(rt, pr_exe::DRAMalloc__global_broadcast /*eventlabel*/, blockSize);
  #else
  dramalloc::DramAllocator *allocator = new dramalloc::DramAllocator(rt, pr_exe::DRAMalloc__global_broadcast /*eventlabel*/);
  #endif
  printf("Finish initialize DRAMalloc\n");

  if((blockSize % sizeof(Vertex)) != 0){
    fprintf(stderr, "blockSize must be an integer multiple of sizeof(Vertex)!\n");
    return 1;
  }
  
  Vertex* g_v_bin_global_va = reinterpret_cast<Vertex *>(allocator->mm_malloc_global(g_v_bin_size, blockSize, num_nodes, 0));
  Value* g_v_val_global_va  = reinterpret_cast<Value *>(allocator->mm_malloc_global(g_v_val_size, blockSize, num_nodes, 0));
  uint64_t* nlist_beg_global_va = reinterpret_cast<uint64_t *>(allocator->mm_malloc_global(nlist_beg_size, blockSize, num_nodes, 0));
  Iterator* partitions_global_va = reinterpret_cast<Iterator *>(allocator->mm_malloc_global(partitions_size, blockSize, num_nodes, 0));


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
    n = fread(sa1, sizeof(vertex_t), len/sizeof(vertex_t), in_file_gv); // read in all vertices 
    for(int64_t j = 0; j < len/sizeof(vertex_t); j++){
        int64_t offset = (uint64_t)(sa1[j].neighbors);
        uint64_t *loc_nlist = nlist_beg_global_va + offset;
        sa1[j].neighbors = loc_nlist;
        sa1[j].val = 1.0;
        sa1[j].gv_bin = reinterpret_cast<uint64_t>(g_v_bin_global_va);

        // if(sa1[j].id < 10){
        //   printf("vid = %lu, degree = %lu, orig_vid = %lu\n", sa1[j].id, sa1[j].deg, sa1[j].orig_vid);
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
    n = fread(sa1, sizeof(int64_t), len/sizeof(int64_t), in_file_nl); // read in all edges
    va1 = va1 + len;
  }

  fclose(in_file_nl);
  #if not defined GEM5_MODE
  gettimeofday(&end1,NULL);
  time = (end1.tv_sec-start1.tv_sec) + (end1.tv_usec-start1.tv_usec) / 1000000.0;
  printf("Loading nlist_beg_global time:%lf s\n", time); fflush(stdout);
  #endif

  /*---------------------------- Initialize g_v_val_global ----------------------------*/
  printf("Initialize g_v_val_global.\n"); fflush(stdout);
  #if not defined GEM5_MODE
  gettimeofday(&start1,NULL);
  #endif

  va1 = reinterpret_cast<uint64_t>(g_v_val_global_va);
  va1_end = reinterpret_cast<uint64_t>(g_v_val_global_va) + g_v_val_size;

  while(va1 < va1_end){
    uint64_t * sa1 = reinterpret_cast<uint64_t *>(allocator->translate_udva2sa(va1));
    int64_t len = blockSize;
    if((va1 + len) > va1_end){
      len = va1_end - va1;
    }
    memset(sa1, 0, len);
    va1 = va1 + len;
  }
  #if not defined GEM5_MODE
  gettimeofday(&end1,NULL);
  time = (end1.tv_sec-start1.tv_sec) + (end1.tv_usec-start1.tv_usec) / 1000000.0;
  printf("Initialize g_v_val_global time:%lf s\n", time); fflush(stdout);
  #endif


  /*---------------------------- Initialize partitions_global ----------------------------*/
  printf("Initialize partitions_global.\n"); fflush(stdout);
  #if not defined GEM5_MODE
  gettimeofday(&start1,NULL);
  #endif

#ifdef SHUFFLE_PARTITIONS
  Iterator *partitions_local_va = reinterpret_cast<Iterator *>(malloc(partitions_size));

  std::mt19937 g(42); // fixed seed for reproducibility

  uint64_t offset = 0;

  for (int i = 0; i < num_partitions; i++) {
    partitions_local_va[i].begin = g_v_bin_global_va + offset;
    offset = std::min((i+1) * num_pairs_per_part, num_split_verts);
    partitions_local_va[i].end = g_v_bin_global_va + offset;
  }

  // shuffle partitions to avoid bank conflict
  printf("Shuffle the partition array");
  std::shuffle(partitions_local_va, partitions_local_va + num_partitions, g);

#ifdef DEBUG_PARTITIONS
  printf("After shuffling partitions_local_va:\n");
  for (int i = 0; i < num_partitions; i++) {
    printf("Partition 1 idx=%d: begin = %p, end = %p\n", i, partitions_local_va0[i].begin, partitions_local_va0[i].end);
  }
#endif

  CopyLocal2Global(allocator, blockSize, (uint64_t)partitions_global_va, (uint64_t)partitions_local_va, partitions_size);

#else

  va1 = reinterpret_cast<uint64_t>(partitions_global_va);
  va1_end = reinterpret_cast<uint64_t>(partitions_global_va) + partitions_size;
  uint64_t offset = 0;
  uint64_t tmp = 0;

  while(va1 < va1_end){
    Iterator* sa1 = reinterpret_cast<Iterator*>(allocator->translate_udva2sa(va1));
    int64_t len = blockSize;
    if((va1 + len) > va1_end){
      len = va1_end - va1;
    }
    memset(sa1, 0, len);
    for(int64_t j = 0; j < len/sizeof(Iterator); j++){
      sa1[j].begin = g_v_bin_global_va + offset;
      tmp++;
      offset = std::min(tmp * num_pairs_per_part, num_split_verts);
      sa1[j].end = g_v_bin_global_va + offset;
      // sa1[j].begin = g_v_bin_global_va + offset;
      // offset = offset + 1;
      // sa1[j].end = g_v_bin_global_va +  num_split_verts;
    }
    va1 = va1 + len;
  }
#endif
  #if not defined GEM5_MODE
  gettimeofday(&end1,NULL);
  time = (end1.tv_sec-start1.tv_sec) + (end1.tv_usec-start1.tv_usec) / 1000000.0;
  printf("Initialize partitions_global time:%lf s\n", time); fflush(stdout);
  #endif

  /*---------------------------- Start UpDown ----------------------------*/
  printf("Finish DRAM loading, start running PR.\n");
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
  /* operands
    X8: Pointer to partitions (64-bit DRAM address)
    X9: Number of lanes
    X10: Number of partitions per lane
    X11: Pointer to inKVSet (64-bit DRAM address)
    X12: Input KVSet length
    X13: Pointer to outKVSet (64-bit DRAM address)
    X14: Output KVSet length
    X15: Top flag offset in the scratchpad (in Bytes)
  */
  UpDown::operands_t ops(7);
  ops.set_operand(0, (uint64_t) partitions_global_va);
  ops.set_operand(1, (uint64_t) PART_PARM);
  ops.set_operand(2, (uint64_t) num_lanes);
  ops.set_operand(3, (uint64_t) g_v_bin_global_va);
  ops.set_operand(4, (uint64_t) num_split_verts);
  ops.set_operand(5, (uint64_t) g_v_val_global_va);
  ops.set_operand(6, (uint64_t) num_split_verts);

  UpDown::networkid_t nwid(0, false, 0);

  UpDown::event_t evnt_ops( pr_exe::InitUpDown__init/*Event Label*/,
                            nwid,
                            UpDown::CREATE_THREAD /*Thread ID*/,
                            &ops /*Operands*/);

  // Init top flag to 0
  uint64_t val = 0;
  rt->ud2t_memcpy(&val,
                  sizeof(uint64_t),
                  nwid,
                  TOP_FLAG_OFFSET /*Offset*/);

  rt->send_event(evnt_ops);

  gettimeofday(&start, nullptr);
  rt->start_exec(nwid);

  rt->test_wait_addr(nwid, TOP_FLAG_OFFSET, 1);
  gettimeofday(&end, nullptr);
  time = (end.tv_sec-start.tv_sec) + (end.tv_usec-start.tv_usec) / 1000000.0;
  printf("PR time: %lf s\n", time);


  // printf("\n[");
  // va1 = reinterpret_cast<uint64_t>(g_v_val_global_va);
  // Value * sa1 = reinterpret_cast<Value *>(allocator->translate_udva2sa(va1));
  // for(int64_t i = 0; i < 100; i++){
  //   printf("%lg, ", sa1[i]);
  // }
  // printf("]\n");

  #if not defined GEM5_MODE
	for(int j=0; j<num_lanes; j++)
	{
		printf("UD = %d, Lane = %d\n",(j / 64) , j%64);
		rt->print_stats((j / 64) , j%64);
		#ifdef DETAIL_STATS
		rt->print_histograms(j / 64 , j%64);
		#endif
	}
  for(unsigned int node=0; node<machine.NumNodes; ++node) {
    rt->print_node_stats(node);
  }
	#endif


  #ifdef VALIDATE_RESULT
  Value* g_v_val  = reinterpret_cast<Value *>(rt->mm_malloc(g_v_val_size));
  Value* g_v_val_buffer  = reinterpret_cast<Value *>(malloc(g_v_val_size));
  /* -------------------------- Copy for global to local memory -----------------------*/
  CopyGlobal2Local(allocator, blockSize, (uint64_t)g_v_val_global_va, (uint64_t)g_v_val, g_v_val_size);
  /* ----------------------------------------------------------------------------------*/
  memcpy(reinterpret_cast<void *>(g_v_val_buffer), reinterpret_cast<void *>(g_v_val), g_v_val_size);
  printf("PR UpDown finish\n");
  fflush(stdout);
  #endif

  delete rt;
  printf("UDKVMSR PageRank program finishes!\n"); fflush(stdout);


  /* Run Top PR */
  #ifdef VALIDATE_RESULT
  gettimeofday(&start, nullptr);
  Value* g_v_val_tmp  = reinterpret_cast<Value *>(malloc(g_v_val_size));
  memset(g_v_val_tmp, 0, g_v_val_size);

  in_file_gv = fopen(filename, "rb");
  if (!in_file_gv) {
    printf("Error when openning file %s, exiting.\n", filename);
    exit(EXIT_FAILURE);
  }

  in_file_nl = fopen(filename2, "rb");
  if (!in_file_nl) {
    printf("Error when openning file %s, exiting.\n", filename2);
    exit(EXIT_FAILURE);
  }

  fseek(in_file_gv, 0, SEEK_SET);
  fseek(in_file_nl, 0, SEEK_SET);
  n = fread(&num_verts, sizeof(num_verts),1, in_file_gv);
  n = fread(&num_split_verts, sizeof(num_split_verts),1, in_file_gv);
  n = fread(&num_edges, sizeof(num_edges), 1, in_file_nl);
  n = fread(&nlist_size, sizeof(nlist_size), 1, in_file_nl);


  g_v_bin_global_va = reinterpret_cast<Vertex *>(malloc(g_v_bin_size));
  nlist_beg_global_va = reinterpret_cast<uint64_t *>(malloc(nlist_beg_size));


  /*---------------------------- Load g_v_bin ----------------------------*/
  printf("Load g_v_bin_global.\n"); fflush(stdout);
  #if not defined GEM5_MODE
  gettimeofday(&start1,NULL);
  #endif

  va1 = reinterpret_cast<uint64_t>(g_v_bin_global_va);
  va1_end = reinterpret_cast<uint64_t>(g_v_bin_global_va) + g_v_bin_size;

  while(va1 < va1_end){
    vertex_t * sa1 = reinterpret_cast<vertex_t *>(va1);
    int64_t len = blockSize;
    if((va1 + len) > va1_end){
      len = va1_end - va1;
    }
    n = fread(sa1, sizeof(vertex_t), len/sizeof(vertex_t), in_file_gv); // read in all vertices 
    for(int64_t j = 0; j < len/sizeof(vertex_t); j++){
        int64_t offset = (uint64_t)(sa1[j].neighbors);
        uint64_t *loc_nlist = nlist_beg_global_va + offset;
        sa1[j].neighbors = loc_nlist;
        sa1[j].val = 1.0;
        sa1[j].gv_bin = reinterpret_cast<uint64_t>(g_v_bin_global_va);
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
    uint64_t * sa1 = reinterpret_cast<uint64_t *>(va1);
    int64_t len = blockSize;
    if((va1 + len) > va1_end){
      len = va1_end - va1;
    }
    n = fread(sa1, sizeof(int64_t), len/sizeof(int64_t), in_file_nl); // read in all edges
    va1 = va1 + len;
  }

  fclose(in_file_nl);
  #if not defined GEM5_MODE
  gettimeofday(&end1,NULL);
  time = (end1.tv_sec-start1.tv_sec) + (end1.tv_usec-start1.tv_usec) / 1000000.0;
  printf("Loading nlist_beg_global time:%lf s\n", time); fflush(stdout);
  #endif



  printf("CPU pr start.\n"); fflush(stdout);
  pagerank_top(g_v_bin_global_va, g_v_val_tmp, num_split_verts);
  gettimeofday(&end, nullptr);
  printf("CPU pr end.\n"); fflush(stdout);
  time = (end.tv_sec-start.tv_sec) + (end.tv_usec-start.tv_usec) / 1000000.0;

  if(compare(g_v_val_buffer, g_v_val_tmp, num_split_verts)){
    printf("Validate Pass! Time: %lf s\n", time);
    fflush(stdout);
    free(g_v_val_buffer);
    g_v_val_buffer = NULL;
    free(g_v_val_tmp);
    g_v_val_tmp = NULL;
    return 0;
  }else{
    printf("Validate Failed! Time: %lf s\n", time);
    fflush(stdout);
    free(g_v_val_buffer);
    g_v_val_buffer = NULL;
    free(g_v_val_tmp);
    g_v_val_tmp = NULL;
    return 1;
  }

  #endif

  return 0;
}