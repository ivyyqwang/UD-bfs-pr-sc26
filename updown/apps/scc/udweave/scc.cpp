#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cmath>
#include <sys/types.h>
#include <sys/time.h>
#include <bit>
#include <cstdint>
#include <vector>
#include <unordered_set>
#include <iostream>


/* --------- UpDown Header --------- */
#include <simupdown.h>
#include <dramalloc.hpp>
#include <basimupdown.h>
#include "scc_exe.hpp"

#define VALIDATE_RESULT

#define USAGE "USAGE: ./scc <gv_bin> <nl_bin> <num_lanes>"

#define TOP_FLAG_OFFSET     0
#define HEAP_OFFSET 1600



typedef struct vertex {
    uint64_t *dests;        // Neighbor list // 0 // In Edges of the node
    uint64_t degree;        // 8
    uint64_t edges_before;  // 16
    uint64_t vertex_id;     // 24

    uint64_t color;         // 32 color = -1 -> vertex has been deleted
    uint64_t scc;           // 40
    uint64_t unused0;       // 48 (padding)
    uint64_t unused1;  
} vertex_t;



uint64_t* deleted_init;


std::string make_T_filename(const char* original, const char* marker_suffix)
{
    std::string s(original);
    std::string suffix(marker_suffix);

    auto pos = s.rfind(suffix);
    if (pos == std::string::npos) {
        std::cerr << "ERROR: cannot find suffix '" << suffix
                  << "' in filename '" << s << "'\n";
        std::exit(1);
    }

    s.insert(pos, "_T");
    return s;
}


void printGraph(dramalloc::DramAllocator *allocator, vertex_t* gv, uint64_t* nl, uint64_t num_verts) {
    
    return; // For debugging: Easy deactivation

    printf("Vertices:\n");
    for(uint64_t i=0; i<num_verts; i++) {
        vertex_t* vert = reinterpret_cast<vertex_t *>(allocator->translate_udva2sa((uint64_t)(gv + i)));
        printf("ID: %lu, edge: %p, deg: %lu, eBef: %lu, color: %ld, scc: %ld, E: ", 
            vert->vertex_id, vert->dests, vert->degree, vert->edges_before, 
            vert->color, vert->scc
        );

        for(uint64_t j=0; j<vert->degree; j++) {
            uint64_t* neighbor = reinterpret_cast<uint64_t *>(allocator->translate_udva2sa((uint64_t)&(vert->dests[j])));
            printf("%lu ", *neighbor);
        }
        printf("\n");
        fflush(stdout);
    }
}

void printGraphCPU(std::vector<vertex_t> &gv) {

    return; // For debugging: Easy deactivation

    for(auto &v : gv) {
        printf("id: %lu, deg: %lu, edgesBefore: %lu, color: %ld, scc: %ld", v.vertex_id, v.degree, v.edges_before, v.color, v.scc);
        
        printf(", E: ");
        uint64_t* edges = v.dests;
        for(uint64_t e=0; e<v.degree; e++) {
            vertex_t &n = gv[edges[e]];
            printf("%lu ", n.vertex_id);
        }
        printf("\n");
    }
}


/**
 * Copy the color and SCC ID from gvSrc to gvDst
 */
void copyData(UpDown::BASimUDRuntime_t *rt, vertex_t* gvSrc, vertex_t* gvDst, uint64_t num_verts) {
    UpDown::networkid_t nwid(0);
    
    UpDown::operands_t ops(4);
    ops.set_operand(0, (UpDown::word_t)gvSrc);
    ops.set_operand(1, (UpDown::word_t)gvDst);
    ops.set_operand(2, (UpDown::word_t)num_verts);
    ops.set_operand(3, (UpDown::word_t)rt->getMachineConfig().NumNodes * 2048);
    
    UpDown::event_t event(scc_exe::CopyData__start, nwid, UpDown::CREATE_THREAD, &ops);
    UpDown::word_t flag = 0;
    rt->t2ud_memcpy(&flag, sizeof(UpDown::word_t), nwid, TOP_FLAG_OFFSET);
    rt->send_event(event);
    rt->start_exec(nwid);
    rt->test_wait_addr(nwid, TOP_FLAG_OFFSET, 1);
}


/**
 * Mark all vertices whose color = -1 and degree != as deleted (sets degree = 0)
 */
void markVerticesDeleted(UpDown::BASimUDRuntime_t *rt, vertex_t* gvSrc0, vertex_t* gvSrc1,vertex_t* gvSrcT, uint64_t num_verts, uint64_t* verticesleft, uint64_t* verticesDeleted, uint64_t* verticesIgnored) {
    UpDown::networkid_t nwid(0);
    
    UpDown::operands_t ops(5);
    ops.set_operand(0, (UpDown::word_t)gvSrc0);
    ops.set_operand(1, (UpDown::word_t)gvSrc1);
    ops.set_operand(2, (UpDown::word_t)gvSrcT);
    ops.set_operand(3, (UpDown::word_t)num_verts);
    ops.set_operand(4, (UpDown::word_t)rt->getMachineConfig().NumNodes * 2048);
    
    UpDown::event_t event(scc_exe::DeleteVertices__start, nwid, UpDown::CREATE_THREAD, &ops);
    UpDown::word_t flag = 0;
    rt->t2ud_memcpy(&flag, sizeof(UpDown::word_t), nwid, TOP_FLAG_OFFSET);
    rt->send_event(event);
    rt->start_exec(nwid);
    rt->test_wait_addr(nwid, TOP_FLAG_OFFSET, 1);

    rt->ud2t_memcpy(verticesleft, sizeof(UpDown::word_t), nwid, TOP_FLAG_OFFSET + 8);
    rt->ud2t_memcpy(verticesDeleted, sizeof(UpDown::word_t), nwid, TOP_FLAG_OFFSET + 16);
    rt->ud2t_memcpy(verticesIgnored, sizeof(UpDown::word_t), nwid, TOP_FLAG_OFFSET + 24);
}

