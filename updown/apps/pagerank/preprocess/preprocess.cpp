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
  uint64_t deg;
  uint64_t id;
  uint64_t offset;
  uint64_t orig_vid;
  uint64_t split_start;
  uint64_t split_bound;
  double val;
  uint64_t padding;
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
    size = fwrite(&total_verts, sizeof(uint64_t), 1, out_file);

    size = fwrite(verts, sizeof(vertex_t), total_verts, out_file);

    fclose(out_file);

    return;
    
    // int num_of_block_verts = 32 * 1024 / sizeof(vertex_t);
    // for(uint64_t i = 0; i < total_vert;){
    //     uint64_t len = total_vert - i;
    //     if(len > num_of_block_verts){
    //         len = num_of_block_verts;
    //     }
    //     fwrite(&verts[i], sizeof(uint64_t), len, out_file);
    //     i = i + len;
    // }
}

int main(int argc, char *argv[])
{
    if(argc!= 5)
    {
        printf("%s <input_filename> <output_filename> <num vertices> <max_deg>\n",argv[0]);
        return 1;
    }
    char* input_filename = argv[1];
    char* output_filename = argv[2];
    uint64_t max_v = atoi(argv[3]);
    uint64_t max_deg = atoi(argv[4]);

    printf("input_filename = %s\n", input_filename); fflush(stdout);
    
    read_graph(input_filename, max_v);
    printf("Loading graph finished\n"); fflush(stdout);

    uint64_t split_vertices = 0;
    for(uint64_t i = 0; i < nnodes; i++){
        uint64_t num_split = adj_list[i].size() / max_deg;
        if(num_split > 0){
            split_vertices += num_split + 1;
        }
    }
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
        uint64_t num_split = deg / max_deg;
        verts[i].id = i;
        verts[i].offset = offset;
        verts[i].orig_vid = i;
        verts[i].val = 1.0;
        verts[i].padding = 0;
        nedeges += deg;
        if(deg > max_orig_degree){
            max_orig_degree = deg;
        }
        if(num_split == 0){
            verts[i].deg = deg;
            verts[i].split_start = 0;
            verts[i].split_bound = 0;
            offset += deg;
            if(deg % 8 > 0){
                offset += 8 - (deg % 8);
            }
        }
        else{
            num_split = num_split + 1;
            uint64_t split_deg = (deg / num_split) + 1;
            verts[i].deg = 0;
            verts[i].split_start = split_vid;
            verts[i].split_bound = split_vid + num_split;
            for(uint64_t j = verts[i].split_start; j < verts[i].split_bound; j++){
                if((j - verts[i].split_start) == (deg % num_split)){
                    split_deg--;
                }
                verts[j].deg = split_deg;
                verts[j].id = j;
                verts[j].orig_vid = i;
                verts[j].split_start = verts[i].split_start;
                verts[j].split_bound = verts[i].split_bound;
                verts[j].val = 1.0;
                verts[j].padding = 0;
            }
            split_vid += num_split;
        }
    }
    for(uint64_t i = nnodes; i < total_verts; i++){
        uint64_t deg = verts[i].deg;
        verts[i].offset = offset;
        offset += deg;
        if(deg % 8 > 0){
            offset += 8 - (deg % 8);
        }
    }

    printf("Finish split vertices, max_orig_degree = %ld\n", max_orig_degree); fflush(stdout);
    gv_bin(output_filename, verts);
    printf("Finish gv_bin generated\n"); fflush(stdout);

    printf("Read in %ld edges and %ld offset\n", nedeges, offset); fflush(stdout);

    uint64_t *counter = (uint64_t*)malloc(nnodes*sizeof(uint64_t));
    memset(counter, 0, nnodes*sizeof(uint64_t));
    uint64_t *offset_list = (uint64_t*)malloc(total_verts*sizeof(uint64_t));
    for(uint64_t i = 0; i < total_verts; i++){
        offset_list[i] = verts[i].offset;
    }
    uint64_t *edge_bin = (uint64_t*)malloc(offset*sizeof(uint64_t));
    memset(edge_bin, -1, offset*sizeof(uint64_t));

    uint64_t *edge_bin2 = (uint64_t*)malloc(offset*sizeof(uint64_t));
    memset(edge_bin2, -1, offset*sizeof(uint64_t));

    printf("Finish allocator\n"); fflush(stdout);

    for(uint64_t i = 0; i < nnodes; i++){
        for (set<uint64_t>::iterator iter = adj_list[i].begin(); iter != adj_list[i].end(); iter++)
        {
            uint64_t src = verts[i].id;
            uint64_t dest = *iter;
            uint64_t orig_src = src;
            uint64_t orig_dest = dest;
            if(src > dest){
                // printf("%ld: %ld %ld\n", i, src, dest); fflush(stdout);
                if(verts[src].split_start != verts[src].split_bound){
                    uint64_t new_src = (counter[src] % (verts[src].split_bound - verts[src].split_start)) + verts[src].split_start;
                    counter[src]++;
                    src = new_src;
                    // printf("new_src %ld\n", new_src); fflush(stdout);
                }
                if(verts[dest].split_start != verts[dest].split_bound){
                    uint64_t new_dest = (counter[dest] % (verts[dest].split_bound - verts[dest].split_start)) + verts[dest].split_start;
                    counter[dest]++;
                    dest = new_dest;
                    // printf("new_dest %ld\n", new_dest); fflush(stdout);
                }
                edge_bin[offset_list[src]] = dest;
                edge_bin2[offset_list[src]] = orig_dest;
                offset_list[src]++;
                edge_bin[offset_list[dest]] = src;
                edge_bin2[offset_list[dest]] = orig_src;
                offset_list[dest]++;
            }else{
                break;
            }
        }
    }

    printf("Read in %ld edges and %ld offset\n", nedeges, offset); fflush(stdout);

    std::string binfile_nl = std::string(output_filename) + "_nl" + ".bin";
    char* binfilename = const_cast<char*>(binfile_nl.c_str()); 
    printf("Binfile:%s\n", binfilename); fflush(stdout);
    FILE* out_file = fopen(binfilename, "wb");
    if (!out_file) {
          exit(EXIT_FAILURE);
    }
    fseek(out_file, 0, SEEK_SET);
    size_t size = fwrite(&nedeges, sizeof(uint64_t), 1, out_file);
    size = fwrite(&offset, sizeof(uint64_t), 1, out_file);
    size = fwrite(edge_bin, sizeof(uint64_t), offset, out_file);
    fclose(out_file);

    std::string binfile_orig_nl = std::string(output_filename) + "_orig_nl" + ".bin";
    binfilename = const_cast<char*>(binfile_orig_nl.c_str()); 
    printf("Binfile:%s\n", binfilename); fflush(stdout);
    out_file = fopen(binfilename, "wb");
    if (!out_file) {
          exit(EXIT_FAILURE);
    }
    fseek(out_file, 0, SEEK_SET);
    size = fwrite(&nedeges, sizeof(uint64_t), 1, out_file);
    size = fwrite(&offset, sizeof(uint64_t), 1, out_file);
    size = fwrite(edge_bin2, sizeof(uint64_t), offset, out_file);
    fclose(out_file);
    
    
    
    return 0;
    
}

