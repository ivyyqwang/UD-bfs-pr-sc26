#include "LMStaticMap.udwh"
#include "basimupdown.h"
#include "emEFA.hpp"

#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <filesystem>
#include <fstream>
#include <iostream>
#include <random>
#include <sstream>
#include <stdio.h>
#include <string>
#include <string_view>
#include <vector>

#include "em.hpp"

#define SQL_DUMP 0

#ifndef DRAM_ALLOC_BLOCKSIZE
#define DRAM_ALLOC_BLOCKSIZE (1UL << 20)
#endif

#ifndef DRAM_ALLOC_STARTNODE
#define DRAM_ALLOC_STARTNODE 0UL
#endif

bool run_BFS_push_only(Graph<UpDown::BASimUDRuntime_t> &graph,
                       UpDown::BASimUDRuntime_t *rt, uint64_t num_lanes,
                       uint64_t source) {
  for (uint64_t i = 0; i < graph.N; i++) {
    graph.vertexs[i].scratch1 = std::numeric_limits<uint64_t>::max();
    graph.vertexs[i].scratch2 = std::numeric_limits<uint64_t>::max();
    graph.vertexs[i].scratch3 = std::numeric_limits<uint64_t>::max();
    graph.vertexs[i].scratch4 = std::numeric_limits<uint64_t>::max();
  }
  return BFS_push_only_on_UpDown(graph, source, rt, num_lanes);
}

bool run_BFS_pull_only(Graph<UpDown::BASimUDRuntime_t> &graph,
                       UpDown::BASimUDRuntime_t *rt, uint64_t num_lanes,
                       uint64_t source) {
  for (uint64_t i = 0; i < graph.N; i++) {
    graph.vertexs[i].scratch1 = std::numeric_limits<uint64_t>::max();
    graph.vertexs[i].scratch2 = std::numeric_limits<uint64_t>::max();
    graph.vertexs[i].scratch3 = std::numeric_limits<uint64_t>::max();
    graph.vertexs[i].scratch4 = std::numeric_limits<uint64_t>::max();
  }
  return BFS_pull_only_on_UpDown(graph, source, rt, num_lanes);
}

bool run_BFS_push_to_pull(Graph<UpDown::BASimUDRuntime_t> &graph,
                          UpDown::BASimUDRuntime_t *rt, uint64_t num_lanes,
                          uint64_t source) {
  for (uint64_t i = 0; i < graph.N; i++) {
    graph.vertexs[i].scratch1 = std::numeric_limits<uint64_t>::max();
    graph.vertexs[i].scratch2 = std::numeric_limits<uint64_t>::max();
    graph.vertexs[i].scratch3 = std::numeric_limits<uint64_t>::max();
    graph.vertexs[i].scratch4 = std::numeric_limits<uint64_t>::max();
  }
  return BFS_push_to_pull_on_UpDown(graph, source, rt, num_lanes);
}

bool run_BFS_pull_only_multi(Graph<UpDown::BASimUDRuntime_t> &graph,
                             UpDown::BASimUDRuntime_t *rt, uint64_t num_lanes,
                             uint64_t source) {
  for (uint64_t i = 0; i < graph.N; i++) {
    graph.vertexs[i].scratch1 = std::numeric_limits<uint64_t>::max();
    graph.vertexs[i].scratch2 = std::numeric_limits<uint64_t>::max();
    graph.vertexs[i].scratch3 = std::numeric_limits<uint64_t>::max();
    graph.vertexs[i].scratch4 = std::numeric_limits<uint64_t>::max();
  }
  return BFS_pull_only_with_multi_on_UpDown(graph, source, rt, num_lanes);
}

bool run_BFS(Graph<UpDown::BASimUDRuntime_t> &graph,
             UpDown::BASimUDRuntime_t *rt, uint64_t num_lanes,
             uint64_t source) {
  for (uint64_t i = 0; i < graph.N; i++) {
    graph.vertexs[i].scratch1 = std::numeric_limits<uint64_t>::max();
    graph.vertexs[i].scratch2 = std::numeric_limits<uint64_t>::max();
    graph.vertexs[i].scratch3 = std::numeric_limits<uint64_t>::max();
    graph.vertexs[i].scratch4 = std::numeric_limits<uint64_t>::max();
  }
  return BFS_push_to_pull_multi_on_UpDown(graph, source, rt, num_lanes);
}
bool run_CC(Graph<UpDown::BASimUDRuntime_t> &graph,
            UpDown::BASimUDRuntime_t *rt, uint64_t num_lanes) {
  for (uint64_t i = 0; i < graph.N; i++) {
    graph.vertexs[i].scratch1 = i;
    graph.vertexs[i].scratch2 = std::numeric_limits<uint64_t>::max();
    graph.vertexs[i].scratch3 = std::numeric_limits<uint64_t>::max();
    graph.vertexs[i].scratch4 = std::numeric_limits<uint64_t>::max();
  }
  return CC_on_UpDown(graph, rt, num_lanes);
}