void copyAndMarkVerticesDeletedCPU(std::vector<vertex_t> &gv, std::vector<vertex_t> &gvT, uint64_t *verticesLeft, uint64_t* verticesDeleted, uint64_t *verticesIgnored) {

    // Algorithm:
    //    Mark vertices as deleted in gvT and gv
    //    copy the scc information from gvT to gv
    //    reset the color for all vertices that are not in an SCC yet
    *verticesLeft = 0;
    *verticesDeleted = 0;
    *verticesIgnored = 0;

    for(uint64_t i=0; i<gv.size(); i++) {
        gv[i].color = gvT[i].color;
        gv[i].scc   = gvT[i].scc;

        // Mark vertex as deleted
        if(gv[i].color == -1 && gv[i].degree != 0) {
            gv[i].degree = 0;
            (*verticesDeleted)++;
        }
        if(gvT[i].color == -1 && gvT[i].degree != 0) {
            gvT[i].degree = 0;
        }

        // Reset the color
        if(gv[i].degree != 0) {
            gv[i].color = gv[i].vertex_id;
            (*verticesLeft)++;
        } else {
            (*verticesIgnored)++;
        }
        if(gvT[i].degree != 0) {
            gvT[i].color = gvT[i].vertex_id;
        }
    }
}


/**
 * Copies vertices from gvSrc to gvDst.
 * Essentially a memcopy over the entire vertex array.
 */
void initVertices(UpDown::BASimUDRuntime_t *rt, vertex_t* gvSrc, vertex_t* gvDst, uint64_t num_verts) {
    UpDown::networkid_t nwid(0);
    
    UpDown::operands_t ops(4);
    ops.set_operand(0, (UpDown::word_t)gvSrc);
    ops.set_operand(1, (UpDown::word_t)gvDst);
    ops.set_operand(2, (UpDown::word_t)num_verts);
    ops.set_operand(3, (UpDown::word_t)rt->getMachineConfig().NumNodes * 2048);
    
    UpDown::event_t event(scc_exe::InitVertices__start, nwid, UpDown::CREATE_THREAD, &ops);
    UpDown::word_t flag = 0;
    rt->t2ud_memcpy(&flag, sizeof(UpDown::word_t), nwid, TOP_FLAG_OFFSET);
    rt->send_event(event);
    rt->start_exec(nwid);
    rt->test_wait_addr(nwid, TOP_FLAG_OFFSET, 1);
}


/**
 * Finds all vertices, which have color == vertexID && degree != 0 && color != -1
 */
void findVerticesOfSameColor(UpDown::BASimUDRuntime_t *rt, vertex_t* gv, uint64_t num_verts) {
    UpDown::networkid_t nwid(0);
    
    UpDown::operands_t ops(3);
    ops.set_operand(0, (UpDown::word_t)gv);
    ops.set_operand(1, (UpDown::word_t)num_verts);
    ops.set_operand(2, (UpDown::word_t)rt->getMachineConfig().NumNodes * 2048);
    
    UpDown::event_t event(scc_exe::FindVerticesOfSameColor__start, nwid, UpDown::CREATE_THREAD, &ops);
    UpDown::word_t flag = 0;
    rt->t2ud_memcpy(&flag, sizeof(UpDown::word_t), nwid, TOP_FLAG_OFFSET);
    rt->send_event(event);
    rt->start_exec(nwid);
    rt->test_wait_addr(nwid, TOP_FLAG_OFFSET, 1);
}

/**
 * Terminates all threads from the load balancing framework.
 */
void terminateUpDownThreads(UpDown::BASimUDRuntime_t* rt) {
    
    UpDown::networkid_t nwid(0);
    UpDown::word_t threadID;
    rt->ud2t_memcpy(&threadID, sizeof(UpDown::word_t), nwid, HEAP_OFFSET + 80);
    
    UpDown::operands_t ops(2);
    ops.set_operand(0, (UpDown::word_t)-1);
    
    UpDown::event_t event(scc_exe::Coloring_MULTI_main__run_iter, nwid, threadID, &ops);
    UpDown::word_t flag = 0;
    rt->t2ud_memcpy(&flag, sizeof(UpDown::word_t), nwid, TOP_FLAG_OFFSET);
    rt->send_event(event);
    rt->start_exec(nwid);
    rt->test_wait_addr(nwid, TOP_FLAG_OFFSET, 1);
}

