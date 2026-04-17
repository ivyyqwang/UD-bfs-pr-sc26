# K-Core Readme

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

It will preprocess graph.txt downloaded from SNAP, generate `<output_filename>` txt file, `<output_filename>_gv.bin` and `<output_filename>_nl.bin` as UpDown program input.

```bash
cd preprocess/
make
./preprocess <input_filename> <output_filename> 
```

eg: 
```
cd preprocess/
make
./preprocess RMAT_scale_12_seed_1_edges.txt RMAT_s12_kcore.txt
```


### Run Louvain
```bash
cd udweave/compact/
make
cd ../
make
./kcore <gv_bin> <nl_bin> <num_lanes> <DifferencePercentForCompaction>
```

eg: 
```
cd udweave/compact/
make
cd ../
make
./kcore ../preprocess/RMAT_s12_kcore.txt_gv.bin ../preprocess/RMAT_s12_kcore.txt_nl.bin 2048 100
```

