#include "common.h"

#define VALIDATE_RESULT
#define NUM_THREADS 127

#define USAGE "USAGE: ./louvain <num_nodes> <g_v_bin> <nl_bin> (<nl_weight_bin>)"

template <class To, class From>
std::enable_if_t<sizeof(To) == sizeof(From) &&
                     std::is_trivially_copyable_v<From> &&
                     std::is_trivially_copyable_v<To>,
                 To>
// constexpr support needs compiler magic
bit_cast(const From &src) noexcept {
  static_assert(std::is_trivially_constructible_v<To>,
                "This implementation additionally requires "
                "destination type to be trivially constructible");

  To dst;
  std::memcpy(&dst, &src, sizeof(To));
  return dst;
}

const uint64_t num_control_lanes_per_level = 32;


class UDGraph {
public:
  uint64_t num_verts;
  uint64_t num_edges;
  uint64_t nlist_size;
  double total_weight;
  UpDown::word_t total_weight_int;
  vertex_t* g_v_bin;
  uint64_t* nlist_beg;
  double* nlist_weight;
  vertex_t* g_v_bin_copy;
  uint64_t* nlist_beg_copy;
  double* nlist_weight_copy;
  vertex_t* g_v_bin_local;
  uint64_t* nlist_beg_local;
  double* nlist_weight_local;
  vertex_t* g_v_bin_copy_local;
  uint64_t* nlist_beg_copy_local;
  double* nlist_weight_copy_local;
  uint64_t blockSize; 

  double* neigh_weight;
  uint64_t *neigh_pos;

  bool filter_flag;
  uint64_t num_lanes;

  UpDown::BASimUDRuntime_t* rt;
  dramalloc::DramAllocator* allocator;

  UDGraph();
  ~UDGraph();
  UDGraph(char *filename_v, char *filename_e, char *filename_w, UpDown::BASimUDRuntime_t* _rt, dramalloc::DramAllocator *allocator);
  void init(double &time);
  void init(UDGraph *g, double &time);
  double quality(double &time);
  void one_level(uint64_t &nb_moves, double &time);
  UDGraph* partition2UDGraph_binary(double &time);
  void re_compute_attr(double &time);
  void re_compute_attr1(double &time);
  void re_compute_attr2(double &time);
  void free_malloc();
  void compute_comm();
};

void UDGraph::free_malloc(){
  free(neigh_weight);
  free(neigh_pos);

  free(g_v_bin);
  free(nlist_beg);
  free(nlist_weight);
  free(g_v_bin_copy);
  free(nlist_beg_copy);
  free(nlist_weight_copy);
}

UDGraph::~UDGraph(){
}

UDGraph::UDGraph(){
  num_verts = 0;
  num_edges = 0;
  nlist_size = 0;
  total_weight = 0.0;
  blockSize = 1UL * 32 * 1024; // 32KB

  neigh_weight = NULL;
  neigh_pos = NULL;

  g_v_bin = NULL;
  neigh_weight = NULL;
  neigh_pos = NULL;
  g_v_bin_copy = NULL;
  nlist_beg_copy = NULL;
  nlist_weight_copy = NULL;

  rt = NULL;
  allocator = NULL;
  filter_flag = true;
}


void UDGraph::re_compute_attr(double &time){
  uint64_t log2_num_control_lanes_per_level = std::log2(num_control_lanes_per_level);
  UpDown::word_t flag = 0;
  uint64_t sim_ticks_start, sim_ticks_end;
  UpDown::word_t num_moves = 0;


  /* ------------------------- UpDown Start ------------------------- */
  sim_ticks_start = rt->getSimTicks();
  UpDown::networkid_t nwid0(0, false, 0);
  UpDown::operands_t ops0(7);
  ops0.set_operand(0, num_lanes);
  ops0.set_operand(1, g_v_bin);
  ops0.set_operand(2, num_verts);
  ops0.set_operand(3, num_lanes);
  ops0.set_operand(4, (uint64_t)log2_num_control_lanes_per_level);
  ops0.set_operand(5, (uint64_t)0);
  ops0.set_operand(6, (uint64_t)filter_flag);

  UpDown::event_t event0(louvain_exe::re_compute_attr_phase0_master__init, nwid0, UpDown::CREATE_THREAD, &ops0); // generate start event 

  flag = 0;
  rt->t2ud_memcpy(&flag, sizeof(UpDown::word_t), nwid0, 0); // copy the value of flag to the scratchpad of NWID 0

  // start executing
  rt->send_event(event0);
  rt->start_exec(nwid0);
  rt->test_wait_addr(nwid0, 0, 1);

  rt->ud2t_memcpy(&num_moves, sizeof(UpDown::word_t), nwid0, 8); 

  sim_ticks_end = rt->getSimTicks();
  time += (sim_ticks_end - sim_ticks_start)/2.0/1e9;
  if(num_moves == 0){
    this->filter_flag = !(this->filter_flag);
    printf("Reverse UpDown\n");
  }
  /* ------------------------- UpDown End ------------------------- */

  // for(uint64_t i = 0; i < num_verts; i++){
  //   vertex_t* vert = &(g_v_bin[i]);
  //   if(num_lanes > 2048){
  //     vert = reinterpret_cast<vertex_t *>(allocator->translate_udva2sa((uint64_t)&(g_v_bin[i])));
  //   }
  //   if(filter_flag){
  //     if(vert->community < vert->new_community){
  //       num_moves++;
  //     }
  //   }else{
  //     if(vert->community > vert->new_community){
  //       num_moves++;
  //     }
  //   }
  // }
  // if(num_moves == 0){
  //   this->filter_flag = !(this->filter_flag);
  //   printf("Reverse\n");
  // }

  /* ------------------------- UpDown Start ------------------------- */
  sim_ticks_start = rt->getSimTicks();
  UpDown::networkid_t nwid1(0, false, 0);
  UpDown::operands_t ops1(7);
  ops1.set_operand(0, num_lanes);
  ops1.set_operand(1, g_v_bin);
  ops1.set_operand(2, num_verts);
  ops1.set_operand(3, num_lanes);
  ops1.set_operand(4, (uint64_t)log2_num_control_lanes_per_level);
  ops1.set_operand(5, (uint64_t)0);
  ops1.set_operand(6, (uint64_t)filter_flag);

  UpDown::event_t event1(louvain_exe::re_compute_attr_phase1_master__init, nwid1, UpDown::CREATE_THREAD, &ops1); // generate start event 

  flag = 0;
  rt->t2ud_memcpy(&flag, sizeof(UpDown::word_t), nwid1, 0); // copy the value of flag to the scratchpad of NWID 0

  // start executing
  rt->send_event(event1);
  rt->start_exec(nwid1);
  rt->test_wait_addr(nwid1, 0, 1);

  sim_ticks_end = rt->getSimTicks();
  time += (sim_ticks_end - sim_ticks_start)/2.0/1e9;
  /* ------------------------- UpDown End ------------------------- */

  // for(uint64_t i = 0; i < num_verts; i++){
  //   vertex_t* vert = &(g_v_bin[i]);
  //   if(num_lanes > 2048){
  //     vert = reinterpret_cast<vertex_t *>(allocator->translate_udva2sa((uint64_t)&(g_v_bin[i])));
  //   }
  //   uint64_t old_community = vert->community;
  //   if(filter_flag){
  //     if(vert->community < vert->new_community){
  //       vert->community = vert->new_community;
  //     }
  //     vert->in = 0.0;
  //     vert->tot = 0.0;
  //     vert->old_community = old_community;
  //   }else{
  //     if(vert->community > vert->new_community){
  //       vert->community = vert->new_community;
  //     }
  //     vert->in = 0.0;
  //     vert->tot = 0.0;
  //     vert->old_community = old_community;
  //   }
  // }

  /* ------------------------- UpDown Start ------------------------- */
  sim_ticks_start = rt->getSimTicks();
  UpDown::networkid_t nwid2(0, false, 0);
  UpDown::operands_t ops2(4);
  ops2.set_operand(0, num_verts);
  ops2.set_operand(1, num_edges);
  ops2.set_operand(2, g_v_bin);
  ops2.set_operand(3, num_lanes);

  UpDown::event_t event2(louvain_exe::re_compute_attr_phase2_main_control__init, nwid2, UpDown::CREATE_THREAD, &ops2); // generate start event 

  flag = 0;
  rt->t2ud_memcpy(&flag, sizeof(UpDown::word_t), nwid2, 0); // copy the value of flag to the scratchpad of NWID 0

  // start executing
  rt->send_event(event2);
  rt->start_exec(nwid2);
  rt->test_wait_addr(nwid2, 0, 1);

  sim_ticks_end = rt->getSimTicks();
  time += (sim_ticks_end - sim_ticks_start)/2.0/1e9;
  /* ------------------------- UpDown End ------------------------- */

  
  // for(uint64_t i = 0; i < num_verts; i++){
  //   vertex_t* vert = &(g_v_bin[i]);
  //   if(num_lanes > 2048){
  //     vert = reinterpret_cast<vertex_t *>(allocator->translate_udva2sa((uint64_t)&(g_v_bin[i])));
  //   }
  //   uint64_t cid = vert->community;
  //   for(uint64_t j = 0; j < vert->deg; j++){
  //     uint64_t* neigh_ptr = &(vert->neigh_ptr[j]);
  //     if(num_lanes > 2048){
  //       neigh_ptr = reinterpret_cast<uint64_t *>(allocator->translate_udva2sa((uint64_t)&(vert->neigh_ptr[j]))); 
  //     }
  //     uint64_t neigh_vid = *neigh_ptr;
  //     double* weight_ptr = &(vert->weight_ptr[j]);
  //     if(num_lanes > 2048){
  //       weight_ptr = reinterpret_cast<double *>(allocator->translate_udva2sa((uint64_t)&(vert->weight_ptr[j]))); 
  //     }
  //     double neigh_weight = *weight_ptr;
  //     vertex_t* vert2 = &(g_v_bin[neigh_vid]);
  //     if(num_lanes > 2048){
  //       vert2 = reinterpret_cast<vertex_t *>(allocator->translate_udva2sa((uint64_t)&(g_v_bin[neigh_vid])));
  //     }
  //     uint64_t neigh_comm = vert2->community;
  //     vertex_t* vert3 = &(g_v_bin[cid]);
  //     if(num_lanes > 2048){
  //       vert3 = reinterpret_cast<vertex_t *>(allocator->translate_udva2sa((uint64_t)&(g_v_bin[cid])));
  //     }
  //     if(cid == neigh_comm){
  //       vert3->in += neigh_weight;
  //     }
  //     vert3->tot += neigh_weight;
  //   }
  // }
  // return;
}