/**
 * Computes the edges_before field of the vertex_t struct, which is the prefix sum of
 * the vertex' degrees before.
 */
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

    UpDown::event_t event(scc_exe::PrefixSum__start, nwid, UpDown::CREATE_THREAD, &ops);

    // start executing
    rt->send_event(event);
    rt->start_exec(nwid);

    // wait until the value at address TOP_FLAG_OFFSET in network ID 0 becomes 1
    rt->test_wait_addr(nwid, TOP_FLAG_OFFSET, 1);
    
    uint64_t maxDegree;
    rt->ud2t_memcpy(&maxDegree, sizeof(UpDown::word_t), nwid, TOP_FLAG_OFFSET + sizeof(UpDown::word_t));
    
    // rt->db_write_stats(0, num_lanes, "prefixSum");
    // rt->db_write_node_stats(0, rt->getMachineConfig().NumNodes, "prefixSum");
    // rt->reset_node_stats();
    // rt->reset_stats();
    
    return maxDegree;
}


void runColoringIteration(UpDown::BASimUDRuntime_t* rt, vertex_t* gvSrc, 
                            vertex_t* gvDst, 
                            uint64_t num_verts, uint64_t num_edges,
                            uint64_t* num_vertices_updated, uint64_t* num_vertices_visited) {


    uint64_t num_lanes = rt->getMachineConfig().NumNodes * rt->getMachineConfig().NumStacks * rt->getMachineConfig().NumUDs * rt->getMachineConfig().NumLanes;
    UpDown::networkid_t nwid(0);
    UpDown::operands_t ops(5);
    ops.set_operand(0, num_verts);
    ops.set_operand(1, num_edges);
    ops.set_operand(2, gvSrc);
    ops.set_operand(3, gvDst);
    ops.set_operand(4, num_lanes);
    UpDown::event_t event(scc_exe::Coloring_MULTI_main__start, nwid, UpDown::CREATE_THREAD, &ops);
    UpDown::word_t flag = 0;

    rt->t2ud_memcpy(&flag, sizeof(UpDown::word_t), nwid, TOP_FLAG_OFFSET);

    // printf("target: %p, source: %p, g_v_bin_global0: %p, g_v_bin_global1: %p\nGV0\n", g_v_bin_global_target, g_v_bin_global, g_v_bin_global0, g_v_bin_global1);
    // printGraph(allocator, g_v_bin_global0, nlist_beg_global, num_verts);

    // printf("target: %p, source: %p, g_v_bin_global0: %p, g_v_bin_global1: %p\nGV1\n", g_v_bin_global_target, g_v_bin_global, g_v_bin_global0, g_v_bin_global1);
    // printGraph(allocator, g_v_bin_global1, nlist_beg_global, num_verts);

    // start executing
    rt->send_event(event);
    rt->start_exec(nwid);
    rt->test_wait_addr(nwid, TOP_FLAG_OFFSET, 1);

    rt->ud2t_memcpy(num_vertices_updated, sizeof(uint64_t), nwid, HEAP_OFFSET + 64);

    *num_vertices_visited = *num_vertices_updated >> 32;
    *num_vertices_updated = (*num_vertices_updated << 32) >> 32;
}

uint64_t runColoringCPU(std::vector<vertex_t> &gv) {
    uint64_t iters = 0;
    uint64_t edgesTraversed = 0;

    bool hasChanged;
    do {
        hasChanged = false;

        // Algorithm:
        //    Walk through all the edges of a vertex
        //    Check the neighboring vertex
        //    If vertex is not deleted (color = -1)
        //       Adopt the color if color(neighbor) > color(thisVertex)
        //    Start at the beginning until convergence is achieved

        for(auto &v : gv) {
            if(v.color == -1) {
                continue;
            }

            uint64_t* edges = v.dests;
            for(uint64_t e=0; e<v.degree; e++) {
                edgesTraversed++;
                vertex_t &n = gv[edges[e]];

                if(n.color != -1 && n.color > v.color) {
                    v.color = n.color;
                    hasChanged = true;
                }
            }
        }

        // printf("Iteration %lu:\n", iters);
        // printGraphCPU(gv);
        iters++;
    } while(hasChanged);
    return edgesTraversed;
}


bool compareGraphs(dramalloc::DramAllocator *allocator, vertex_t* upDownGV, std::vector<vertex_t> &cpuGV) {


    for(uint64_t i=0; i<cpuGV.size(); i++) {
        vertex_t* updownVert = reinterpret_cast<vertex_t *>(allocator->translate_udva2sa((uint64_t)&(upDownGV[i])));

        if(updownVert->color != cpuGV[i].color || updownVert->scc != cpuGV[i].scc ||
           updownVert->degree != cpuGV[i].degree) {
            printf("Missmatch found!\nUpDown Vertex:\n");
            printf("\tid: %lu, deg: %lu, edgesBefore: %lu, color: %lu, scc: %lu\n", 
                    updownVert->vertex_id, updownVert->degree, updownVert->edges_before, updownVert->color, updownVert->scc);

            printf("CPU Vertex:\n");
            printf("\tid: %lu, deg: %lu, edgesBefore: %lu, color: %lu, scc: %lu\n", 
                    cpuGV[i].vertex_id, cpuGV[i].degree, cpuGV[i].edges_before, cpuGV[i].color, cpuGV[i].scc);
            return false;
        }
    }
    printf("Graphs equal\n");
    return true;
}

