#include "simupdown.h"
#include "dramalloc.hpp"
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cmath>
#include <sys/types.h>
#include <sys/time.h>
#include "k_truss_exe.hpp"


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

#define USAGE "USAGE: ./k_truss_udweave <k> <gv_bin> <nl_bin> <num_lanes>"

#define K_OFFSET 65496
#define INTERSECT_RESULT 65520
#define TOP_FLAG 65528

#define MASTER_BUFFER_START 112
#define ITERA 24
#define GV_LOCAL 104

typedef uint64_t* ptr;
typedef uint64_t word_t;

typedef struct vertex_local{
	uint64_t deg;
	uint64_t id;
	ptr neigh;
  	ptr count_ptr;
} vertexl_t;

typedef struct vertex{
	uint64_t deg;
	uint64_t id;
	ptr neigh;
	ptr count_ptr;
	uint64_t min_vid;
	uint64_t max_vid;
	ptr neigh_local;
	ptr count_ptr_local;
} vertex_t;

typedef vertexl_t* vertexptr;

word_t intersection_constrain_v(vertexptr g_v_bin, uint64_t va, uint64_t vb, uint64_t threshold, double &n_edges){
	ptr list_a = g_v_bin[va].neigh;
	uint64_t size_a = g_v_bin[va].deg;
	ptr list_b = g_v_bin[vb].neigh;
	uint64_t size_b = g_v_bin[vb].deg;

	ptr count_a = g_v_bin[va].count_ptr;
	ptr count_b = g_v_bin[vb].count_ptr;

	word_t size = 0;
	word_t pos0 = 0, pos1 = 0;
	word_t a, b;
#ifdef BOUNDARY_CHECK
	if(size_a == 0 || size_b == 0 || list_a[2*(size_a - 1)] < list_b[0] || list_a[0] > list_b[2*(size_b - 1)])
		return 0;
#endif
	while(pos0 < size_a && pos1 < size_b)
	{
		a = list_a[pos0];
		b = list_b[pos1];
		if(a >= threshold)
		  	break;
		if(b >= threshold)
		  	break;
		if(a < b)
		  	pos0++;
		else if(a > b)
		  	pos1++;
		else{
		  	size++;
			// if(((uint64_t)&(count_a[pos0])) == ((uint64_t)&(g_v_bin[1].count_ptr[0]))){
			// 	printf("a: %lu %lu %lu\n", va, vb, a);
			// }
			// if(((uint64_t)&(count_b[pos1])) == ((uint64_t)&(g_v_bin[1].count_ptr[0]))){
			// 	printf("b: %lu %lu %lu\n", va, vb, a);
			// }
			count_a[pos0]++;
			count_b[pos1]++;
			pos0++;
			pos1++;
		}
	}
	n_edges = n_edges + pos0 + pos1;
	return size;
}

word_t three_clique_count_cpu(uint64_t svert, uint64_t evert, vertexptr g_v_bin, double &n_edges)
{
    word_t count = 0;
    int64_t i1 = 0;
    for(i1=svert; i1<evert; i1++)
    {
        word_t v1 = i1;
        uint64_t deg1 = g_v_bin[v1].deg;
        if(deg1 == 0)
            continue;
        uint64_t i2;
        for(i2=0; i2<deg1; i2++)
        {
            n_edges++;
            word_t v2 = g_v_bin[v1].neigh[i2];
            if(v2 >= v1)
                break;
            uint64_t deg2 = g_v_bin[v2].deg;
            if (deg2 == 0)
                continue;
          
            uint64_t len3 = intersection_constrain_v(g_v_bin, v1, v2, v2, n_edges);
            count = count + len3;
            g_v_bin[v1].count_ptr[i2] = g_v_bin[v1].count_ptr[i2] + len3;
			// if(((uint64_t)&(g_v_bin[v1].count_ptr[i2])) == ((uint64_t)&(g_v_bin[1].count_ptr[0]))){
			// 	printf("%lu[%lu] = %lu\n", v1, i2, len3);
			// }
        }
    }
    return count;
}

