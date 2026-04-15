#include "louvain_cpu.h"
#include "louvain_updown.h"
#include <sys/types.h>
#include <sys/time.h>

#define USAGE "USAGE: ./louvain <num_nodes> <g_v_bin> <nl_bin> (<nl_weight_bin>)"

#define VALIDATE_RESULT

bool is_close(double a, double b, double epsilon=1e-6) {
  if (a > b) {
    return (a - b) < epsilon;
  }
  return (b - a) < epsilon;
}



int main(int argc, char* argv[]) {
    /* Read file name and number of lanes from input, set up machine parameters*/
	if (argc < 4) {
		printf("Insufficient Input Params\n");
		printf("%s\n", USAGE);
		exit(1);
	}
    
    uint64_t num_nodes = atoi(argv[1]);
	char* filename_gv = argv[2];
	char* filename_nl = argv[3];
    char* edge_weight_filename = NULL;
	uint64_t num_lanes = num_nodes * 2048;

    if(argc == 5){
        edge_weight_filename = argv[4];
    }
    
	printf("Input File Name:%s , %s\n", filename_gv, filename_nl);
	printf("Num Lanes:%ld\n", num_lanes);
    fflush(stdout);

	// Set up machine parameters
	UpDown::ud_machine_t machine;
	machine.MapMemSize = 1UL << 37; // 128GB
	machine.GMapMemSize = 1UL << 37; // 128GB
	machine.LocalMemAddrMode = 1;
	machine.NumLanes = num_lanes > 64 ? 64 : num_lanes;
	machine.NumUDs = std::ceil(num_lanes / 64.0) > 4 ? 4 : std::ceil(num_lanes / 64.0);
	machine.NumStacks = std::ceil(num_lanes / (64.0 * 4)) > 8 ? 8 : std::ceil(num_lanes / (64.0 * 4));
	machine.NumNodes = std::ceil(num_lanes / (64.0 * 4 * 8));

    /* if UpDown node == 1, dramalloc will map global memory to local memory */
	if(num_lanes <= 2048){
		machine.MapMemSize = 1UL << 38; // 256GB
		machine.GMapMemSize = 1UL << 32; // 4GB
	}
    
    // machine.MemBandwidth = 17200;
    // machine.MemLatency = 2;
    // machine.InterNodeLatency = 100;
    // machine.MemBandwidth = 12000;


    /* Load UpDown binary code */
	UpDown::BASimUDRuntime_t* rt = new UpDown::BASimUDRuntime_t(machine, "louvain_exe.bin", 0, 100);
    
    /* Initialize DRAM memory allocator */
    dramalloc::DramAllocator *allocator = new dramalloc::DramAllocator(rt, louvain_exe::DRAMalloc__global_broadcast /*eventlabel*/);

    printf("dramalloc\n");
	fflush(stdout);


    /* ------------ Load Graph ------------*/
    #ifdef VALIDATE_RESULT
    Graph* cpu_g = new Graph(filename_gv, filename_nl, edge_weight_filename);
    #endif
    UDGraph* ud_g = new UDGraph(filename_gv, filename_nl, edge_weight_filename, rt, allocator);

    #ifdef VALIDATE_RESULT
    for(uint64_t i = 0; i < cpu_g->num_verts; i++){
        vertex_t* vert = &(ud_g->g_v_bin[i]);
        if(ud_g->num_lanes > 2048){
            vert = reinterpret_cast<vertex_t *>(allocator->translate_udva2sa((uint64_t)&(ud_g->g_v_bin[i])));
        }
        if(vert->vid != cpu_g->g_v_bin[i].vid){
            printf("idx = %lu, ud vid (%lu) != cpu vid (%lu)\n", i, vert->vid, cpu_g->g_v_bin[i].vid);
            exit(1);
        }
        if(vert->vertex_weight != cpu_g->g_v_bin[i].vertex_weight){
            printf("idx = %lu, ud weight (%lu) != cpu weight (%lu)\n", i, vert->vertex_weight, cpu_g->g_v_bin[i].vertex_weight);
            exit(1);
        }
        if(vert->deg != cpu_g->g_v_bin[i].deg){
            printf("idx = %lu, ud deg (%lu) != cpu deg (%lu)\n", i, vert->deg, cpu_g->g_v_bin[i].deg);
            exit(1);
        }
        for(uint64_t j = 0; j < vert->deg; j++){
            uint64_t* neigh_ptr = &(vert->neigh_ptr[j]);
            if(ud_g->num_lanes > 2048){
                neigh_ptr = reinterpret_cast<uint64_t *>(allocator->translate_udva2sa((uint64_t)&(vert->neigh_ptr[j]))); 
            }
            if(neigh_ptr[0] != cpu_g->g_v_bin[i].neigh_ptr[j]){
                printf("nv[%lu][%lu]: ud (%lu) 0x%lx %lu cpu (%lu), deg = %lu\n", i, j, neigh_ptr[0], neigh_ptr, neigh_ptr - ud_g->g_v_bin[0].neigh_ptr, cpu_g->g_v_bin[i].neigh_ptr[j], vert->deg);
                exit(1);
            }
        }
    }
    #endif

    printf("==== Graph Loading done ==== \n"); fflush(stdout);

    timeval start, end;
    double init_time = 0, modularity_time = 0, local_move_time = 0, aggregation_time = 0, time;
    uint64_t init_times = 0, modularity_times = 0, local_move_times = 0, aggregation_times = 0;

    rt->reset_all_stats();

    /* ------------ Initalize Graph ------------*/
    ud_g->init(init_time);
    cout << "Init time: " << init_time << " s" << endl; fflush(stdout);
    init_times += 1;

    #ifdef VALIDATE_RESULT
    cpu_g->init();
    for(uint64_t i = 0; i < cpu_g->num_verts; i++){
        int64_t* ud_n2c = &(ud_g->g_v_bin[i].community);
        if(ud_g->num_lanes > 2048){
            ud_n2c = reinterpret_cast<int64_t *>(allocator->translate_udva2sa(reinterpret_cast<uint64_t>(&(ud_g->g_v_bin[i].community))));
        }
        if(ud_n2c[0] != cpu_g->n2c[i]){
            printf("ud_n2c[%lu] (%lu) != cpu_n2c[%lu] (%lu)\n", i, ud_n2c[0], i, cpu_g->n2c[i]);
            exit(1);
        }
        double* ud_in = &(ud_g->g_v_bin[i].in);
        if(ud_g->num_lanes > 2048){
            ud_in = reinterpret_cast<double*>(allocator->translate_udva2sa(reinterpret_cast<uint64_t>(&(ud_g->g_v_bin[i].in))));
        }
        if(ud_in[0] != cpu_g->in[i]){
            printf("ud_in[%lu] (%lf) (0x%lx) != cpu_in[%lu] (%lf)\n", i, ud_in[0], &(ud_g->g_v_bin[i]), i, cpu_g->in[i]);
            exit(1);
        }
        double* ud_tot = &(ud_g->g_v_bin[i].tot);
        if(ud_g->num_lanes > 2048){
            ud_tot = reinterpret_cast<double*>(allocator->translate_udva2sa(reinterpret_cast<uint64_t>(&(ud_g->g_v_bin[i].tot))));
        }
        if(ud_tot[0] != cpu_g->tot[i]){
            printf("ud_tot[%lu] (%lf) != cpu_tot[%lu] (%lf)\n", i, ud_tot[0], i, cpu_g->tot[i]);
            exit(1);
        }
        double* ud_w = &(ud_g->g_v_bin[i].weight);
        if(ud_g->num_lanes > 2048){
            ud_w = reinterpret_cast<double*>(allocator->translate_udva2sa(reinterpret_cast<uint64_t>(&(ud_g->g_v_bin[i].weight))));
        }
        if(ud_w[0] != cpu_g->tot[i]){
            printf("ud_weight[%lu] (%lf) != cpu_tot[%lu] (%lf)\n", i, ud_w[0], i, cpu_g->tot[i]);
            exit(1);
        }
        if(ud_g->total_weight != cpu_g->total_weight){
            printf("ud_total_weight (%lf) != cpu_total_weight (%lf)\n", ud_g->total_weight, cpu_g->total_weight);
            exit(1);
        }
    }
    #endif

    int level = 0;
    double quality = ud_g->quality(modularity_time);
    modularity_times += 1;
    

    double next_qual;

    #ifdef VALIDATE_RESULT
    double cpu_quality = cpu_g->quality();
    if(!is_close(quality, cpu_quality)){
    // if(quality != cpu_quality){
        printf("ud_quality (%lf) != cpu_quality (%lf)\n", quality, cpu_quality);
        exit(1);
    }
    #endif


    // double precision  = 0.0001L;
    // uint64_t max_iter = 1000;
    // double precision  = 0.0000001L;
    // uint64_t max_iter = 1000;
    uint64_t iter = 0;
    double new_qual = quality;
    uint64_t max_iter = 100;



    while(true){
        cout << "level " << level << ":\n";
        cout << "  network size: " << ud_g->num_verts << " nodes, " << ud_g->num_edges << " links, " << ud_g->total_weight << " weight" << endl;

        double cur_qual = new_qual;
        double pre_qual = new_qual;
        uint64_t nb_moves = 0;
        iter = 0;
        double precision  = 0.0000001L;
        double max_diff = 0;
        
        while(true) {
            // printf("vid = %lu, deg = %lu, comm = %lu\n", cpu_g->g_v_bin[1].vid, cpu_g->g_v_bin[1].deg, cpu_g->n2c[1]); fflush(stdout);
            // uint64_t* ud_n2c = reinterpret_cast<uint64_t *>(allocator->translate_udva2sa(reinterpret_cast<uint64_t>(&(ud_g->g_v_bin[7308].tot))));
            // printf("0x%lx 0x%lx\n", ud_n2c[0], cpu_g->tot[7308]);
            nb_moves = 0;
            ud_g->one_level(nb_moves, local_move_time);
            local_move_times += 1;
            iter += 1;
            #ifdef VALIDATE_RESULT
            cpu_g->one_level();
            for(uint64_t i = 0; i < ud_g->num_verts; i++){
                vertex* n2c_new = &(ud_g->g_v_bin[i]);
                if(ud_g->num_lanes > 2048){
                    n2c_new = reinterpret_cast<vertex *>(allocator->translate_udva2sa(reinterpret_cast<uint64_t>(&(ud_g->g_v_bin[i]))));
                }
                if(n2c_new->new_community != cpu_g->n2c_new[i]){
                    printf("ud_n2c_new[%lu] (%lu) val = %lf 0x%lx != cpu_n2c_new[%lu] (%lu) val = %lf 0x%lx\n", i, n2c_new->new_community, bit_cast<uint64_t, double>(n2c_new->new_increase), n2c_new->new_increase, i, cpu_g->n2c_new[i], cpu_g->new_increase[i], bit_cast<uint64_t, double>(cpu_g->new_increase[i]));
                    printf("ud flag = %lu, cpu flag = %lu", ud_g->filter_flag, cpu_g->filter_flag);
                    printf("ud_n2c[%lu] (%lu) != cpu_n2c[%lu] (%lu)\n", i, n2c_new->community, i, cpu_g->n2c[i]);
                    exit(1);
                }
            }
            #endif

            ud_g->re_compute_attr(modularity_time);
            ud_g->filter_flag = !(ud_g->filter_flag);

            #ifdef VALIDATE_RESULT
            cpu_g->re_compute_attr();
            for(uint64_t i = 0; i < cpu_g->num_verts; i++){
                int64_t* ud_n2c = &(ud_g->g_v_bin[i].community);
                if(ud_g->num_lanes > 2048){
                    ud_n2c = reinterpret_cast<int64_t *>(allocator->translate_udva2sa(reinterpret_cast<uint64_t>(&(ud_g->g_v_bin[i].community))));
                }
                if(ud_n2c[0] != cpu_g->n2c[i]){
                    printf("ud_n2c[%lu] (%lu) != cpu_n2c[%lu] (%lu)\n", i, ud_n2c[0], i, cpu_g->n2c[i]);
                    exit(1);
                }
                double* ud_in = &(ud_g->g_v_bin[i].in);
                if(ud_g->num_lanes > 2048){
                    ud_in = reinterpret_cast<double*>(allocator->translate_udva2sa(reinterpret_cast<uint64_t>(&(ud_g->g_v_bin[i].in))));
                }
                if(ud_in[0] != cpu_g->in[i]){
                    printf("ud_in[%lu] (%lf) != cpu_in[%lu] (%lf)\n", i, ud_in[0], i, cpu_g->in[i]);
                    exit(1);
                }
                double* ud_tot = &(ud_g->g_v_bin[i].tot);
                if(ud_g->num_lanes > 2048){
                    ud_tot = reinterpret_cast<double*>(allocator->translate_udva2sa(reinterpret_cast<uint64_t>(&(ud_g->g_v_bin[i].tot))));
                }
                if(ud_tot[0] != cpu_g->tot[i]){
                    printf("ud_tot[%lu] (%lf) != cpu_tot[%lu] (%lf)\n", i, ud_tot[0], i, cpu_g->tot[i]);
                    exit(1);
                }
                if(ud_g->total_weight != cpu_g->total_weight){
                    printf("ud_total_weight (%lf) != cpu_total_weight (%lf)\n", ud_g->total_weight, cpu_g->total_weight);
                    exit(1);
                }
            }
            cpu_g->filter_flag = !(cpu_g->filter_flag);
            #endif

            new_qual = ud_g->quality(modularity_time);
            modularity_times += 1;

            #ifdef VALIDATE_RESULT
            cpu_quality = cpu_g->quality();
            // if(new_qual != cpu_quality){
            if(!is_close(new_qual, cpu_quality)){
                printf("ud_quality (%lf) != cpu_quality (%lf)\n", new_qual, cpu_quality);
                exit(1);
            }
            #endif
            cout << "Itera " << iter << ": quality increased from " << cur_qual << " to " << new_qual << ", diff = " << (new_qual - cur_qual) << endl;
            cout << "Init time: " << init_time << " s, compute modularity time: " << modularity_time << "s, local movment time: " << local_move_time << "s, aggregation time: " << aggregation_time << "s" << endl;
            cout << "Init times: " << init_times << ", compute modularity times: " << modularity_times << ", local movment times: " << local_move_times << ", aggregation time: " << aggregation_times << endl;
            
            if(max_diff < (new_qual-cur_qual)){
                max_diff = new_qual - cur_qual;
                if((max_diff / 100 ) > precision){
                    precision = max_diff / 100;
                    cout << "new precision = " << precision << endl;
                }
            }
            
            if((new_qual-cur_qual) <= precision){
                ud_g->re_compute_attr1(modularity_time);
                #ifdef VALIDATE_RESULT
                cpu_g->re_compute_attr1();
                for(uint64_t i = 0; i < cpu_g->num_verts; i++){
                    int64_t* ud_n2c = &(ud_g->g_v_bin[i].community);
                    if(ud_g->num_lanes > 2048){
                        ud_n2c = reinterpret_cast<int64_t *>(allocator->translate_udva2sa(reinterpret_cast<uint64_t>(&(ud_g->g_v_bin[i].community))));
                    }
                    if(ud_n2c[0] != cpu_g->n2c[i]){
                        printf("ud_n2c[%lu] (%lu) != cpu_n2c[%lu] (%lu)\n", i, ud_n2c[0], i, cpu_g->n2c[i]);
                        exit(1);
                    }
                    double* ud_in = &(ud_g->g_v_bin[i].in);
                    if(ud_g->num_lanes > 2048){
                        ud_in = reinterpret_cast<double*>(allocator->translate_udva2sa(reinterpret_cast<uint64_t>(&(ud_g->g_v_bin[i].in))));
                    }
                    if(ud_in[0] != cpu_g->in[i]){
                        printf("ud_in[%lu] (%lf) != cpu_in[%lu] (%lf)\n", i, ud_in[0], i, cpu_g->in[i]);
                        exit(1);
                    }
                    double* ud_tot = &(ud_g->g_v_bin[i].tot);
                    if(ud_g->num_lanes > 2048){
                        ud_tot = reinterpret_cast<double*>(allocator->translate_udva2sa(reinterpret_cast<uint64_t>(&(ud_g->g_v_bin[i].tot))));
                    }
                    if(ud_tot[0] != cpu_g->tot[i]){
                        printf("ud_tot[%lu] (%lf) != cpu_tot[%lu] (%lf)\n", i, ud_tot[0], i, cpu_g->tot[i]);
                        exit(1);
                    }
                    if(ud_g->total_weight != cpu_g->total_weight){
                        printf("ud_total_weight (%lf) != cpu_total_weight (%lf)\n", ud_g->total_weight, cpu_g->total_weight);
                        exit(1);
                    }
                }
                #endif

                new_qual = ud_g->quality(modularity_time);
                modularity_times += 1;

                #ifdef VALIDATE_RESULT
                cpu_quality = cpu_g->quality();
                // if(new_qual != cpu_quality){
                if(!is_close(new_qual, cpu_quality)){
                    printf("ud_quality (%lf) != cpu_quality (%lf)\n", new_qual, cpu_quality);
                    exit(1);
                }
                #endif
                cout << "  quality increased from " << cur_qual << " to " << new_qual << ", diff = " << (new_qual - cur_qual) << endl;
                cout << "Init time: " << init_time << " s, compute modularity time: " << modularity_time << "s, local movment time: " << local_move_time << "s, aggregation time: " << aggregation_time << "s" << endl;
                cout << "Init times: " << init_times << ", compute modularity times: " << modularity_times << ", local movment times: " << local_move_times << ", aggregation time: " << aggregation_times << endl;

                if((new_qual-cur_qual) < 0){
                    ud_g->re_compute_attr2(modularity_time);

                    #ifdef VALIDATE_RESULT
                    cpu_g->re_compute_attr2();
                    for(uint64_t i = 0; i < cpu_g->num_verts; i++){
                        int64_t* ud_n2c = &(ud_g->g_v_bin[i].community);
                        if(ud_g->num_lanes > 2048){
                            ud_n2c = reinterpret_cast<int64_t *>(allocator->translate_udva2sa(reinterpret_cast<uint64_t>(&(ud_g->g_v_bin[i].community))));
                        }
                        if(ud_n2c[0] != cpu_g->n2c[i]){
                            printf("ud_n2c[%lu] (%lu) != cpu_n2c[%lu] (%lu)\n", i, ud_n2c[0], i, cpu_g->n2c[i]);
                            exit(1);
                        }
                        double* ud_in = &(ud_g->g_v_bin[i].in);
                        if(ud_g->num_lanes > 2048){
                            ud_in = reinterpret_cast<double*>(allocator->translate_udva2sa(reinterpret_cast<uint64_t>(&(ud_g->g_v_bin[i].in))));
                        }
                        if(ud_in[0] != cpu_g->in[i]){
                            printf("ud_in[%lu] (%lf) != cpu_in[%lu] (%lf)\n", i, ud_in[0], i, cpu_g->in[i]);
                            exit(1);
                        }
                        double* ud_tot = &(ud_g->g_v_bin[i].tot);
                        if(ud_g->num_lanes > 2048){
                            ud_tot = reinterpret_cast<double*>(allocator->translate_udva2sa(reinterpret_cast<uint64_t>(&(ud_g->g_v_bin[i].tot))));
                        }
                        if(ud_tot[0] != cpu_g->tot[i]){
                            printf("ud_tot[%lu] (%lf) != cpu_tot[%lu] (%lf)\n", i, ud_tot[0], i, cpu_g->tot[i]);
                            exit(1);
                        }
                        if(ud_g->total_weight != cpu_g->total_weight){
                            printf("ud_total_weight (%lf) != cpu_total_weight (%lf)\n", ud_g->total_weight, cpu_g->total_weight);
                            exit(1);
                        }
                    }
                    #endif

                    new_qual = ud_g->quality(modularity_time);
                    modularity_times += 1;

                    #ifdef VALIDATE_RESULT
                    cpu_quality = cpu_g->quality();
                    // if(new_qual != cpu_quality){
                    if(!is_close(new_qual, cpu_quality)){
                        printf("ud_quality (%lf) != cpu_quality (%lf)\n", new_qual, cpu_quality);
                        exit(1);
                    }
                    #endif
                }
            }
                
            if((new_qual-cur_qual) <= precision){
                break;
            }
            cur_qual = new_qual;
            // printf("pass one iteration\n");
        }
        
        if((iter >= max_iter) || ((new_qual - pre_qual) <= precision) ){
            ud_g->compute_comm();
            break;
        }

        // break;

        pre_qual = new_qual;

        
        UDGraph *ud_g2 = ud_g->partition2UDGraph_binary(aggregation_time);
        aggregation_times += 1;

        #ifdef VALIDATE_RESULT
        Graph *cpu_g2 = cpu_g->partition2graph_binary();
        for(uint64_t i = 0; i < cpu_g2->num_verts; i++){
            vertex_t* vert = &(ud_g2->g_v_bin[i]);
            if(ud_g2->num_lanes > 2048){
                vert = reinterpret_cast<vertex_t *>(allocator->translate_udva2sa((uint64_t)&(ud_g2->g_v_bin[i])));
            }
            if(vert->vid != cpu_g2->g_v_bin[i].vid){
                printf("idx = %lu, ud vid (%lu) != cpu vid (%lu)\n", i, vert->vid, cpu_g2->g_v_bin[i].vid);
                exit(1);
            }
            if(vert->vertex_weight != cpu_g2->g_v_bin[i].vertex_weight){
                printf("idx = %lu, ud weight (%lu) != cpu weight (%lu)\n", i, vert->vertex_weight, cpu_g2->g_v_bin[i].vertex_weight);
                exit(1);
            }
            if(vert->deg != cpu_g2->g_v_bin[i].deg){
                printf("idx = %lu, ud deg (%lu) != cpu deg (%lu)\n", i, vert->deg, cpu_g2->g_v_bin[i].deg);
                exit(1);
            }
            for(uint64_t j = 0; j < vert->deg; j++){
                uint64_t* neigh_ptr = &(vert->neigh_ptr[j]);
                if(ud_g2->num_lanes > 2048){
                    neigh_ptr = reinterpret_cast<uint64_t *>(allocator->translate_udva2sa((uint64_t)&(vert->neigh_ptr[j]))); 
                }
                if(neigh_ptr[0] != cpu_g2->g_v_bin[i].neigh_ptr[j]){
                    printf("nv[%lu][%lu]: ud (%lu) cpu (%lu)\n", i, j, neigh_ptr[0], cpu_g2->g_v_bin[i].neigh_ptr[j]);
                    exit(1);
                }
                double* weight_ptr = &(vert->weight_ptr[j]);
                if(ud_g2->num_lanes > 2048){
                    weight_ptr = reinterpret_cast<double *>(allocator->translate_udva2sa((uint64_t)&(vert->weight_ptr[j]))); 
                }
                if(weight_ptr[0] != cpu_g2->g_v_bin[i].weight_ptr[j]){
                    printf("nv[%lu][%lu] weight: ud (%lf) cpu (%lf)\n", i, j, weight_ptr[0], cpu_g2->g_v_bin[i].weight_ptr[j]);
                    exit(1);
                }
            }
            // if(i == 0){
            //     double tmp = 0;
            //     printf("N[0] = ");
            //     for(uint64_t j = 0; j < vert->deg; j++){
            //         printf("(%lu, %lf) ", cpu_g2->g_v_bin[i].neigh_ptr[j], cpu_g2->g_v_bin[i].weight_ptr[j]);
            //         tmp += cpu_g2->g_v_bin[i].weight_ptr[j];
            //     }
            //     printf(" total = %lf\n", tmp);
            // }
        }
        printf("Pass new graph generation\n");

        #endif
        ud_g2->init(ud_g, init_time);
        init_times += 1;
        
        delete ud_g;
        ud_g = ud_g2;
        #ifdef VALIDATE_RESULT
        cpu_g2->init();
        delete cpu_g;
        cpu_g = cpu_g2;
        for(uint64_t i = 0; i < cpu_g->num_verts; i++){
            int64_t* ud_n2c = &(ud_g->g_v_bin[i].community);
            if(ud_g->num_lanes > 2048){
                ud_n2c = reinterpret_cast<int64_t *>(allocator->translate_udva2sa(reinterpret_cast<uint64_t>(&(ud_g->g_v_bin[i].community))));
            }
            if(ud_n2c[0] != cpu_g->n2c[i]){
                printf("ud_n2c[%lu] (%lu) != cpu_n2c[%lu] (%lu)\n", i, ud_n2c[0], i, cpu_g->n2c[i]);
                exit(1);
            }
            double* ud_in = &(ud_g->g_v_bin[i].in);
            if(ud_g->num_lanes > 2048){
                ud_in = reinterpret_cast<double*>(allocator->translate_udva2sa(reinterpret_cast<uint64_t>(&(ud_g->g_v_bin[i].in))));
            }
            if(ud_in[0] != cpu_g->in[i]){
                printf("ud_in[%lu] (%lf) != cpu_in[%lu] (%lf)\n", i, ud_in[0], i, cpu_g->in[i]);
                exit(1);
            }
            double* ud_tot = &(ud_g->g_v_bin[i].tot);
            if(ud_g->num_lanes > 2048){
                ud_tot = reinterpret_cast<double*>(allocator->translate_udva2sa(reinterpret_cast<uint64_t>(&(ud_g->g_v_bin[i].tot))));
            }
            if(ud_tot[0] != cpu_g->tot[i]){
                printf("ud_tot[%lu] (%lf) != cpu_tot[%lu] (%lf)\n", i, ud_tot[0], i, cpu_g->tot[i]);
                exit(1);
            }
            double* ud_w = &(ud_g->g_v_bin[i].weight);
            if(ud_g->num_lanes > 2048){
                ud_w = reinterpret_cast<double*>(allocator->translate_udva2sa(reinterpret_cast<uint64_t>(&(ud_g->g_v_bin[i].weight))));
            }
            if(ud_w[0] != cpu_g->tot[i]){
                printf("ud_weight[%lu] (%lf) != cpu_tot[%lu] (%lf)\n", i, ud_w[0], i, cpu_g->tot[i]);
                exit(1);
            }
            if(ud_g->total_weight != cpu_g->total_weight){
                printf("ud_total_weight (%lf) != cpu_total_weight (%lf)\n", ud_g->total_weight, cpu_g->total_weight);
                exit(1);
            }
            // if(i == 0){
            //     printf("v[0].tot. = %lf\n", cpu_g->tot[0]);
            // }
        }
        #endif
        level++;
    }

    // cout << ud_g->quality() << endl;
    delete ud_g;
    #ifdef VALIDATE_RESULT
    delete cpu_g;
    #endif

    cout << "Init time: " << init_time << " s, compute modularity time: " << modularity_time << "s, local movment time: " << local_move_time << "s, aggregation time: " << aggregation_time << "s" << endl;

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
  
    return 0;
}