void UDGraph::re_compute_attr1(double &time){
  uint64_t log2_num_control_lanes_per_level = std::log2(num_control_lanes_per_level);
  UpDown::word_t flag = 0;
  uint64_t sim_ticks_start, sim_ticks_end;
  UpDown::word_t num_moves = 0;



  /* ------------------------- UpDown Start ------------------------- */
  sim_ticks_start = rt->getSimTicks();
  UpDown::networkid_t nwid1(0, false, 0);
  UpDown::operands_t ops1(7);
  ops1.set_operand(0, num_lanes);
  ops1.set_operand(1, g_v_bin);
  ops1.set_operand(2, num_verts);
  ops1.set_operand(3, num_lanes);
  ops1.set_operand(4, (uint64_t)log2_num_control_lanes_per_level);
  ops1.set_operand(5, (uint64_t)0);
  ops1.set_operand(6, (uint64_t)filter_flag);

  UpDown::event_t event1(louvain_exe::re_compute_attr1_phase1_master__init, nwid1, UpDown::CREATE_THREAD, &ops1); // generate start event 

  flag = 0;
  rt->t2ud_memcpy(&flag, sizeof(UpDown::word_t), nwid1, 0); // copy the value of flag to the scratchpad of NWID 0

  // start executing
  rt->send_event(event1);
  rt->start_exec(nwid1);
  rt->test_wait_addr(nwid1, 0, 1);

  sim_ticks_end = rt->getSimTicks();
  time += (sim_ticks_end - sim_ticks_start)/2.0/1e9;
  /* ------------------------- UpDown End ------------------------- */

  // for(uint64_t i = 0; i < num_verts; i++){
  //   vertex_t* vert = &(g_v_bin[i]);
  //   if(num_lanes > 2048){
  //     vert = reinterpret_cast<vertex_t *>(allocator->translate_udva2sa((uint64_t)&(g_v_bin[i])));
  //   }
  //   if(filter_flag){
  //     if(vert->old_community < vert->new_community){
  //       vert->community = vert->new_community;
  //     }else{
  //       vert->community = vert->old_community;
  //     }
  //     vert->in = 0.0;
  //     vert->tot = 0.0;
  //   }else{
  //     if(vert->old_community > vert->new_community){
  //       vert->community = vert->new_community;
  //     }else{
  //       vert->community = vert->old_community;
  //     }
  //     vert->in = 0.0;
  //     vert->tot = 0.0;
  //   }
  // }

  /* ------------------------- UpDown Start ------------------------- */
  sim_ticks_start = rt->getSimTicks();
  UpDown::networkid_t nwid2(0, false, 0);
  UpDown::operands_t ops2(4);
  ops2.set_operand(0, num_verts);
  ops2.set_operand(1, num_edges);
  ops2.set_operand(2, g_v_bin);
  ops2.set_operand(3, num_lanes);

  UpDown::event_t event2(louvain_exe::re_compute_attr_phase2_main_control__init, nwid2, UpDown::CREATE_THREAD, &ops2); // generate start event 

  flag = 0;
  rt->t2ud_memcpy(&flag, sizeof(UpDown::word_t), nwid2, 0); // copy the value of flag to the scratchpad of NWID 0

  // start executing
  rt->send_event(event2);
  rt->start_exec(nwid2);
  rt->test_wait_addr(nwid2, 0, 1);

  sim_ticks_end = rt->getSimTicks();
  time += (sim_ticks_end - sim_ticks_start)/2.0/1e9;
  /* ------------------------- UpDown End ------------------------- */

  
  // for(uint64_t i = 0; i < num_verts; i++){
  //   vertex_t* vert = &(g_v_bin[i]);
  //   if(num_lanes > 2048){
  //     vert = reinterpret_cast<vertex_t *>(allocator->translate_udva2sa((uint64_t)&(g_v_bin[i])));
  //   }
  //   uint64_t cid = vert->community;
  //   for(uint64_t j = 0; j < vert->deg; j++){
  //     uint64_t* neigh_ptr = &(vert->neigh_ptr[j]);
  //     if(num_lanes > 2048){
  //       neigh_ptr = reinterpret_cast<uint64_t *>(allocator->translate_udva2sa((uint64_t)&(vert->neigh_ptr[j]))); 
  //     }
  //     uint64_t neigh_vid = *neigh_ptr;
  //     double* weight_ptr = &(vert->weight_ptr[j]);
  //     if(num_lanes > 2048){
  //       weight_ptr = reinterpret_cast<double *>(allocator->translate_udva2sa((uint64_t)&(vert->weight_ptr[j]))); 
  //     }
  //     double neigh_weight = *weight_ptr;
  //     vertex_t* vert2 = &(g_v_bin[neigh_vid]);
  //     if(num_lanes > 2048){
  //       vert2 = reinterpret_cast<vertex_t *>(allocator->translate_udva2sa((uint64_t)&(g_v_bin[neigh_vid])));
  //     }
  //     uint64_t neigh_comm = vert2->community;
  //     vertex_t* vert3 = &(g_v_bin[cid]);
  //     if(num_lanes > 2048){
  //       vert3 = reinterpret_cast<vertex_t *>(allocator->translate_udva2sa((uint64_t)&(g_v_bin[cid])));
  //     }
  //     if(cid == neigh_comm){
  //       vert3->in += neigh_weight;
  //     }
  //     vert3->tot += neigh_weight;
  //   }
  // }
  // return;
}

