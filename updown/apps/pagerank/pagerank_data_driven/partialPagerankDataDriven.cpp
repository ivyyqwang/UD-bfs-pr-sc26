
#include "../utils.hpp"
#include <algorithm>
#include <cmath>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <iterator>
#include <random>
#include <string>
#include <sys/time.h>
#include <sys/types.h>

#ifndef DRAMALLOC
#define DRAMALLOC
#include "dramalloc.hpp"
#endif

#ifdef BASIM
#include <basimupdown.h>
#endif

#define VALIDATE_RESULT
// #define DEBUG
#define PRINT_STATS
#define SHUFFLE_PARTITIONS
// #define DEBUG_GRAPH

/* If the graph is too large and couldn't fit into the simulated physical memory,
enable this flag to increase the memory by increasing the node configuration */
// #define OUT_OF_PHYSICAL_MEMORY

#ifdef VALIDATE_RESULT
#include <fstream>
#endif

#include "out/pagerank_pull_split_dd.hpp"

#define USAGE                                                                                                                                                  \
  "USAGE: ./partialPagerankDataDriven <graph_file_path> <num_nodes> (<num_top_iteration> <num_updown_iteration>)\n\
  graph_file_path: \tpath to the graph file (prefix without _gv.bin or _nl.bin).\n\
  num_nodes: \tnumber of nodes, minimum is 1.\n\
  num_top_iteration: \tnumber of top iterations to perform.\n\
  num_updown_iteration: \tnumber of updown iterations to perform.\n"

#define NUM_LANE_PER_UD 64
#define NUM_UD_PER_CLUSTER 4
#define NUM_CLUSTER_PER_NODE 8
#define TOP_FLAG_OFFSET 0

#define NUM_PR_ITERATIONS 5
#define NUM_TOP_ITERATIONS 10
#define VOLUME_SIZE_OFFSET (1152)

#define ALPHA 0.85

typedef struct Vertex {
  uint64_t deg;
  uint64_t id;
  uint64_t *neigh;
  uint64_t orig_vid;
  uint64_t split_start;
  uint64_t split_bound;
  double val;
  uint64_t active_flag;
} vertex_t;

struct Iterator {
  Vertex *begin;
  Vertex *end;
};

void pagerank_top(Vertex *g_v_in, Vertex *g_v_out, uint64_t num_vertices, uint64_t num_split_vertices, uint64_t num_itera, double eps) {
  for (uint64_t i = 0; i < num_itera; i++) {
    uint64_t vid = 0;
    uint64_t deg, uid;
    double old_val, new_val;
    uint64_t *edge_list;
    for (vid = 0; vid < num_vertices; vid++) {
      deg = g_v_in[vid].deg;
      old_val = g_v_in[vid].val * deg;
      new_val = 0.0;

      if (deg == 0) {
        continue;
      }
      // flag == 0, skip
      if (g_v_in[vid].active_flag == 0) {
        g_v_out[vid].val = g_v_in[vid].val * deg;
        continue;
      }

      // root split vertices.
      if ((g_v_in[vid].split_start != g_v_in[vid].split_bound) && (g_v_in[vid].id == g_v_in[vid].orig_vid)) {
        for (uid = g_v_in[vid].split_start; uid < g_v_in[vid].split_bound; uid++) {
          Vertex *split_v = &g_v_out[uid];
          uint64_t split_v_deg = split_v->deg;
          for (uint64_t idx = 0; idx < split_v_deg; idx++) {
            uint64_t tmp_vid = split_v->neigh[idx];
            double tmp_val = g_v_in[tmp_vid].val;
            new_val += tmp_val;
          }
        }
        new_val = new_val * ALPHA + (1 - ALPHA) / num_vertices;

        double diff = std::abs(new_val - old_val);
        bool significant = (diff > eps);
        g_v_out[vid].val = new_val;
#ifdef DEBUG
        printf("[TOP] Vertex %lu update in iteration %lu, new value = %le, old value = %le, diff = %le, eps = %le, significant = %d\n", vid, i, new_val,
               old_val, diff, eps, significant);
#endif

        if (!significant) {
          g_v_out[vid].val = old_val;
          continue;
        }
        g_v_out[vid].val = new_val;
        for (uid = g_v_in[vid].split_start; uid < g_v_in[vid].split_bound; uid++) {
          Vertex *split_v = &g_v_out[uid];
          uint64_t split_v_deg = split_v->deg;
          for (uint64_t idx = 0; idx < split_v_deg; idx++) {
            uint64_t tmp_vid = split_v->neigh[idx];
            g_v_out[tmp_vid].active_flag = 1;
#ifdef DEBUG
            printf("[TOP] Update neighbor vid=%lu active flag to 1 for vertex %lu (sibling vertex %lu)\n", tmp_vid, vid, uid);
#endif
          }
        }

      } else {
        for (uint64_t idx = 0; idx < deg; idx++) {
          uint64_t tmp_vid = g_v_out[vid].neigh[idx];
          double tmp_val = g_v_in[tmp_vid].val;
          new_val += tmp_val;
        }
        new_val = new_val * ALPHA + (1 - ALPHA) / num_vertices;

        double diff = std::abs(new_val - old_val);
        bool significant = (diff > eps);
        g_v_out[vid].val = new_val;
#ifdef DEBUG
        printf("[TOP] Vertex %lu update in iteration %lu, new value = %le, old value = %le, diff = %le, eps = %le, significant = %d\n", vid, i, new_val,
               old_val, diff, eps, significant);
#endif

        if (!significant) {
          g_v_out[vid].val = old_val;
          continue;
        }
        g_v_out[vid].val = new_val;
        for (uint64_t idx = 0; idx < deg; idx++) {
          uint64_t tmp_vid = g_v_out[vid].neigh[idx];
          g_v_out[tmp_vid].active_flag = 1;
#ifdef DEBUG
          printf("[TOP] Update neighbor vid=%lu active flag to 1 for vertex %lu\n", tmp_vid, vid);
#endif
        }
      }
    }

    uint64_t active_count = 0;
    // Swap the input and output graph value
    for (uint64_t vid = 0; vid < num_split_vertices; vid++) {
      if (g_v_in[vid].orig_vid != g_v_in[vid].id) {
        // If the vertex is a split vertex, use the original vertex's value and active flag
        g_v_in[vid].val = g_v_in[g_v_in[vid].orig_vid].val;
        g_v_in[vid].active_flag = g_v_in[g_v_in[vid].orig_vid].active_flag;
      } else {
        // For non-split vertex, compute the weighted pagerank value
        g_v_in[vid].val = g_v_out[vid].val / g_v_in[vid].deg;
        g_v_in[vid].active_flag = g_v_out[vid].active_flag;
        if (g_v_in[vid].active_flag == 1) {
          active_count = active_count + 1;
        }
      }
      uint64_t u;
      std::memcpy(&u, &g_v_in[vid].val, sizeof(float));
#ifdef DEBUG
      printf("[TOP] After iteration %lu, Vertex %lu val = %le (%lu), active_flag = %lu\n", i, vid, g_v_in[vid].val, u, g_v_in[vid].active_flag);
#endif
      // Clear up the value and flag for the next iteration
      g_v_out[vid].val = 0.0;
      g_v_out[vid].active_flag = 0;
    }
    printf("Iteration %ld: Number of vertices activated for next iteration (active set size) = %lu\n", i, active_count);
    if (active_count == 0) {
      printf("Early terminate at iteration %lu as active set size is 0.\n", i);
      break;
    }
  }
}

