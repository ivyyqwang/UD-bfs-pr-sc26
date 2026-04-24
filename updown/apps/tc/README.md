# Triangle Counting Readme

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

It will preprocess graph.txt downloaded from SNAP, generate `<output_filename>` txt file, `<output_filename>_gv.bin` and `<output_filename>_nl.bin` as UpDown program input. `<num_vertex>` is the number of vertices in the graph, and the number can be equal or larger than the exact number of vertices. In addtition, the vertex id in neighbor list is sorted based on vid. Reorder will remap vid based on its degree, from highest to lowest, to reduce load imbalanced issue.

```bash
cd preprocess/
make
./preprocess <input_filename> <output_filename> <num_vertex>
```

eg: 
```
cd preprocess/
make
./preprocess RMAT_scale_12_seed_1_edges.txt RMAT_s12_tc.txt 4096
```


### Run TC
```bash
cd install/updown/apps/
./tc_udweave <gv_bin> <nl_bin> <num_lanes> (<network_latency> <network_bandwidth>)
```

eg: 
```
cd install/updown/apps/
./tc_udweave ../../../apps/tc/preprocess/RMAT_s12_tc.txt_gv.bin   ../../../apps/tc/preprocess/RMAT_s12_tc.txt_nl.bin 2048
```