void UDGraph::re_compute_attr2(double &time){
  uint64_t log2_num_control_lanes_per_level = std::log2(num_control_lanes_per_level);
  UpDown::word_t flag = 0;
  uint64_t sim_ticks_start, sim_ticks_end;
  UpDown::word_t num_moves = 0;



  /* ------------------------- UpDown Start ------------------------- */
  sim_ticks_start = rt->getSimTicks();
  UpDown::networkid_t nwid1(0, false, 0);
  UpDown::operands_t ops1(7);
  ops1.set_operand(0, num_lanes);
  ops1.set_operand(1, g_v_bin);
  ops1.set_operand(2, num_verts);
  ops1.set_operand(3, num_lanes);
  ops1.set_operand(4, (uint64_t)log2_num_control_lanes_per_level);
  ops1.set_operand(5, (uint64_t)0);
  ops1.set_operand(6, (uint64_t)filter_flag);

  UpDown::event_t event1(louvain_exe::re_compute_attr2_phase1_master__init, nwid1, UpDown::CREATE_THREAD, &ops1); // generate start event 

  flag = 0;
  rt->t2ud_memcpy(&flag, sizeof(UpDown::word_t), nwid1, 0); // copy the value of flag to the scratchpad of NWID 0

  // start executing
  rt->send_event(event1);
  rt->start_exec(nwid1);
  rt->test_wait_addr(nwid1, 0, 1);

  sim_ticks_end = rt->getSimTicks();
  time += (sim_ticks_end - sim_ticks_start)/2.0/1e9;
  /* ------------------------- UpDown End ------------------------- */

  // for(uint64_t i = 0; i < num_verts; i++){
  //   vertex_t* vert = &(g_v_bin[i]);
  //   if(num_lanes > 2048){
  //     vert = reinterpret_cast<vertex_t *>(allocator->translate_udva2sa((uint64_t)&(g_v_bin[i])));
  //   }
  //   vert->community = vert->old_community;
  //   vert->in = 0.0;
  //   vert->tot = 0.0;
  // }

  /* ------------------------- UpDown Start ------------------------- */
  sim_ticks_start = rt->getSimTicks();
  UpDown::networkid_t nwid2(0, false, 0);
  UpDown::operands_t ops2(4);
  ops2.set_operand(0, num_verts);
  ops2.set_operand(1, num_edges);
  ops2.set_operand(2, g_v_bin);
  ops2.set_operand(3, num_lanes);

  UpDown::event_t event2(louvain_exe::re_compute_attr_phase2_main_control__init, nwid2, UpDown::CREATE_THREAD, &ops2); // generate start event 

  flag = 0;
  rt->t2ud_memcpy(&flag, sizeof(UpDown::word_t), nwid2, 0); // copy the value of flag to the scratchpad of NWID 0

  // start executing
  rt->send_event(event2);
  rt->start_exec(nwid2);
  rt->test_wait_addr(nwid2, 0, 1);

  sim_ticks_end = rt->getSimTicks();
  time += (sim_ticks_end - sim_ticks_start)/2.0/1e9;
  /* ------------------------- UpDown End ------------------------- */

  
  // for(uint64_t i = 0; i < num_verts; i++){
  //   vertex_t* vert = &(g_v_bin[i]);
  //   if(num_lanes > 2048){
  //     vert = reinterpret_cast<vertex_t *>(allocator->translate_udva2sa((uint64_t)&(g_v_bin[i])));
  //   }
  //   uint64_t cid = vert->community;
  //   for(uint64_t j = 0; j < vert->deg; j++){
  //     uint64_t* neigh_ptr = &(vert->neigh_ptr[j]);
  //     if(num_lanes > 2048){
  //       neigh_ptr = reinterpret_cast<uint64_t *>(allocator->translate_udva2sa((uint64_t)&(vert->neigh_ptr[j]))); 
  //     }
  //     uint64_t neigh_vid = *neigh_ptr;
  //     double* weight_ptr = &(vert->weight_ptr[j]);
  //     if(num_lanes > 2048){
  //       weight_ptr = reinterpret_cast<double *>(allocator->translate_udva2sa((uint64_t)&(vert->weight_ptr[j]))); 
  //     }
  //     double neigh_weight = *weight_ptr;
  //     vertex_t* vert2 = &(g_v_bin[neigh_vid]);
  //     if(num_lanes > 2048){
  //       vert2 = reinterpret_cast<vertex_t *>(allocator->translate_udva2sa((uint64_t)&(g_v_bin[neigh_vid])));
  //     }
  //     uint64_t neigh_comm = vert2->community;
  //     vertex_t* vert3 = &(g_v_bin[cid]);
  //     if(num_lanes > 2048){
  //       vert3 = reinterpret_cast<vertex_t *>(allocator->translate_udva2sa((uint64_t)&(g_v_bin[cid])));
  //     }
  //     if(cid == neigh_comm){
  //       vert3->in += neigh_weight;
  //     }
  //     vert3->tot += neigh_weight;
  //   }
  // }
  // return;
}