word_t fliter_count_cpu(uint64_t svert, uint64_t evert, vertexptr g_v_bin, double &n_edges, uint64_t k, uint64_t &edge)
{
    word_t count = 0;
    uint64_t i1 = 0;
    uint64_t edge_tc = 0;
    uint64_t nv = 0;
    uint64_t updated_edges = 0;
    for(i1=svert; i1<evert; i1++)
    {
        word_t v1 = i1;
        uint64_t deg1 = g_v_bin[v1].deg;
        if (deg1 == 0)
            continue;
        nv++;
        uint64_t i2, tmp_k;
        uint64_t new_deg = 0;
        edge = edge + deg1;
        for(i2=0; i2<deg1; i2++)
        {
            tmp_k = g_v_bin[v1].count_ptr[i2];
            edge_tc = edge_tc + tmp_k;
            if(tmp_k >= (k-2)){
              n_edges++;
              if(i2 != new_deg){
                g_v_bin[v1].neigh[new_deg] = g_v_bin[v1].neigh[i2];
                g_v_bin[v1].count_ptr[new_deg] = 0;
              }else{
                g_v_bin[v1].count_ptr[new_deg] = 0;
              }
              new_deg++;
              updated_edges++;
            }else{
              count = count + tmp_k;
            }
        }
        g_v_bin[v1].deg = new_deg;
        n_edges++;
    }
    printf("number of vertices: %lu, updated_edges: %lu\n", nv, updated_edges);
    return count;
}

word_t k_truss_cpu(uint64_t svert, uint64_t evert, vertexptr g_v_bin, uint64_t k){
	double total_tc_traversed_edge = 0, total_fliter_traversed_edge = 0, total_fliter_write_edge = 0;
	uint64_t num_iteration = 0;
	uint64_t total_tc = 0;
	uint64_t total_deleted_edges = 0;
	while(true){
		double tc_traversed_edge = 0, fliter_write_edge = 0;
		uint64_t tc = three_clique_count_cpu(svert, evert, g_v_bin, tc_traversed_edge);
		uint64_t edges = 0;
		uint64_t deleted_edges = fliter_count_cpu(svert, evert, g_v_bin, fliter_write_edge, k, edges);
		total_tc_traversed_edge = total_tc_traversed_edge + tc_traversed_edge;
		total_tc = total_tc + tc;
		total_deleted_edges = total_deleted_edges + deleted_edges;
		total_fliter_traversed_edge = total_fliter_traversed_edge + edges;
		total_fliter_write_edge = total_fliter_write_edge + fliter_write_edge;
		printf("Iteration %lu:\n", num_iteration);
    	printf("edges: %lu, TC: %lu, deleted_tc:%lu\n", edges, tc, deleted_edges);
		// printf("edges: %lu, TC: %lu, tc_traversed_edge: %lg, fliter_traversed_edge: %lu, fliter_write: %lg, deleted_edges:%lu\n", edges, tc, tc_traversed_edge, edges, fliter_write_edge, deleted_edges);
		// printf("total TC: %lu, total tc_traversed_edge: %lg, total fliter_traversed_edge: %lg, total fliter_write: %lg, total deleted_edges:%lu\n", total_tc, total_tc_traversed_edge, total_fliter_traversed_edge, total_fliter_write_edge, total_deleted_edges);
		// fflush(stdout);
		// if(num_iteration == 2 || num_iteration == 1){
        //     for(long i1=svert; i1<evert; i1++){
        //         word_t v1 = i1;
        //         uint64_t deg1 = g_v_bin[v1].deg;
        //         if(deg1 > 0)
        //             printf("vi = %lu, deg = %lu\n", v1, deg1);
        //     }
        // }
        num_iteration++;
		if(deleted_edges == 0){
			return num_iteration;
		}
	}
}



