#include "common.h"

template <class To, class From>
std::enable_if_t<sizeof(To) == sizeof(From) &&
                     std::is_trivially_copyable_v<From> &&
                     std::is_trivially_copyable_v<To>,
                 To>
// constexpr support needs compiler magic
bit_cast2(const From &src) noexcept {
  static_assert(std::is_trivially_constructible_v<To>,
                "This implementation additionally requires "
                "destination type to be trivially constructible");

  To dst;
  std::memcpy(&dst, &src, sizeof(To));
  return dst;
}



class Graph {
public:
  uint64_t num_verts;
  uint64_t num_edges;
  uint64_t nlist_size;
  double total_weight;
  double precision;
  vertex_t* g_v_bin;
  uint64_t neigh_last;

  uint64_t *n2c;
  double* in;
  double* tot;
  double* neigh_weight;
  uint64_t *neigh_pos;

  uint64_t *n2c_new;
  uint64_t *n2c_old;
  double * new_increase;
  double* in_new;
  double* tot_new;

  bool filter_flag;


  Graph();
  ~Graph();
  Graph(char *filename_v, char *filename_e, char *filename_w = NULL);
  double nb_selfloops(uint64_t vid);
  double weighted_degree(uint64_t vid);
  void init();
  double quality();
  void remove(uint64_t node, uint64_t comm, double dnodecomm);
  void insert(uint64_t node, uint64_t comm, double dnodecomm);
  double gain(uint64_t node, uint64_t comm, double dnodecomm, double w_degree);
  double gain0(uint64_t node, uint64_t comm, double dnodecomm, double w_degree);
  void neigh_comm(uint64_t vid);
  void one_level();
  Graph* partition2graph_binary();
  void re_compute_attr();
  void re_compute_attr1();
  void re_compute_attr2();
};

Graph::~Graph(){
  free(n2c);
  free(in);
  free(tot);
  free(neigh_weight);
  free(neigh_pos);
  free(n2c_new);
  free(n2c_old);
  free(in_new);
  free(tot_new);
  free(new_increase);

  free(g_v_bin[0].neigh_ptr);
  free(g_v_bin[0].weight_ptr);
  // cout << g_v_bin << endl;
  free(g_v_bin);
}

Graph::Graph(){
  num_verts = 0;
  num_edges = 0;
  nlist_size = 0;
  total_weight = 0.0;
  precision = 0.000001L;
  g_v_bin = NULL;
  neigh_last = 0;
  n2c = NULL;
  in = NULL;
  neigh_weight = NULL;
  neigh_pos = NULL;
  filter_flag = true;
}

void Graph::remove(uint64_t node, uint64_t comm, double dnodecomm){
  assert(node >= 0 && node < num_verts);
  in_new[comm] -= 2.0L*dnodecomm + this->nb_selfloops(node);
  tot_new[comm] -= this->weighted_degree(node);
  // n2c[node] = -1;
}

void Graph::insert(uint64_t node, uint64_t comm, double dnodecomm){
  assert(node >= 0 && node < num_verts);
  in_new[comm] += 2.0L*dnodecomm + this->nb_selfloops(node);
  tot_new[comm] += this->weighted_degree(node);
  n2c_new[node] = comm;
  // n2c_[node] = comm;
}

double Graph::gain(uint64_t node, uint64_t comm, double dnodecomm, double w_degree){
  assert(node >= 0 && node < num_verts);
  double totc = tot[comm];
  double m2   = this->total_weight;
  // if(node == 0 && comm == 855){
  //   printf("dnodecomm = 0x%lx, totc = 0x%lx 0x%lx, w_degree/m2 = 0x%lx, w_degree = 0x%lx\n", bit_cast2<uint64_t, double>(dnodecomm), bit_cast2<uint64_t, double>(totc), &(tot[7308]), bit_cast2<uint64_t, double>((w_degree/m2)), bit_cast2<uint64_t, double>((w_degree)));
  // }
  return (dnodecomm - totc*(w_degree/m2));
}

