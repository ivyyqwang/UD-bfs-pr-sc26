#include "simupdown.h"
#include "dramalloc.hpp"
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cmath>
#include <sys/types.h>
#include <sys/time.h>
#include "three_clique_mm_exe.hpp"


#if defined GEM5_MODE
    #include "gem5/m5ops.h"
    #undef BASIM
    #undef CPU_CMP
#else
  #define CPU_CMP
#endif

#ifdef BASIM
#include <basimupdown.h>
#endif

//#define DEBUG
//#define TESTBIN
#define CPU_CMP

#define USAGE   "USAGE: ./tc_udweave <gv_bin> <nl_bin> <num_lanes> (<network_latency> <network_bandwidth>)\n"\
                "gv_bin: the binary file for vertex list\n"\
                "nl_bin: the binary file for neighbor list\n"\
                "num_lanes: number of lanes to use\n"\
                "network_latency: network latency in cycles (optional, default: 1100)\n"\
                "network_bandwidth: network bandwidth in GB/s (optional, default: 0 (unlimited))\n"

#define INTERSECT_RESULT 65520
#define TOP_FLAG 65528

typedef uint64_t* ptr;
typedef uint64_t word_t;

typedef struct vertex_local{
  uint64_t deg;
  uint64_t id;
  ptr neigh;
} vertexl_t;

typedef struct vertex{
  uint64_t deg;
  uint64_t id;
  ptr neigh;
  uint64_t min_vid; 
  uint64_t max_vid;
  uint64_t reserved0;  
  uint64_t reserved1; 
  uint64_t reserved2;
} vertex_t;

typedef vertexl_t* vertexptr;


word_t intersection(vertexptr u0, vertexptr u1, ptr u0u1){
  word_t size = 0;
  if(u0->deg == 0 || u1->deg == 0)
    return 0;
  if(!(u0->neigh[u0->deg - 1] < u1->neigh[0]) && !(u0->neigh[0] > u1->neigh[u1->deg - 1]))
  // At least some overlap
  {
      word_t pos0 = 0, pos1 = 0;
      while(pos0 != u0->deg && pos1 != u1->deg)
      {
        if(u0->neigh[pos0] < u1->neigh[pos1])
          pos0++;
        else if(u0->neigh[pos0] > u1->neigh[pos1])
          pos1++;
        else
        {
          u0u1[size++] = u0->neigh[pos0];
          pos0++;
          pos1++;
        }
      }
  }
  return size;
}


long three_clique_count_cpu(uint64_t svert, uint64_t evert, vertexl_t* g_v_bin)
{
    long count = 0;
    long i1 = 0;
    for(i1=svert; i1<evert; i1++)
    {
        long count2 = 0;
        long v1 = i1;
        uint64_t deg1 = g_v_bin[v1].deg;
        // printf("v1 = %ld, deg = %llu\n", v1, deg1);
        if (deg1 == 0)
            continue;
        int i2;
        for(i2=0; i2<deg1; i2++)
        {
            long v2 = g_v_bin[v1].neigh[i2];
            if(v2 >= v1)
                break;
            
            // printf("%d %d\n", v1, v2);

            uint64_t deg2 = g_v_bin[v2].deg;
            if (deg2 == 0)
                continue;

            
            uint64_t* list3 = reinterpret_cast<uint64_t*>(malloc(deg2 * sizeof(uint64_t)));
            // list3 = N(v1)^N(v2)
            uint64_t len3 = intersection(&g_v_bin[v1], &g_v_bin[v2], list3);

            
            int i3;
            for(i3=0; i3<len3; i3++)
            {
                long v3 = list3[i3];
                
                if(v3 >= v2)
                    break;
                // printf("%d %d %d\n", v1, v2, v3);
                count2++;

            }
            free(list3);
            list3 = NULL;
        }
        count = count + count2;
        // printf("CPU[%d] v[%ld] count num = %ld\n",gl_ud_id,v1,count2);
    }
    return count;
}