uint64_t runBFSIteration(UpDown::BASimUDRuntime_t* rt, vertex_t* gvSrc, 
                            vertex_t* gvDst, 
                            uint64_t num_verts, uint64_t num_edges,
                            bool init,
                            uint64_t* num_vertices_updated, uint64_t* num_vertices_visited) {


    uint64_t num_lanes = rt->getMachineConfig().NumNodes * rt->getMachineConfig().NumStacks * rt->getMachineConfig().NumUDs * rt->getMachineConfig().NumLanes;
    UpDown::networkid_t nwid(0);
    UpDown::word_t flag = 0;
    UpDown::operands_t ops(5);
    UpDown::event_t event;
    if(init) {
        ops.set_operand(0, num_verts);
        ops.set_operand(1, num_edges);
        ops.set_operand(2, gvSrc);
        ops.set_operand(3, gvDst);
        ops.set_operand(4, num_lanes);
        event = UpDown::event_t(scc_exe::BFS_LB_main__start, nwid, UpDown::CREATE_THREAD, &ops);
    } else {
        UpDown::word_t threadID;
        rt->ud2t_memcpy(&threadID, sizeof(UpDown::word_t), nwid, HEAP_OFFSET + 80);
        ops.set_operand(0, 0);
        event = UpDown::event_t(scc_exe::BFS_LB_main__run_iter, nwid, threadID, &ops);
    }


    rt->t2ud_memcpy(&flag, sizeof(UpDown::word_t), nwid, TOP_FLAG_OFFSET);

    // printf("target: %p, source: %p, g_v_bin_global0: %p, g_v_bin_global1: %p\nGV0\n", g_v_bin_global_target, g_v_bin_global, g_v_bin_global0, g_v_bin_global1);
    // printGraph(allocator, g_v_bin_global0, nlist_beg_global, num_verts);

    // printf("target: %p, source: %p, g_v_bin_global0: %p, g_v_bin_global1: %p\nGV1\n", g_v_bin_global_target, g_v_bin_global, g_v_bin_global0, g_v_bin_global1);
    // printGraph(allocator, g_v_bin_global1, nlist_beg_global, num_verts);

    /////////////////////////////
    uint64_t sim_ticks_start = rt->getSimTicks();
    // start executing
    rt->send_event(event);
    rt->start_exec(nwid);
    rt->test_wait_addr(nwid, TOP_FLAG_OFFSET, 1);

    rt->ud2t_memcpy(num_vertices_updated, sizeof(uint64_t), nwid, HEAP_OFFSET + 64);

    *num_vertices_visited = *num_vertices_updated >> 32;
    *num_vertices_updated = (*num_vertices_updated << 32) >> 32;

    return sim_ticks_start - rt->getSimTicks();
}


uint64_t runBFSCPU(std::vector<vertex_t> &gv, std::vector<vertex_t> &gvT) {
    uint64_t edgesTraversed = 0;
    uint64_t iters = 0;

    // initialize
    // copy the colors from the normal graph
    for(uint64_t i=0; i<gv.size(); i++) {
        gvT[i].color = gv[i].color;

        // set all vertices whose color == scc to visited
        // (Identifying root vertices)
        if(gvT[i].color == gvT[i].vertex_id) {
            gvT[i].scc = gvT[i].color;
            gvT[i].color = -1;
        }
    }

    bool hasChanged;
    do {
        hasChanged = false;

        // Algorithm:
        //    Walk through all the edges of a vertex
        //    Continue from the top, if this vertex has been visited/deleted (color = -1)
        //    Otherwise, check the neighboring vertex
        //    If neighbor has been visited/deleted (color = -1) and neighbor sccID == this vertex color
        //       Copy color to sccID
        //       Mark this vertex as visited (set color = -1)
        //    Start at the beginning until convergence is achieved

        for(auto &v : gvT) {
            if(v.color == -1) {
                continue;
            }

            uint64_t* edges = v.dests;
            for(uint64_t e=0; e<v.degree; e++) {
                vertex_t &n = gvT[edges[e]];
                edgesTraversed++;

                if(n.color == -1 && n.scc == v.color) {
                    v.scc = v.color;
                    v.color = -1;
                    hasChanged = true;
                }
            }
        }

        printf("Iteration %lu:\n", iters);
        printGraphCPU(gvT);
        iters++;

    } while(hasChanged);
    return edgesTraversed;
}



void loadGV(dramalloc::DramAllocator *allocator, FILE* inFile, vertex_t* target, uint64_t* nlist, uint64_t num_verts) {
    for(uint64_t i = 0; i < num_verts; i++){
        // You need to copy from updown to top code.
        vertex_t* vert0 = reinterpret_cast<vertex_t *>(allocator->translate_udva2sa((uint64_t)&(target[i]))); // compute vertex addr
        if(fread(vert0, sizeof(vertex_t), 1, inFile) == 0){
            fprintf(stderr, "Error reading vertex\n");
            exit(EXIT_FAILURE);
        }
        uint64_t offset = reinterpret_cast<uint64_t>(vert0->dests);
        uint64_t *loc_nlist = nlist + offset;
        vert0->dests = loc_nlist; // update neighbor ptr
    }
}