bool run_PR(Graph<UpDown::BASimUDRuntime_t> &graph,
            UpDown::BASimUDRuntime_t *rt, uint64_t num_lanes,
            unsigned long max_iters) {
  uint64_t starting_value = bit_cast<uint64_t, double>(1.0 / graph.N);
  for (uint64_t i = 0; i < graph.N; i++) {
    graph.vertexs[i].scratch1 = starting_value;
    graph.vertexs[i].scratch2 = starting_value;
    graph.vertexs[i].scratch3 = 0;
    graph.vertexs[i].scratch4 = std::numeric_limits<uint64_t>::max();
  }
  return PR_on_UpDown(graph, max_iters, 1.0 / graph.N, rt, num_lanes);
}

int main(int argc, char *argv[]) {
  //-------------Set up machine parameters
  //------------Read file name and number of lanes from input

  if (argc < 4) {
    printf("Insufficient Input Params\n");
    printf("./em <graph file> <algorithm> <number of lanes> <optional "
           "algorithm argument>\n");
    printf("current supported algorithms are BFS, CC, and PR\n");
    printf("BFS has the following variations, BFS_PUSH_ONLY, "
           "BFS_PULL_ONLY_BASIC, BFS_PUSH_PULL_BASIC, BFS_PULL_ONLY\n");
    exit(1);
  }

  std::string fname = argv[1];

  std::string algorithm = argv[2];

  uint64_t num_lanes = atoi(argv[3]);

  UpDown::ud_machine_t machine(argc, argv);
  machine.MapMemSize = 1UL << 37; // 256GB
  machine.GMapMemSize = 1UL << 37;
  machine.LocalMemAddrMode = 1;
  machine.NumLanes = num_lanes > 64 ? 64 : num_lanes;
  machine.NumUDs =
      std::ceil(num_lanes / 64.0) > 4 ? 4 : std::ceil(num_lanes / 64.0);
  machine.NumStacks = std::ceil(num_lanes / (64.0 * 4)) > 8
                          ? 8
                          : std::ceil(num_lanes / (64.0 * 4));
  machine.NumNodes = std::ceil(num_lanes / (64.0 * 4 * 8));

  // DRAM alloc config
  uint64_t blockSize = DRAM_ALLOC_BLOCKSIZE;
  uint64_t numNodes = machine.NumNodes;
  // uint64_t numNodes = 1;
  uint64_t startNode = DRAM_ALLOC_STARTNODE;

  // Create the runtime

  // Create the runtime and load the UpDown binary
  UpDown::BASimUDRuntime_t *rt =
      new UpDown::BASimUDRuntime_t(machine, "emEFA.bin", 0, 100);

  dramalloc::DramAllocator *allocator = new dramalloc::DramAllocator(
      rt, emEFA::DRAMalloc__global_broadcast /*eventlabel*/);

  Graph graph(rt, fname, allocator, blockSize, numNodes, startNode);
  std::cout << "done loading the graph: " << fname << "\n";
  // graph.print();

  bool correct = true;

  if (algorithm == "CC") {
    correct = run_CC(graph, rt, num_lanes);
  }
  if (algorithm == "BFS") {
    if (argc < 5) {
      printf("BFS requires specifying the source vertex\n");
      exit(1);
    }
    uint64_t source = atoi(argv[4]);
    correct = run_BFS(graph, rt, num_lanes, source);
  }
  if (algorithm == "BFS_PUSH_ONLY") {
    if (argc < 5) {
      printf("BFS requires specifying the source vertex\n");
      exit(1);
    }
    uint64_t source = atoi(argv[4]);
    correct = run_BFS_push_only(graph, rt, num_lanes, source);
  }
  if (algorithm == "BFS_PULL_ONLY_BASIC") {
    if (argc < 5) {
      printf("BFS requires specifying the source vertex\n");
      exit(1);
    }
    uint64_t source = atoi(argv[4]);
    correct = run_BFS_pull_only(graph, rt, num_lanes, source);
  }
  if (algorithm == "BFS_PUSH_PULL_BASIC") {
    if (argc < 5) {
      printf("BFS requires specifying the source vertex\n");
      exit(1);
    }
    uint64_t source = atoi(argv[4]);
    correct = run_BFS_push_to_pull(graph, rt, num_lanes, source);
  }
  if (algorithm == "BFS_PULL_ONLY") {
    if (argc < 5) {
      printf("BFS requires specifying the source vertex\n");
      exit(1);
    }
    uint64_t source = atoi(argv[4]);
    correct = run_BFS_pull_only_multi(graph, rt, num_lanes, source);
  }
  if (algorithm == "PR") {
    if (argc < 5) {
      printf("PR requires specifying the maximum number of iterations\n");
      exit(1);
    }
    uint64_t max_iters = atoi(argv[4]);
    correct = run_PR(graph, rt, num_lanes, max_iters);
  }

  if (!correct) {
    std::cerr << "something is wrong\n";
    return 1;
  }

#if SQL_DUMP == 1
  rt->db_write_stats(0, num_lanes, "end");
#endif

  std::string base_name = std::filesystem::path(fname).filename();
  std::string stats_fname = std::string("lane_stats_") + base_name +
                            std::string("_") + std::to_string(num_lanes) +
                            std::string(".txt");

  freopen(stats_fname.c_str(), "w", stdout);

  for (uint64_t i = 0; i < num_lanes; i++) {
    rt->print_stats(i);
  }
  for (unsigned int node = 0; node < machine.NumNodes; ++node) {
    rt->print_node_stats(node);
  }
  std::fclose(stdout);

  return 0;
}