bool compare(vertex_t *val_array0, vertex_t *val_array1, uint64_t num_vertices) {
  bool return_value = true;
  for (uint64_t i = 0; i < num_vertices; i++) {
    if (val_array0[i].deg == 0 && val_array1[i].deg == 0) {
      continue;
    }
    if (!(almostEqual(val_array0[i].val, val_array1[i].val) && val_array0[i].active_flag == val_array1[i].active_flag)) {
      printf("Vertex %lu not match, %le != %le\n", i, val_array0[i].val, val_array1[i].val);
      printf("\tUpdown: vid=%lu, deg = %lu, orig_vid=%lu, split_start=%lu, split_bound=%lu, new_value=%le, flag = %lu\n", val_array0[i].id, val_array0[i].deg,
             val_array0[i].orig_vid, val_array0[i].split_start, val_array0[i].split_bound, val_array0[i].val, val_array0[i].active_flag);
      printf("\tTop: vid=%lu, deg = %lu, orig_vid=%lu, split_start=%lu, split_bound=%lu, new_value=%le, flag = %lu\n", val_array1[i].id, val_array1[i].deg,
             val_array1[i].orig_vid, val_array1[i].split_start, val_array1[i].split_bound, val_array1[i].val, val_array1[i].active_flag);
      return_value = false;
      // return return_value;
    }
  }
  return return_value;
}