double UDGraph::quality(double &time) {  // UpDown Kernel
  double q = 0;
  uint64_t log2_num_control_lanes_per_level = std::log2(num_control_lanes_per_level);

  /* ------------------------- UpDown Start ------------------------- */
  uint64_t sim_ticks_start = rt->getSimTicks();
  UpDown::networkid_t nwid(0, false, 0);
  UpDown::operands_t ops(7);
  ops.set_operand(0, num_lanes);
  ops.set_operand(1, this->total_weight);
  ops.set_operand(2, g_v_bin);
  ops.set_operand(3, num_verts);
  ops.set_operand(4, num_lanes);
  ops.set_operand(5, (uint64_t)log2_num_control_lanes_per_level);
  ops.set_operand(6, (uint64_t)0);

  UpDown::event_t event(louvain_exe::quality_master__init, nwid, UpDown::CREATE_THREAD, &ops); // generate start event

  UpDown::word_t flag = 0;
  rt->t2ud_memcpy(&flag, sizeof(UpDown::word_t), nwid, 0); // copy the value of flag to the scratchpad of NWID 0

  // start executing
  rt->send_event(event);
  rt->start_exec(nwid);
  rt->test_wait_addr(nwid, 0, 1);
  rt->ud2t_memcpy(&q, sizeof(double), nwid, 8);
  // rt->ud2t_memcpy(&flag, sizeof(UpDown::word_t), nwid, 8); 
  uint64_t sim_ticks_end = rt->getSimTicks();
  time += (sim_ticks_end - sim_ticks_start)/2.0/1e9;
  // printf("simTick = %lu\n", sim_ticks_end - sim_ticks_start);
  return q;
  /* ------------------------- UpDown End ------------------------- */

  // double q2  = 0.0L;
  // double m = this->total_weight;
  // for(uint64_t i=0; i < num_verts; i++){
  //   vertex_t* vert = &(g_v_bin[i]);
  //   if(num_lanes > 2048){
  //     vert = reinterpret_cast<vertex_t *>(allocator->translate_udva2sa((uint64_t)&(g_v_bin[i]))); // compute vertex addr
  //   }
  //   if(vert->tot > 0){
  //     q2 += vert->in - (vert->tot*vert->tot)/m;
  //   }
  // }
  // q2 /= m;
  // return q2;
}

UDGraph::UDGraph(char *vertex_filename, char *edge_filename, char *edge_weight_filename, UpDown::BASimUDRuntime_t* _rt, dramalloc::DramAllocator *_allocator) {
  this->filter_flag = true;
  this->rt = _rt;
  this->allocator = _allocator;
  this->num_lanes = rt->getMachineConfig().NumNodes * 2048;
  blockSize = 1UL * 32 * 1024; // 32KB
  /* ------------------ Load UDGraph ------------------ */
  num_edges = 0;
  num_verts = 0;
  nlist_size = 0;
  FILE* in_file_gv = fopen(vertex_filename, "rb");
  if (!in_file_gv) {
    exit(EXIT_FAILURE);
  }
  FILE* in_file_nl = fopen(edge_filename, "rb");
  if (!in_file_nl) {
    exit(EXIT_FAILURE);
  }
  FILE* in_file_weight_nl = NULL;
  if(edge_weight_filename != NULL) {
    FILE* in_file_weight_nl = fopen(edge_weight_filename, "rb");
    if (!in_file_weight_nl) {
      exit(EXIT_FAILURE);
    }
  }

  size_t file_size = 0;
  fseek(in_file_gv, 0, SEEK_SET);
  fseek(in_file_nl, 0, SEEK_SET);
  file_size = fread(&num_verts, sizeof(uint64_t),1, in_file_gv);
  file_size = fread(&num_edges, sizeof(uint64_t),1, in_file_gv);
  file_size = fread(&nlist_size, sizeof(uint64_t), 1, in_file_nl);

  printf("nlist_size = %lu\n", nlist_size);
  uint64_t g_v_bin_size = num_verts * sizeof(vertex_t);
  uint64_t nlist_beg_size = nlist_size * sizeof(uint64_t);
  uint64_t nlist_weight_size = nlist_size * sizeof(double);

  g_v_bin = reinterpret_cast<vertex_t *>(allocator->mm_malloc_global(g_v_bin_size, blockSize, rt->getMachineConfig().NumNodes, 0));
  nlist_beg = reinterpret_cast<uint64_t *>(allocator->mm_malloc_global(nlist_beg_size, blockSize, rt->getMachineConfig().NumNodes, 0));
  nlist_weight = reinterpret_cast<double*>(allocator->mm_malloc_global(nlist_weight_size, blockSize, rt->getMachineConfig().NumNodes, 0));

  g_v_bin_copy = reinterpret_cast<vertex_t *>(allocator->mm_malloc_global(g_v_bin_size, blockSize, rt->getMachineConfig().NumNodes, 0));
  nlist_beg_copy = reinterpret_cast<uint64_t *>(allocator->mm_malloc_global(nlist_beg_size, blockSize, rt->getMachineConfig().NumNodes, 0));
  nlist_weight_copy = reinterpret_cast<double*>(allocator->mm_malloc_global(nlist_weight_size, blockSize, rt->getMachineConfig().NumNodes, 0));

  g_v_bin_local = reinterpret_cast<vertex_t *>(rt->mm_malloc(g_v_bin_size));
  nlist_beg_local = reinterpret_cast<uint64_t *>(rt->mm_malloc(nlist_beg_size));
  nlist_weight_local = reinterpret_cast<double*>(rt->mm_malloc(nlist_weight_size));

  g_v_bin_copy_local = reinterpret_cast<vertex_t *>(rt->mm_malloc(g_v_bin_size));
  nlist_beg_copy_local = reinterpret_cast<uint64_t *>(rt->mm_malloc(nlist_beg_size));
  nlist_weight_copy_local = reinterpret_cast<double*>(rt->mm_malloc(nlist_weight_size));

  if((num_verts < 4096) || (num_lanes <= 2048)){ // compact to one node
    this->num_lanes = 2048; 
    g_v_bin = g_v_bin_local;
    nlist_beg = nlist_beg_local;
    nlist_weight = nlist_weight_local;
    g_v_bin_copy = g_v_bin_copy_local;
    nlist_beg_copy = nlist_beg_copy_local;
    nlist_weight_copy = nlist_weight_copy_local;
  }

  /* memory access require 64B align */
  /* Load g_v_bin */
  uint64_t max_deg = 0;
  for(uint64_t i = 0; i < num_verts; i++){
    vertex_t* vert = &(g_v_bin[i]);
    if(num_lanes > 2048){
      vert = reinterpret_cast<vertex_t *>(allocator->translate_udva2sa((uint64_t)&(g_v_bin[i]))); // compute vertex addr
    }
    if(fread(vert, sizeof(vertex_t), 1, in_file_gv) == 0){
        fprintf(stderr, "Error reading vertex from %s, load #v = %lu\n", vertex_filename, i);
        exit(EXIT_FAILURE);
    }
    uint64_t offset = (uint64_t)(vert->neigh_ptr);
    uint64_t * loc_nlist = nlist_beg + offset;
    double * loc_weight_nlist = nlist_weight + offset;
    uint64_t deg = vert->deg;
    vert->neigh_ptr = loc_nlist;
    vert->weight_ptr = loc_weight_nlist;
    vert->vertex_weight = 1;
    if (max_deg < deg)
			max_deg = deg;
  }
  fclose(in_file_gv);
  printf("==== Loading gv graph done ====\n"); fflush(stdout);


  /* Load nl_bin */
  uint64_t addr1 = reinterpret_cast<uint64_t>(nlist_beg);
  uint64_t addr1_end = addr1 + nlist_beg_size;
  // printf("addr1 = 0x%lx, nlist_size = %lu, nlist_beg_size = %lu, addr1_end = 0x%lx\n", addr1, nlist_size, nlist_beg_size, addr1_end);
  while(addr1 < addr1_end){
    uint64_t* sa1 = reinterpret_cast<uint64_t *>(addr1);
    if(num_lanes > 2048){
      sa1 = reinterpret_cast<uint64_t *>(allocator->translate_udva2sa(addr1));
    }
    int64_t len = blockSize;
    if ((addr1 + len) > addr1_end) {
        len = addr1_end - addr1;
    }
    size_t to_read = len / sizeof(int64_t);
    if (fread(sa1, sizeof(int64_t), to_read, in_file_nl) != to_read) {
        fprintf(stderr, "Error reading neighbor list from %s\n", edge_filename);
        exit(EXIT_FAILURE);
    }
    addr1 = addr1 + len;
  }
  fclose(in_file_nl);
  // printf("nv[714958][47] = %lu 0x%lx, nv[714958][48] = %lu 0x%lx, addr1_end = 0x%lx\n", g_v_bin[714958].neigh_ptr[47], &(g_v_bin[714958].neigh_ptr[47]), g_v_bin[714958].neigh_ptr[48], &(g_v_bin[714958].neigh_ptr[48]), addr1_end);
  printf("==== Loading nl graph done ====\n"); fflush(stdout);

  /* Load nlist_weight */
  if(in_file_weight_nl != NULL) {
    addr1 = reinterpret_cast<uint64_t>(nlist_weight);
    addr1_end = addr1 + nlist_weight_size;
    while(addr1 < addr1_end){
      double* sa1 = reinterpret_cast<double*>(addr1);
      if(num_lanes > 2048){
        sa1 = reinterpret_cast<double*>(allocator->translate_udva2sa(addr1));
      }
      int64_t len = blockSize;
      if ((addr1 + len) > addr1_end) {
          len = addr1_end - addr1;
      }
      size_t to_read = len / sizeof(double);
      if (fread(sa1, sizeof(double), to_read, in_file_weight_nl) != to_read) {
          fprintf(stderr, "Error reading neighbor list from %s\n", edge_weight_filename);
          exit(EXIT_FAILURE);
      }
      addr1 = addr1 + len;
    }
    fclose(in_file_weight_nl);
  }else{
    double* tmp = reinterpret_cast<double*>(malloc(nlist_weight_size));
    for(uint64_t i = 0; i < nlist_size; i++){
      tmp[i] = 1.0;
    }
    addr1 = reinterpret_cast<uint64_t>(nlist_weight);
    addr1_end = addr1 + nlist_weight_size;
    // printf("nv[714958][47] = %lu 0x%lx, nv[714958][48] = %lu 0x%lx, addr1_end = 0x%lx\n", g_v_bin[714958].neigh_ptr[47], &(g_v_bin[714958].neigh_ptr[47]), g_v_bin[714958].neigh_ptr[48], &(g_v_bin[714958].neigh_ptr[48]), addr1_end);
    while(addr1 < addr1_end){
      double* sa1 = reinterpret_cast<double*>(addr1);
      if(num_lanes > 2048){
        sa1 = reinterpret_cast<double*>(allocator->translate_udva2sa(addr1));
      }
      int64_t len = blockSize;
      if ((addr1 + len) > addr1_end) {
          len = addr1_end - addr1;
      }
      memcpy(sa1, tmp, len);
      addr1 = addr1 + len;
    }
  }
  // printf("nv[714958][47] = %lu 0x%lx, nv[714958][48] = %lu 0x%lx\n", g_v_bin[714958].neigh_ptr[47], &(g_v_bin[714958].neigh_ptr[47]), g_v_bin[714958].neigh_ptr[48], &(g_v_bin[714958].neigh_ptr[48]));
  printf("# vertices: %lu , # edges:%lu , avg deg: %lf, max deg: %lu, total edge size: %lu bytes\n", num_verts, num_edges, ((double)num_edges)/num_verts, max_deg, nlist_size * sizeof(uint64_t));
}