void loadGVCPU(FILE* inFile, std::vector<vertex_t> &gv, std::vector<uint64_t> &nlist) {
    for(uint64_t i = 0; i < gv.size(); i++){
        if(fread(&(gv[i]), sizeof(vertex_t), 1, inFile) == 0) {
            fprintf(stderr, "Error reading vertex\n");
            exit(EXIT_FAILURE);
        }
        uint64_t *loc_nlist = nlist.data() + reinterpret_cast<uint64_t>(gv[i].dests);
        gv[i].dests = loc_nlist; // update neighbor ptr
        gv[i].scc = -1;
        gv[i].color = gv[i].vertex_id;

        // printf("id: %lu, deg: %lu, edgesBefore: %lu, color: %lu, scc: %lu\n", gv[i].vertex_id, gv[i].degree, gv[i].edges_before, gv[i].color, gv[i].scc);
    }
}

void loadNL(dramalloc::DramAllocator *allocator, FILE* inFile, uint64_t* nlist, uint64_t nlist_size, uint64_t blockSize) {
    uint64_t addr1 = reinterpret_cast<uint64_t>(nlist);
    uint64_t addr1_end = addr1 + nlist_size;
    while(addr1 < addr1_end){
        uint64_t* sa1 = reinterpret_cast<uint64_t *>(allocator->translate_udva2sa(addr1));
        int64_t len = blockSize;
        if ((addr1 + len) > addr1_end) {
            len = addr1_end - addr1;
        }
        size_t to_read = len / sizeof(int64_t);
        if (fread(sa1, sizeof(int64_t), to_read, inFile) != to_read) {
            fprintf(stderr, "Error reading neighbor list\n");
            exit(EXIT_FAILURE);
        }
        addr1 = addr1 + len;
    }
}

