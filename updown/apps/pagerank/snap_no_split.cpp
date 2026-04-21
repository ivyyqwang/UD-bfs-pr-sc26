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

typedef struct Vertex{
  uint64_t id;
  uint64_t deg;
  uint64_t padding;
  double val;
}vertex_t;

using namespace std;

uint64_t nnodes = 0;
uint64_t nedeges = 0;
std::set<uint64_t>* adj_list;
uint64_t total_verts = 0;


uint64_t read_graph(char  * filename, uint64_t max_v)
{
    std::ifstream fin(filename);
    std::string line;
    std::istringstream sin(line);
    uint64_t id = 1;
    bool first_line = true;
    double edges_tmp = 0;

    nnodes = max_v;
    first_line = false;
    std::unordered_map<uint64_t, uint64_t> vertex_id;
    adj_list = new std::set<uint64_t>[nnodes];
    uint64_t num_lines = 0;
          
    while (getline(fin, line) && (line[0] != '\n'))
    {
        if(line[0] == '\n' || line[0] == '#'){
            continue;
        }
        std::istringstream sin(line);
        /* filter out no-edge vertices */
        uint64_t tmp;
        uint64_t v1, v2;
        // cout << line << endl;
        if(num_lines == 0){
            num_lines++;
            if(sin >> v1 >> v2 >> tmp){
                printf("%ld %ld %ld\n", v1, v2, tmp); fflush(stdout);
                continue;
            }else{
                printf("%d %d\n",v1,v2); fflush(stdout);
            }
        }else{
            sin >> v1 >> v2;
        }
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
            if(vertex_id[v1] > nnodes){
                printf("Error vertex_id1 = %lu > nnodes = %ld\n", vertex_id[v1], nnodes);
                fflush(stdout);
            }
            if(vertex_id[v2] > nnodes){
                printf("Error vertex_id2 = %lu > nnodes = %ld\n", vertex_id[v2], nnodes);
                fflush(stdout);
            }
            adj_list[vertex_id[v1]-1].insert(vertex_id[v2]-1);
            adj_list[vertex_id[v2]-1].insert(vertex_id[v1]-1);
            edges_tmp = edges_tmp + 2;
        }
        
    }
    // printf("undirected edges = %lg\n", edges_tmp);
    // fflush(stdout);
    nnodes = id - 1;

    printf("vertices = %lu, undirected edges = %lg\n", nnodes, edges_tmp);
    fflush(stdout);

    
    fin.close();
    return 0;
}

void gv_bin(char  * filename, vertex_t *verts){
    std::string binfile_gv = std::string(filename) + "_gv" + ".bin";
    char* binfilename = const_cast<char*>(binfile_gv.c_str()); 
    printf("Binfile:%s\n", binfilename);
    FILE* out_file = fopen(binfilename, "wb");
    if (!out_file) {
          exit(EXIT_FAILURE);
    }
    fseek(out_file, 0, SEEK_SET);
    size_t size = fwrite(&nnodes, sizeof(uint64_t), 1, out_file);
    size = fwrite(verts, sizeof(vertex_t), total_verts, out_file);
    fclose(out_file);

    return;
}

int main(int argc, char *argv[])
{
    if(argc!= 4)
    {
        printf("%s <input_filename> <output_filename> <num vertices>\n",argv[0]);
        return 1;
    }
    char* input_filename = argv[1];
    char* output_filename = argv[2];
    uint64_t max_v = atoi(argv[3]);

    printf("input_filename = %s\n", input_filename); fflush(stdout);
    
    read_graph(input_filename, max_v);
    printf("Loading graph finished\n"); fflush(stdout);

    uint64_t split_vertices = 0;
    printf("Read in %ld vertices and %ld split vertices\n", nnodes, split_vertices); fflush(stdout);

    total_verts = nnodes + split_vertices;
    uint64_t max_orig_degree = 0;
    uint64_t offset = 0;
    uint64_t split_vid = nnodes;
    vertex_t* verts = (vertex_t*)malloc(total_verts * sizeof(vertex_t));
    nedeges = 0;
    printf("total_verts %ld\n", total_verts); fflush(stdout);

    for(uint64_t i = 0; i < nnodes; i++){
        uint64_t deg = adj_list[i].size();
        verts[i].id = i;
        verts[i].padding = 0;
        verts[i].deg = deg;
        verts[i].val = 1.0;
        nedeges += deg;
    }
    
    gv_bin(output_filename, verts);
    printf("Finish gv_bin generated\n"); fflush(stdout);


    std::string binfile_nl = std::string(output_filename) + "_nl" + ".bin";
    char* binfilename = const_cast<char*>(binfile_nl.c_str()); 
    printf("Binfile:%s\n", binfilename); fflush(stdout);
    FILE* out_file = fopen(binfilename, "wb");
    if (!out_file) {
          exit(EXIT_FAILURE);
    }
    fseek(out_file, 0, SEEK_SET);
    size_t size = fwrite(&nedeges, sizeof(uint64_t), 1, out_file);
    for(uint64_t i = 0; i < nnodes; i++){
        std::vector<uint64_t> tmp(adj_list[i].begin(), adj_list[i].end());
        size = fwrite(tmp.data(), sizeof(uint64_t), tmp.size(), out_file);
        // size = fwrite(&adj_list[i], sizeof(uint64_t), adj_list[i].size(), out_file);
    }
    fclose(out_file);
    
    return 0;
}