void UDGraph::init(double &time){
  /* ------------------ Community Partitation ------------------ */

  neigh_weight = reinterpret_cast<double*>(malloc(num_verts * sizeof(double)));
  neigh_pos = reinterpret_cast<uint64_t*>(malloc(nlist_size * sizeof(uint64_t)));

  /* Initilize Community Partitation */

  uint64_t sim_ticks_start, sim_ticks_end;
  UpDown::word_t flag;

  /* ------------------------- UpDown Start ------------------------- */
  sim_ticks_start = rt->getSimTicks();
  UpDown::networkid_t nwid(0, false, 0);
  UpDown::operands_t ops(4);
  ops.set_operand(0, num_verts);
  ops.set_operand(1, num_edges);
  ops.set_operand(2, g_v_bin);
  ops.set_operand(3, num_lanes);

  UpDown::event_t event(louvain_exe::init_graph_phase1_main_control__init, nwid, UpDown::CREATE_THREAD, &ops); // generate start event 
  flag = 0;
  rt->t2ud_memcpy(&flag, sizeof(UpDown::word_t), nwid, 0); // copy the value of flag to the scratchpad of NWID 0

  // start executing
  rt->send_event(event);
  rt->start_exec(nwid);
  rt->test_wait_addr(nwid, 0, 1);
  sim_ticks_end = rt->getSimTicks();
  time += (sim_ticks_end - sim_ticks_start)/2.0/1e9;

  rt->ud2t_memcpy(&total_weight, sizeof(double), nwid, 16);
  rt->ud2t_memcpy(&total_weight_int, sizeof(UpDown::word_t), nwid, 16);
  /* ------------------------- UpDown End ------------------------- */

  // /* ------------------ init1 ------------------ */
  // total_weight = 0;
  // for(uint64_t vid = 0; vid < num_verts; vid++){ // each vertex is a community
  //   vertex_t* vert = &(g_v_bin[vid]);
  //   if(num_lanes > 2048){
  //     vert = reinterpret_cast<vertex_t *>(allocator->translate_udva2sa((uint64_t)&(g_v_bin[vid]))); // compute vertex addr
  //   }
  //   vert->community = vid;
  //   vert->in = 0.0L;
  //   vert->tot = 0.0L;
  //   for(uint64_t i = 0; i < vert->deg; i++){
  //     uint64_t* neigh_ptr = &(vert->neigh_ptr[i]);
  //     double* weight_pt = &(vert->weight_ptr[i]);
  //     if(num_lanes > 2048){
  //       neigh_ptr = reinterpret_cast<uint64_t *>(allocator->translate_udva2sa((uint64_t)&(vert->neigh_ptr[i]))); 
  //       weight_pt = reinterpret_cast<double *>(allocator->translate_udva2sa((uint64_t)&(vert->weight_ptr[i]))); 
  //     }
  //     if(vid == *neigh_ptr){
  //       vert->in  += *weight_pt;
  //     }
  //     vert->tot += *weight_pt;
  //     total_weight += *weight_pt;
  //   }
  //   vert->weight = vert->tot;
  // }
  // total_weight_int = bit_cast<uint64_t, double>(total_weight);
  // // printf("total_weight = %lf (%lu, %lu)\n", total_weight, total_weight, total_weight_int);


  for(uint64_t i = 0; i < num_verts; i++){
    neigh_weight[i] = -1.0;
  }
}