uint64_t read_and_load_nlistbin(const char* binfilename, const char* binfilename2 , vertexl_t *g_v_bin, uint64_t* nlist_beg, uint64_t* count_addr){
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

	size_t file_size;

	fseek(in_file_gv, 0, SEEK_SET);
	fseek(in_file_nl, 0, SEEK_SET);
	file_size = fread(&num_nodes, sizeof(num_nodes),1, in_file_gv);
	file_size = fread(&nlist_size, sizeof(nlist_size), 1, in_file_nl);

	uint64_t num_edges = 0, max_deg = 0;
	uint64_t curr_base = 0;
	for(int i=0; i<num_nodes; i++)
	{
    	file_size = fread(&(g_v_bin[i]), 3*sizeof(uint64_t), 1, in_file_gv);                      // read in vertices 
		uint64_t * loc_nlist = reinterpret_cast<uint64_t *>(((uint64_t)nlist_beg) + curr_base);
		uint64_t deg = g_v_bin[i].deg;
		fread(loc_nlist, sizeof(uint64_t), deg, in_file_nl);                                      // read in all vertices
		g_v_bin[i].neigh = loc_nlist;
    	g_v_bin[i].count_ptr = reinterpret_cast<uint64_t *>(((uint64_t)count_addr) + curr_base);

		num_edges += deg;
		if (max_deg < deg)
			max_deg = deg;

		curr_base += deg * sizeof(uint64_t);
    if((curr_base % 64) > 0)
		  curr_base = curr_base + (64 - (curr_base % 64));

#ifdef TESTBIN
		print_array(g_v_bin[i].neigh, g_v_bin[i].deg);
		printf("Input pair %lu: key=%lu deg=%lu nlist_ptr=%lu\n", i, g_v_bin[i].id, g_v_bin[i].deg, g_v_bin[i].neigh);
#endif
	}

	printf("# vertices: %lu , # edges:%lu , avg deg: %lf, max deg: %lu, total edge size: %lu bytes\n", num_nodes, num_edges, ((double)num_edges)/num_nodes, max_deg, curr_base);
	fflush(stdout);
	return max_deg;
}


