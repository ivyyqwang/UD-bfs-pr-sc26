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
#include <cstdint>

typedef uint64_t* ptr;


typedef struct tmp_vertex{
  uint64_t reserved0;  
  uint64_t reserved1;  
  uint64_t reserved2;  
  uint64_t reserved3;  
} tmp_vertex_t;

typedef struct vertex{
    uint64_t offset;
    uint64_t degree;
    uint64_t edges_before;
    uint64_t vertex_id;
    uint64_t scratch1;
    uint64_t scratch2;
    uint64_t scratch3;
    uint64_t scratch4;
} vertex_t;


using namespace std;

uint64_t nnodes = 0;
uint64_t nedeges = 0;

map<uint64_t, uint64_t> vid_map;
std::map<uint64_t, std::vector<uint64_t>> adj_list;
map<uint64_t, uint64_t> deg_list;
std::map<uint64_t, std::vector<uint64_t>> adj_listT;
map<uint64_t, uint64_t> deg_listT;


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
        // cout << line << endl;
        sin >> v1 >> v2;
//        cout << v1 << v2;
        // printf("%d %d\n",v1,v2);
        // printf("#: %lu\n", deg_list[v1]);
        if(vid_map.find(v1) == vid_map.end()){ // first v1
            vid_map[v1] = id;
            // vid_map[v1] = v1;
            id++;
        }
        if(vid_map.find(v2) == vid_map.end()){ // first v2
            vid_map[v2] = id;
            // vid_map[v2] = v2;
            id++;
        }
        v1 = vid_map[v1];
        v2 = vid_map[v2];
        if(adj_list.find(v1) == adj_list.end()) { // first
            adj_list[v1] = {v2};
            deg_list[v1] = 1;
        }else{
            adj_list[v1].push_back(v2);
            deg_list[v1] = deg_list[v1] + 1;
        }
        if(adj_listT.find(v2) == adj_listT.end()) { // first
            adj_listT[v2] = {v1};
            deg_listT[v2] = 1;
        }else{
            adj_listT[v2].push_back(v1);
            deg_listT[v2] = deg_listT[v2] + 1;
        }
        nedeges++;
    }
    nnodes = id;

    printf("vertices = %lu, edges = %lu\n", nnodes, nedeges);
    fflush(stdout);
    fin.close();
    return 0;
}
void write_graph(char *filename, char *output_filename)
{

    std::string mapFile = std::string(output_filename) + "_mapping.txt";

    std::ifstream fin(filename);
    std::string line;
    std::ofstream fout(mapFile.c_str());

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


void transfer2bin(std::string &filename, std::map<uint64_t, 
                    std::vector<uint64_t>> &list, map<uint64_t, uint64_t> &degs)
{
    std::string binfile_gv, binfile_nl;
    char* binfilename;
    FILE* out_file, *in_file;

    uint64_t num_nodes = nnodes;

    vertex_t *g_v_bin = (vertex_t*)malloc(num_nodes*sizeof(vertex_t));
    uint64_t offset = 0;

    binfile_gv = filename + "_gv" + ".bin";
    binfile_nl = filename + "_nl" + ".bin";

    binfilename = const_cast<char*>(binfile_gv.c_str()); 
    printf("Binfile: %s\n", binfilename);
    out_file = fopen(binfilename, "wb");
    if (!out_file) {
          exit(EXIT_FAILURE);
    }
    fseek(out_file, 0, SEEK_SET);
    fwrite(&num_nodes, sizeof(uint64_t), 1, out_file);
    fwrite(&nedeges, sizeof(uint64_t), 1, out_file);
    tmp_vertex_t tmp;
    tmp.reserved0 = 0;
    tmp.reserved1 = 0;
    tmp.reserved2 = 0;
    tmp.reserved3 = 0;

    uint64_t edges_before = 0;
    for(uint64_t i=0; i< num_nodes; i++){
        fwrite(&offset, sizeof(uint64_t), 1, out_file);
        fwrite(&degs[i], sizeof(uint64_t), 1, out_file);
        fwrite(&edges_before, sizeof(uint64_t), 1, out_file);
        fwrite(&i, sizeof(uint64_t), 1, out_file);
        uint64_t deg = degs[i];
        edges_before += deg;
        if(deg % 8 > 0){
            deg = (deg / 8) * 8 + 8;
        }
        offset += deg;
        fwrite(&tmp, sizeof(tmp), 1, out_file);
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
        // printf("vid = %lu, deg = %lu\n", i, degs[i]); fflush(stdout);
        fwrite(list[i].data(), sizeof(uint64_t), degs[i], out_file);
        uint64_t deg = degs[i];
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

    std::string output_filename_string = std::string(output_filename);
    transfer2bin(output_filename_string, adj_list, deg_list);

    output_filename_string += "_T";
    transfer2bin(output_filename_string, adj_listT, deg_listT);
    
    return 0;
    
}