double Graph::gain0(uint64_t node, uint64_t comm, double dnodecomm, double w_degree){
  assert(node >= 0 && node < num_verts);
  double totc = tot[comm] - this->weighted_degree(node);
  double m2   = this->total_weight;
  // if(node == 3529){
  //   printf("old cid = %lu, best_nblinks = 0x%lx, tot = 0x%lx, w_deg = 0x%lx, w_degree/total_weight = 0x%lx\n", comm, bit_cast2<uint64_t, double>(dnodecomm), bit_cast2<uint64_t, double>(tot[comm]), bit_cast2<uint64_t, double>(this->weighted_degree(node)), bit_cast2<uint64_t, double>(w_degree/m2));
  // }
  return (dnodecomm - totc*(w_degree/m2));
}

double Graph::weighted_degree(uint64_t vid){
  assert(vid >= 0 && vid < num_verts);
  double res = 0.0L;
  for(uint64_t i = 0; i < g_v_bin[vid].deg; i++){
    res += g_v_bin[vid].weight_ptr[i];
  }
  return res;
}

double Graph::nb_selfloops(uint64_t vid){
  assert(vid >= 0 && vid < num_verts);
  double res = 0.0L;
  for(uint64_t i = 0; i < g_v_bin[vid].deg; i++){
    if(vid == g_v_bin[vid].neigh_ptr[i]){
      res += g_v_bin[vid].weight_ptr[i];
    }
  }
  return res;
}

void Graph::re_compute_attr(){
  uint64_t num_moves = 0;
  for(uint64_t i = 0; i < num_verts; i++){
    if(filter_flag){
      if(n2c[i] < n2c_new[i]){
        num_moves++;
      }
    }else{
      if(n2c[i] > n2c_new[i]){
        num_moves++;
      }
    }
  }
  if(num_moves == 0){
    this->filter_flag = !(this->filter_flag);
    printf("Reverse CPU\n");
  }

  for(uint64_t i = 0; i < num_verts; i++){
    uint64_t old_comm = n2c[i];
    if(filter_flag){
      if(n2c[i] < n2c_new[i]){
        n2c[i] = n2c_new[i];
      }
    }else{
      if(n2c[i] > n2c_new[i]){
        n2c[i] = n2c_new[i];
      }
    }
    n2c_old[i] = old_comm;
    in[i] = 0.0;
    tot[i] = 0.0;
  }
  for(uint64_t i = 0; i < num_verts; i++){
    uint64_t cid = n2c[i];
    for(uint64_t j = 0; j < g_v_bin[i].deg; j++){
      uint64_t neigh_vid = g_v_bin[i].neigh_ptr[j];
      double neigh_weight = g_v_bin[i].weight_ptr[j];
      uint64_t neigh_comm = n2c[neigh_vid];
      if(cid == neigh_comm){
        in[cid] += neigh_weight;
      }
      tot[cid] += neigh_weight;
    }
  }
  return;
}

void Graph::re_compute_attr1(){
  for(uint64_t i = 0; i < num_verts; i++){
    if(filter_flag){
      if(n2c_old[i] < n2c_new[i]){
        n2c[i] = n2c_new[i];
      }else{
        n2c[i] = n2c_old[i];
      }
    }else{
      if(n2c_old[i] > n2c_new[i]){
        n2c[i] = n2c_new[i];
      }else{
        n2c[i] = n2c_old[i];
      }
    }
    in[i] = 0.0;
    tot[i] = 0.0;
  }
  for(uint64_t i = 0; i < num_verts; i++){
    uint64_t cid = n2c[i];
    for(uint64_t j = 0; j < g_v_bin[i].deg; j++){
      uint64_t neigh_vid = g_v_bin[i].neigh_ptr[j];
      double neigh_weight = g_v_bin[i].weight_ptr[j];
      uint64_t neigh_comm = n2c[neigh_vid];
      if(cid == neigh_comm){
        in[cid] += neigh_weight;
      }
      tot[cid] += neigh_weight;
    }
  }
  return;
}

void Graph::re_compute_attr2(){
  for(uint64_t i = 0; i < num_verts; i++){
    n2c[i] = n2c_old[i];
    in[i] = 0.0;
    tot[i] = 0.0;
  }
  for(uint64_t i = 0; i < num_verts; i++){
    uint64_t cid = n2c[i];
    for(uint64_t j = 0; j < g_v_bin[i].deg; j++){
      uint64_t neigh_vid = g_v_bin[i].neigh_ptr[j];
      double neigh_weight = g_v_bin[i].weight_ptr[j];
      uint64_t neigh_comm = n2c[neigh_vid];
      if(cid == neigh_comm){
        in[cid] += neigh_weight;
      }
      tot[cid] += neigh_weight;
    }
  }
  return;
}