void convert_to_new_struct(int num_nodes, vertexl_t *g_v_bin, vertex_t* g_v_bin_new){
  for(int i = 0; i < num_nodes; i++){
    g_v_bin_new[i].id = g_v_bin[i].id;
    g_v_bin_new[i].deg = g_v_bin[i].deg;
    g_v_bin_new[i].neigh = g_v_bin[i].neigh;
    g_v_bin_new[i].count_ptr = g_v_bin[i].count_ptr;
    g_v_bin_new[i].min_vid = g_v_bin[i].neigh[0];
    g_v_bin_new[i].max_vid = g_v_bin[i].neigh[g_v_bin[i].deg - 1];
    g_v_bin_new[i].neigh_local = g_v_bin[i].neigh;
    g_v_bin_new[i].count_ptr_local = g_v_bin[i].count_ptr;
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



int main(int argc, char* argv[]) {
	if (argc < 5) {
		printf("Insufficient Input Params\n");
		printf("%s\n", USAGE);
		exit(1);
	}
	uint64_t k = atoi(argv[1]);
	char* filename = argv[2];
	char* filename2 = argv[3];
	uint64_t num_lanes = atoi(argv[4]);
	uint64_t num_control_lanes_per_level = 32;
    uint64_t block_size = 1UL * 32 * 1024;
    printf("block_size = %lu\n", block_size);
	
	printf("File Name:%s , ", filename);
	printf("Num Lanes:%ld\n", num_lanes);

	// Set up machine parameters
	UpDown::ud_machine_t machine;
	machine.MapMemSize = 1UL << 39; // 512GB
	machine.GMapMemSize = 1UL << 37; // 128GB
	machine.LocalMemAddrMode = 1;
	machine.NumLanes = num_lanes > 64 ? 64 : num_lanes;
	machine.NumUDs = std::ceil(num_lanes / 64.0) > 4 ? 4 : std::ceil(num_lanes / 64.0);
	machine.NumStacks = std::ceil(num_lanes / (64.0 * 4)) > 8 ? 8 : std::ceil(num_lanes / (64.0 * 4));
	machine.NumNodes = std::ceil(num_lanes / (64.0 * 4 * 8));

	if(num_lanes <= 2048){
		machine.MapMemSize = 1UL << 39; // 512GB
		machine.GMapMemSize = 1UL << 32; // 4GB
	}


	#ifdef GEM5_MODE
	UpDown::UDRuntime_t *test_rt = new UpDown::UDRuntime_t(machine);
	#else 
	UpDown::BASimUDRuntime_t* test_rt = new UpDown::BASimUDRuntime_t(machine, "k_truss_exe.bin", 0, 100);
	test_rt->topPerNode = 1;
	#endif

	// #ifdef DEBUG
	printf("=== Base Addresses ===\n");
	test_rt->dumpBaseAddrs();
	printf("\n=== Machine Config ===\n");
	test_rt->dumpMachineConfig();
	// #endif

	fflush(stdout);

    uint64_t num_nodes = test_rt->getMachineConfig().NumNodes;
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

    uint64_t svert = 0;
    uint64_t evert = num_verts;
    // uint64_t evert = 1000;

    fclose(in_file_gv);
    fclose(in_file_nl);
    printf("num_verts = %lu, nlist_size = %lu\n",num_verts,nlist_size);

    uint64_t g_v_bin_size = num_verts * sizeof(vertexl_t) + 8 * sizeof(uint64_t);
    uint64_t g_v_bin_new_size = num_verts * sizeof(vertex_t) + 8 * sizeof(uint64_t);
    uint64_t nlist_beg_size = (nlist_size + num_verts * 8 + 8) * sizeof(uint64_t);
    uint64_t count_size = (nlist_size + num_verts * 8 + 8) * sizeof(uint64_t);

    vertexl_t *g_v_bin = reinterpret_cast<vertexl_t *>(test_rt->mm_malloc(g_v_bin_size));
    vertex_t *g_v_bin_new = reinterpret_cast<vertex_t *>(test_rt->mm_malloc(g_v_bin_new_size));
    uint64_t* nlist_beg = reinterpret_cast<uint64_t*>(test_rt->mm_malloc(nlist_beg_size));
    uint64_t* count_addr = reinterpret_cast<uint64_t*>(test_rt->mm_malloc(count_size));
    memset(count_addr, 0, count_size);

    uint64_t total_size = g_v_bin_new_size + nlist_beg_size + g_v_bin_size + count_size;

    // Load all the neighborlists
    read_and_load_nlistbin(filename, filename2,  g_v_bin , nlist_beg, count_addr);

    // Convert to different vertex data struct and launch TC

    convert_to_new_struct(num_verts, g_v_bin, g_v_bin_new);



    /*--------------------- Compute DRAM Buffer Size to store out-of-thread event -------------------------*/

    uint64_t total_verts_per_lane = std::ceil((evert - svert) / (double)(num_lanes) / 8.0) * 8 + 8;
    printf("total_verts_per_lane = %lu\n",total_verts_per_lane);
    // uint64_t intersect_per_lane = 131072 * 2048 * 4 / num_lanes + 2048;
    uint64_t intersect_per_lane = (1UL << 38) / num_lanes / sizeof(uint64_t); // 256GB
    // uint64_t intersect_per_lane = 2048;


    uint64_t masterblock_size = (total_verts_per_lane * num_lanes * sizeof(uint64_t)) * 2;
    uint64_t intblock_size = (intersect_per_lane * num_lanes * sizeof(uint64_t));

    // Allocate space for master and intersection temporary areas
    uint64_t *masterblock = reinterpret_cast<uint64_t *>(test_rt->mm_malloc((masterblock_size)));
    uint64_t *intblock = reinterpret_cast<uint64_t *>(test_rt->mm_malloc(intblock_size));
    memset(intblock, 0, intblock_size);


    total_size = total_size;

    printf("Space allocated: Masters 0x%lX %lu\n", masterblock, masterblock_size); 
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

    /* Copy to CPU */
    #ifdef CPU_CMP
    uint64_t* nlist_beg_new = reinterpret_cast<uint64_t*>(malloc(nlist_beg_size));
    uint64_t* count_addr_new = reinterpret_cast<uint64_t*>(malloc(count_size));
    memset(count_addr_new, 0, count_size);
    uint64_t max_deg = 0;
    uint64_t curr_base = 0;
    num_edges = 0;
    for(uint64_t i = 0; i < num_verts; i++)
    {
        uint64_t * loc_nlist = reinterpret_cast<uint64_t *>(((uint64_t)nlist_beg) + curr_base);
        uint64_t * loc_nlist_new = reinterpret_cast<uint64_t *>(((uint64_t)nlist_beg_new) + curr_base);
        uint64_t deg = g_v_bin[i].deg;
        memcpy(loc_nlist_new, loc_nlist, deg * sizeof(uint64_t));
        g_v_bin[i].neigh = loc_nlist_new;
        g_v_bin[i].count_ptr = reinterpret_cast<uint64_t *>(((uint64_t)count_addr_new) + curr_base);

        curr_base += deg * sizeof(uint64_t);
    if((curr_base % 64) > 0)
            curr_base = curr_base + (64 - (curr_base % 64));
    }
    #endif


#if defined GEM5_MODE
    m5_switch_cpu();
#endif

    /* Initialize DRAMALLOC */
    printf("Start initialize DRAMalloc\n");
    #ifdef GEM5
    dramalloc::DramAllocator *allocator = new dramalloc::DramAllocator(test_rt, k_truss_exe::DRAMalloc__global_broadcast /*eventlabel*/, blockSize);
    #else
    dramalloc::DramAllocator *allocator = new dramalloc::DramAllocator(test_rt, k_truss_exe::DRAMalloc__global_broadcast /*eventlabel*/);
    #endif
    printf("Finish initialize DRAMalloc set flag to 1\n");


    uint64_t g_v_bin_new_global = (uint64_t)allocator->mm_malloc_global(g_v_bin_new_size, block_size, num_nodes, 0);
    printf("g_v_bin_new_global = 0x%lX, g_v_bin_new_size = %lu\n", g_v_bin_new_global, g_v_bin_new_size);
    uint64_t nlist_beg_global = (uint64_t)allocator->mm_malloc_global(nlist_beg_size, block_size, num_nodes, 0);
    printf("nlist_beg_global = 0x%lX, nlist_beg_size = %lu\n", nlist_beg_global, nlist_beg_size);
    uint64_t count_addr_global = (uint64_t)allocator->mm_malloc_global(count_size, block_size, num_nodes, 0);
    printf("count_addr_global = 0x%lX, count_size = %lu\n", count_addr_global, count_size);
    

    for(int i = 0; i < num_verts; i++){
        g_v_bin_new[i].neigh = (uint64_t*)(((uint64_t)(g_v_bin_new[i].neigh)) - (uint64_t)nlist_beg + (uint64_t)nlist_beg_global);
        g_v_bin_new[i].count_ptr = (uint64_t*)(((uint64_t)(g_v_bin_new[i].count_ptr)) - (uint64_t)count_addr + (uint64_t)count_addr_global);
    }



    /* copy g_v_bin_new */
    printf("g_v_bin_new_global = 0x%lX, g_v_bin_new_size = %lu\n", g_v_bin_new_global, g_v_bin_new_size);
    CopyLocal2Global(allocator, block_size, g_v_bin_new_global, (uint64_t)g_v_bin_new, g_v_bin_new_size);
    // dram_copy(test_rt, (uint64_t)g_v_bin_new, g_v_bin_new_global, g_v_bin_new_size);

    /* copy nlist_beg_global */
    printf("nlist_beg_global = 0x%lX, nlist_beg_size = %lu\n", nlist_beg_global, nlist_beg_size);
    CopyLocal2Global(allocator, block_size, nlist_beg_global, (uint64_t)nlist_beg, nlist_beg_size);
    // dram_copy(test_rt, (uint64_t)nlist_beg, nlist_beg_global, nlist_beg_size);

        /* copy count_addr_global */
    printf("count_addr_global = 0x%lX, count_addr_size = %lu\n", count_addr_global, count_size);
    CopyLocal2Global(allocator, block_size, count_addr_global, (uint64_t)count_addr, count_size);


    
    UpDown::word_t ops_data[9];
    UpDown::operands_t ops(9, ops_data);
    
    UpDown::networkid_t nwid(0, false, 0);
    uint64_t updown_count = 0;
    uint64_t flag = 0;
    uint64_t mastersize = total_verts_per_lane * sizeof(uint64_t); // bytes
    uint64_t intsize = intersect_per_lane * sizeof(uint64_t); // bytes
    uint64_t input_k = k-2;

    timeval start,end;

    printf("Starting UD now %lu\n", intsize);
    fflush(stdout);


    #if not defined GEM5_MODE
    gettimeofday(&start,NULL);
    #endif

    uint64_t log2_num_control_lanes_per_level = std::log2(num_control_lanes_per_level);
    log2_num_control_lanes_per_level = log2_num_control_lanes_per_level << 32;

    test_rt->t2ud_memcpy(&flag, 8, nwid, TOP_FLAG); // set signal flag to 0
    test_rt->t2ud_memcpy(&flag, 8, nwid, ITERA); // set itera to  0
    // test_rt->t2ud_memcpy(&masterblock, 8, nwid, MASTER_BUFFER_START); // set masterblock
    test_rt->t2ud_memcpy(&input_k, 8, nwid, K_OFFSET); // set k
    test_rt->t2ud_memcpy(&g_v_bin_new, 8, nwid, GV_LOCAL);

    uint64_t num_combine = 1;
    num_combine = (num_combine << 32) + 2048;
    uint64_t num_lanes_tmp = num_lanes;
    num_lanes_tmp = (num_lanes_tmp << 32) + num_lanes_tmp;

    ops.set_operand(0, (UpDown::word_t) num_lanes_tmp);     // num_lanes_in
    ops.set_operand(1, (UpDown::word_t) num_combine);   // g_v_in
    ops.set_operand(2, (UpDown::word_t) g_v_bin_new_global);   // master_start
    ops.set_operand(3, (UpDown::word_t) intblock);    // master_size
    ops.set_operand(4, (UpDown::word_t) intsize);      // intersection_start
    ops.set_operand(5, (UpDown::word_t) masterblock );       // intersection_size
    ops.set_operand(6, (UpDown::word_t) masterblock + masterblock_size/2);
    ops.set_operand(7, (uint64_t)mastersize);
    ops.set_operand(8, (UpDown::word_t) log2_num_control_lanes_per_level); 
    test_rt->send_event(UpDown::event_t(
        k_truss_exe::main_master__init_tc, /*Event Label*/
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
    uint64_t k_max = k_truss_cpu(svert, evert, g_v_bin, k);
    // double tc_traversed_edge = 0, fliter_write_edge = 0;
    // uint64_t edges_tmp = 0;
    // uint64_t tc = three_clique_count_cpu(svert, evert, g_v_bin, tc_traversed_edge);
    // uint64_t deleted_edges = fliter_count_cpu(svert, evert, g_v_bin, fliter_write_edge, k, edges_tmp);
    // printf("CPU TC: %lu, deleted_edges: %lu\n", tc, deleted_edges);

    // for(uint64_t i = 0; i < num_verts; i++){
    //   if(g_v_bin[i].deg != g_v_bin_new[i].deg){
    //       printf("g_v_bin[%lu].deg (%lu) != g_v_bin_new[%lu].deg (%lu)\n", i, g_v_bin[i].deg, i, g_v_bin_new[i].deg);
    //       fflush(stdout);
    //       return -1;
    //   }
    //   uint64_t deg = g_v_bin[i].deg;
    //   if(deg > 0){
    // 	if(g_v_bin_new[i].min_vid != g_v_bin_new[i].neigh[0]){
    // 		printf("g_v_bin_new[i].min_vid != g_v_bin_new[i].neigh[0]\n");
    // 		fflush(stdout);
    // 		return -1;
    // 	}
    // 	if(g_v_bin_new[i].max_vid != g_v_bin_new[i].neigh[deg-1]){
    // 		printf("g_v_bin_new[i].max_vid != g_v_bin_new[i].neigh[deg-1]\n");
    // 		fflush(stdout);
    // 		return -1;
    // 	}
    //   }
    //   for(uint64_t j = 0; j < deg; j++){
    //     if(g_v_bin[i].neigh[j] != g_v_bin_new[i].neigh[j]){
    //       printf("edge N(%lu)[%lu] (%lu) != N_new(%lu)[%lu] (%lu)\n", i, j, g_v_bin[i].neigh[j], i, j, g_v_bin_new[i].neigh[j]);
    //       fflush(stdout);
    //       return -1;
    //     }
    //     if(g_v_bin[i].count_ptr[j] != g_v_bin_new[i].count_ptr[j]){
    //       printf("edge count N(%lu)[%lu] (%lu) != N_new(%lu)[%lu] (%lu) addr = 0x%lx\n", i, j, g_v_bin[i].count_ptr[j], i, j, g_v_bin_new[i].count_ptr[j], &(g_v_bin_new[i].count_ptr[j]));
    //       fflush(stdout);
    //       return -1;
    //     } 
    //   }
    // }

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
	#endif

    printf("UD k=%lu, itera: %lu\n", k, updown_count);
    #ifdef CPU_CMP
    printf("CPU k=%lu, itera: %lu\n", k, k_max);
    #endif

	delete test_rt;

	printf("KTruss program finishes.\n");

	return 0;
}


