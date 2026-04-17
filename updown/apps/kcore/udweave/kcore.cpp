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
#include "kcore_exe.hpp"

// #define VALIDATE_RESULT

#define USAGE "USAGE: ./kcore <gv_bin> <nl_bin> <num_lanes> <DifferencePercentForCompaction>"

#define TOP_FLAG_OFFSET     0
#define HEAP_OFFSET 1600


typedef struct vertex{
    uint64_t *dests;        // 0
    uint64_t degree;        // 8
    uint64_t edges_before;  // 16
    uint64_t vertex_id;     // 24
    uint64_t scratch1;      // 32 score
    uint64_t scratch2;      // 40 original score
    uint64_t scratch3;      // 48 iteration + 1
    uint64_t scratch4;      // 56
} vertex_t;

uint64_t* kcore_cpu(uint64_t num_verts, vertex_t *g_v_bin, int k)
{
    uint64_t *val = reinterpret_cast<uint64_t *>(malloc(num_verts * sizeof(uint64_t)));

    // Initialize current degree (scratch1) from original degree
    for (uint64_t i = 0; i < num_verts; ++i) {
	    val[i] = 0;
    }

    uint64_t k_iter = 1;
    while(k_iter < 60) {
	    for (uint64_t i = 0; i < num_verts; ++i) {
		    if (g_v_bin[i].degree < k_iter) {
			    g_v_bin[i].degree = 0;
		    }
	    }

	    // get actual degree
	    for (uint64_t i = 0; i < num_verts; ++i) {
		    if (g_v_bin[i].degree == 0) {
			    val[i] = 0;
			    continue;
		    }

		    // update updated degree in scratch1
		    for(uint64_t j=0; j<g_v_bin[i].degree; j++) {
			    uint64_t des_vid = g_v_bin[i].dests[j];
			    if (g_v_bin[des_vid].degree > 0) {
				    val[i] = val[i] + 1;
			    }
		    }
	    }

	    //delete all <k degrees
	    uint64_t num_empty = 0;
	    for(uint64_t i=0; i < num_verts; i++) {
		    if (g_v_bin[i].degree == 0) {
			    val[i] = 0;
			    ++num_empty;
			    continue;
		    }
		    if (val[i] > g_v_bin[i].degree) {
			    printf("ERROR\n");
			    return val;
		    }
		    if (val[i] < k_iter) {
			    ++num_empty;
			    g_v_bin[i].degree = 0;
			    val[i] = 0;
		    }
	    }
	    if (num_verts - num_empty == 0) {
		    break;
	    }
	    printf("K: %lu\n", k_iter);
	    printf("Nonempty: %lu\n", num_verts - num_empty);

	    // the end
	    for (uint64_t i = 0; i < num_verts; ++i) {
		    val[i] = 0;
	    }
	    ++k_iter;
    }

    return val;
}


size_t CopyGlobal2Local(dramalloc::DramAllocator *allocator, uint64_t chunck_size, uint64_t global_addr, uint64_t local_addr, uint64_t copy_size) {
  uint64_t current_copy_size = 0;
  uint64_t current_global_addr = global_addr;
  uint64_t current_local_addr = local_addr;
  while (current_copy_size < copy_size) {
    uint64_t size = chunck_size;
    if ((copy_size - current_copy_size) < size)
      size = copy_size - current_copy_size;
    void *current_global_addr_sa = allocator->translate_udva2sa(current_global_addr);
    memcpy(reinterpret_cast<void *>(current_local_addr), current_global_addr_sa, size);
    current_copy_size = current_copy_size + size;
    current_global_addr = current_global_addr + size;
    current_local_addr = current_local_addr + size;
  }
  return current_copy_size;
}

