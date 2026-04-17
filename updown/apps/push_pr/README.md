# Push-PR Readme

### Generate input graph

``` bash
cd preprocess/
python3 RMAT_agile.py <scale>
```

This will generate 1 file `<filename>` containing edges for an RMAT graph of scale `scale`. 

eg: 
```
cd preprocess/
python3 RMAT_agile.py 12
```

### Generate input binary graph (CSR)

It will preprocess graph.txt downloaded from SNAP, generate `<output_filename>` txt file, `<output_filename>_gv.bin` and `<output_filename>_nl.bin` as UpDown program input. `<num_vertex>` is the number of vertices in the graph, and the number can be equal or larger than the exact number of vertices. In addtition, the vertex id in neighbor list is sorted based on vid. Reorder will remap vid based on its degree, from highest to lowest, to reduce load imbalanced issue and only keep the edges (v0, v1) where v0 > v1.

```bash
cd preprocess/
make
./preprocess <input_filename> <output_filename> <num_vertex> <max_deg>
```

eg: 
```
cd preprocess/
make
./preprocess RMAT_scale_12_seed_1_edges.txt RMAT_s12_pr.txt 4096 512
```


### Run
```bash
cd install/updown/apps/
./pr_udweave <graph_file_gv.bin> <graph_file_nl.bin> <num_nodes>  (<network_latency> <network_bandwidth>)
```

eg: 
```
cd install/updown/apps/
./pr_udweave ../../../apps/push_pr/preprocess/RMAT_s12_pr.txt_gv.bin  ../../../apps/push_pr/preprocess/RMAT_s12_pr.txt_nl.bin 1
```