double Graph::quality() {
  double q  = 0.0L;
  double m = this->total_weight;
  for(uint64_t i=0; i < num_verts; i++){
    if(tot[i] > 0){
      q += in[i] - (tot[i]*tot[i])/m;
    }
  }
  q /= m;
  return q;
}

Graph::Graph(char *vertex_filename, char *edge_filename, char *edge_weight_filename) {
  this->filter_flag = true;
  /* ------------------ Load Graph ------------------ */
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
  file_size = fread(&num_verts, sizeof(num_verts),1, in_file_gv);
  file_size = fread(&num_edges, sizeof(num_edges),1, in_file_gv);
  file_size = fread(&nlist_size, sizeof(nlist_size), 1, in_file_nl);

  g_v_bin = reinterpret_cast<vertex_t *>(malloc(num_verts * sizeof(vertex_t)));
  uint64_t* nlist_beg = reinterpret_cast<uint64_t*>(malloc(nlist_size * sizeof(uint64_t)));
  double* nlist_weight = reinterpret_cast<double*>(malloc(nlist_size * sizeof(double)));
  
  file_size = fread(g_v_bin, sizeof(vertex_t), num_verts, in_file_gv); // read in all vertices 
  file_size = fread(nlist_beg, sizeof(uint64_t), nlist_size, in_file_nl); // read in all edges
  fclose(in_file_gv);
  fclose(in_file_nl);

  if(in_file_weight_nl != NULL) {
    file_size = fread(nlist_weight, sizeof(double), nlist_size, in_file_weight_nl); // read in all edge weight
    fclose(in_file_weight_nl);
  }else{
    for(uint64_t i = 0; i < nlist_size; i++){
      nlist_weight[i] = 1.0;
    }
  }

  uint64_t max_deg = 0;
  for(uint64_t i = 0; i < num_verts; i++){
    uint64_t offset = (uint64_t)(g_v_bin[i].neigh_ptr);
    uint64_t * loc_nlist = nlist_beg + offset;
    double * loc_weight_nlist = nlist_weight + offset;
		uint64_t deg = g_v_bin[i].deg;
		g_v_bin[i].neigh_ptr = loc_nlist;
    g_v_bin[i].weight_ptr = loc_weight_nlist;
    g_v_bin[i].vertex_weight = 1;
		// num_edges += deg;
		if (max_deg < deg)
			max_deg = deg;
    total_weight += this->weighted_degree(i);
  }
  printf("# vertices: %lu , # edges:%lu , avg deg: %lf, max deg: %lu, total edge size: %lu bytes\n", num_verts, num_edges, ((double)num_edges)/num_verts, max_deg, nlist_size * sizeof(uint64_t));
}

void Graph::init(){
  /* ------------------ Community Partitation ------------------ */
  precision = 0.000001L;
  n2c = reinterpret_cast<uint64_t*>(malloc(num_verts * sizeof(uint64_t)));
  in = reinterpret_cast<double*>(malloc(num_verts * sizeof(double)));
  tot = reinterpret_cast<double*>(malloc(num_verts * sizeof(double)));

  n2c_new = reinterpret_cast<uint64_t *>(malloc(num_verts * sizeof(uint64_t)));
  n2c_old = reinterpret_cast<uint64_t *>(malloc(num_verts * sizeof(uint64_t)));
  in_new = reinterpret_cast<double*>(malloc(num_verts * sizeof(double)));
  tot_new = reinterpret_cast<double*>(malloc(num_verts * sizeof(double)));
  new_increase = reinterpret_cast<double *>(malloc(num_verts * sizeof(double)));

  /* Initilize Community Partitation */
  total_weight = 0;
  for(uint64_t i = 0; i < num_verts; i++){ // each vertex is a community
    n2c[i] = i;
    in[i] = this->nb_selfloops(i);
    tot[i] = this->weighted_degree(i);
    total_weight += tot[i];
  }

  neigh_weight = reinterpret_cast<double*>(malloc(num_verts * sizeof(uint64_t)));
  neigh_pos = reinterpret_cast<uint64_t*>(malloc(num_verts * sizeof(uint64_t)));
  neigh_last = 0;
  for(uint64_t i = 0; i < num_verts; i++){
    neigh_weight[i] = -1;
  }
}