void UDGraph::init(UDGraph *g, double &time){
  /* ------------------ Community Partitation ------------------ */
  neigh_weight = g->neigh_weight;
  neigh_pos = g->neigh_pos;

  /* Initilize Community Partitation */
  // Require to implenment to UpDown

  uint64_t sim_ticks_start, sim_ticks_end;
  UpDown::word_t flag;

  /* ------------------------- UpDown Start ------------------------- */
  sim_ticks_start = rt->getSimTicks();
  UpDown::networkid_t nwid(0, false, 0);
  UpDown::operands_t ops(4);
  ops.set_operand(0, num_verts);
  ops.set_operand(1, num_edges);
  ops.set_operand(2, g_v_bin);
  ops.set_operand(3, num_lanes);

  UpDown::event_t event(louvain_exe::init_graph_phase1_main_control__init, nwid, UpDown::CREATE_THREAD, &ops); // generate start event 
  flag = 0;
  rt->t2ud_memcpy(&flag, sizeof(UpDown::word_t), nwid, 0); // copy the value of flag to the scratchpad of NWID 0

  // start executing
  rt->send_event(event);
  rt->start_exec(nwid);
  rt->test_wait_addr(nwid, 0, 1);
  sim_ticks_end = rt->getSimTicks();
  time += (sim_ticks_end - sim_ticks_start)/2.0/1e9;

  rt->ud2t_memcpy(&total_weight, sizeof(double), nwid, 16);
  rt->ud2t_memcpy(&total_weight_int, sizeof(UpDown::word_t), nwid, 16);
  /* ------------------------- UpDown End ------------------------- */

  // /* ------------------ init1 ------------------ */
  // total_weight = 0;
  // for(uint64_t vid = 0; vid < num_verts; vid++){ // each vertex is a community
  //   vertex_t* vert = &(g_v_bin[vid]);
  //   if(num_lanes > 2048){
  //     vert = reinterpret_cast<vertex_t *>(allocator->translate_udva2sa((uint64_t)&(g_v_bin[vid]))); // compute vertex addr
  //   }
  //   vert->community = vid;
  //   vert->in = 0.0L;
  //   vert->tot = 0.0L;
  //   for(uint64_t i = 0; i < vert->deg; i++){
  //     uint64_t* neigh_ptr = &(vert->neigh_ptr[i]);
  //     double* weight_pt = &(vert->weight_ptr[i]);
  //     if(num_lanes > 2048){
  //       neigh_ptr = reinterpret_cast<uint64_t *>(allocator->translate_udva2sa((uint64_t)&(vert->neigh_ptr[i]))); 
  //       weight_pt = reinterpret_cast<double *>(allocator->translate_udva2sa((uint64_t)&(vert->weight_ptr[i]))); 
  //     }
  //     if(vid == *neigh_ptr){
  //       vert->in  += *weight_pt;
  //     }
  //     vert->tot += *weight_pt;
  //     total_weight += *weight_pt;
  //   }
  //   vert->weight = vert->tot;
  // }
  // total_weight_int = bit_cast<uint64_t, double>(total_weight);
  // // printf("total_weight = %lf (%lu, %lu)\n", total_weight, total_weight, total_weight_int);

}

void UDGraph::one_level(uint64_t &nb_moves, double &time) {
  uint64_t sim_ticks_start, sim_ticks_end;
  UpDown::word_t flag;

  /* ------------------ UpDown ------------------ */
  sim_ticks_start = rt->getSimTicks();
  UpDown::networkid_t nwid(0, false, 0);
  UpDown::operands_t ops(5);
  ops.set_operand(0, num_verts);
  ops.set_operand(1, num_edges);
  ops.set_operand(2, g_v_bin);
  ops.set_operand(3, num_lanes);
  ops.set_operand(4, total_weight_int);

  UpDown::event_t event(louvain_exe::one_level_main_control__init, nwid, UpDown::CREATE_THREAD, &ops); // generate start event 
  flag = 0;
  rt->t2ud_memcpy(&flag, sizeof(UpDown::word_t), nwid, 0); // copy the value of flag to the scratchpad of NWID 0

  // start executing
  rt->send_event(event);
  rt->start_exec(nwid);
  rt->test_wait_addr(nwid, 0, 1);
  sim_ticks_end = rt->getSimTicks();
  time += (sim_ticks_end - sim_ticks_start)/2.0/1e9;
  rt->ud2t_memcpy(&nb_moves, sizeof(UpDown::word_t), nwid, 16);
  
  
  
  /* ------------------ CPU ------------------ */
  // for each vertices: remove the node from its community and insert it in the best community
  for (uint64_t node = 0 ; node < num_verts ; node++) {
    // printf("node = %lu\n", node);
    // fflush(stdout);
    vertex_t* vert = &(g_v_bin[node]);
    if(num_lanes > 2048){
      vert = reinterpret_cast<vertex_t *>(allocator->translate_udva2sa((uint64_t)&(g_v_bin[node])));
    }
    uint64_t node_comm = vert->community;
    
    // computation of all neighboring communities of current node
    /* clean previous neigh_weight */
    uint64_t neigh_last = 0;
    int deg = vert->deg;
    neigh_pos[0] = node_comm;
    neigh_weight[neigh_pos[0]] = 0;
    neigh_last = 1;
    double w_degree = 0;
    for(uint64_t i = 0; i < deg; i++){
      uint64_t* neigh_ptr = &(vert->neigh_ptr[i]);
      if(num_lanes > 2048){
        neigh_ptr = reinterpret_cast<uint64_t *>(allocator->translate_udva2sa((uint64_t)&(vert->neigh_ptr[i]))); 
      }
      uint64_t neigh = *neigh_ptr;
      double* weight_ptr = &(vert->weight_ptr[i]);
      if(num_lanes > 2048){
        weight_ptr = reinterpret_cast<double *>(allocator->translate_udva2sa((uint64_t)&(vert->weight_ptr[i]))); 
      }
      double neigh_w = *weight_ptr;
      vertex_t* vert2 = &(g_v_bin[neigh]);
      if(num_lanes > 2048){
        vert2 = reinterpret_cast<vertex_t *>(allocator->translate_udva2sa((uint64_t)&(g_v_bin[neigh])));
      }
      uint64_t neigh_comm = vert2->community;
      w_degree += neigh_w;
      
      if(neigh != node){
        if(neigh_weight[neigh_comm] == -1){
          neigh_weight[neigh_comm] = 0.0L;
          neigh_pos[neigh_last++] = neigh_comm;
        }
        neigh_weight[neigh_comm] += neigh_w;
      }
    }
    /* Phase 2*/
    vertex_t* vert2 = &(g_v_bin[node_comm]);
    if(num_lanes > 2048){
      vert2 = reinterpret_cast<vertex_t *>(allocator->translate_udva2sa((uint64_t)&(g_v_bin[node_comm])));
    }
    double tmp = vert2->tot - w_degree;
    // compute the nearest community for node
    // default choice for future insertion is the former community
    uint64_t best_comm = neigh_pos[0];
    double best_nblinks  = neigh_weight[neigh_pos[0]];
    double best_increase = best_nblinks - tmp*(w_degree/total_weight);

    for(uint64_t i=1; i < neigh_last; i++){
      vertex_t* vert3 = &(g_v_bin[neigh_pos[i]]);
      if(num_lanes > 2048){
        vert3 = reinterpret_cast<vertex_t *>(allocator->translate_udva2sa((uint64_t)&(g_v_bin[neigh_pos[i]])));
      }
      double increase = neigh_weight[neigh_pos[i]] - vert3->tot*(w_degree/total_weight);
      if(increase > best_increase){
        best_comm = neigh_pos[i];
        best_nblinks = neigh_weight[neigh_pos[i]];
        best_increase = increase;
      }else if(increase == best_increase && best_comm > neigh_pos[i]){
        best_comm = neigh_pos[i];
        best_nblinks = neigh_weight[neigh_pos[i]];
        best_increase = increase;
      }
    }
    vert->new_community = best_comm;
    vert->new_increase = best_increase;
    if (best_comm!=node_comm){
      nb_moves++;
    }
    for (uint64_t i=0 ; i<neigh_last ; i++)
      neigh_weight[neigh_pos[i]]=-1;
    // neigh_last = 0;
  }
}