void compactGraph(dramalloc::DramAllocator *allocator, vertex_t* gv, uint64_t* nl, uint64_t num_verts, uint64_t* num_edges) {

    uint64_t new_num_edges = 0;
    for(uint64_t i=0; i<num_verts; i++) {
        vertex_t* vert = reinterpret_cast<vertex_t *>(allocator->translate_udva2sa((uint64_t)(gv + i)));
        if(vert->degree == 0) {
            vert->edges_before = new_num_edges;
            continue;
        }

        // Write remapped neighbors into nlDst
        uint64_t new_deg = 0;
        for(uint64_t j = 0; j < vert->degree; j++) {
            uint64_t* targetVID = reinterpret_cast<uint64_t *>(allocator->translate_udva2sa((uint64_t)(vert->dests + j)));
            vertex_t* targetVert = reinterpret_cast<vertex_t *>(allocator->translate_udva2sa((uint64_t)(gv + *targetVID)));

            // printf("NL ID: %lu, ID: %lu, Deg: %lu\n", *targetVID, targetVert->vertex_id, targetVert->degree);
            if(targetVert->degree != 0) {
                uint64_t* newVIDPtr = reinterpret_cast<uint64_t *>(allocator->translate_udva2sa((uint64_t)(vert->dests + new_deg)));
                *newVIDPtr = *targetVID;
                new_deg++;
            }
        }

        vert->degree = new_deg;
        vert->edges_before = new_num_edges;
        vert->scratch1 = 0;
        new_num_edges += new_deg;
    }

    *num_edges = new_num_edges;
}

void printData(dramalloc::DramAllocator *allocator, vertex_t* gv, uint64_t* nl, uint64_t num_verts) {
    printf("Vertices:\n");
    for(uint64_t i=0; i<num_verts; i++) {
        vertex_t* vert = reinterpret_cast<vertex_t *>(allocator->translate_udva2sa((uint64_t)(gv + i)));
        printf("ID: %lu, Deg: %lu, EdgesBefore: %lu, Offset: %p, S1: %lu, S2: %lu, S3: %lu, Neighbors: ", 
            vert->vertex_id, vert->degree, vert->edges_before, vert->dests,
            vert->scratch1, vert->scratch2, vert->scratch3);

        // for(uint64_t j=0; j<vert->degree; j++) {
        //     uint64_t* neighbor = reinterpret_cast<uint64_t *>(allocator->translate_udva2sa((uint64_t)(vert->dests + j)));
        //     printf("%lu ", *neighbor);
        // }
        printf("\n");
        fflush(stdout);
    }
}

void terminateUpDownThreads(UpDown::BASimUDRuntime_t* rt) {
    
    UpDown::networkid_t nwid(0);
    UpDown::word_t threadID;
    rt->ud2t_memcpy(&threadID, sizeof(UpDown::word_t), nwid, HEAP_OFFSET + 80);
    
    UpDown::operands_t ops(2);
    ops.set_operand(0, (UpDown::word_t)-1);
    
    UpDown::event_t event(kcore_exe::KCORE_MULTI_main__run_iter, nwid, threadID, &ops);
    UpDown::word_t flag = 0;
    rt->t2ud_memcpy(&flag, sizeof(UpDown::word_t), nwid, TOP_FLAG_OFFSET);
    rt->send_event(event);
    rt->start_exec(nwid);
    rt->test_wait_addr(nwid, TOP_FLAG_OFFSET, 1);
}

void initUDkCore(UpDown::BASimUDRuntime_t* rt, vertex_t* g_v_bin_global, uint64_t num_verts, 
                 uint64_t num_edges, uint64_t num_lanes, UpDown::word_t* threadID) {

    UpDown::networkid_t nwid(0);
    UpDown::operands_t ops(4);
    ops.set_operand(0, num_verts);
    ops.set_operand(1, num_edges);
    // important to note: vertices already point to neighbor list so nl_bin is not passed here
    ops.set_operand(2, g_v_bin_global);
    ops.set_operand(3, num_lanes);
    UpDown::event_t event(kcore_exe::KCORE_MULTI_main__start, nwid, UpDown::CREATE_THREAD, &ops); // generate start event

    UpDown::word_t flag = 0;
    rt->t2ud_memcpy(&flag, sizeof(UpDown::word_t), nwid, TOP_FLAG_OFFSET); // copy the value of flag to the scratchpad of NWID 0

    // start executing
    rt->send_event(event);
    rt->start_exec(nwid);
    
    // wait until the value at address TOP_FLAG_OFFSET in network ID 0 becomes 1
    rt->test_wait_addr(nwid, TOP_FLAG_OFFSET, 1);

    rt->ud2t_memcpy(threadID, sizeof(UpDown::word_t), nwid, HEAP_OFFSET + 80);
}