uint64_t read_and_load_nlistbin(const char* binfilename, const char* binfilename2 , vertexl_t *g_v_bin, uint64_t* nlist_beg){
  printf("Binfile:%s\n", binfilename);
  fflush(stdout);
  FILE* in_file_gv = fopen(binfilename, "rb");
  if (!in_file_gv) {
        exit(EXIT_FAILURE);
  }
  FILE* in_file_nl = fopen(binfilename2, "rb");
  if (!in_file_nl) {
        exit(EXIT_FAILURE);
  }
  uint64_t num_nodes, nlist_size = 0;

  fseek(in_file_gv, 0, SEEK_SET);
  fseek(in_file_nl, 0, SEEK_SET);
  fread(&num_nodes, sizeof(num_nodes),1, in_file_gv);
  fread(&nlist_size, sizeof(nlist_size), 1, in_file_nl);

  //vertexl_t *g_v_bin = reinterpret_cast<vertexl_t *>(malloc(num_nodes * sizeof(vertexl_t)));
  fread(g_v_bin, sizeof(vertexl_t), num_nodes, in_file_gv); // read in all vertices 
  // fread(nlist_beg, sizeof(uint64_t), nlist_size, in_file_nl); // read in all vertices
  uint64_t num_edges = 0, max_deg = 0;
  uint64_t curr_base = 0;
  for(int i=0; i<num_nodes; i++)
  {
    uint64_t * loc_nlist = reinterpret_cast<uint64_t *>(((uint64_t)nlist_beg) + curr_base);
    uint64_t deg = g_v_bin[i].deg;
    fread(loc_nlist, sizeof(uint64_t), deg, in_file_nl); // read in all vertices
    g_v_bin[i].neigh = loc_nlist;

    num_edges += deg;
    if (max_deg < deg)
      max_deg = deg;

    curr_base += deg * sizeof(uint64_t);
    curr_base = curr_base + (64 - (curr_base % 64));

    #ifdef TESTBIN
    print_array(g_v_bin[i].neigh, g_v_bin[i].deg);
    printf("Input pair %lu: key=%lu deg=%lu nlist_ptr=%lu\n", i, g_v_bin[i].id, g_v_bin[i].deg, g_v_bin[i].neigh);
    #endif
  }

  printf("# vertices: %lu , # edges:%lu , avg deg: %lf, max deg: %lu\n", num_nodes, num_edges, ((double)num_edges)/num_nodes, max_deg);
  fflush(stdout);
  return max_deg;

}


void convert_to_new_struct(int num_nodes, vertexl_t *g_v_bin, vertex_t* g_v_bin_new){
  for(int i = 0; i < num_nodes; i++){
    g_v_bin_new[i].id = g_v_bin[i].id;
    g_v_bin_new[i].deg = g_v_bin[i].deg;
    g_v_bin_new[i].neigh = g_v_bin[i].neigh;
    g_v_bin_new[i].min_vid = g_v_bin[i].neigh[0];
    g_v_bin_new[i].max_vid = g_v_bin[i].neigh[(g_v_bin[i].deg-1)];
    g_v_bin_new[i].reserved0 = 0;
    g_v_bin_new[i].reserved1 = 0;
    g_v_bin_new[i].reserved2 = 0;
#ifdef DEBUG
  printf("g_v_bin_new:%lu, i:%lu v:%lu, deg:%lu, neigh:%lu\n", g_v_bin_new, i, g_v_bin_new[i].id, g_v_bin_new[i].deg, g_v_bin_new[i].neigh);
#endif
  }
}