void UDGraph::compute_comm() {
  // Renumber communities
  // uint64_t *renumber = reinterpret_cast<uint64_t*>(allocator->mm_malloc_global(num_verts * sizeof(uint64_t), blockSize, rt->getMachineConfig().NumNodes, 0));
  uint64_t *renumber = reinterpret_cast<uint64_t*>(malloc(num_verts * sizeof(uint64_t)));
  for(uint64_t i = 0; i < num_verts; i++){ // UpDown
    renumber[i] = -1;
  }
  for(uint64_t node = 0; node < num_verts; node++){ // UpDown
    vertex_t* vert = &(g_v_bin[node]);
    if(num_lanes > 2048){
      vert = reinterpret_cast<vertex_t *>(allocator->translate_udva2sa((uint64_t)&(g_v_bin[node])));
    }
    renumber[vert->community]++;
  }
  uint64_t last = 0;
  for(uint64_t i = 0; i < num_verts; i++){
    // uint64_t * addr = reinterpret_cast< uint64_t *>(allocator->translate_udva2sa((uint64_t)&(renumber[i]))); 
    uint64_t * addr = &(renumber[i]);
    if(addr[0] != -1){
      addr[0] = last++;
      // if(i < 5)
      //   cout << "renumber[" << i << "] = " << renumber[i] << endl;
    }
  }
  printf("current num of comm = %lu\n", last); fflush(stdout);
  free(renumber);
}