void runIterUDkCore(UpDown::BASimUDRuntime_t* rt, uint64_t num_lanes, UpDown::word_t threadID) {
    
    UpDown::networkid_t nwid(0);
    
    UpDown::word_t flag = 0;
    rt->t2ud_memcpy(&flag, sizeof(UpDown::word_t), nwid, TOP_FLAG_OFFSET);

    UpDown::operands_t ops(2);
    ops.set_operand(0, 0);
    UpDown::event_t event(kcore_exe::KCORE_MULTI_main__run_iter, nwid, threadID, &ops);


    // start executing
    rt->send_event(event);
    rt->start_exec(nwid);

    // wait until the value at address TOP_FLAG_OFFSET in network ID 0 becomes 1
    rt->test_wait_addr(nwid, TOP_FLAG_OFFSET, 1);
}


uint64_t markVerticesDeleted(UpDown::BASimUDRuntime_t* rt, vertex_t* g_v_bin_global, uint64_t num_verts, 
                         uint64_t k) {

    UpDown::networkid_t nwid(0);
    UpDown::word_t flag = 0;
    rt->t2ud_memcpy(&flag, sizeof(UpDown::word_t), nwid, TOP_FLAG_OFFSET);

    //MarkVertices::start(uint64_t* src, uint64_t k, uint64_t numVertices, uint64_t numLanes)
    UpDown::word_t num_lanes = rt->getMachineConfig().NumLanes * rt->getMachineConfig().NumUDs * rt->getMachineConfig().NumStacks * rt->getMachineConfig().NumNodes;
    UpDown::operands_t ops(4);
    ops.set_operand(0, (UpDown::word_t) g_v_bin_global);
    ops.set_operand(1, (UpDown::word_t) k);
    ops.set_operand(2, (UpDown::word_t) num_verts);
    ops.set_operand(3, (UpDown::word_t) num_lanes);

    UpDown::event_t event(kcore_exe::MarkVertices__start, nwid, UpDown::CREATE_THREAD, &ops);

    // start executing
    rt->send_event(event);
    rt->start_exec(nwid);

    // wait until the value at address TOP_FLAG_OFFSET in network ID 0 becomes 1
    rt->test_wait_addr(nwid, TOP_FLAG_OFFSET, 1);
    
    uint64_t num_empty;
    rt->ud2t_memcpy(&num_empty, sizeof(UpDown::word_t), nwid, HEAP_OFFSET + 64);
    
    const char label[] = "K";
    char result[16];
    snprintf(result, sizeof(result), "%s%lu", label, k);
    rt->db_write_stats(0, num_lanes, result);
    rt->db_write_node_stats(0, rt->getMachineConfig().NumNodes, result);
    rt->reset_node_stats();
    rt->reset_stats();
    
    return num_empty;
}