size_t CopyLocal2Global(dramalloc::DramAllocator* allocator, uint64_t chunck_size, uint64_t global_addr, uint64_t local_addr, uint64_t copy_size){
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


/* ------------------------ run function ---------------------------------*/
/* cpu_id = 0, execute TC */
extern "C" {
int run(UpDown::UDRuntime_t* test_rt, int argc, char* argv[]) {
  /*------------- Initialize Input Parameter ----------------------*/
    char* filename = argv[1];
    char* filename2 = argv[2];
    uint64_t num_lanes = atoi(argv[3]);
    uint64_t num_control_lanes_per_level = 32;
    int mode = 0;
    uint64_t svert = 0, evert;
    uint64_t cpu_id = atoi(argv[argc-1]);
    uint64_t num_nodes = test_rt->getMachineConfig().NumNodes;
    uint64_t block_size = 1UL * 32 * 1024;
    printf("block_size = %lu\n", block_size);
    UpDown::ud_machine_t machine = test_rt->getMachineConfig();
#ifdef ASST_FASTSIM
    test_rt->set_barrier_times(num_nodes);
#elif defined (GEM5)
    test_rt->set_barrier_times(num_nodes);
#else
    test_rt->set_barrier_times(1);
#endif

    test_rt->barrier(cpu_id);

    if(cpu_id == 0){
        
        /*--------------- Load Input Graph ---------------------*/
        uint64_t num_edges=0, num_verts=0, nlist_size = 0;
        printf("Binfile:%s\n", filename);

        FILE* in_file_gv = fopen(filename, "rb");
        if (!in_file_gv) {
                exit(EXIT_FAILURE);
        }
        FILE* in_file_nl = fopen(filename2, "rb");
        if (!in_file_nl) {
                exit(EXIT_FAILURE);
        }

        fseek(in_file_gv, 0, SEEK_SET);
        fseek(in_file_nl, 0, SEEK_SET);
        fread(&num_verts, sizeof(num_verts),1, in_file_gv);
        fread(&nlist_size, sizeof(nlist_size), 1, in_file_nl);

        fclose(in_file_gv);
        fclose(in_file_nl);
        printf("num_verts = %lu, nlist_size = %lu\n",num_verts,nlist_size);

        uint64_t g_v_bin_size = num_verts * sizeof(vertexl_t) + 8 * sizeof(uint64_t);
        uint64_t g_v_bin_new_size = num_verts * sizeof(vertex_t) + 8 * sizeof(uint64_t);
        uint64_t nlist_beg_size = (nlist_size + num_verts * 8 + 8) * sizeof(uint64_t);

        vertexl_t *g_v_bin = reinterpret_cast<vertexl_t *>(test_rt->mm_malloc(g_v_bin_size));
        vertex_t *g_v_bin_new = reinterpret_cast<vertex_t *>(test_rt->mm_malloc(g_v_bin_new_size));
        uint64_t* nlist_beg = reinterpret_cast<uint64_t*>(test_rt->mm_malloc(nlist_beg_size));

        uint64_t total_size = g_v_bin_new_size + nlist_beg_size + g_v_bin_size;

        // Load all the neighborlists
        read_and_load_nlistbin(filename, filename2,  g_v_bin , nlist_beg);

        // Convert to different vertex data struct and launch TC

        convert_to_new_struct(num_verts, g_v_bin, g_v_bin_new);

        if(mode == 0 || evert > num_verts){
            evert = num_verts;
        }



      /*--------------------- Compute DRAM Buffer Size to store out-of-thread event -------------------------*/

        uint64_t total_verts_per_lane = std::ceil((evert - svert) / (double)(num_lanes) / 8.0) * 8 + 8;
        printf("total_verts_per_lane = %lu\n",total_verts_per_lane);
        // uint64_t intersect_per_lane = 131072 * 2048 * 4 / num_lanes + 2048;
        uint64_t intersect_per_lane = (1UL << 36) / num_lanes / sizeof(uint64_t); // 64GB
        // uint64_t intersect_per_lane = 2048;


        uint64_t masterblock_size = (total_verts_per_lane * num_lanes * sizeof(uint64_t));
        uint64_t intblock_size = (intersect_per_lane * num_lanes * sizeof(uint64_t));

        // Allocate space for master and intersection temporary areas
        uint64_t *masterblock = reinterpret_cast<uint64_t *>(test_rt->mm_malloc((masterblock_size)));
        uint64_t *intblock = reinterpret_cast<uint64_t *>(test_rt->mm_malloc(intblock_size));
        memset(intblock, 0, intblock_size);


        total_size = total_size;

        printf("Space allocated: Masters %lu\n", masterblock_size); 
        printf("Space allocated: Ints %lu\n", intblock_size);


        // Assign v to masterblock
        for(int i=0; i < num_lanes; i++)
        {
            masterblock[i * total_verts_per_lane] = 0;
        }

        for(uint64_t i = svert; i < evert; i++)
        {
            uint64_t lane_id = (i - svert) % num_lanes;
            uint64_t current_index = masterblock[lane_id * total_verts_per_lane] + 1;
            masterblock[lane_id * total_verts_per_lane] = current_index;
            masterblock[lane_id * total_verts_per_lane + current_index] = i; 

        }



#if defined GEM5_MODE
        m5_switch_cpu();
#endif

        /* Initialize DRAMALLOC */
        printf("Start initialize DRAMalloc\n");
        #ifdef GEM5
        dramalloc::DramAllocator *allocator = new dramalloc::DramAllocator(test_rt, machine /*machineConfig*/, three_clique_mm_exe::DRAMalloc__global_broadcast /*eventlabel*/, blockSize);
        #else
        dramalloc::DramAllocator *allocator = new dramalloc::DramAllocator(test_rt, machine /*machineConfig*/, three_clique_mm_exe::DRAMalloc__global_broadcast /*eventlabel*/);
        #endif
        printf("Finish initialize DRAMalloc set flag to 1\n");


        uint64_t g_v_bin_new_global = (uint64_t)allocator->mm_malloc_global(g_v_bin_new_size, block_size, num_nodes, 0);
        printf("g_v_bin_new_global = 0x%lX, g_v_bin_new_size = %lu\n", g_v_bin_new_global, g_v_bin_new_size);
        uint64_t nlist_beg_global = (uint64_t)allocator->mm_malloc_global(nlist_beg_size, block_size, num_nodes, 0);
        printf("nlist_beg_global = 0x%lX, nlist_beg_size = %lu\n", nlist_beg_global, nlist_beg_size);
        

        for(int i = 0; i < num_verts; i++){
            g_v_bin_new[i].neigh = (uint64_t*)(((uint64_t)(g_v_bin_new[i].neigh)) - (uint64_t)nlist_beg + (uint64_t)nlist_beg_global);
        }


        /* copy g_v_bin_new */
        printf("g_v_bin_new_global = 0x%lX, g_v_bin_new_size = %lu\n", g_v_bin_new_global, g_v_bin_new_size);
        CopyLocal2Global(allocator, block_size, g_v_bin_new_global, (uint64_t)g_v_bin_new, g_v_bin_new_size);
        // dram_copy(test_rt, (uint64_t)g_v_bin_new, g_v_bin_new_global, g_v_bin_new_size);

        /* copy nlist_beg_global */
        printf("nlist_beg_global = 0x%lX, nlist_beg_size = %lu\n", nlist_beg_global, nlist_beg_size);
        CopyLocal2Global(allocator, block_size, nlist_beg_global, (uint64_t)nlist_beg, nlist_beg_size);
        // dram_copy(test_rt, (uint64_t)nlist_beg, nlist_beg_global, nlist_beg_size);

        
        UpDown::word_t ops_data[8];
        UpDown::operands_t ops(8, ops_data);
        
        UpDown::networkid_t nwid(0, false, 0);
        uint64_t updown_count = 0;
        uint64_t flag = 0;
        uint64_t mastersize = total_verts_per_lane * sizeof(uint64_t); // bytes
        uint64_t intsize = intersect_per_lane * sizeof(uint64_t); // bytes

        timeval start,end;

        printf("Starting UD now\n");
        fflush(stdout);


        #if not defined GEM5_MODE
        gettimeofday(&start,NULL);
        #endif

        uint64_t log2_num_control_lanes_per_level = std::log2(num_control_lanes_per_level);

        test_rt->t2ud_memcpy(&flag, 8, nwid, TOP_FLAG); // set signal flag to 0

        ops.set_operand(0, (UpDown::word_t) num_lanes);     // num_lanes_in
        ops.set_operand(1, (UpDown::word_t) g_v_bin_new_global);   // g_v_in
        ops.set_operand(2, (UpDown::word_t) masterblock);   // master_start
        ops.set_operand(3, (UpDown::word_t) mastersize);    // master_size
        ops.set_operand(4, (UpDown::word_t) intblock);      // intersection_start
        ops.set_operand(5, (UpDown::word_t) intsize);       // intersection_size
        ops.set_operand(6, (uint64_t)log2_num_control_lanes_per_level);
        ops.set_operand(7, (uint64_t)0);
        test_rt->send_event(UpDown::event_t(
            three_clique_mm_exe::main_master__init_tc, /*Event Label*/
            nwid, /* Network ID*/
            UpDown::CREATE_THREAD, /*Thread ID*/
            &ops /*Operands*/
            ));

        #if defined GEM5_MODE
        m5_dump_reset_stats(0,0);
        #endif
        test_rt->start_exec(nwid);
        test_rt->test_wait_addr(nwid, TOP_FLAG, 1);
        #if defined GEM5_MODE
        m5_dump_reset_stats(0,0);
        #endif

        test_rt->ud2t_memcpy(&updown_count, 8, nwid, INTERSECT_RESULT); // set signal flag to 0
        
        #if not defined GEM5_MODE
        gettimeofday(&end,NULL);
        double time = (end.tv_sec-start.tv_sec) + (end.tv_usec-start.tv_usec) / 1000000.0;
        printf("Three Clique time:%lf s\n", time);
        #endif

        printf("TOP: Intersection test done.\n");

                /*--------------------- CPU validation -----------------------*/
#ifdef CPU_CMP
        uint64_t cpu_count = three_clique_count_cpu(svert, evert, g_v_bin);
        printf("Three Clique Count: Reference:%lu\n", cpu_count);
#endif

        
        printf("Three Clique Count UD: %lu\n", updown_count);
        #ifdef CPU_CMP
        printf("Three Clique Count CPU: %lu\n", cpu_count);
        #endif
    }
    printf("CPU = %lu waiting to finish\n", cpu_id);
    test_rt->barrier(cpu_id);
    printf("CPU = %lu finished\n", cpu_id);

    return 0;
}
}

int main(int argc, char* argv[]) {

  /* ------------------ Input Parameters ------------------ */
  if (argc < 4) {
    printf("Insufficient Input Params\n");
    printf("%s\n", USAGE);
    exit(1);
  }
  char* filename = argv[1];
  char* filename2 = argv[2];
  uint64_t num_lanes = atoi(argv[3]);

  uint64_t network_latency = 1100;
  uint64_t network_bandwidth = 0;

  if(argc >= 5){
    network_latency = atoi(argv[4]);
  }
  if(argc >= 6){
    network_bandwidth = atoi(argv[5]);
  }

  printf("Input File: %s , %s\n", filename, filename2);
  printf("Num Lanes:%ld\n", num_lanes);
  fflush(stdout);

  /*------------------ Set up Machine Config ------------------*/
  uint64_t num_control_lanes_per_level = 32;
  uint64_t block_size = 1UL * 32 * 1024;
  // Set up machine parameters
  UpDown::ud_machine_t machine;
  machine.MapMemSize = 1UL << 37; // 128GB
  machine.GMapMemSize = 1UL << 38; // 256GB
  machine.LocalMemAddrMode = 1;
  machine.NumLanes = num_lanes > 64 ? 64 : num_lanes;
  machine.NumUDs = std::ceil(num_lanes / 64.0) > 4 ? 4 : std::ceil(num_lanes / 64.0);
  machine.NumStacks = std::ceil(num_lanes / (64.0 * 4)) > 8 ? 8 : std::ceil(num_lanes / (64.0 * 4));
  machine.NumNodes = std::ceil(num_lanes / (64.0 * 4 * 8));

  if(num_lanes <= 2048){
    machine.MapMemSize = 1UL << 38; // 256GB
    machine.GMapMemSize = 1UL << 32; // 4GB
  }

  machine.InterNodeLatency = network_latency;
  machine.InterNodeBandwidth = network_bandwidth;

  printf("network_latency = %lu, network_bandwidth = %lu\n", network_latency, network_bandwidth);
  fflush(stdout);

  UpDown::BASimUDRuntime_t* test_rt = new UpDown::BASimUDRuntime_t(machine, "three_clique_mm_exe.bin", 0);

#ifdef DEBUG
  printf("=== Base Addresses ===\n");
  test_rt->dumpBaseAddrs();
  printf("\n=== Machine Config ===\n");
  test_rt->dumpMachineConfig();
#endif

  uint64_t num_nodes = test_rt->getMachineConfig().NumNodes;

  /*--------------- Load Input Graph ---------------------*/
  uint64_t num_edges=0, num_verts=0, nlist_size = 0;
  FILE* in_file_gv = fopen(filename, "rb");
  if (!in_file_gv) {
          exit(EXIT_FAILURE);
  }
  FILE* in_file_nl = fopen(filename2, "rb");
  if (!in_file_nl) {
          exit(EXIT_FAILURE);
  }

  fseek(in_file_gv, 0, SEEK_SET);
  fseek(in_file_nl, 0, SEEK_SET);
  fread(&num_verts, sizeof(num_verts),1, in_file_gv);
  fread(&nlist_size, sizeof(nlist_size), 1, in_file_nl);

  fclose(in_file_gv);
  fclose(in_file_nl);
  printf("num_verts = %lu, nlist_size = %lu\n",num_verts,nlist_size);

  uint64_t g_v_bin_size = num_verts * sizeof(vertexl_t) + 8 * sizeof(uint64_t);
  uint64_t g_v_bin_new_size = num_verts * sizeof(vertex_t) + 8 * sizeof(uint64_t);
  uint64_t nlist_beg_size = (nlist_size + num_verts * 8 + 8) * sizeof(uint64_t);

  vertexl_t *g_v_bin = reinterpret_cast<vertexl_t *>(test_rt->mm_malloc(g_v_bin_size));
  vertex_t *g_v_bin_new = reinterpret_cast<vertex_t *>(test_rt->mm_malloc(g_v_bin_new_size));
  uint64_t* nlist_beg = reinterpret_cast<uint64_t*>(test_rt->mm_malloc(nlist_beg_size));

  uint64_t total_size = g_v_bin_new_size + nlist_beg_size + g_v_bin_size;

  // Load all the neighborlists
  read_and_load_nlistbin(filename, filename2,  g_v_bin , nlist_beg);

  // Convert to different vertex data struct and launch TC
  convert_to_new_struct(num_verts, g_v_bin, g_v_bin_new);


  /*--------------------- Compute DRAM Buffer Size to store out-of-thread event -------------------------*/

  uint64_t total_verts_per_lane = std::ceil((num_verts) / (double)(num_lanes) / 8.0) * 8 + 8;
  printf("total_verts_per_lane = %lu\n",total_verts_per_lane);
  // uint64_t intersect_per_lane = 131072 * 2048 * 4 / num_lanes + 2048;
  uint64_t intersect_per_lane = (1UL << 36) / num_lanes / sizeof(uint64_t); // 64GB
  // uint64_t intersect_per_lane = 2048;

  uint64_t masterblock_size = (total_verts_per_lane * num_lanes * sizeof(uint64_t));
  uint64_t intblock_size = (intersect_per_lane * num_lanes * sizeof(uint64_t));

  // Allocate space for master and intersection temporary areas
  uint64_t *masterblock = reinterpret_cast<uint64_t *>(test_rt->mm_malloc((masterblock_size)));
  uint64_t *intblock = reinterpret_cast<uint64_t *>(test_rt->mm_malloc(intblock_size));
  memset(intblock, 0, intblock_size);


  printf("Space allocated: Masters %lu\n", masterblock_size); 
  printf("Space allocated: Ints %lu\n", intblock_size);


  // Assign v to masterblock
  for(int i=0; i < num_lanes; i++)
  {
      masterblock[i * total_verts_per_lane] = 0;
  }

  for(uint64_t i = 0; i < num_verts; i++)
  {
    uint64_t lane_id = i % num_lanes;
    uint64_t current_index = masterblock[lane_id * total_verts_per_lane] + 1;
    masterblock[lane_id * total_verts_per_lane] = current_index;
    masterblock[lane_id * total_verts_per_lane + current_index] = i; 
  }
  /* Initialize DRAMALLOC */
  printf("Start initialize DRAMalloc\n");
  dramalloc::DramAllocator *allocator = new dramalloc::DramAllocator(test_rt, three_clique_mm_exe::DRAMalloc__global_broadcast /*eventlabel*/);
  printf("Finish initialize DRAMalloc set flag to 1\n");

  uint64_t g_v_bin_new_global = (uint64_t)allocator->mm_malloc_global(g_v_bin_new_size, block_size, num_nodes, 0);
  printf("g_v_bin_new_global = 0x%lX, g_v_bin_new_size = %lu\n", g_v_bin_new_global, g_v_bin_new_size);
  uint64_t nlist_beg_global = (uint64_t)allocator->mm_malloc_global(nlist_beg_size, block_size, num_nodes, 0);
  printf("nlist_beg_global = 0x%lX, nlist_beg_size = %lu\n", nlist_beg_global, nlist_beg_size);
          
  for(int i = 0; i < num_verts; i++){
    g_v_bin_new[i].neigh = (uint64_t*)(((uint64_t)(g_v_bin_new[i].neigh)) - (uint64_t)nlist_beg + (uint64_t)nlist_beg_global);
  }

  /* copy g_v_bin_new */
  printf("g_v_bin_new_global = 0x%lX, g_v_bin_new_size = %lu\n", g_v_bin_new_global, g_v_bin_new_size);
  CopyLocal2Global(allocator, block_size, g_v_bin_new_global, (uint64_t)g_v_bin_new, g_v_bin_new_size);

  /* copy nlist_beg_global */
  printf("nlist_beg_global = 0x%lX, nlist_beg_size = %lu\n", nlist_beg_global, nlist_beg_size);
  CopyLocal2Global(allocator, block_size, nlist_beg_global, (uint64_t)nlist_beg, nlist_beg_size);
          

  /*--------------------- Execute UpDown Execution -------------------------*/
  UpDown::word_t ops_data[8];
  UpDown::operands_t ops(8, ops_data);

  UpDown::networkid_t nwid(0, false, 0);
  uint64_t updown_count = 0;
  uint64_t flag = 0;
  uint64_t mastersize = total_verts_per_lane * sizeof(uint64_t); // bytes
  uint64_t intsize = intersect_per_lane * sizeof(uint64_t); // bytes

  timeval start,end;
  printf("Starting UD now\n");
  fflush(stdout);
  uint64_t log2_num_control_lanes_per_level = std::log2(num_control_lanes_per_level);

  test_rt->t2ud_memcpy(&flag, 8, nwid, TOP_FLAG); // set signal flag to 0
  ops.set_operand(0, (UpDown::word_t) num_lanes);     // num_lanes_in
  ops.set_operand(1, (UpDown::word_t) g_v_bin_new_global);   // g_v_in
  ops.set_operand(2, (UpDown::word_t) masterblock);   // master_start
  ops.set_operand(3, (UpDown::word_t) mastersize);    // master_size
  ops.set_operand(4, (UpDown::word_t) intblock);      // intersection_start
  ops.set_operand(5, (UpDown::word_t) intsize);       // intersection_size
  ops.set_operand(6, (uint64_t)log2_num_control_lanes_per_level);
  ops.set_operand(7, (uint64_t)0);
  test_rt->send_event(UpDown::event_t(
      three_clique_mm_exe::main_master__init_tc, /*Event Label*/
      nwid, /* Network ID*/
      UpDown::CREATE_THREAD, /*Thread ID*/
      &ops /*Operands*/
      ));

  test_rt->start_exec(nwid);
  test_rt->test_wait_addr(nwid, TOP_FLAG, 1);
  test_rt->ud2t_memcpy(&updown_count, 8, nwid, INTERSECT_RESULT); // set signal flag to 0
  
  #if not defined GEM5_MODE
  gettimeofday(&end,NULL);
  double time = (end.tv_sec-start.tv_sec) + (end.tv_usec-start.tv_usec) / 1000000.0;
  printf("Three Clique time:%lf s\n", time);
  #endif

  printf("TOP: Intersection test done.\n");

  /*--------------------- CPU validation -----------------------*/
#ifdef CPU_CMP
  uint64_t cpu_count = three_clique_count_cpu(0, num_verts, g_v_bin);
  printf("Three Clique Count: Reference:%lu\n", cpu_count);
#endif

  #if not defined GEM5_MODE
  for(int j=0; j<num_lanes; j++)
  {
    printf("UD = %d, Lane = %d\n",(j / 64) , j%64);
    test_rt->print_stats((j / 64) , j%64);
    #ifdef DETAIL_STATS
      test_rt->print_histograms(j / 64 , j%64);
    #endif
  }
  for(unsigned int node=0; node<machine.NumNodes; ++node) {
    test_rt->print_node_stats(node);
  }
  #endif

  printf("Three Clique Count UD: %lu\n", updown_count);
#ifdef CPU_CMP
  printf("Three Clique Count CPU: %lu\n", cpu_count);
#endif

  delete test_rt;

  printf("TC program finishes.\n");

  return 0;
}


