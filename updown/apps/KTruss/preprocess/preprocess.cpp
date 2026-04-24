#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <map>
#include <vector>
#include <cassert>
#include <algorithm>
#include <set>
#include <cstring>

typedef uint64_t* ptr;

typedef struct vertex{
  uint64_t deg;
  uint64_t id;
  ptr neigh;
} vertex_t;


using namespace std;

uint64_t nnodes = 0;
uint64_t nedeges = 0;
vector< set<uint64_t> > adj_list;
vector<uint64_t> deg_list;


vector< pair<uint64_t, uint64_t> > degree_vec;
map<uint64_t, uint64_t> index_map;
map<uint64_t, uint64_t> index_map2;

map<int, int> vertex_id;


uint64_t read_graph(char  * filename, int m)
{
    std::ifstream fin(filename);
    std::string line;
    std::istringstream sin(line);
    uint64_t id = 1;
    bool first_line = true;
    uint64_t *vertex_id = NULL;
    nnodes = m;
    adj_list.resize(nnodes);
    deg_list.resize(nnodes);
    vertex_id = (uint64_t *)malloc(nnodes*sizeof(uint64_t));
    memset(vertex_id, 0, nnodes*sizeof(uint64_t));
    
    while (getline(fin, line) && (line[0] != '\n'))
    {
        if(line[0] == '%' || line[0] == '\n'){
            continue;
        }
        std::istringstream sin(line);
        /* filter out no-edge vertices */
        uint64_t tmp;
        uint64_t v1, v2;
//        cout << line << endl;
        sin >> v1 >> v2;
//        cout << v1 << v2;
//        printf("%d %d\n",v1,v2);
        if(vertex_id[v1] == 0)
        {
            vertex_id[v1] = id;
            id++;
        }
        if(vertex_id[v2] == 0)
        {
            vertex_id[v2] = id;
            id++;
        }
        if(vertex_id[v1] != vertex_id[v2])
        {
            adj_list[vertex_id[v1]-1].insert(vertex_id[v2]-1);
            adj_list[vertex_id[v2]-1].insert(vertex_id[v1]-1);
        }
        
    }

    nnodes = id - 1;
    free(vertex_id);
    fin.close();
    return 0;
}


void build_degree_vec()
{
    degree_vec.clear();
    uint64_t i = 0;
    nedeges = 0;
    for(i=0; i<nnodes; i++){
        degree_vec.push_back(pair<uint64_t, uint64_t>(i, adj_list[i].size()));
        nedeges = adj_list[i].size() + nedeges;
    }
}

bool vec_cmp(pair<int, int> a, pair<int, int> b) {
    return a.second > b.second;
}

void node_index_reorder()
{
    uint64_t id;
    for(uint64_t i=0;i<nnodes;i++)
    {
        id = degree_vec[i].first;
        index_map.insert( pair<uint64_t, uint64_t>(id,i) );
        index_map2.insert( pair<uint64_t, uint64_t>(i,id) );
        
//        cout << id << " " << index_map[id] << " " << i << endl;
    }
}

void transfer_graph(char  * filename, char *output_filename)
{
    
    std::ifstream fin(filename);
    std::string line;
    std::ofstream fout(output_filename);
    while (std::getline(fin, line) && (line[0] == '#'))
    {
        fout << line << endl;
    }
    
    uint64_t tmp_i;
    for(tmp_i=0; tmp_i<nnodes; tmp_i++)
    {
        uint64_t i = index_map2[tmp_i];
        uint64_t degree = 0;
        set<uint64_t> list_tmp;
        for (set<uint64_t>::iterator iter = adj_list[i].begin(); iter != adj_list[i].end(); iter++)
        {
            list_tmp.insert(index_map[*iter]);
        }
        for (set<uint64_t>::iterator iter = list_tmp.begin(); iter != list_tmp.end(); iter++)
        {
            if(tmp_i > *iter)
            {
                fout << tmp_i << " " << *iter << endl;
                degree++;
            }
        }
        deg_list[tmp_i] = degree;

    }
    
    return;
}