uint64_t startPrefixSum(UpDown::BASimUDRuntime_t* rt, vertex_t* g_v_bin_global, uint64_t num_verts) {

    UpDown::networkid_t nwid(0);
    UpDown::word_t flag = 0;
    rt->t2ud_memcpy(&flag, sizeof(UpDown::word_t), nwid, TOP_FLAG_OFFSET);

    //MarkVertices::start(uint64_t* src, uint64_t k, uint64_t numVertices, uint64_t numLanes)
    UpDown::word_t num_lanes = rt->getMachineConfig().NumLanes * rt->getMachineConfig().NumUDs * rt->getMachineConfig().NumStacks * rt->getMachineConfig().NumNodes;
    UpDown::operands_t ops(3);
    ops.set_operand(0, (UpDown::word_t) g_v_bin_global);
    ops.set_operand(1, (UpDown::word_t) num_verts);
    ops.set_operand(2, num_lanes);

    UpDown::event_t event(kcore_exe::PrefixSum__start, nwid, UpDown::CREATE_THREAD, &ops);

    // start executing
    rt->send_event(event);
    rt->start_exec(nwid);

    // wait until the value at address TOP_FLAG_OFFSET in network ID 0 becomes 1
    rt->test_wait_addr(nwid, TOP_FLAG_OFFSET, 1);
    
    uint64_t maxDegree;
    rt->ud2t_memcpy(&maxDegree, sizeof(UpDown::word_t), nwid, TOP_FLAG_OFFSET + sizeof(UpDown::word_t));
    
    rt->db_write_stats(0, num_lanes, "prefixSum");
    rt->db_write_node_stats(0, rt->getMachineConfig().NumNodes, "prefixSum");
    rt->reset_node_stats();
    rt->reset_stats();
    
    return maxDegree;
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
	uint64_t num_lanes = atol(argv[3]);
	
	printf("Input File Name: %s, %s\n", filename_gv, filename_nl);
	printf("Num Lanes: %ld\n", num_lanes);

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
		machine.MapMemSize = 1UL << 34; // 64GB
		machine.GMapMemSize = 1UL << 34; // 4GB
	}

    uint64_t num_nodes = machine.NumNodes;
    printf("Number of Nodes: %lu\n", num_nodes);

    /* Load UpDown binary code */
	UpDown::BASimUDRuntime_t* rt = new UpDown::BASimUDRuntime_t(machine, "kcore_exe.bin", 0, 100);
    
    /* Initialize DRAM memory allocator */
    dramalloc::DramAllocator *allocator = new dramalloc::DramAllocator(rt, kcore_exe::DRAMalloc__global_broadcast /*eventlabel*/);


    printf("=== Base Addresses ===\n");
    rt->dumpBaseAddrs();
    printf("\n=== Machine Config ===\n");
    rt->dumpMachineConfig();


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

    vertex_t* g_v_bin_global = reinterpret_cast<vertex_t *>(allocator->mm_malloc_global(g_v_bin_size, blockSize, num_nodes, 0));
    uint64_t* nlist_beg_global =  reinterpret_cast<uint64_t *>(allocator->mm_malloc_global(nlist_beg_size, blockSize, num_nodes, 0));

    assert(g_v_bin_global != nullptr && "Could not allocate memory for gv_bin!");
    assert(nlist_beg_global != nullptr && "Could not allocate memory for nlist_beg_global!");

    /* memory access require 64B align */
    /* Load gv_bin */

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
    }
    fclose(in_file_gv);
    printf("==== Loading gv graph done ====\n"); fflush(stdout);

    // printData(allocator, g_v_bin_global, nlist_beg_global, num_verts);

    uint64_t max_deg = startPrefixSum(rt, g_v_bin_global, num_verts);

    // for(uint64_t i = 0; i < num_verts; i++){
    //     // pointer to where vertex is stored in UpDown
    //     vertex_t* vert = reinterpret_cast<vertex_t *>(allocator->translate_udva2sa((uint64_t)&(g_v_bin_global[i]))); // compute vertex addr
    //     if(vert->edges_before != vert->scratch1 || vert->vertex_id != vert->scratch2) {
    //         printf("ERROR: vertex: %lu, deg: %lu, eb: %lu, s1: %lu, s2: %lu\n", vert->vertex_id, vert->degree, vert->edges_before, vert->scratch1, vert->scratch2);
    //     }
    // }

    // return 0;


    // Load nl_bin
    uint64_t addr1 = reinterpret_cast<uint64_t>(nlist_beg_global);
    uint64_t addr1_end = addr1 + nlist_beg_size;
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
        addr1 = addr1 + len;
    }
    fclose(in_file_nl);
    printf("==== Loading nl graph done ====\n");
    printf("# vertices: %lu, # edges: %lu, avg deg: %lf, max deg: %lu, total edge size: %lu bytes\n", num_verts, num_edges, ((double)num_edges)/num_verts, max_deg, nlist_beg_size);
    const uint64_t compactAfterMarkingNumVertices = ceil((num_verts * atol(argv[4])) / 100.0);
    printf("Compacting after %lu vertices are marked for deletion.\n", compactAfterMarkingNumVertices);

    fflush(stdout);

    // ------------------------ Start UpDown Program ------------------------
    
    uint64_t num_next_compact = compactAfterMarkingNumVertices;
    bool runInit = true;
    uint64_t sim_ticks_start;
    UpDown::word_t threadID;
    uint64_t traversedEdges = 0;

    uint64_t k;
    for(k=1; k<=max_deg; k++) {
        uint64_t sim_ticks_start = rt->getSimTicks();
        // delete all <k degrees
        // uint64_t markVerticesDeleted(UpDown::BASimUDRuntime_t* rt, vertex_t* g_v_bin_global, uint64_t num_verts, uint64_t k)
        uint64_t num_empty = markVerticesDeleted(rt, g_v_bin_global, num_verts, k);
        printf("K: %lu, vertices: %lu, marked: %lu, active: %lu\n", k, num_verts, num_empty, (num_verts-num_empty));
        
        if ((num_verts - num_empty) < k) {
            k = k - 1;
            break;
        }

        // For statistics only
        // Determine the number of egdes to traverse
        for(uint64_t i=0; i<num_verts; i++) {
            vertex_t* vert = reinterpret_cast<vertex_t *>(allocator->translate_udva2sa((uint64_t)(g_v_bin_global + i)));
            traversedEdges += vert->degree; // degree = 0, when marked deleted.
        }

        // update egdes and degrees, since vertices have been deleted
        if(runInit) {
            initUDkCore(rt, g_v_bin_global, num_verts, num_edges, num_lanes, &threadID);
            runInit = false;
        } else {
            runIterUDkCore(rt, num_lanes, threadID);
        }


        

        if(num_empty > num_next_compact) {
            runInit = true; // run the init next
            num_next_compact += compactAfterMarkingNumVertices;
            terminateUpDownThreads(rt);
            // printData(allocator, g_v_bin_global, nlist_beg_global, num_verts);
            compactGraph(allocator, g_v_bin_global, nlist_beg_global, num_verts, &num_edges);
            // printData(allocator, g_v_bin_global, nlist_beg_global, num_verts);
        }
        uint64_t sim_ticks_end = rt->getSimTicks();
        printf("Time: Start: %lu, End: %lu, Diff: %lu\n", sim_ticks_start, sim_ticks_end, sim_ticks_end - sim_ticks_start);
    }
    printf("K-Core Finished (No Errors!)\n"); fflush(stdout);
    printf("Final K: %lu\n", k);
    printf("traversedEdges: %lu\n", traversedEdges);


    
    #ifdef VALIDATE_RESULT
        vertex_t *g_v_bin = reinterpret_cast<vertex_t *>(rt->mm_malloc(g_v_bin_size));
        uint64_t *nlist_beg = reinterpret_cast<uint64_t *>(rt->mm_malloc(nlist_beg_size));
        // -------------------------- Copy for global to local memory -----------------------
        CopyGlobal2Local(allocator, blockSize, (uint64_t)g_v_bin_global, (uint64_t)g_v_bin, g_v_bin_size);
        CopyGlobal2Local(allocator, blockSize, (uint64_t)nlist_beg_global, (uint64_t)nlist_beg, nlist_beg_size);
        uint64_t offset = nlist_beg - nlist_beg_global;
        for(uint64_t i = 0; i < num_verts; i++){
            g_v_bin[i].dests = g_v_bin[i].dests + offset;
        }
        uint64_t *correct = kcore_cpu(num_verts, g_v_bin, 60);
        uint64_t max_degree_check = 0;
        for (uint64_t i = 0; i < num_verts; i++) {
        	// scratch1 is the updated degree
        	uint64_t scratch1 = g_v_bin[i].scratch1;
        	if (max_degree_check < scratch1) {
        		max_degree_check = scratch1;
        	}
        	if (g_v_bin[i].degree == 0) {
        		continue;
        	}
        	if (scratch1 != correct[i]) {
        		printf("UpDown  : %ld\n", scratch1);
        		printf("TopCode : %lu\n", correct[i]);
        		printf("Degree  : %lu\n", g_v_bin[i].degree);
        		printf("K       : %lu (Scratch4)\n", g_v_bin[i].scratch4);
        		printf("ERROR FINAL\n");
        		return 1;
        	}
        }
    
        printf("K-Core Finished (No Errors!)\n"); fflush(stdout);
        printf("Max Degree: %lu\n", max_degree_check);
        printf("Final K: %lu\n", k);
    #endif
    return 0;
}
