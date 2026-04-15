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
  uint64_t* neigh_ptr;
  uint64_t deg;
  uint64_t edges_before;
  uint64_t vid;
  uint64_t community;  
  uint64_t new_community;  
  double* weight_ptr; 
  double tot;
  double in;
  uint64_t weight;
  uint64_t reserved0;  
  uint64_t reserved1;  
  uint64_t reserved2;  
  uint64_t reserved3;  
  uint64_t reserved4;
  uint64_t reserved5; 
} vertex_t;


using namespace std;

uint64_t nnodes = 0;
uint64_t nedeges = 0;

map<uint64_t, uint64_t> vid_map;
std::map<uint64_t, std::vector<uint64_t>> adj_list;
map<uint64_t, uint64_t> deg_list;


uint64_t read_graph(char  * filename)
{
    std::ifstream fin(filename);
    std::string line;
    std::istringstream sin(line);
    uint64_t id = 0;
          
    while (getline(fin, line) && (line[0] != '\n'))
    {
        if(line[0] == '\n' || line[0] == '#'){
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
        if(vid_map.find(v1) == vid_map.end()){ // first v1
            vid_map[v1] = id;
            id++;
        }
        if(vid_map.find(v2) == vid_map.end()){ // first v2
            vid_map[v2] = id;
            id++;
        }
        v1 = vid_map[v1];
        v2 = vid_map[v2];
        if(v1 == v2){
            if(adj_list.find(v1) == adj_list.end()) { // first
            adj_list[v1] = {v2};
            deg_list[v1] = 1;
            }else{
                adj_list[v1].push_back(v2);
                deg_list[v1] = deg_list[v1] + 1;
            }
            nedeges+=1;
        }else{
            if(adj_list.find(v1) == adj_list.end()) { // first
                adj_list[v1] = {v2};
                deg_list[v1] = 1;
            }else{
                adj_list[v1].push_back(v2);
                deg_list[v1] = deg_list[v1] + 1;
            }
            if(adj_list.find(v2) == adj_list.end()) { // first
                adj_list[v2] = {v1};
                deg_list[v2] = 1;
            }else{
                adj_list[v2].push_back(v1);
                deg_list[v2] = deg_list[v2] + 1;
            }
            nedeges+=2;
        }
    }
    nnodes = id;

    printf("vertices = %lu, edges = %lu\n", nnodes, nedeges);
    fflush(stdout);
    fin.close();
    return 0;
}

void write_graph(char  * filename, char *output_filename)
{
    std::ifstream fin(filename);
    std::string line;
    std::ofstream fout(output_filename);

    while (getline(fin, line) && (line[0] != '\n')){
        if(line[0] == '\n' || line[0] == '#'){
            continue;
        }
        std::istringstream sin(line);
        uint64_t tmp;
        uint64_t v1, v2;
        sin >> v1 >> v2;
        fout << vid_map[v1] << " " << vid_map[v2] << endl;
    }
    fin.close();
    fout.close();
    return;
}


void transfer2bin(char  * filename)
{
    std::string binfile_gv, binfile_nl;
    char* binfilename;
    FILE* out_file, *in_file;

    uint64_t num_nodes = nnodes;
    uint64_t offset = 0;

    binfile_gv = std::string(filename) + "_gv" + ".bin";
    binfile_nl = std::string(filename) + "_nl" + ".bin";

    binfilename = const_cast<char*>(binfile_gv.c_str()); 
    printf("Binfile:%s\n", binfilename);
    out_file = fopen(binfilename, "wb");
    if (!out_file) {
          exit(EXIT_FAILURE);
    }
    fseek(out_file, 0, SEEK_SET);
    fwrite(&num_nodes,sizeof(uint64_t),1,out_file);
    fwrite(&nedeges,sizeof(uint64_t),1,out_file);


    uint64_t weight = 1;
    uint64_t edges_before = 0;
    uint64_t tmp = 0;
    for(uint64_t i=0; i< num_nodes; i++){
        fwrite(&offset, sizeof(uint64_t), 1, out_file);
        fwrite(&deg_list[i], sizeof(uint64_t), 1, out_file);
        fwrite(&edges_before, sizeof(uint64_t), 1, out_file);
        fwrite(&i, sizeof(uint64_t), 1, out_file);
        fwrite(&weight, sizeof(uint64_t), 1, out_file);
        fwrite(&i, sizeof(uint64_t), 1, out_file);
        fwrite(&tmp, sizeof(uint64_t), 1, out_file);
        fwrite(&tmp, sizeof(uint64_t), 1, out_file);
        fwrite(&tmp, sizeof(uint64_t), 1, out_file);
        fwrite(&tmp, sizeof(uint64_t), 1, out_file);
        fwrite(&tmp, sizeof(uint64_t), 1, out_file);
        fwrite(&tmp, sizeof(uint64_t), 1, out_file);
        fwrite(&tmp, sizeof(uint64_t), 1, out_file);
        fwrite(&tmp, sizeof(uint64_t), 1, out_file);
        fwrite(&tmp, sizeof(uint64_t), 1, out_file);
        fwrite(&tmp, sizeof(uint64_t), 1, out_file);
        uint64_t deg = deg_list[i];
        edges_before += deg;
        if(deg % 8 > 0){
            deg = (deg / 8) * 8 + 8;
        }
        offset += deg;
    }
    fclose(out_file);

    uint64_t nlist_size = offset;
    offset = 0;
  
    binfilename = const_cast<char*>(binfile_nl.c_str()); 
    printf("Binfile:%s\n", binfilename);
    out_file = fopen(binfilename, "wb");
    if (!out_file) {
          exit(EXIT_FAILURE);
    }
    fseek(out_file, 0, SEEK_SET);
    printf("Size of uint64_t:%d, writing nlarray:%lu in NL\n", sizeof(uint64_t), nlist_size);
    fwrite(&nlist_size,sizeof(uint64_t), 1, out_file);
    for(uint64_t i=0; i< num_nodes;i++)
    {
        // printf("vid = %lu, deg = %lu\n", i, deg_list[i]); fflush(stdout);
        fwrite(adj_list[i].data(), sizeof(uint64_t), deg_list[i], out_file);
        uint64_t deg = deg_list[i];
        uint64_t tmp = 0;
        while(deg % 8 > 0){
            fwrite(&tmp, sizeof(uint64_t), 1, out_file);
            deg++;
        }
    }
    fclose(out_file);
}

int main(int argc, char *argv[])
{
    if(argc!= 3)
    {
        printf("%s <input_filename> <output_filename>\n",argv[0]);
        return 1;
    }
    char* input_filename = argv[1];
    char* output_filename = argv[2];
    
    read_graph(input_filename);
    printf("Input Graph Loading Finished\n"); fflush(stdout);
    write_graph(input_filename, output_filename);
    printf("Output Graph Writing Finished\n"); fflush(stdout);
    transfer2bin(output_filename);
    
    return 0;
    
}

