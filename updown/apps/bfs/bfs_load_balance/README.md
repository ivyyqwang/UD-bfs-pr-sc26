# Load-Balacing BFS Readme

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

It will preprocess graph.txt downloaded from SNAP, generate `<output_filename>` adjacency file as UpDown program input.

```bash
cd preprocess/
make
./preprocess <input_filename> <output_filename> 
```

eg: 
```
cd preprocess/
make
./preprocess RMAT_scale_12_seed_1_edges.txt RMAT_s12_lbbfs.adj
```


### Run Louvain
```bash
cd udweave/
make
./LBBFS <graph file> <number of lanes> <root vid>
```

eg: 
```
cd udweave/
make
./LBBFS ../preprocess/RMAT_s12_lbbfs.adj 2048 0
```

