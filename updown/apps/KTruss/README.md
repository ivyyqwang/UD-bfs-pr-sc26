# K-Truss Readme

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
./MtxReorderOrientation <input_filename> <output_filename> <num_vertex>
```

eg: 
```
cd preprocess/
make
./MtxReorderOrientation RMAT_scale_12_seed_1_edges.txt RMAT_s12_ktruss.txt 4096
```


### Run KTruss
```bash
cd install/updown/apps/
./k_truss_udweave <k> <gv_bin> <nl_bin> <num_lanes>
```

eg: 
```
cd install/updown/apps/
./k_truss_udweave 3 ../../../apps/KTruss/preprocess/RMAT_s12_ktruss.txt_gv.bin  ../../../apps/KTruss/preprocess/RMAT_s12_ktruss.txt_nl.bin 2048
```