void transfer2bin(char  * filename)
{

    uint64_t **adjlists; // Adjacency lists
    uint64_t* vertices;
    uint64_t* degrees;

    std::string binfile, binfile_gv, binfile_nl, binfile_jac;
    char* binfilename;
    FILE* out_file, *in_file;

    uint64_t num_nodes = nnodes;

    printf("num_nodes = %d\n",num_nodes);

    adjlists = (uint64_t**)malloc(num_nodes*sizeof(uint64_t*));
    vertices = (uint64_t*)malloc(num_nodes*sizeof(uint64_t));
    degrees = (uint64_t*)malloc(num_nodes*sizeof(uint64_t));


    uint64_t data;
    struct vertex *g_v_bin = (struct vertex*)malloc(num_nodes*sizeof(struct vertex));
    uint64_t ranked=0;
    uint64_t neighbor_array_size=0;
  
    uint64_t ii = 0;
    uint64_t kk = 0;
    uint64_t max_deg = adj_list[0].size();
 
    for(kk=0; kk<num_nodes; kk++){
        uint64_t i = index_map2[kk];
        vertices[ranked] = kk;
        degrees[ranked] = deg_list[kk]; 
        uint64_t* adjlist_local = NULL;
        if (degrees[ranked] > 0)
        {
            adjlist_local = new uint64_t[degrees[ranked]*2];
            neighbor_array_size += degrees[ranked]*2;
            uint64_t e=0;
            set<uint64_t> list_tmp;
            for (set<uint64_t>::iterator iter = adj_list[i].begin(); iter != adj_list[i].end(); iter++)
            {
                list_tmp.insert(index_map[*iter]);
            }
            for (set<uint64_t>::iterator iter = list_tmp.begin(); e < degrees[ranked] && iter != list_tmp.end(); iter++)
            // for (set<int>::iterator iter = adj_list[i].begin(); e < degrees[ranked] && iter != adj_list[i].end(); iter++)
            {
                uint64_t vid = (*iter);
                adjlist_local[2*e] = vid;
                adjlist_local[2*e+1] = 0;
                e++;
            }
        }
        adjlists[ii++] = adjlist_local;
        ranked++;
    }
    printf("Adjacency Lists created\n");

    binfile = std::string(filename) + ".bin";
    binfile_gv = std::string(filename) + "_gv" + ".bin";
    binfile_nl = std::string(filename) + "_nl" + ".bin";
    
    binfilename = const_cast<char*>(binfile.c_str()); 

    printf("Binfile:%s\n", binfilename);
    out_file = fopen(binfilename, "wb");
    if (!out_file) {
          exit(EXIT_FAILURE);
    }
    fseek(out_file, 0, SEEK_SET);
    printf("Size of uint64_t:%d, writing num_nodes:%d, neighbor_array_size:%d\n", sizeof(uint64_t), num_nodes, neighbor_array_size);
    fwrite(&num_nodes, sizeof(uint64_t), 1, out_file);
    fwrite(&neighbor_array_size, sizeof(uint64_t), 1, out_file);
    for(uint64_t i = 0; i < num_nodes; i++){
      fwrite(&degrees[i], sizeof(degrees[i]), 1, out_file);
      fwrite(&vertices[i], sizeof(vertices[i]), 1, out_file);
      fwrite(adjlists[i], sizeof(uint64_t), degrees[i], out_file);
    //   printf("%d ",i);
    }
    fclose(out_file);

    binfilename = const_cast<char*>(binfile_gv.c_str()); 
    printf("Binfile:%s\n", binfilename);
    out_file = fopen(binfilename, "wb");
    if (!out_file) {
          exit(EXIT_FAILURE);
    }
    fseek(out_file, 0, SEEK_SET);
    printf("Size of uint64_t:%d, writing num_nodes:%llu in new file\n", sizeof(uint64_t), num_nodes);
    fwrite(&num_nodes,sizeof(uint64_t),1,out_file);
    for(uint64_t i=0; i< num_nodes;i++){
      fwrite(&degrees[i], sizeof(degrees[i]), 1, out_file);
      fwrite(&vertices[i], sizeof(vertices[i]), 1, out_file);
      fwrite(&adjlists[i], sizeof(adjlists[i]), 1, out_file);
    }
    fclose(out_file);

//     FILE* in_file_gv = fopen( binfilename, "rb");
//   if (!in_file_gv) {
//         exit(EXIT_FAILURE);
//   }
//     fseek(in_file_gv, 0, SEEK_SET);
//     uint64_t num_verts;
//     fread(&num_verts, sizeof(uint64_t),1, in_file_gv);
//      printf("num_verts = %lu %lu\n",num_verts, num_nodes);
//      fclose(in_file_gv);
  
    binfilename = const_cast<char*>(binfile_nl.c_str()); 
    printf("Binfile:%s\n", binfilename);
    out_file = fopen(binfilename, "wb");
    if (!out_file) {
          exit(EXIT_FAILURE);
    }
    fseek(out_file, 0, SEEK_SET);
    printf("Size of uint64_t:%d, writing nlarray:%d in NL\n", sizeof(uint64_t), neighbor_array_size);
    fwrite(&neighbor_array_size,sizeof(uint64_t), 1, out_file);
    for(uint64_t i=0; i< num_nodes;i++)
    {
      fwrite(adjlists[i], sizeof(uint64_t), degrees[i]*2, out_file);
    }
    fclose(out_file);
}

int main(int argc, char *argv[])
{
    if(argc!= 4)
    {
        printf("%s <input_filename> <output_filename>  <num_vertex>\n",argv[0]);
    }
    char* input_filename = argv[1];
    char* output_filename = argv[2];
    int num_v = atoi(argv[3]);

    read_graph(input_filename, num_v);
    printf("read_graph\n"); fflush(stdout);
    build_degree_vec();
    printf("build_degree_vec\n"); fflush(stdout);
    sort(degree_vec.begin(), degree_vec.end(), vec_cmp);
    printf("sort\n"); fflush(stdout);
    node_index_reorder();
    printf("node_index_reorder\n"); fflush(stdout);
    transfer_graph(input_filename, output_filename);
    printf("transfer_graph\n"); fflush(stdout);
    transfer2bin(output_filename);
    printf("transfer2bin\n"); fflush(stdout);
    
    return 0;
    
}