UDGraph* UDGraph::partition2UDGraph_binary(double &time) {
  // Renumber communities
  // uint64_t *renumber = reinterpret_cast<uint64_t*>(allocator->mm_malloc_global(num_verts * sizeof(uint64_t), blockSize, rt->getMachineConfig().NumNodes, 0));
  uint64_t *renumber = reinterpret_cast<uint64_t*>(malloc(num_verts * sizeof(uint64_t)));
  for(uint64_t i = 0; i < num_verts; i++){ // UpDown
    renumber[i] = -1;
  }
  for(uint64_t node = 0; node < num_verts; node++){ // UpDown
    vertex_t* vert = &(g_v_bin[node]);
    if(num_lanes > 2048){
      vert = reinterpret_cast<vertex_t *>(allocator->translate_udva2sa((uint64_t)&(g_v_bin[node])));
    }
    renumber[vert->community]++;
  }
  uint64_t last = 0;
  for(uint64_t i = 0; i < num_verts; i++){
    // uint64_t * addr = reinterpret_cast< uint64_t *>(allocator->translate_udva2sa((uint64_t)&(renumber[i]))); 
    uint64_t * addr = &(renumber[i]);
    if(addr[0] != -1){
      addr[0] = last++;
      // if(i < 5)
      //   cout << "renumber[" << i << "] = " << renumber[i] << endl;
    }
  }
  printf("current num of comm = %lu\n", last); fflush(stdout);

  // Compute communities
  // uint64_t **comm_nodes = reinterpret_cast<uint64_t**>(allocator->mm_malloc_global(last * sizeof(uint64_t*), blockSize, rt->getMachineConfig().NumNodes, 0));
  // uint64_t *comm_weight = reinterpret_cast<uint64_t*>(allocator->mm_malloc_global(last * sizeof(uint64_t), blockSize, rt->getMachineConfig().NumNodes, 0));
  // uint64_t *comm_idx = reinterpret_cast<uint64_t*>(allocator->mm_malloc_global(last * sizeof(uint64_t), blockSize, rt->getMachineConfig().NumNodes, 0));
  // uint64_t *comm_deg = reinterpret_cast<uint64_t*>(allocator->mm_malloc_global(last * sizeof(uint64_t), blockSize, rt->getMachineConfig().NumNodes, 0));
  // uint64_t *comm_neigh_idx = reinterpret_cast<uint64_t*>(allocator->mm_malloc_global(last * sizeof(uint64_t), blockSize, rt->getMachineConfig().NumNodes, 0));

  uint64_t **comm_nodes = reinterpret_cast<uint64_t**>(malloc(last * sizeof(uint64_t*)));
  uint64_t *comm_weight = reinterpret_cast<uint64_t*>(malloc(last * sizeof(double)));
  uint64_t *comm_idx = reinterpret_cast<uint64_t*>(malloc(last * sizeof(uint64_t)));
  uint64_t *comm_deg = reinterpret_cast<uint64_t*>(malloc(last * sizeof(uint64_t)));
  uint64_t *comm_neigh_idx = reinterpret_cast<uint64_t*>(malloc(last * sizeof(uint64_t)));

  for(uint64_t node = 0; node < last; node++){ // UpDown
    comm_weight[node] = 0;
    comm_deg[node] = 0;
    comm_neigh_idx[node] = -1;
    comm_idx[node] = 0;
  }
  for(uint64_t node = 0; node < num_verts; node++){ // UpDown
    vertex_t* vert = &(g_v_bin[node]);
    if(num_lanes > 2048){
      vert = reinterpret_cast<vertex_t *>(allocator->translate_udva2sa((uint64_t)&(g_v_bin[node])));
    }
    comm_deg[renumber[vert->community]]++;
    comm_weight[renumber[vert->community]] += vert->vertex_weight;
    // if(renumber[g_v_bin[node].community] == 0){
    //   printf("node %lu, weight %lu\n", node, comm_deg[renumber[g_v_bin[node].community]]);
    // }
  }
  for(uint64_t node = 0; node < last; node++){
    // comm_nodes[node] = reinterpret_cast<uint64_t*>(allocator->mm_malloc_global(comm_deg[node] * sizeof(uint64_t), blockSize, rt->getMachineConfig().NumNodes, 0));
    comm_nodes[node] = reinterpret_cast<uint64_t*>(malloc(comm_deg[node] * sizeof(uint64_t)));
  }
  for(uint64_t node = 0; node < num_verts; node++){
    vertex_t* vert = &(g_v_bin[node]);
    if(num_lanes > 2048){
      vert = reinterpret_cast<vertex_t *>(allocator->translate_udva2sa((uint64_t)&(g_v_bin[node])));
    }
    uint64_t comm = renumber[vert->community];
    comm_nodes[comm][comm_idx[comm]] = node;
    comm_idx[comm]++;
  }

  // Compute weighted UDGraph
  UDGraph* g2 = new UDGraph();
  uint64_t nbc = last;
  g2->rt = rt;
  g2->allocator = allocator;
  g2->num_verts = nbc;
  if((nbc < 4096) || (num_lanes <= 2048)){
    g2->num_lanes = 2048;
    g2->g_v_bin = this->g_v_bin_copy_local;
    g2->nlist_beg = this->nlist_beg_copy_local;
    g2->nlist_weight = this->nlist_weight_copy_local;
    g2->g_v_bin_copy = this->g_v_bin_local;
    g2->nlist_beg_copy = this->nlist_beg_local;
    g2->nlist_weight_copy = this->nlist_weight_local;
  }else{
    g2->num_lanes = num_lanes;
    g2->g_v_bin = this->g_v_bin_copy;
    g2->nlist_beg = this->nlist_beg_copy;
    g2->nlist_weight = this->nlist_weight_copy;
    g2->g_v_bin_copy = this->g_v_bin;
    g2->nlist_beg_copy = this->nlist_beg;
    g2->nlist_weight_copy = this->nlist_weight;
  }

  g2->g_v_bin_local = this->g_v_bin_copy_local;
  g2->nlist_beg_local = this->nlist_beg_copy_local;
  g2->nlist_weight_local = this->nlist_weight_copy_local;
  g2->g_v_bin_copy_local = this->g_v_bin_local;
  g2->nlist_beg_copy_local = this->nlist_beg_local;
  g2->nlist_weight_copy_local = this->nlist_weight_local;

  uint64_t* neigh_ptr = g2->nlist_beg;
  double* weight_ptr = g2->nlist_weight;
  uint64_t offset = 0;
  uint64_t num_verts_edges = 0;
  g2->total_weight = 0;

  for(uint64_t comm = 0; comm < nbc; comm++){
    vertex_t* vert = &(g2->g_v_bin[comm]);
    if(g2->num_lanes > 2048){
      vert = reinterpret_cast<vertex_t *>(allocator->translate_udva2sa((uint64_t)&(g2->g_v_bin[comm])));
    }
    vert->vid = comm;
    vert->vertex_weight = comm_weight[comm];
    vert->neigh_ptr = &(neigh_ptr[offset]);  
    vert->weight_ptr = &(weight_ptr[offset]);
    uint64_t size_c = comm_deg[comm];
    uint64_t comm_deg = 0;
    for(uint64_t node = 0; node < size_c; node++){
      uint64_t node_id = comm_nodes[comm][node];
      vertex_t* vert2 = &(g_v_bin[node_id]);
      if(num_lanes > 2048){
        vert2 = reinterpret_cast<vertex_t *>(allocator->translate_udva2sa((uint64_t)&(g_v_bin[node_id])));
      }
      uint64_t deg = vert2->deg;
      for(uint64_t i=0; i<deg; i++){
        uint64_t* neigh_ptr_tmp = &(vert2->neigh_ptr[i]);
        if(num_lanes > 2048){
          neigh_ptr_tmp = reinterpret_cast<uint64_t *>(allocator->translate_udva2sa((uint64_t)&(vert2->neigh_ptr[i]))); 
        }
        uint64_t neigh = neigh_ptr_tmp[0];
        vertex_t* vert3 = &(g_v_bin[neigh]);
        if(num_lanes > 2048){
          vert3 = reinterpret_cast<vertex_t *>(allocator->translate_udva2sa((uint64_t)&(g_v_bin[neigh])));
        }
        uint64_t neigh_comm = renumber[vert3->community];
        double* weight_ptr_tmp = &(vert2->weight_ptr[i]);
        if(num_lanes > 2048){
          weight_ptr_tmp = reinterpret_cast<double *>(allocator->translate_udva2sa((uint64_t)&(vert2->weight_ptr[i]))); 
        }
        double neigh_weight = weight_ptr_tmp[0];
        // if(comm == 0 && neigh_comm == 1){
        //   cout << "edges(0,1): new weight " << neigh_weight << ", old edge("  << node_id << "," <<  neigh << ")" << endl;
        // }
        g2->total_weight += neigh_weight;
        if(comm_neigh_idx[neigh_comm] == -1){
          comm_neigh_idx[neigh_comm] = comm_deg;
          neigh_ptr_tmp = &(neigh_ptr[offset+comm_deg]);
          if(g2->num_lanes > 2048){
            neigh_ptr_tmp = reinterpret_cast<uint64_t *>(allocator->translate_udva2sa((uint64_t)&(neigh_ptr[offset+comm_deg]))); 
          }
          neigh_ptr_tmp[0] = neigh_comm;
          weight_ptr_tmp = &(weight_ptr[offset+comm_deg]);
          if(g2->num_lanes > 2048){
            weight_ptr_tmp = reinterpret_cast<double *>(allocator->translate_udva2sa((uint64_t)&(weight_ptr[offset+comm_deg]))); 
          }
          weight_ptr_tmp[0] = neigh_weight;
          comm_deg++;
        }else{
          uint64_t idx = comm_neigh_idx[neigh_comm];
          neigh_ptr_tmp = &(neigh_ptr[offset+idx]);
          if(g2->num_lanes > 2048){
            neigh_ptr_tmp = reinterpret_cast<uint64_t *>(allocator->translate_udva2sa((uint64_t)&(neigh_ptr[offset+idx]))); 
          }
          if(neigh_ptr_tmp[0] != neigh_comm){
            printf("Error, neigh_ptr[offset+idx] != neigh_comm\n");
            fflush(stdout);
            exit(1);
          }
          weight_ptr_tmp = &(weight_ptr[offset+idx]);
          if(g2->num_lanes > 2048){
            weight_ptr_tmp = reinterpret_cast<double *>(allocator->translate_udva2sa((uint64_t)&(weight_ptr[offset+idx]))); 
          }
          weight_ptr_tmp[0] += neigh_weight;
        }
      }
    }
    vert->edges_before = num_verts_edges;
    num_verts_edges += comm_deg;
    vert->deg = comm_deg;
    for(uint64_t i  = 0; i < comm_deg; i++){
      uint64_t* neigh_ptr_tmp = &(neigh_ptr[offset+i]);
      if(g2->num_lanes > 2048){
        neigh_ptr_tmp = reinterpret_cast<uint64_t *>(allocator->translate_udva2sa((uint64_t)&(neigh_ptr[offset+i]))); 
      }
      uint64_t neigh_comm = neigh_ptr_tmp[0];
      comm_neigh_idx[neigh_comm] = -1;
    }
    if(comm_deg % 8 > 0){
      comm_deg = (comm_deg / 8) * 8 + 8;
    }
    offset += comm_deg;
  }

  g2->nlist_size = offset;
  g2->num_edges = num_verts_edges;
  // printf("0000000\n"); fflush(stdout);
  if(g2->num_lanes > 2048){
    int64_t nnodes = ((g2->num_edges + (2048 * NUM_THREADS * 8) - 1) / (2048 * NUM_THREADS * 8)) + 1;
    while((nnodes * 2048 * 2) <= g2->num_lanes){
      g2->num_lanes = g2->num_lanes / 2;
    }
    printf("new num of lanes = %lu\n", g2->num_lanes); fflush(stdout);
  }
  free(renumber);
  for(uint64_t i = 0; i < nbc; i++){
    uint64_t *tmp = comm_nodes[i];
    free(tmp);
  }
  free(comm_nodes);
  free(comm_weight);
  free(comm_idx);
  free(comm_deg);
  free(comm_neigh_idx);
  // printf("111111\n"); fflush(stdout);

  return g2;
}