int main(int argc, char *argv[]) {
  timeval start, end;
  timeval start1, end1;
  double time;
  uint64_t blockSize = 1UL * 32 * 1024; // 32KB

  gettimeofday(&start, NULL);

  /*---------------------------- Input Parameter ----------------------------*/

  if (argc < 3) {
    printf("Insufficient Input Params\n");
    printf("%s\n", USAGE);
    exit(1);
  }

  std::string file_prefix(argv[1]);
  uint64_t num_nodes = atoi(argv[2]);
  uint64_t num_uds_per_node = NUM_UD_PER_CLUSTER * NUM_CLUSTER_PER_NODE;
  uint64_t num_lanes_per_ud = NUM_LANE_PER_UD;
  uint64_t num_top_iter = argc >= 4 ? atoi(argv[3]) : NUM_TOP_ITERATIONS;
  uint64_t num_updown_iter = argc >= 5 ? atoi(argv[4]) : NUM_PR_ITERATIONS;
  int PART_PARM = 3;

  char *graph_file = strdup(file_prefix.c_str());
  char *path = strtok(graph_file, "/");
  while (path != NULL) {
    graph_file = path;
    path = strtok(NULL, "/");
  }
  graph_file = strtok(graph_file, ".");

#ifdef OUT_OF_PHYSICAL_MEMORY
  uint64_t num_machine_nodes = num_nodes * 2;
#else
  uint64_t num_machine_nodes = num_nodes;
#endif

  printf("Test configurations: \n\tnum_nodes = %ld, \n\tnum_uds_per_node = %ld, \n\tnum_lanes_per_ud = %ld, ", num_nodes, num_uds_per_node, num_lanes_per_ud);
  fflush(stdout);
  uint64_t num_lanes = num_nodes * num_uds_per_node * num_lanes_per_ud;

  if (!is_power_of_2(num_lanes)) {
    printf("The number of lanes to be a power of 2!!!\n");
    exit(1);
  }
  printf("Num Lanes:%ld\n", num_lanes);
  fflush(stdout);

  /*---------------------------- read input files ----------------------------*/
  printf("File prefix:%s , ", file_prefix.c_str());
  FILE *in_file_gv = fopen((file_prefix + "_gv.bin").c_str(), "rb");
  if (!in_file_gv) {
    printf("Error when openning file, exiting.\n");
    exit(EXIT_FAILURE);
  }
  FILE *in_file_nl = fopen((file_prefix + "_nl.bin").c_str(), "rb");
  if (!in_file_nl) {
    printf("Error when openning file, exiting.\n");
    exit(EXIT_FAILURE);
  }
  FILE *in_file_orig_nl = fopen((file_prefix + "_orig_nl.bin").c_str(), "rb");
  if (!in_file_nl) {
    printf("Error when openning file, exiting.\n");
    exit(EXIT_FAILURE);
  }

  uint64_t num_verts, num_split_verts, num_edges, nlist_size;
  fseek(in_file_gv, 0, SEEK_SET);
  fseek(in_file_nl, 0, SEEK_SET);
  fseek(in_file_orig_nl, 0, SEEK_SET);

  if (fread(&num_verts, sizeof(num_verts), 1, in_file_gv) != 1) {
    fprintf(stderr, "Error reading num_verts from %s\n", file_prefix.c_str());
    exit(EXIT_FAILURE);
  }
  if (fread(&num_split_verts, sizeof(num_split_verts), 1, in_file_gv) != 1) {
    fprintf(stderr, "Error reading num_split_verts from %s\n", file_prefix.c_str());
    exit(EXIT_FAILURE);
  }
  if (fread(&num_edges, sizeof(num_edges), 1, in_file_nl) != 1) {
    fprintf(stderr, "Error reading num_edges from %s\n", file_prefix.c_str());
    exit(EXIT_FAILURE);
  }
  if (fread(&nlist_size, sizeof(nlist_size), 1, in_file_nl) != 1) {
    fprintf(stderr, "Error reading nlist_size from %s\n", file_prefix.c_str());
    exit(EXIT_FAILURE);
  }
  if (fread(&num_edges, sizeof(num_edges), 1, in_file_orig_nl) != 1) {
    fprintf(stderr, "Error reading num_edges from %s\n", file_prefix.c_str());
    exit(EXIT_FAILURE);
  }
  if (fread(&nlist_size, sizeof(nlist_size), 1, in_file_orig_nl) != 1) {
    fprintf(stderr, "Error reading nlist_size from %s\n", file_prefix.c_str());
    exit(EXIT_FAILURE);
  }
  printf("num_verts = %lu, num_split_verts = %lu\n", num_verts, num_split_verts);
  printf("num_edges = %lu, nlist_size = %lu\n\n", num_edges, nlist_size);
  fflush(stdout);

  double val = (1.0 - ALPHA) / num_verts;

  double epsilon = 1.0 / num_verts;
  printf("Initial PR value = %lf, Epsilon = %lf\n", val, epsilon);

  /*---------------------------- compute memory size ----------------------------*/
  uint64_t g_v_bin_size = num_split_verts * sizeof(vertex_t);
  uint64_t nlist_beg_size = nlist_size * sizeof(uint64_t);
  uint64_t num_partitions = num_lanes * PART_PARM;
  uint64_t num_pairs_per_part = ceil((num_split_verts + 0.0) / num_partitions);
  uint64_t partitions_size = (num_partitions) * sizeof(Iterator);

  uint64_t localDRAMRequirement = blockSize;
  uint64_t globalDRAMRequirement = g_v_bin_size * 2 + nlist_beg_size * 2 + partitions_size * 2;
#ifdef VALIDATE_RESULT
  localDRAMRequirement = g_v_bin_size + blockSize;
  printf("\tPrivate DRAM: g_v_bin_size: %lu\n\tSum: %lu\n", g_v_bin_size, localDRAMRequirement);
  printf("\tGlobal DRAM: g_v_bin_size: %lu\n\tnlist_beg_size: %lu\n\tpartitions_size: %lu\n\tSum: %lu\n", g_v_bin_size, nlist_beg_size, partitions_size,
         globalDRAMRequirement);
#else
  printf("sizeof(vertex_t): %lu\n", sizeof(vertex_t));
  printf("Allocation info: \tPrivate DRAM: blockSize: %lu\n\tSum: %lu\n", blockSize, localDRAMRequirement);
  printf("\tGlobal DRAM: g_v_bin_size: %lu\n\tnlist_beg_size: %lu\n\tpartitions_size: %lu\n\tSum: %lu\n", g_v_bin_size, nlist_beg_size, partitions_size,
         globalDRAMRequirement);
#endif

  localDRAMRequirement = next_power_of_2_or_same(localDRAMRequirement);
  globalDRAMRequirement = next_power_of_2_or_same(globalDRAMRequirement);
  printf("Local DRAM Size: %lu, Global DRAM Size: %lu\n", localDRAMRequirement, globalDRAMRequirement);
  fflush(stdout);

  /*---------------------------- UpDown Machine Configuration ----------------------------*/
  // Set up machine parameters
  UpDown::ud_machine_t machine;

  /* A smaller memory configuration for testing */
  if (num_lanes <= 2048) {
    machine.MapMemSize = globalDRAMRequirement;
    machine.GMapMemSize = 1UL << 30; // 1GB
  } else {
    machine.MapMemSize = localDRAMRequirement;
    machine.GMapMemSize = globalDRAMRequirement;
  }

  machine.LocalMemAddrMode = 1;
  machine.NumLanes = num_lanes > 64 ? 64 : num_lanes;
  machine.NumUDs = std::ceil(num_lanes / 64.0) > 4 ? 4 : std::ceil(num_lanes / 64.0);
  machine.NumStacks = std::ceil(num_lanes / (64.0 * 4)) > 8 ? 8 : std::ceil(num_lanes / (64.0 * 4));
  machine.NumNodes = num_machine_nodes;

  printf("Machine Local DRAM Size: %lu, Global DRAM Size: %lu\n", machine.MapMemSize, machine.GMapMemSize);
  fflush(stdout);
  printf("Current memory consumption: %lu KB\n", getMemoryUsageKB());
  fflush(stdout);

  UpDown::BASimUDRuntime_t *rt = new UpDown::BASimUDRuntime_t(machine, "pagerank_pull_split_dd.bin", 0, 100,
                                                              std::string(graph_file) + "_" + argv[2] + "nds_" + std::to_string(num_top_iter) + "top_" +
                                                                  std::to_string(num_updown_iter) + "ud_" + std::to_string(PART_PARM) + "part");

#ifdef DEBUG
  printf("=== Base Addresses ===\n");
  rt->dumpBaseAddrs();
  printf("\n=== Machine Config ===\n");
  rt->dumpMachineConfig();
#endif

  gettimeofday(&start, nullptr);

  Vertex *g_v_bin_local_va0 = reinterpret_cast<Vertex *>(malloc(g_v_bin_size));
  Vertex *g_v_bin_local_va1 = reinterpret_cast<Vertex *>(malloc(g_v_bin_size));
  uint64_t *nlist_beg_local_va = reinterpret_cast<uint64_t *>(malloc(nlist_beg_size));
  uint64_t *orig_nlist_beg_local_va = reinterpret_cast<uint64_t *>(malloc(nlist_beg_size));

  /*---------------------------- Load g_v_bin ----------------------------*/
  printf("Load g_v_bin_local.\n");
  fflush(stdout);

  gettimeofday(&start1, NULL);

  uint64_t va0 = reinterpret_cast<uint64_t>(g_v_bin_local_va0);
  uint64_t va0_end = reinterpret_cast<uint64_t>(g_v_bin_local_va0) + g_v_bin_size;

  uint64_t va1 = reinterpret_cast<uint64_t>(g_v_bin_local_va1);
  uint64_t va1_end = reinterpret_cast<uint64_t>(g_v_bin_local_va1) + g_v_bin_size;

  while (va1 < va1_end) {
    vertex_t *sa0 = reinterpret_cast<vertex_t *>((va0));
    vertex_t *sa1 = reinterpret_cast<vertex_t *>((va1));
    int64_t len = blockSize;
    if ((va1 + len) > va1_end) {
      len = va1_end - va1;
    }
    size_t to_read = len / sizeof(vertex_t);
    if (fread(sa1, sizeof(vertex_t), to_read, in_file_gv) != to_read) {
      fprintf(stderr, "Error reading neighbor list from %s_gv.bin\n", file_prefix.c_str());
      exit(EXIT_FAILURE);
    }
    memcpy(sa0, sa1, len);
    for (int64_t j = 0; j < len / sizeof(vertex_t); j++) {
      int64_t offset = (uint64_t)(sa1[j].neigh);
      uint64_t *loc_nlist = orig_nlist_beg_local_va + offset;
      sa1[j].neigh = loc_nlist;
      sa1[j].val = 0.0;
      sa1[j].active_flag = 0;
      // printf("gv_bin1: vid = %lu, addr = %p, neighbors = %p, deg = %lu, orig_vid = %lu, split_start_vid = %lu, split_end_vid = %lu\n", sa1[j].id,
      // g_v_bin_local_va1 + sa1[j].id, sa1[j].neigh, sa1[j].deg, sa1[j].orig_vid, sa1[j].split_start, sa1[j].split_bound);
    }
    for (int64_t j = 0; j < len / sizeof(vertex_t); j++) {
      int64_t offset = (uint64_t)(sa0[j].neigh);
      uint64_t *loc_nlist = nlist_beg_local_va + offset;
      sa0[j].neigh = loc_nlist;
      sa0[j].val = val;
      sa0[j].active_flag = 1;
      // printf("gv_bin0: vid = %lu, addr = %p, neighbors = %p, deg = %lu, orig_vid = %lu, split_start_vid = %lu, split_end_vid = %lu\n", sa0[j].id,
      // g_v_bin_local_va0 + sa0[j].id, sa0[j].neigh, sa0[j].deg, sa0[j].orig_vid, sa0[j].split_start, sa0[j].split_bound);
    }
    va1 = va1 + len;
    va0 = va0 + len;
  }

  for (uint64_t idx = num_verts; idx < num_split_verts; idx++) {
    vertex_t *sa = g_v_bin_local_va0 + idx;
    uint64_t orig_vid = sa->orig_vid;
    vertex_t *orig_v_sa0 = g_v_bin_local_va0 + orig_vid;
    vertex_t *orig_v_sa1 = g_v_bin_local_va1 + orig_vid;
    orig_v_sa0->deg += sa->deg;
    orig_v_sa0->id = orig_vid;

    orig_v_sa1->deg += sa->deg;
    orig_v_sa1->id = orig_vid;
    orig_v_sa1->active_flag = 0;
  }
  for (uint64_t idx = 0; idx < num_verts; idx++) {
    vertex_t *sa0 = g_v_bin_local_va0 + idx;
    sa0->val = val / sa0->deg;
    sa0->active_flag = 1;
    for (uint64_t sibling = sa0->split_start; sibling < sa0->split_bound; sibling++) {
      vertex_t *sibling_sa0 = g_v_bin_local_va0 + sibling;
      sibling_sa0->val = sa0->val;
      sibling_sa0->active_flag = 1;
    }
    vertex_t *sa1 = g_v_bin_local_va1 + idx;
    sa1->val = 0.0;
    sa1->active_flag = 0;
  }
  fclose(in_file_gv);

  gettimeofday(&end1, NULL);
  time = (end1.tv_sec - start1.tv_sec) + (end1.tv_usec - start1.tv_usec) / 1000000.0;
  printf("Loading g_v_bin_local time:%lf s\n", time);
  fflush(stdout);

  /*---------------------------- Load nlist_bin ----------------------------*/
  printf("Load nlist_beg_local.\n");
  fflush(stdout);

  gettimeofday(&start1, NULL);

  va1 = reinterpret_cast<uint64_t>(nlist_beg_local_va);
  va1_end = reinterpret_cast<uint64_t>(nlist_beg_local_va) + nlist_beg_size;

  while (va1 < va1_end) {
    uint64_t *sa1 = reinterpret_cast<uint64_t *>((va1));
    int64_t len = blockSize;
    if ((va1 + len) > va1_end) {
      len = va1_end - va1;
    }
    size_t to_read = len / sizeof(int64_t);
    if (fread(sa1, sizeof(int64_t), to_read, in_file_nl) != to_read) {
      fprintf(stderr, "Error reading neighbor list from %s_nl.bin\n", file_prefix.c_str());
      exit(EXIT_FAILURE);
    }
    va1 = va1 + len;
  }

  va1 = reinterpret_cast<uint64_t>(orig_nlist_beg_local_va);
  va1_end = reinterpret_cast<uint64_t>(orig_nlist_beg_local_va) + nlist_beg_size;

  while (va1 < va1_end) {
    uint64_t *sa1 = reinterpret_cast<uint64_t *>((va1));
    int64_t len = blockSize;
    if ((va1 + len) > va1_end) {
      len = va1_end - va1;
    }
    size_t to_read = len / sizeof(int64_t);
    if (fread(sa1, sizeof(int64_t), to_read, in_file_orig_nl) != to_read) {
      fprintf(stderr, "Error reading neighbor list from %s_orig_nl.bin\n", file_prefix.c_str());
      exit(EXIT_FAILURE);
    }
    va1 = va1 + len;
  }

  fclose(in_file_nl);

  gettimeofday(&end1, NULL);
  time = (end1.tv_sec - start1.tv_sec) + (end1.tv_usec - start1.tv_usec) / 1000000.0;
  printf("Loading nlist_beg_local time:%lf s\n", time);
  fflush(stdout);

  printf("CPU pr start.\n");
  fflush(stdout);
  pagerank_top(g_v_bin_local_va0, g_v_bin_local_va1, num_verts, num_split_verts, num_top_iter, epsilon);
  gettimeofday(&end, nullptr);
  printf("CPU pr end, run for %ld iterations.\n", num_top_iter);
  fflush(stdout);
  time = (end.tv_sec - start.tv_sec) + (end.tv_usec - start.tv_usec) / 1000000.0;

  /*---------------------------- Initialize DramAllocator ----------------------------*/
  printf("Initialize DRAMalloc\n");

  dramalloc::DramAllocator *allocator = new dramalloc::DramAllocator(rt, pagerank_pull_split_dd::DRAMalloc__global_broadcast /*eventlabel*/);
  printf("Finish initialize DRAMalloc\n");

  if ((blockSize % sizeof(Vertex)) != 0) {
    fprintf(stderr, "blockSize must be an integer multiple of sizeof(Vertex)!\n");
    return 1;
  }

  Vertex *g_v_bin_global_va0 = reinterpret_cast<Vertex *>(allocator->mm_malloc_global(g_v_bin_size, blockSize, num_machine_nodes, 0));
  printf("Allocate g_v_bin_global_va0 addr: %p\n", g_v_bin_global_va0);
  Vertex *g_v_bin_global_va1 = reinterpret_cast<Vertex *>(allocator->mm_malloc_global(g_v_bin_size, blockSize, num_machine_nodes, 0));
  printf("Allocate g_v_bin_global_va1 addr: %p\n", g_v_bin_global_va1);
  uint64_t *nlist_beg_global_va = reinterpret_cast<uint64_t *>(allocator->mm_malloc_global(nlist_beg_size, blockSize, num_machine_nodes, 0));
  printf("Allocate nlist_beg_global_va addr: %p\n", nlist_beg_global_va);
  uint64_t *orig_nlist_beg_global_va = reinterpret_cast<uint64_t *>(allocator->mm_malloc_global(nlist_beg_size, blockSize, num_machine_nodes, 0));
  printf("Allocate orig_nlist_beg_global_va addr: %p\n", orig_nlist_beg_global_va);
  Iterator *partitions_global_va0 = reinterpret_cast<Iterator *>(allocator->mm_malloc_global(partitions_size, blockSize, num_machine_nodes, 0));
  printf("Allocate partitions_global_va0 addr: %p\n", partitions_global_va0);
  Iterator *partitions_global_va1 = reinterpret_cast<Iterator *>(allocator->mm_malloc_global(partitions_size, blockSize, num_machine_nodes, 0));
  printf("Allocate partitions_global_va1 addr: %p\n", partitions_global_va1);

  /*---------------------------- Copy data to global DRAM ----------------------------*/
  printf("Copy data to global DRAM.\n");
  gettimeofday(&start1, NULL);

  CopyLocal2Global(allocator, blockSize, (uint64_t)g_v_bin_global_va0, (uint64_t)g_v_bin_local_va0, g_v_bin_size);
  CopyLocal2Global(allocator, blockSize, (uint64_t)g_v_bin_global_va1, (uint64_t)g_v_bin_local_va1, g_v_bin_size);
  CopyLocal2Global(allocator, blockSize, (uint64_t)nlist_beg_global_va, (uint64_t)nlist_beg_local_va, nlist_beg_size);
  CopyLocal2Global(allocator, blockSize, (uint64_t)orig_nlist_beg_global_va, (uint64_t)orig_nlist_beg_local_va, nlist_beg_size);
  gettimeofday(&end1, NULL);
  time = (end1.tv_sec - start1.tv_sec) + (end1.tv_usec - start1.tv_usec) / 1000000.0;
  printf("Copy data to global DRAM time:%lf s\n", time);
  fflush(stdout);

  /*---------------------------- Free local memory ----------------------------*/
  printf("Free local memory.\n");
  fflush(stdout);
  free(nlist_beg_local_va);
  free(orig_nlist_beg_local_va);
  free(g_v_bin_local_va1);

  /*---------------------------- Reset the neighbor list pointer to global memory ----------------------------*/
  printf("Reset the neighbor list pointer to global memory.\n");

  for (uint64_t vid = 0; vid < num_split_verts; vid++) {
    Vertex *sa0 = reinterpret_cast<Vertex *>(allocator->translate_udva2sa(reinterpret_cast<uint64_t>(g_v_bin_global_va0) + vid * sizeof(Vertex)));
    sa0->neigh = reinterpret_cast<uint64_t *>(reinterpret_cast<uint64_t>(nlist_beg_global_va) +
                                              (reinterpret_cast<uint64_t>(sa0->neigh) - reinterpret_cast<uint64_t>(nlist_beg_local_va)));

    Vertex *sa1 = reinterpret_cast<Vertex *>(allocator->translate_udva2sa(reinterpret_cast<uint64_t>(g_v_bin_global_va1) + vid * sizeof(Vertex)));
    sa1->neigh = reinterpret_cast<uint64_t *>(reinterpret_cast<uint64_t>(orig_nlist_beg_global_va) +
                                              (reinterpret_cast<uint64_t>(sa1->neigh) - reinterpret_cast<uint64_t>(orig_nlist_beg_local_va)));
  }

  /*---------------------------- Initialize partitions_global0 ----------------------------*/
  printf("Initialize partitions_global0.\n");
  fflush(stdout);
  Iterator *partitions_local_va0 = reinterpret_cast<Iterator *>(malloc(partitions_size));

  Iterator *partitions_local_va1 = reinterpret_cast<Iterator *>(malloc(partitions_size));

  std::mt19937 g(42); // fixed seed for reproducibility

  gettimeofday(&start1, NULL);

  // va1 = reinterpret_cast<uint64_t>(partitions_global_va0);
  // va1_end = reinterpret_cast<uint64_t>(partitions_global_va0) + partitions_size;
  // uint64_t tmp = 0;
  uint64_t offset = 0;

  for (int i = 0; i < num_partitions; i++) {
    partitions_local_va0[i].begin = g_v_bin_global_va0 + offset;
    offset = std::min((i + 1) * num_pairs_per_part, num_split_verts);
    partitions_local_va0[i].end = g_v_bin_global_va0 + offset;
  }

#ifdef SHUFFLE_PARTITIONS
  // shuffle partitions to avoid bank conflict
  printf("Shuffle the partition array");
  std::shuffle(partitions_local_va0, partitions_local_va0 + num_partitions, g);

#ifdef DEBUG
  printf("After shuffling partitions_local_va0:\n");
  for (int i = 0; i < num_partitions; i++) {
    printf("Partition 1 idx=%d: begin = %p, end = %p\n", i, partitions_local_va0[i].begin, partitions_local_va0[i].end);
  }
#endif
#endif

  CopyLocal2Global(allocator, blockSize, (uint64_t)partitions_global_va0, (uint64_t)partitions_local_va0, partitions_size);

  gettimeofday(&end1, NULL);
  time = (end1.tv_sec - start1.tv_sec) + (end1.tv_usec - start1.tv_usec) / 1000000.0;
  printf("Initialize partitions_global0 time:%lf s\n", time);
  fflush(stdout);

  free(partitions_local_va0);

  /*---------------------------- Initialize partitions_global1 ----------------------------*/
  printf("Initialize partitions_global1.\n");
  fflush(stdout);

  gettimeofday(&start1, NULL);

  offset = 0;
  num_pairs_per_part = ceil((num_verts + 0.0) / num_partitions);

  for (int i = 0; i < num_partitions; i++) {
    partitions_local_va1[i].begin = g_v_bin_global_va1 + offset;
    offset = std::min((i + 1) * num_pairs_per_part, num_verts);
    partitions_local_va1[i].end = g_v_bin_global_va1 + offset;
  }

#ifdef SHUFFLE_PARTITIONS
  // shuffle partitions to avoid bank conflict
  std::shuffle(partitions_local_va1, partitions_local_va1 + num_partitions, g);

#ifdef DEBUG
  printf("After shuffling partitions_local_va0:\n");
  for (int i = 0; i < num_partitions; i++) {
    printf("Patition 2 idx=%d: begin = %p, end = %p\n", i, partitions_local_va1[i].begin, partitions_local_va1[i].end);
  }
#endif
#endif

  CopyLocal2Global(allocator, blockSize, (uint64_t)partitions_global_va1, (uint64_t)partitions_local_va1, partitions_size);

  gettimeofday(&end1, NULL);
  time = (end1.tv_sec - start1.tv_sec) + (end1.tv_usec - start1.tv_usec) / 1000000.0;
  printf("Initialize partitions_global1 time:%lf s\n", time);
  fflush(stdout);
  free(partitions_local_va1);

  /*---------------------------- Start UpDown ----------------------------*/
  printf("Finish DRAM loading, start running PR.\n");
  fflush(stdout);

  uint64_t iter = 0;
  double alpha = ALPHA;
  rt->reset_all_stats();

  while (iter < num_updown_iter) {
    printf("PageRank iteration %ld\n", iter);
    fflush(stdout);
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
    UpDown::operands_t ops(8);
    ops.set_operand(0, (uint64_t)partitions_global_va0);
    ops.set_operand(1, (uint64_t)num_verts);
    ops.set_operand(2, (uint64_t)num_lanes);
    ops.set_operand(3, (uint64_t)g_v_bin_global_va0);
    ops.set_operand(4, (uint64_t)num_split_verts);
    ops.set_operand(5, (uint64_t)g_v_bin_global_va1);
    ops.set_operand(6, (double)epsilon);
    ops.set_operand(7, (double)(alpha));
    UpDown::networkid_t nwid(0, false, 0);

    UpDown::event_t evnt_ops(pagerank_pull_split_dd::InitUpDown__init /*Event Label*/, nwid, UpDown::CREATE_THREAD /*Thread ID*/, &ops /*Operands*/);

    // Init top flag to 0
    uint64_t val = 0;
    rt->ud2t_memcpy(&val, sizeof(uint64_t), nwid, TOP_FLAG_OFFSET /*Offset*/);

    rt->send_event(evnt_ops);

    rt->start_exec(nwid);

    rt->test_wait_addr(nwid, TOP_FLAG_OFFSET, 1);

    // check the active set volumn
    for (uint64_t i = 0; i < num_verts; i++) {
      Vertex *temp_vertex = (Vertex *)allocator->translate_udva2sa((uint64_t)(g_v_bin_global_va0 + i));
      temp_vertex->active_flag = 0;
    }

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
    ops.set_operand(0, (uint64_t)partitions_global_va1);
    ops.set_operand(1, (uint64_t)PART_PARM);
    ops.set_operand(2, (uint64_t)num_lanes);
    ops.set_operand(3, (uint64_t)g_v_bin_global_va1);
    ops.set_operand(4, (uint64_t)num_split_verts);
    ops.set_operand(5, (uint64_t)g_v_bin_global_va0);
    ops.set_operand(6, (double)epsilon);
    ops.set_operand(7, (uint64_t)num_verts);

    UpDown::event_t merge_evnt_ops(pagerank_pull_split_dd::InitMerge__init /*Event Label*/, nwid, UpDown::CREATE_THREAD /*Thread ID*/, &ops /*Operands*/);

    // Init top flag to 0
    val = 0;
    rt->t2ud_memcpy(&val, sizeof(uint64_t), nwid, TOP_FLAG_OFFSET /*Offset*/);

    rt->send_event(merge_evnt_ops);

    rt->start_exec(nwid);

    rt->test_wait_addr(nwid, TOP_FLAG_OFFSET, 1);
    printf("Finish merging split vertices\n");

    printf("Finish PageRank iteration %ld\n", iter);
    fflush(stdout);

    uint64_t active_count = 0;
    for (int i = 0; i < num_verts; i++) {
      Vertex *temp_vertex_0 = (Vertex *)allocator->translate_udva2sa((uint64_t)(g_v_bin_global_va0 + i));

      if (temp_vertex_0->deg == 0)
        continue;

      if ((temp_vertex_0->active_flag & 1) == 1) {
        active_count = active_count + 1;
      }
    }

    uint64_t volume_count = 0;
    for (uint64_t i = 0; i < NUM_LANE_PER_UD * NUM_UD_PER_CLUSTER * NUM_CLUSTER_PER_NODE * num_nodes; i++) {
      rt->ud2t_memcpy(&val, sizeof(uint64_t), i, VOLUME_SIZE_OFFSET /*Offset*/);
      volume_count += val;
      // clear the counter
      val = 0;
      rt->t2ud_memcpy(&val, sizeof(uint64_t), i, VOLUME_SIZE_OFFSET /*Offset*/);
    }
    printf("Iteration %ld: Number of vertices activated for next iteration (active set size) = %lu, volume = %lu\n", iter, active_count, volume_count);

    if (active_count == 0) {
      printf("Early terminate at iteration %ld as active set size is 0.\n", iter);
      break;
    }
    iter++;

#ifdef ENABLE_SQLITE
    std::string iter_str = "iteration_" + std::to_string(iter);
    for (int j = 0; j < num_lanes; j++) {
    // dump statistics into the DB
#ifdef ENABLE_SQLITE
      rt->db_write_stats(0, num_lanes, iter_str.c_str());
#ifdef DETAIL_STATS
      rt->db_write_event_stats(0, num_lanes, iter_str.c_str());
#endif
#endif
    }
    rt->reset_all_stats();
#endif
  }

#ifdef PRINT_STATS
  for (int j = 0; j < num_lanes; j++) {
    printf("UD = %d, Lane = %d\n", (j / 64), j % 64);
    rt->print_stats((j / 64), j % 64);
#ifdef DETAIL_STATS
    rt->print_histograms(j / 64, j % 64);
#endif
  }
#endif

#ifdef VALIDATE_RESULT
  Vertex *g_v_bin = reinterpret_cast<Vertex *>(rt->mm_malloc(g_v_bin_size));
  Vertex *g_v_bin_buffer = reinterpret_cast<Vertex *>(malloc(g_v_bin_size));
  /* -------------------------- Copy for global to local memory -----------------------*/
  CopyGlobal2Local(allocator, blockSize, (uint64_t)g_v_bin_global_va0, (uint64_t)g_v_bin, g_v_bin_size);
  /* ----------------------------------------------------------------------------------*/
  memcpy(reinterpret_cast<void *>(g_v_bin_buffer), reinterpret_cast<void *>(g_v_bin), g_v_bin_size);
  printf("PR UpDown finish\n");
  fflush(stdout);
#endif

  // delete rt;
  printf("UDKVMSR PageRank program finishes.\n");

/* Run Top PR */
#ifdef VALIDATE_RESULT
  gettimeofday(&start, nullptr);

  in_file_gv = fopen((file_prefix + "_gv.bin").c_str(), "rb");
  if (!in_file_gv) {
    printf("Error when openning file %s, exiting.\n", (file_prefix + "_gv.bin").c_str());
    exit(EXIT_FAILURE);
  }

  in_file_nl = fopen((file_prefix + "_nl.bin").c_str(), "rb");
  if (!in_file_nl) {
    printf("Error when openning file %s, exiting.\n", (file_prefix + "_nl.bin").c_str());
    exit(EXIT_FAILURE);
  }

  in_file_orig_nl = fopen((file_prefix + "_orig_nl.bin").c_str(), "rb");
  if (!in_file_nl) {
    printf("Error when openning file %s, exiting.\n", (file_prefix + "_orig_nl.bin").c_str());
    exit(EXIT_FAILURE);
  }

  fseek(in_file_gv, 0, SEEK_SET);
  fseek(in_file_nl, 0, SEEK_SET);
  if (fread(&num_verts, sizeof(num_verts), 1, in_file_gv) != 1) {
    fprintf(stderr, "Error reading num_verts from %s\n", (file_prefix + "_gv.bin").c_str());
    exit(EXIT_FAILURE);
  }
  if (fread(&num_split_verts, sizeof(num_split_verts), 1, in_file_gv) != 1) {
    fprintf(stderr, "Error reading num_split_verts from %s\n", (file_prefix + "_gv.bin").c_str());
    exit(EXIT_FAILURE);
  }
  if (fread(&num_edges, sizeof(num_edges), 1, in_file_nl) != 1) {
    fprintf(stderr, "Error reading num_edges from %s\n", (file_prefix + "_nl.bin").c_str());
    exit(EXIT_FAILURE);
  }
  if (fread(&nlist_size, sizeof(nlist_size), 1, in_file_nl) != 1) {
    fprintf(stderr, "Error reading nlist_size from %s\n", (file_prefix + "_nl.bin").c_str());
    exit(EXIT_FAILURE);
  }
  if (fread(&num_edges, sizeof(num_edges), 1, in_file_orig_nl) != 1) {
    fprintf(stderr, "Error reading num_edges from %s\n", file_prefix.c_str());
    exit(EXIT_FAILURE);
  }
  if (fread(&nlist_size, sizeof(nlist_size), 1, in_file_orig_nl) != 1) {
    fprintf(stderr, "Error reading nlist_size from %s\n", file_prefix.c_str());
    exit(EXIT_FAILURE);
  }

  g_v_bin_global_va0 = reinterpret_cast<Vertex *>(malloc(g_v_bin_size));
  g_v_bin_global_va1 = reinterpret_cast<Vertex *>(malloc(g_v_bin_size));
  nlist_beg_global_va = reinterpret_cast<uint64_t *>(malloc(nlist_beg_size));
  orig_nlist_beg_global_va = reinterpret_cast<uint64_t *>(malloc(nlist_beg_size));

  /*---------------------------- Load g_v_bin ----------------------------*/
  printf("Load g_v_bin_global.\n");
  fflush(stdout);

  gettimeofday(&start1, NULL);

  va0 = reinterpret_cast<uint64_t>(g_v_bin_global_va0);
  va0_end = reinterpret_cast<uint64_t>(g_v_bin_global_va0) + g_v_bin_size;

  va1 = reinterpret_cast<uint64_t>(g_v_bin_global_va1);
  va1_end = reinterpret_cast<uint64_t>(g_v_bin_global_va1) + g_v_bin_size;

  while (va1 < va1_end) {
    vertex_t *sa0 = reinterpret_cast<vertex_t *>((va0));
    vertex_t *sa1 = reinterpret_cast<vertex_t *>((va1));
    int64_t len = blockSize;
    if ((va1 + len) > va1_end) {
      len = va1_end - va1;
    }
    size_t to_read = len / sizeof(vertex_t);
    if (fread(sa1, sizeof(vertex_t), to_read, in_file_gv) != to_read) {
      fprintf(stderr, "Error reading neighbor list from %s_gv.bin\n", file_prefix.c_str());
      exit(EXIT_FAILURE);
    }
    memcpy(sa0, sa1, len);
    for (int64_t j = 0; j < len / sizeof(vertex_t); j++) {
      int64_t offset = (uint64_t)(sa1[j].neigh);
      uint64_t *loc_nlist = orig_nlist_beg_global_va + offset;
      sa1[j].neigh = loc_nlist;
      sa1[j].val = 0.0;
      sa1[j].active_flag = 0;
      // printf("gv_bin1: vid = %lu, addr = %p, neighbors = %p, deg = %lu, orig_vid = %lu, split_start_vid = %lu, split_end_vid = %lu\n", sa1[j].id,
      // g_v_bin_global_va1 + sa1[j].id, sa1[j].neigh, sa1[j].deg, sa1[j].orig_vid, sa1[j].split_start, sa1[j].split_bound);
    }
    for (int64_t j = 0; j < len / sizeof(vertex_t); j++) {
      int64_t offset = (uint64_t)(sa0[j].neigh);
      uint64_t *loc_nlist = nlist_beg_global_va + offset;
      sa0[j].neigh = loc_nlist;
      sa0[j].val = val;
      sa0[j].active_flag = 1;
      // printf("gv_bin0: vid = %lu, addr = %p, neighbors = %p, deg = %lu, orig_vid = %lu, split_start_vid = %lu, split_end_vid = %lu\n", sa0[j].id,
      // g_v_bin_global_va0 + sa0[j].id, sa0[j].neigh, sa0[j].deg, sa0[j].orig_vid, sa0[j].split_start, sa0[j].split_bound);
    }
    va1 = va1 + len;
    va0 = va0 + len;
  }

  for (uint64_t idx = num_verts; idx < num_split_verts; idx++) {
    vertex_t *sa = g_v_bin_global_va0 + idx;
    uint64_t orig_vid = sa->orig_vid;
    vertex_t *orig_v_sa0 = g_v_bin_global_va0 + orig_vid;
    vertex_t *orig_v_sa1 = g_v_bin_global_va1 + orig_vid;
    orig_v_sa0->deg += sa->deg;
    orig_v_sa0->id = orig_vid;

    orig_v_sa1->deg += sa->deg;
    orig_v_sa1->id = orig_vid;
    orig_v_sa1->active_flag = 0;
  }
  for (uint64_t idx = 0; idx < num_verts; idx++) {
    vertex_t *sa0 = g_v_bin_global_va0 + idx;
    sa0->val = val / sa0->deg;
    sa0->active_flag = 1;
    for (uint64_t sibling = sa0->split_start; sibling < sa0->split_bound; sibling++) {
      vertex_t *sibling_sa0 = g_v_bin_global_va0 + sibling;
      sibling_sa0->val = sa0->val;
      sibling_sa0->active_flag = 1;
    }
    vertex_t *sa1 = g_v_bin_global_va1 + idx;
    sa1->val = 0.0;
    sa1->active_flag = 0;
  }
  fclose(in_file_gv);

  gettimeofday(&end1, NULL);
  time = (end1.tv_sec - start1.tv_sec) + (end1.tv_usec - start1.tv_usec) / 1000000.0;
  printf("Loading g_v_bin_global time:%lf s\n", time);
  fflush(stdout);

  /*---------------------------- Load nlist_bin ----------------------------*/
  printf("Load nlist_beg_global.\n");
  fflush(stdout);

  gettimeofday(&start1, NULL);

  va1 = reinterpret_cast<uint64_t>(nlist_beg_global_va);
  va1_end = reinterpret_cast<uint64_t>(nlist_beg_global_va) + nlist_beg_size;

  while (va1 < va1_end) {
    uint64_t *sa1 = reinterpret_cast<uint64_t *>((va1));
    int64_t len = blockSize;
    if ((va1 + len) > va1_end) {
      len = va1_end - va1;
    }
    size_t to_read = len / sizeof(int64_t);
    if (fread(sa1, sizeof(int64_t), to_read, in_file_nl) != to_read) {
      fprintf(stderr, "Error reading neighbor list from %s_nl.bin\n", file_prefix.c_str());
      exit(EXIT_FAILURE);
    }
    va1 = va1 + len;
  }

  va1 = reinterpret_cast<uint64_t>(orig_nlist_beg_global_va);
  va1_end = reinterpret_cast<uint64_t>(orig_nlist_beg_global_va) + nlist_beg_size;

  while (va1 < va1_end) {
    uint64_t *sa1 = reinterpret_cast<uint64_t *>((va1));
    int64_t len = blockSize;
    if ((va1 + len) > va1_end) {
      len = va1_end - va1;
    }
    size_t to_read = len / sizeof(int64_t);
    if (fread(sa1, sizeof(int64_t), to_read, in_file_orig_nl) != to_read) {
      fprintf(stderr, "Error reading neighbor list from %s_orig_nl.bin\n", file_prefix.c_str());
      exit(EXIT_FAILURE);
    }
    va1 = va1 + len;
  }

  fclose(in_file_nl);

  gettimeofday(&end1, NULL);
  time = (end1.tv_sec - start1.tv_sec) + (end1.tv_usec - start1.tv_usec) / 1000000.0;
  printf("Loading nlist_beg_global time:%lf s\n", time);
  fflush(stdout);

  printf("CPU pr start.\n");
  fflush(stdout);
  pagerank_top(g_v_bin_global_va0, g_v_bin_global_va1, num_verts, num_split_verts, num_updown_iter + num_top_iter, epsilon);
  gettimeofday(&end, nullptr);
  printf("CPU pr end.\n");
  fflush(stdout);
  time = (end.tv_sec - start.tv_sec) + (end.tv_usec - start.tv_usec) / 1000000.0;

  if (compare(g_v_bin_buffer, g_v_bin_global_va0, num_verts)) {
    printf("Validate Pass! Time: %lf s\n", time);
    fflush(stdout);
  } else {
    printf("Validate Failed! Time: %lf s\n", time);
    fflush(stdout);
  }

  free(g_v_bin_buffer);
  free(g_v_bin_global_va0);
  free(g_v_bin_global_va1);
  free(nlist_beg_global_va);
  free(orig_nlist_beg_global_va);
#endif

  return 0;
}