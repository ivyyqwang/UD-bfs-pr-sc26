#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cmath>
#include <sys/types.h>
#include <sys/time.h>
#include <bit>
#include <cstdint>


/* --------- UpDown Header --------- */
#include <simupdown.h>
#include <dramalloc.hpp>
#include <basimupdown.h>
#include "compact_exe.hpp"

#define VALIDATE_RESULT

#define USAGE "USAGE: ./compact <gv_bin> <nl_bin> <num_lanes> <k>"

#define TOP_FLAG_OFFSET     0
#define HEAP_OFFSET 1600


typedef struct vertex{
    uint64_t *dests;
    uint64_t degree;
    uint64_t edges_before;
    uint64_t vertex_id;
    uint64_t real_deg; //32
    uint64_t scratch2; //40
    uint64_t scratch3; //48
    uint64_t scratch4; //56
} vertex_t;


uint64_t compact_cpu(uint64_t num_verts, vertex_t *g_v_bin, int k)
{
    uint64_t edges_before = 0;
    uint64_t num_empty = 0;
    for (uint64_t i = 0; i < num_verts; ++i) {
        g_v_bin[i].edges_before = edges_before;
        if (g_v_bin[i].real_deg < k) {
            g_v_bin[i].degree = 0;
            g_v_bin[i].real_deg = 0;
            num_empty++;
            continue;
        }
        uint64_t deg = 0;
        for(uint64_t j = 0; j < g_v_bin[i].degree; j++){
            uint64_t vid = g_v_bin[i].dests[j];
            // if(i == 0){
            //     printf("NV(%lu) = %lu, real_deg = %lu, new_deg = %lu, k = %lu\n", j, vid, g_v_bin[vid].real_deg, deg, k);
            // }
            if(g_v_bin[vid].real_deg >= k){
                g_v_bin[i].dests[deg] = vid;
                deg++;
            }
        }
        // if(g_v_bin[i].real_deg != deg){
        //     printf("error!\n");
        //     return 1;
        // }
        g_v_bin[i].degree = deg;
        edges_before += deg;
    }

    for (uint64_t i = 0; i < num_verts; ++i) {
        g_v_bin[i].real_deg = g_v_bin[i].degree;
    }
    return num_empty;
}