void Graph::neigh_comm(uint64_t node) {
  /* clean previous neigh_weight */
  for (uint64_t i=0 ; i<neigh_last ; i++){
    neigh_weight[neigh_pos[i]]=-1.0;
  }
  neigh_last = 0;
  int deg = g_v_bin[node].deg;
  neigh_pos[0] = n2c[node];
  neigh_weight[neigh_pos[0]] = 0;
  neigh_last = 1;

  for(uint64_t i = 0; i < deg; i++){
    uint64_t neigh = g_v_bin[node].neigh_ptr[i];
    uint64_t neigh_comm = n2c[neigh];
    double neigh_w = g_v_bin[node].weight_ptr[i];
    // if(node == 1)
    //    cout << node << " -> " << neigh << ": comm = " << n2c[neigh] << ", weight = " << neigh_w << " " << g_v_bin[0].weight_ptr[i]  << ", i = " << i << endl;

    if(neigh != node){
      if(neigh_weight[neigh_comm] == -1.0){
        neigh_weight[neigh_comm] = 0.0L;
        neigh_pos[neigh_last++] = neigh_comm;
      }
      neigh_weight[neigh_comm] += neigh_w;
      // if(node == 60 && neigh_comm == 15624){
      //   cout << neigh << ":" << neigh_w << ":" << neigh_weight[neigh_comm] << endl;
      // }
    }
  }
  // if(node == 1){
  //   for (int i=0 ; i<neigh_last ; i++) 
  //   {
  //     uint64_t neigh_comm = neigh_pos[i];
  //     cout << i << ": comm = " << neigh_comm << ", weight = " << neigh_weight[neigh_comm] << endl;
  //   }
  // }
}

void Graph::one_level() {
  // for each vertices: remove the node from its community and insert it in the best community
  for (uint64_t node = 0 ; node < num_verts ; node++) {
    uint64_t node_comm = n2c[node];
    double  w_degree = this->weighted_degree(node);

    // computation of all neighboring communities of current node
    this->neigh_comm(node);
    // remove node from its current community
    this->remove(node, node_comm, neigh_weight[node_comm]);

    // compute the nearest community for node
    // default choice for future insertion is the former community
    uint64_t best_comm = neigh_pos[0];
    double best_nblinks  = neigh_weight[neigh_pos[0]];
    double best_increase = this->gain0(node, neigh_pos[0], neigh_weight[neigh_pos[0]], w_degree);
    for(uint64_t i=1; i < neigh_last; i++){
      double increase = this->gain(node, neigh_pos[i], neigh_weight[neigh_pos[i]], w_degree);
      if(increase > best_increase){
        best_comm = neigh_pos[i];
        best_nblinks = neigh_weight[neigh_pos[i]];
        best_increase = increase;
      }else if(increase == best_increase && best_comm > neigh_pos[i]){
        best_comm = neigh_pos[i];
        best_nblinks = neigh_weight[neigh_pos[i]];
        best_increase = increase;
      }
      // if(node == 1){
      //   cout << node << "->" << neigh_pos[i] << ": increase = " << increase << ", best = " << best_increase << ", best_comm = " << best_comm << endl;
      // }
    }

    // insert node in the nearest community
    this->insert(node, n2c[node], best_nblinks);
    n2c_new[node] = best_comm;
    new_increase[node] = best_increase;
    // cout << "comm[" << node << "]:" << best_comm << endl;
  }
}