void loadNLCPU(FILE* inFile, std::vector<uint64_t> &nlist) {
    if(fread(nlist.data(), sizeof(uint64_t), nlist.size(), inFile) == 0){
        fprintf(stderr, "Error reading vertex\n");
        exit(EXIT_FAILURE);
    }
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



int main(int argc, char* argv[]) {
    /* Read file name and number of lanes from input, set up machine parameters*/
	if (argc < 4) {
		printf("Insufficient Input Params\n");
		printf("%s\n", USAGE);
		exit(1);
	}
	char* filename_gv = argv[1];
	char* filename_nl = argv[2];
	uint64_t num_lanes = atoi(argv[3]);
	
	printf("Input File Name:%s , %s\n", filename_gv, filename_nl);
	printf("Num Lanes: %ld\n", num_lanes);
    fflush(stdout);

	// Set up machine parameters
	UpDown::ud_machine_t machine;
	machine.MapMemSize = 1UL << 32; // 128GB
	machine.GMapMemSize = 1UL << 32; // 128GB
	machine.LocalMemAddrMode = 1;
	machine.NumLanes = num_lanes > 64 ? 64 : num_lanes;
	machine.NumUDs = std::ceil(num_lanes / 64.0) > 4 ? 4 : std::ceil(num_lanes / 64.0);
	machine.NumStacks = std::ceil(num_lanes / (64.0 * 4)) > 8 ? 8 : std::ceil(num_lanes / (64.0 * 4));
	machine.NumNodes = std::ceil(num_lanes / (64.0 * 4 * 8));

    /* if UpDown node == 1, dramalloc will map global memory to local memory */
	if(num_lanes <= 2048){
		machine.MapMemSize = 1UL << 32; // 256GB
		machine.GMapMemSize = 1UL << 32; // 4GB
	}

    uint64_t num_nodes = machine.NumNodes;

    /* Load UpDown binary code */
	UpDown::BASimUDRuntime_t* rt = new UpDown::BASimUDRuntime_t(machine, "scc_exe.bin", 0, 100);
    
    /* Initialize DRAM memory allocator */
    dramalloc::DramAllocator *allocator = new dramalloc::DramAllocator(rt, scc_exe::DRAMalloc__global_broadcast /*eventlabel*/);

	fflush(stdout);


    /* ------------ Load Graph ------------*/
    printf("==== Loading Graph ====\n"); fflush(stdout);
    uint64_t blockSize = 1UL * 32 * 1024; // 32KB
    uint64_t num_edges=0, num_verts=0, nlist_size = 0;

    FILE* in_file_gv = fopen(filename_gv, "rb");
    FILE* in_file_nl = fopen(filename_nl, "rb");
    if (!in_file_gv || !in_file_nl) {
        printf("Error opening files");
        exit(EXIT_FAILURE);
    }

    fseek(in_file_gv, 0, SEEK_SET);
    fseek(in_file_nl, 0, SEEK_SET);
    fread(&num_verts, sizeof(num_verts), 1, in_file_gv);
    fread(&num_edges, sizeof(num_edges), 1, in_file_gv);
    fread(&nlist_size, sizeof(nlist_size), 1, in_file_nl);

    uint64_t g_v_bin_size = num_verts * sizeof(vertex_t) + 8 * sizeof(uint64_t);
    uint64_t nlist_beg_size = nlist_size * sizeof(uint64_t);

    vertex_t *g_v_bin_global0 = reinterpret_cast<vertex_t *>(allocator->mm_malloc_global(g_v_bin_size, blockSize, num_nodes, 0));
    vertex_t *g_v_bin_global1 = reinterpret_cast<vertex_t *>(allocator->mm_malloc_global(g_v_bin_size, blockSize, num_nodes, 0));
    uint64_t* nlist_beg_global = reinterpret_cast<uint64_t *>(allocator->mm_malloc_global(nlist_beg_size, blockSize, num_nodes, 0));
    
    assert(g_v_bin_global0 && "Could not allocate memory for the vertices (0)!");
    assert(g_v_bin_global1 && "Could not allocate memory for the vertices (1)!");
    assert(nlist_beg_global && "Could not allocate memory for the edge list!");
    vertex_t* g_v_bin_global = g_v_bin_global0;
    vertex_t* g_v_bin_global_target = g_v_bin_global1;
    

    deleted_init = (uint64_t*)malloc(num_verts * sizeof(uint64_t));
    assert(deleted_init && "Could not assign memory to mark deleted vertices!");
    


    printf("Loading vertices...\n");
    // loadGV(dramalloc::DramAllocator *allocator, FILE* inFile, vertex_t* target, vertex_t* target2, uint64_t* nlist_beg_global, uint64_t num_verts) {
    loadGV(allocator, in_file_gv, g_v_bin_global0, nlist_beg_global, num_verts);
    uint64_t max_deg = startPrefixSum(rt, g_v_bin_global0, num_verts);
    // Initialize the second array (write all the data from gv_bin_global0 to gv_bin_global1)
    initVertices(rt, g_v_bin_global0, g_v_bin_global1, num_verts);

    printf("done\n");
    


    printf("Loading neighbor list... ");
    // void loadNL(dramalloc::DramAllocator *allocator, FILE* inFile, uint64_t* nlist, uint64_t nlist_size, uint64_t blockSize) {
    loadNL(allocator, in_file_nl, nlist_beg_global, nlist_beg_size, blockSize);
    printf("done\n");
    
    printf("# vertices: %lu, # edges: %lu, avg deg: %lf, max deg: %lu, total edge size: %lu bytes\n", num_verts, num_edges, ((double)num_edges)/num_verts, max_deg, nlist_beg_size);

    printGraph(allocator, g_v_bin_global0, nlist_beg_global, num_verts);

    #ifdef VALIDATE_RESULT
        std::vector<vertex_t> gvValidate(num_verts);
        std::vector<uint64_t> nlValidate(nlist_size);
        fseek(in_file_gv, sizeof(num_edges)+sizeof(num_verts), SEEK_SET);
        fseek(in_file_nl, sizeof(nlist_size), SEEK_SET);
        loadGVCPU(in_file_gv, gvValidate, nlValidate);
        loadNLCPU(in_file_nl, nlValidate);
    #endif

    fclose(in_file_gv);
    fclose(in_file_nl);
    

    // Load the transposed graph
    std::string gv_T_name = make_T_filename(filename_gv, "_gv.bin");
    std::string nl_T_name = make_T_filename(filename_nl, "_nl.bin");
    in_file_gv = fopen(gv_T_name.c_str(), "rb");
    in_file_nl = fopen(nl_T_name.c_str(), "rb");
    if (!in_file_gv || !in_file_nl) {
        printf("Error opening files");
        exit(EXIT_FAILURE);
    }

    

    uint64_t num_edgesT, nlist_sizeT;
    fseek(in_file_gv, sizeof(num_verts), SEEK_SET); // we can skip that, same as normal graph
    fread(&num_edgesT, sizeof(nlist_size), 1, in_file_gv);
    fread(&nlist_sizeT, sizeof(nlist_size), 1, in_file_nl);
    uint64_t nlist_beg_sizeT = nlist_sizeT * sizeof(uint64_t);


    // Transposed graph
    vertex_t *verticesT0 = reinterpret_cast<vertex_t *>(allocator->mm_malloc_global(g_v_bin_size, blockSize, num_nodes, 0));
    // vertex_t *verticesT1 = reinterpret_cast<vertex_t *>(allocator->mm_malloc_global(g_v_bin_size, blockSize, num_nodes, 0));
    uint64_t* nlistT = reinterpret_cast<uint64_t *>(allocator->mm_malloc_global(nlist_beg_sizeT, blockSize, num_nodes, 0));
    assert(verticesT0 && "Could not allocate memory for the transposed graph (vertex list 0)!");
    // assert(verticesT1 && "Could not allocate memory for the transposed graph (vertex list 1)!");
    assert(nlistT && "Could not allocate memory for the transposed graph (edge list)!");
    vertex_t* verticesT = verticesT0;
    vertex_t* verticesT_target = verticesT0;


    printf("Loading vertices (transposed graph)...\n");
    // loadGV(dramalloc::DramAllocator *allocator, FILE* inFile, vertex_t* target, vertex_t* target2, uint64_t* nlist_beg_global, uint64_t num_verts) {
    loadGV(allocator, in_file_gv, verticesT, nlistT, num_verts);
    max_deg = startPrefixSum(rt, verticesT, num_verts);
    // initVertices(rt, verticesT0, verticesT1, num_verts);
    printf("done\n");
    

    printf("Loading neighbor list (transposed graph)... ");
    // void loadNL(dramalloc::DramAllocator *allocator, FILE* inFile, uint64_t* nlist, uint64_t nlist_size, uint64_t blockSize) {
    loadNL(allocator, in_file_nl, nlistT, nlist_beg_sizeT, blockSize);
    printf("done\n");
    printf("# vertices: %lu, # edges: %lu, avg deg: %lf, max deg: %lu, total edge size: %lu bytes\n", num_verts, num_edges, ((double)num_edgesT)/num_verts, max_deg, nlist_beg_sizeT);
    fflush(stdout);

    printGraph(allocator, verticesT, nlistT, num_verts);
    
    #ifdef VALIDATE_RESULT
        std::vector<vertex_t> gvValidateT(num_verts);
        std::vector<uint64_t> nlValidateT(nlist_sizeT);
        fseek(in_file_gv, sizeof(num_edges)+sizeof(num_verts), SEEK_SET);
        fseek(in_file_nl, sizeof(nlist_sizeT), SEEK_SET);
        loadGVCPU(in_file_gv, gvValidateT, nlValidateT);
        loadNLCPU(in_file_nl, nlValidateT);
    #endif

    fclose(in_file_gv);
    fclose(in_file_nl);

    // vector of simticks
    uint64_t simTicks = rt->getSimTicks();
    uint64_t iters = 1;
    uint64_t edgesTraversed = 0;
    int activeCount = num_verts;
    std::vector<uint64_t> lastState(num_verts);
    
    while (true) {
        printf("ITERATION %lu   ==== Coloring Graph ====\n", iters); fflush(stdout);
        uint64_t coloring_iteration = 1;
        uint64_t bfs_iteration = 1;
        uint64_t num_vertices_updated;
        uint64_t num_vertices_visited;

        // reset lastState
        uint64_t hasChanged;
        std::fill(lastState.begin(), lastState.end(), -1);
        while (true) {
            
            std::swap(g_v_bin_global_target, g_v_bin_global);

            // uint64_t runColoringIteration(UpDown::UDRuntime_t *rt, vertex_t* g_v_bin_global, 
            //            vertex_t* g_v_bin_global_target, 
            //            uint64_t num_verts, uint64_t num_edges,
            //            uint64_t* num_vertices_updated, uint64_t* num_vertices_visited);
            runColoringIteration(rt, g_v_bin_global, g_v_bin_global_target, num_verts, num_edges, &num_vertices_updated, &num_vertices_visited);

            std::cout << "Itera " << coloring_iteration << ": num_vertices_updated = " << num_vertices_updated << " num_vertices_visited = " << num_vertices_visited << "\n";
            fflush(stdout);
            terminateUpDownThreads(rt);

            // printf("target: %p, source: %p, g_v_bin_global0: %p, g_v_bin_global1: %p\nGV0\n", g_v_bin_global_target, g_v_bin_global, g_v_bin_global0, g_v_bin_global1);
            // printGraph(allocator, g_v_bin_global0, nlist_beg_global, num_verts);

            // printf("target: %p, source: %p, g_v_bin_global0: %p, g_v_bin_global1: %p\nGV1\n", g_v_bin_global_target, g_v_bin_global, g_v_bin_global0, g_v_bin_global1);
            // printGraph(allocator, g_v_bin_global1, nlist_beg_global, num_verts);

            copyData(rt, g_v_bin_global_target, g_v_bin_global, num_verts);

            hasChanged = 0;
            for(uint64_t i = 0; i < num_verts; i++) {
                vertex_t *vert = reinterpret_cast<vertex_t*>(
                    allocator->translate_udva2sa((uint64_t)&(g_v_bin_global_target[i]))
                );

                if(vert->color != lastState[i]) {
                    hasChanged++;
                }

                lastState[i] = vert->color;
            }
            if (hasChanged) {
                printf("Color changed: %lu\n", hasChanged);
            } else {
                printf("Color not changed\n");
            }

            //if(!num_vertices_updated) {
            if(!hasChanged) {
                printf("BREAKING FROM LOOP, Inner loop converged at iteration %lu\n", coloring_iteration);
                break;
            }
            coloring_iteration++;
        }

        // Check the coloring of the graph
        #ifdef VALIDATE_RESULT
            printGraph(allocator, g_v_bin_global_target, nlist_beg_global, num_verts);
            edgesTraversed += runColoringCPU(gvValidate);
            if(!compareGraphs(allocator, g_v_bin_global_target, gvValidate)) {
                fprintf(stderr, "ERROR IN COLORING\n");
                return 1;
            }
        #endif

        printf("ITERATION %lu   ==== Performing BFS ====\n", iters); fflush(stdout);
        copyData(rt, g_v_bin_global_target, verticesT, num_verts);
        printGraph(allocator, g_v_bin_global, nlist_beg_global, num_verts);
        printGraph(allocator, verticesT, nlistT, num_verts);
        
        findVerticesOfSameColor(rt, verticesT, num_verts);
        // copyData(rt, verticesT, verticesT_target, num_verts);

        printf("Transposed Graph\n");
        printGraph(allocator, verticesT0, nlistT, num_verts);
        // printGraph(allocator, verticesT1, nlistT, num_verts);

        // uint64_t numUpdatesBFS = runIterationBFS(rt, verticesT, num_verts);

        //uint64_t runBFSIteration(UpDown::BASimUDRuntime_t* rt, vertex_t* gvSrc, 
        //                vertex_t* gvDst, 
        //                uint64_t num_verts, uint64_t num_edges,
        //                uint64_t* num_vertices_updated, uint64_t* num_vertices_visited)
        
        hasChanged = 1;
        std::fill(lastState.begin(), lastState.end(), -2);

        runBFSIteration(rt, verticesT, verticesT, num_verts, num_edgesT, true, &num_vertices_updated, &num_vertices_visited);
        printGraph(allocator, verticesT, nlistT, num_verts);
        printf("BFS Iteration complete: iteration: %lu, vertices updated: %lu, visited: %lu\n", bfs_iteration, num_vertices_updated, num_vertices_visited);
        
        // while(num_vertices_updated != 0) {
        while(hasChanged != 0) {
            bfs_iteration++;

            // printGraph(allocator, verticesT1, nlistT, num_verts);
            hasChanged = 0;
            for(uint64_t i = 0; i < num_verts; i++) {
                vertex_t *vert = reinterpret_cast<vertex_t*>(
                    allocator->translate_udva2sa((uint64_t)&(verticesT[i]))
                );

                if(vert->color != lastState[i]) {
                    hasChanged++;
                }

                lastState[i] = vert->color;
            }
            if (hasChanged) {
                printf("State changed: %lu\n", hasChanged);
            } else {
                printf("State did not change\n");
            }

            //if(!num_vertices_updated) {
            if(!hasChanged) {
                printf("BREAKING FROM LOOP, Inner loop converged at iteration %lu\n", bfs_iteration);
                break;
            }

            runBFSIteration(rt, verticesT, verticesT, num_verts, num_edgesT, false, &num_vertices_updated, &num_vertices_visited);
            printGraph(allocator, verticesT, nlistT, num_verts);
            printf("BFS Iteration complete: iteration: %lu, vertices updated: %lu, visited: %lu\n", bfs_iteration, num_vertices_updated, num_vertices_visited);
        } 
        terminateUpDownThreads(rt);


        #ifdef VALIDATE_RESULT
            edgesTraversed += runBFSCPU(gvValidate, gvValidateT);
            if(!compareGraphs(allocator, verticesT, gvValidateT)) {
                fprintf(stderr, "ERROR IN BFS\n");
                return 1;
            }
        #endif


        // Copy the sccIDs back to the original graph
        // Delete all vertices (set degree to 0) whose sccID is known (color == -1)

        g_v_bin_global = g_v_bin_global0;
        g_v_bin_global_target = g_v_bin_global1;

        // printGraph(allocator, g_v_bin_global0, nlistT, num_verts);
        // printGraph(allocator, g_v_bin_global1, nlistT, num_verts);
        // printGraph(allocator, verticesT, nlistT, num_verts);

        // copy the newly discovered SCC to the original graph
        copyData(rt, verticesT, g_v_bin_global0, num_verts);
        copyData(rt, verticesT, g_v_bin_global1, num_verts);

        uint64_t verticesLeft;
        uint64_t verticesDeleted;
        uint64_t verticesIgnored;
        markVerticesDeleted(rt, g_v_bin_global0, g_v_bin_global1, verticesT, num_verts, &verticesLeft, &verticesDeleted, &verticesIgnored);

        // printGraph(allocator, g_v_bin_global0, nlistT, num_verts);
        // printGraph(allocator, g_v_bin_global1, nlistT, num_verts);
        // printGraph(allocator, verticesT, nlistT, num_verts);

        printf("Vertices left: %lu, vertices deleted: %lu, vertices ignored: %lu\n", verticesLeft, verticesDeleted, verticesIgnored);

        #ifdef VALIDATE_RESULT
            copyAndMarkVerticesDeletedCPU(gvValidate, gvValidateT, &verticesLeft, &verticesDeleted, &verticesIgnored);
            if(!compareGraphs(allocator, g_v_bin_global, gvValidate)) {
                fprintf(stderr, "ERROR IN MARKING\n");
                return 1;
            }
            if(!compareGraphs(allocator, verticesT, gvValidateT)) {
                fprintf(stderr, "ERROR IN MARKING (transposed)\n");
                return 1;
            }
            printf("VALIDATION: Vertices left: %lu, vertices deleted: %lu, vertices ignored: %lu\n", verticesLeft, verticesDeleted, verticesIgnored);
        #endif


        if(verticesLeft == 0) {
            break;
        }
        iters++;
    }
    
    // show some statistics
    std::unordered_map<uint64_t, uint64_t> sccIDs;
    for(uint64_t i=0; i<num_verts; i++) {
        vertex_t* vert = reinterpret_cast<vertex_t *>(allocator->translate_udva2sa((uint64_t)(g_v_bin_global0 + i)));
        sccIDs[vert->scc]++;
    }
    printf("Sizes of the SCCs:\nSCC ID\t\t#vertices\n");
    uint64_t totalVerticesAssigned = 0;
    uint64_t largestSCC = 0;
    uint64_t largestSCCID = -1;
    for(auto& [key, value] : sccIDs) {
        // printf("%lu\t\t%lu\n", key, value);
        totalVerticesAssigned += value;
        if(largestSCC < value) {
            largestSCC = value;
            largestSCCID = key;
        }
    }
    printf("Total number of SCCs: %lu\n", sccIDs.size());
    printf("Total number of vertices assigned: %lu\n", totalVerticesAssigned);
    printf("Largest SCC (ID: %lu) has %lu vertices\n", largestSCCID, largestSCC);
    printf("Total simulation ticks: %lu\n", rt->getSimTicks()-simTicks);
    #ifdef VALIDATE_RESULT
        printf("Traversed Edges: %lu\n", edgesTraversed);
    #endif

    // printGraph(allocator, g_v_bin_global, nlist_beg_global, num_verts);

    return 0;
}