int main(int argc, char* argv[]) {
    /* Read file name and number of lanes from input, set up machine parameters*/
	if (argc < 5) {
		printf("Insufficient Input Params\n");
		printf("%s\n", USAGE);
		exit(1);
	}
	char* filename_gv = argv[1];
	char* filename_nl = argv[2];
	uint64_t num_lanes = atoi(argv[3]);
    uint64_t k = atoi(argv[4]);
	
	printf("Input File Name:%s , %s\n", filename_gv, filename_nl);
	printf("Num Lanes:%ld\n", num_lanes);
    fflush(stdout);

	// Set up machine parameters
	UpDown::ud_machine_t machine;
	//machine.MapMemSize = 1UL << 37; // 128GB
	//machine.GMapMemSize = 1UL << 37; // 128GB
	machine.MapMemSize = 1UL << 32; // 64GB
	machine.GMapMemSize = 1UL << 32; // 64GB
	machine.LocalMemAddrMode = 1;
	machine.NumLanes = num_lanes > 64 ? 64 : num_lanes;
	machine.NumUDs = std::ceil(num_lanes / 64.0) > 4 ? 4 : std::ceil(num_lanes / 64.0);
	machine.NumStacks = std::ceil(num_lanes / (64.0 * 4)) > 8 ? 8 : std::ceil(num_lanes / (64.0 * 4));
	machine.NumNodes = std::ceil(num_lanes / (64.0 * 4 * 8));

    /* if UpDown node == 1, dramalloc will map global memory to local memory */
	if(num_lanes <= 2048){
		machine.MapMemSize = 1UL << 32; // 64GB
		machine.GMapMemSize = 1UL << 32; // 4GB
	}

    uint64_t num_nodes = machine.NumNodes;
    printf("Number of Nodes: %lu\n", num_nodes);

    /* Load UpDown binary code */
	UpDown::BASimUDRuntime_t* rt = new UpDown::BASimUDRuntime_t(machine, "compact_exe.bin", 0, 100);
    
    /* Initialize DRAM memory allocator */
    dramalloc::DramAllocator *allocator = new dramalloc::DramAllocator(rt, compact_exe::DRAMalloc__global_broadcast /*eventlabel*/);

	fflush(stdout);


    /* ------------ Load Graph ------------*/
    printf("==== Loading Graph ====\n"); fflush(stdout);
    uint64_t blockSize = 1UL * 32 * 1024; // 32KB
    uint64_t num_edges=0, num_verts=0, nlist_size = 0;

    FILE* in_file_gv = fopen(filename_gv, "rb");
    if (!in_file_gv) {
            exit(EXIT_FAILURE);
    }
    FILE* in_file_nl = fopen(filename_nl, "rb");
    if (!in_file_nl) {
            exit(EXIT_FAILURE);
    }

    fseek(in_file_gv, 0, SEEK_SET);
    fseek(in_file_nl, 0, SEEK_SET);
    fread(&num_verts, sizeof(num_verts),1, in_file_gv);
    fread(&num_edges, sizeof(nlist_size), 1, in_file_gv);
    fread(&nlist_size, sizeof(nlist_size), 1, in_file_nl);

    uint64_t g_v_bin_size = num_verts * sizeof(vertex_t) + 8 * sizeof(uint64_t);
    uint64_t nlist_beg_size = nlist_size * sizeof(uint64_t);

    vertex_t *g_v_bin_global = reinterpret_cast<vertex_t *>(allocator->mm_malloc_global(g_v_bin_size, blockSize, num_nodes, 0));
    uint64_t* nlist_beg_global =  reinterpret_cast<uint64_t *>(allocator->mm_malloc_global(nlist_beg_size, blockSize, num_nodes, 0));

    #ifdef VALIDATE_RESULT
    vertex_t *g_v_bin = reinterpret_cast<vertex_t *>(rt->mm_malloc(g_v_bin_size));
    uint64_t *nlist_beg = reinterpret_cast<uint64_t *>(rt->mm_malloc(nlist_beg_size));
    #endif

    /* memory access require 64B align */
    /* Load gv_bin */
    uint64_t max_deg = 0;
    for(uint64_t i = 0; i < num_verts; i++){
	    // pointer to where vertex is stored in UpDown
        vertex_t* vert = reinterpret_cast<vertex_t *>(allocator->translate_udva2sa((uint64_t)&(g_v_bin_global[i]))); // compute vertex addr
	    // read individual vertices from file
        if(fread(vert, sizeof(vertex_t), 1, in_file_gv) == 0){
            fprintf(stderr, "Error reading vertex from %s\n", filename_gv);
            exit(EXIT_FAILURE);
        }
        uint64_t offset = reinterpret_cast<uint64_t>(vert->dests);
        uint64_t *loc_nlist = nlist_beg_global + offset;
        vert->dests = loc_nlist; // update neighbor ptr
       	vert->real_deg = vert->degree;
        vert->scratch2 = 0;
        vert->scratch3 = 0;
        vert->scratch4 = 0;
        if(max_deg < vert->degree){
            max_deg = vert->degree;
        }

        #ifdef VALIDATE_RESULT
        vertex_t* vert2 = &(g_v_bin[i]);
        vert2->dests = nlist_beg + offset;
        vert2->degree = vert->degree;
        vert2->edges_before = vert->edges_before;
        vert2->vertex_id = vert->vertex_id;
        vert2->real_deg = vert->real_deg;
        vert2->scratch2 = 0;
        vert2->scratch3 = 0;
        vert2->scratch4 = 0;
        #endif
        
    }
    fclose(in_file_gv);
    printf("==== Loading gv graph done ====\n"); fflush(stdout);

    // Load nl_bin
    uint64_t addr1 = reinterpret_cast<uint64_t>(nlist_beg_global);
    uint64_t addr1_end = addr1 + nlist_beg_size;
    #ifdef VALIDATE_RESULT
    uint64_t addr2 = reinterpret_cast<uint64_t>(nlist_beg);
    #endif
    // read from start to end of neighbor list
    // gv has been mapped to corresponding memory address of nl, but actual nl values are filled below:
    
    while(addr1 < addr1_end){
        uint64_t* sa1 = reinterpret_cast<uint64_t *>(allocator->translate_udva2sa(addr1));
        int64_t len = blockSize;
        if ((addr1 + len) > addr1_end) {
            len = addr1_end - addr1;
        }
        size_t to_read = len / sizeof(int64_t);
        if (fread(sa1, sizeof(int64_t), to_read, in_file_nl) != to_read) {
            fprintf(stderr, "Error reading neighbor list from %s\n", filename_nl);
            exit(EXIT_FAILURE);
        }
        // if(addr1 == reinterpret_cast<uint64_t>(nlist_beg_global)){
        //     printf("%lu %lu %lu %lu", sa1[0], sa1[1], sa1[2], sa1[3]);
        // }

        #ifdef VALIDATE_RESULT
        memcpy(reinterpret_cast<void *>(addr2), reinterpret_cast<void *>(sa1), len);
        addr2 = addr2 + len;
        #endif

        addr1 = addr1 + len;
    }
    fclose(in_file_nl);
    printf("==== Loading nl graph done ====\n"); fflush(stdout);
    printf("# vertices: %lu , # edges:%lu , avg deg: %lf, max deg: %lu, total edge size: %lu bytes\n", num_verts, num_edges, ((double)num_edges)/num_verts, max_deg, nlist_beg_size);
    fflush(stdout);

    // ------------------------ Start UpDown Program ------------------------
    int iters = 0;
    uint64_t sim_ticks_start = 0;
    uint64_t sim_ticks_end = 0;
    uint64_t num_verts_per_lane = (num_verts + num_lanes - 1) / num_lanes;
   
    UpDown::networkid_t nwid(0);
    UpDown::operands_t ops(6);
    ops.set_operand(0, num_lanes);
    ops.set_operand(1, g_v_bin_global);
    ops.set_operand(2, num_verts);
    ops.set_operand(3, num_verts_per_lane);
    ops.set_operand(4, 0);
    ops.set_operand(5, k);

    UpDown::event_t event(compact_exe::compact_master__start, nwid, UpDown::CREATE_THREAD, &ops); // generate start event

    UpDown::word_t flag = 0;
    rt->t2ud_memcpy(&flag, sizeof(UpDown::word_t), nwid, TOP_FLAG_OFFSET); // copy the value of flag to the scratchpad of NWID 0

    // start executing
    sim_ticks_start = rt->getSimTicks();
    rt->send_event(event);
    rt->start_exec(nwid);
    
    // wait until the value at address TOP_FLAG_OFFSET in network ID 0 becomes 1
    rt->test_wait_addr(nwid, TOP_FLAG_OFFSET, 1);
    sim_ticks_end = rt->getSimTicks();
    printf("Time: Start: %lu, End: %lu, Diff: %lu\n", sim_ticks_start, sim_ticks_end, sim_ticks_end - sim_ticks_start);
    uint64_t num_empty_updown;
    rt->ud2t_memcpy(&num_empty_updown, sizeof(UpDown::word_t), nwid, 8);

    
    #ifdef VALIDATE_RESULT
    // vertex_t* vert2 = &(g_v_bin[0]);
    // printf("Top     : degree = %lu, edges_before = %lu, vertex_id = %lu, real_deg = %lu\n", vert2->degree, vert2->edges_before, vert2->vertex_id, vert2->real_deg);
    uint64_t num_empty_cpu = compact_cpu(num_verts, g_v_bin, k);
    uint64_t j = 0;
    uint64_t* sa1 = NULL;
    for (uint64_t i = 0; i < num_verts; i++) {
        vertex_t* vert = reinterpret_cast<vertex_t *>(allocator->translate_udva2sa((uint64_t)&(g_v_bin_global[i])));
        vertex_t* vert2 = &(g_v_bin[i]);
        bool pass = true;
        if((vert2->degree != vert->degree) || (vert2->edges_before != vert->edges_before) || (vert2->vertex_id != vert->vertex_id) || (vert2->real_deg != vert->real_deg)){
            pass = false;
        }else{
            for(j = 0; j < vert->degree; j++){
                sa1 = reinterpret_cast<uint64_t *>(allocator->translate_udva2sa(reinterpret_cast<uint64_t>(&(vert->dests[j]))));
                bool find = false;
                for(int k = 0; k < vert->degree; k++){
                    if(sa1[0] == vert2->dests[k]){
                        find = true;
                        break;
                    }
                }
                if(!find){
                    pass = false;
                    break;
                }
            }
        }
        if (!pass) {
            printf("Top     : degree = %lu, edges_before = %lu, vertex_id = %lu, real_deg = %lu, N(%lu)[%lu] = %lu\n", vert2->degree, vert2->edges_before, vert2->vertex_id, vert2->real_deg, i, j, vert2->dests[j]);
            if(sa1 == NULL)
                printf("UpDown  : degree = %lu, edges_before = %lu, vertex_id = %lu, real_deg = %lu\n", vert->degree, vert->edges_before, vert->vertex_id, vert->real_deg);
            else
                printf("UpDown  : degree = %lu, edges_before = %lu, vertex_id = %lu, real_deg = %lu, N(%lu)[%lu] = %lu\n", vert->degree, vert->edges_before, vert->vertex_id, vert->real_deg, i, j, sa1[0]);
            printf("ERROR FINAL\n");
            return 1;
        }
    }
    if(num_empty_updown == num_empty_cpu){
        printf("Compact Finished (No Errors!)\n"); fflush(stdout);
    }else{
        printf("num_empty_updown (%lu) != num_empty_cpu (%lu)\n", num_empty_updown, num_empty_cpu); fflush(stdout);
    }
    #endif
    printf("Final K: %lu\n", k);
    
    return 0;
}
