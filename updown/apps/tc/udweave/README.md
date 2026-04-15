# Triangle Counting Readme

### Generate input graph

``` bash
python3 RMAT_agile.py <scale>
```

This will generate 1 file `<filename>` containing edges for an RMAT graph of scale `scale`. 

eg: 
```
python3 RMAT_agile.py 12
```
If there are issues with numpy or scipy libraries, please run 

```bash 
pip install -r requirements.txt
```

1. TC based on intersection of sorted neighborlists 
### Run preprocessing for triangle Counting
```bash
./preprocess_tc <input-file>
```

This program generates input (`<filename>_edges.bin`) and output reference files (`<filename>.ref.csv`) for the preprocessing phase and input files for the TC phase. (`<filesname>_gv.bin` and `<filename>_nl.bin`). 

eg: 
```
./preprocess_tc RMAT_scale_12_seed_1_edges.txt
```

### Run TC - Linear

``` bash
./triangle_count_v10 <<filename>_gv.bin> <<filename>_nl.bin> <num_lanes> <num_masters> <mode> [<start>] [<end>]
```

The `*gv.bin` and `*_nl.bin>` are binary files for the vertex and neighbor list stores
`<num-lanes>` is same as described above
`<num-masters>` configure the number of masters for workload distribution (4 per node (2048 lanes) is best value from our experiments)
`<mode>` = 0 will run TC for all vertices. 
         = 1 debug mode to run TC on a specified set of vertices (with this mode optional start and end vertex IDS can be provided)

This program will print the output baseline TC and UD computed values as part of the output. (You might need to pipe the output into a logfile and grep for "Triangle Count")

eg:

```
./triangle_count_v10 RMAT_scale_12_seed_1_edges.txt_gv.bin RMAT_scale_12_seed_1_edges.txt_nl.bin 1024 4 0 | tee tc_scale_12.log
grep "Triangle" tc_scale_12.log
```
Source Files : `te/isb/tc/v10_linear`

### Run TC - Binary

``` bash
./triangle_count_v10_binary <<filename>_gv.bin> <<filename>_nl.bin> <num_lanes> <num_masters> <mode> [<start>] [<end>]
```

The `*gv.bin` and `*_nl.bin>` are binary files for the vertex and neighbor list stores
`<num-lanes>` is same as described above
`<num-masters>` configure the number of masters for workload distribution (4 per node (2048 lanes) is best value from our experiments)
`<mode>` = 0 will run TC for all vertices. 
         = 1 debug mode to run TC on a specified set of vertices (with this mode optional start and end vertex IDS can be provided)

This program will print the output baseline TC and UD computed values as part of the output. (You might need to pipe the output into a logfile and grep for "Triangle Count")

eg:

```
./triangle_count_v10_binary RMAT_scale_12_seed_1_edges.txt_gv.bin RMAT_scale_12_seed_1_edges.txt_nl.bin 1024 4 0 | tee tc_scale_12.log
grep "Triangle" tc_scale_12.log
```
Source Files : `te/isb/tc/v10_binary


3. TC based on hybrid hash + sorted list intersection

### Run preprocessing for triangle Counting
```bash
./preprocess_tc_v2 <input-file> <bucket-size> <threshold>
```
`<bucket-size>` number of entries in a bucket for the hash table
`<threshold>` degree threshold that will be used for creating hash table as follows
            = 0 : All edges hashed
            = 1 : edges of vertices with deg > (mean + 1 * stddev) (mean and stddev of the degree distribution)
            = 2 : edges of vertices with deg > (mean + 2 * stddev) (mean and stddev of the degree distribution)
            = 3 : edges of vertices with deg > (mean + 3 * stddev) (mean and stddev of the degree distribution)
            = 4 : edges of vertices with deg > (mean + 4 * stddev) (mean and stddev of the degree distribution)


This program generates (`<filename>_edges_hash.bin`), (`<filesname>_gv.bin` and `<filename>_nl.bin`) files to be used as input for the TC phase.

eg: 
```
./preprocess_tc_v2 RMAT_scale_12_seed_1_edges.txt 4 4
```

### Run TC 

``` bash
./triangle_count_hybrid <<filename>_hash_gv.bin> <<filename>_hash_nl.bin> <<filename>_edgehash.bin> <num_lanes> <num_masters> <mode> [<start>] [<end>] 
```

`<num-lanes>` is same as described above
`<num-masters>` configure the number of masters for workload distribution (4 per node (2048 lanes) is best value from our experiments)
`<mode>` = 0 will run TC for all vertices. 
         = 1 debug mode to run TC on a specified set of vertices (with this mode optional start and end vertex IDS can be provided)

This program will print the output baseline TC and UD computed values as part of the output. (You might need to pipe the output into a logfile and grep for "Triangle Count")

eg:

```
./triangle_count_hybrid RMAT_scale_12_seed_1_edges.txt_hash_gv.bin RMAT_scale_12_seed_1_edges.txt_hash_nl.bin RMAT_scale_12_seed_1_edges.txt_edgehash.bin 1024 4 0 | tee tc_scale_12.log
grep "Triangle" tc_scale_12.log
```

Source Files : `te/isb/tc/v10_hybrid`

-------------

### TC PreProcessing (3 phases) (added for completeness and profiling) 

``` bash
./compute_degrees <<filename>_edges.bin> <num-lanes> [entries-per-bucket] [buckets-per-lane]
./orient_edges <<filename>_edges.bin> <num-lanes> <dumpname-prefix> [entries-per-bucket] [buckets-per-lane]
./neighborlist_sort <<filename>_edges.bin> <num-lanes> <dumpname-prefix> [entries-per-part] [parts-per-lane] [sort-threshold] [total-dsort-lanes] [lanes-per-dsort]

```

The guideline for setting `<num-lanes>` is `4096` for `2` UpDown nodes, etc. (Use minimum - 4096, and scale based on size of graph)
The `<edge-binary>` is a binary format of the input edge file. Phase 2, 3 take inputs that are dumped by the previous phases
In fastsim, `dumpname-prefix=<filename>_edges.bin`. 

Optional Parameters - These have been set based on some tuning. None of these need to be set ideally. 
`entries-per-bucket (defalt 1024), buckets-per-lane (default 16)` for edgeStore SHT for phase 1 and 2
`entries-per-part (defalt 128), parts-per-lane (default 128)` for kvmsr in phases 3 and 4
`sort-threshold (default-400)` threshold after which distributed sort is performed
`total-dsort-lanes (default-64)` total dsort lanes allocated for distributed sorting
`lanes-per-dsort (default-4)` number of lanes used per distributed sorting thread

Source Files : `te/isb/tc/phase1|phase2|phase3`


### Validate preprocessing output

``` bash
python3 tc_preprocess_validate_p2.py <<filename>.ref.csv> <<filename>_edges.bin_to.pga.csv> 
python3 tc_preprocess_validate_p3.py <<filename>.ref.csv> <<filename>_edges.bin_nl.pga.csv> 
```
This will compare the output of preprocessing phase with reference output. It compares the neighborlist stores and will print the total number of vertex neighbors matched and mismatches if any. 