Graph* Graph::partition2graph_binary() {
  // Renumber communities
  uint64_t *renumber = reinterpret_cast<uint64_t*>(malloc(num_verts * sizeof(uint64_t)));
  for(uint64_t i = 0; i < num_verts; i++){
    renumber[i] = -1;
  }
  for(uint64_t node = 0; node < num_verts; node++){
    renumber[n2c[node]]++;
  }
  uint64_t last = 0;
  for(uint64_t i = 0; i < num_verts; i++){
    if(renumber[i] != -1){
      renumber[i] = last++;
      // if(i < 5)
      //   cout << "renumber[" << i << "] = " << renumber[i] << endl;
      
    }
  }

  // Compute communities
  uint64_t **comm_nodes = reinterpret_cast<uint64_t**>(malloc(last * sizeof(uint64_t*)));
  uint64_t *comm_weight = reinterpret_cast<uint64_t *>(malloc(last * sizeof(uint64_t)));
  uint64_t *comm_idx = reinterpret_cast<uint64_t*>(malloc(last * sizeof(uint64_t)));
  uint64_t *comm_deg = reinterpret_cast<uint64_t*>(malloc(last * sizeof(uint64_t)));
  uint64_t *comm_neigh_idx = reinterpret_cast<uint64_t*>(malloc(last * sizeof(uint64_t)));
  for(uint64_t node = 0; node < last; node++){
    comm_weight[node] = 0;
    comm_deg[node] = 0;
    comm_neigh_idx[node] = -1;
  }
  for(uint64_t node = 0; node < num_verts; node++){
    comm_deg[renumber[n2c[node]]]++;
    comm_weight[renumber[n2c[node]]] += g_v_bin[node].vertex_weight;
    // if(renumber[n2c[node]] == 0){
    //   printf("node %lu, weight %lu\n", node, g_v_bin[node].weight);
    // }
  }
  for(uint64_t node = 0; node < last; node++){
    comm_nodes[node] = reinterpret_cast<uint64_t*>(malloc(comm_deg[node] * sizeof(uint64_t)));
    comm_idx[node] = 0;
  }
  for(uint64_t node = 0; node < num_verts; node++){
    uint64_t comm = renumber[n2c[node]];
    comm_nodes[comm][comm_idx[comm]] = node;
    comm_idx[comm]++;
  }

  // Compute weighted graph
  Graph* g2 = new Graph();
  uint64_t nbc = last;
  g2->num_verts = nbc;
  g2->g_v_bin = reinterpret_cast<vertex_t *>(malloc(nbc * sizeof(vertex_t)));
  uint64_t * neigh_ptr = reinterpret_cast<uint64_t *>(malloc(nlist_size * sizeof(uint64_t)));
  double* weight_ptr =  reinterpret_cast<double*>(malloc(nlist_size * sizeof(double)));
  uint64_t offset = 0;
  uint64_t num_verts_edges = 0;
  g2->total_weight = 0;

  for(uint64_t comm = 0; comm < nbc; comm++){
    g2->g_v_bin[comm].vid = comm;
    g2->g_v_bin[comm].vertex_weight = comm_weight[comm];
    g2->g_v_bin[comm].neigh_ptr = &(neigh_ptr[offset]);
    g2->g_v_bin[comm].weight_ptr = &(weight_ptr[offset]);
    uint64_t size_c = comm_deg[comm];
    uint64_t comm_deg = 0;
    for(uint64_t node = 0; node < size_c; node++){
      uint64_t node_id = comm_nodes[comm][node];
      uint64_t deg = g_v_bin[node_id].deg;
      for(uint64_t i=0; i<deg; i++){
        uint64_t neigh = g_v_bin[node_id].neigh_ptr[i];
        uint64_t neigh_comm = renumber[n2c[neigh]];
        double neigh_weight = g_v_bin[node_id].weight_ptr[i];
        // if(comm == 0 && neigh_comm == 1){
        //   cout << "edges(0,1): new weight " << neigh_weight << ", old edge("  << node_id << "," <<  neigh << ")" << endl;
        // }
        g2->total_weight += neigh_weight;
        if(comm_neigh_idx[neigh_comm] == -1){
          comm_neigh_idx[neigh_comm] = comm_deg;
          neigh_ptr[offset+comm_deg] = neigh_comm;
          weight_ptr[offset+comm_deg] = neigh_weight;
          comm_deg++;
        }else{
          uint64_t idx = comm_neigh_idx[neigh_comm];
          if(neigh_ptr[offset+idx] != neigh_comm){
            printf("Error, neigh_ptr[offset+idx] != neigh_comm\n");
            fflush(stdout);
            exit(1);
          }
          weight_ptr[offset+idx] += neigh_weight;
        }
      }
    }
    
    num_verts_edges += comm_deg;
    g2->g_v_bin[comm].deg = comm_deg;
    for(uint64_t i  = 0; i < comm_deg; i++){
      uint64_t neigh_comm = neigh_ptr[offset+i];
      comm_neigh_idx[neigh_comm] = -1;

    }
    if(comm_deg % 8 > 0){
      comm_deg = (comm_deg / 8) * 8 + 8;
    }
    offset += comm_deg;
  }
  g2->nlist_size = offset;
  g2->num_edges = num_verts_edges;
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

  return g2;
}