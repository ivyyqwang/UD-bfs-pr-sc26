# PageRank README

## Preprocessing

### Run preprocessing without vertex splitting

```bash
./snap_no_split <input_graph_file> <output_graph_file> <num_of_vertex>
```

`input_graph_file` is the `graph.txt` download from SNAP dataset.
`output_graph_file` will generate `<output_graph_file>_gv.bin`, `<output_graph_file>_nl.bin` and `<output_graph_file>_orig_nl.bin`.
`num_of_vertex`: max vertex id.

### Run preprocessing with vertex splitting

```bash
./snap <input_graph_file> <output_graph_file> <num_of_vertex>  <max_degree>
```

`input_graph_file` is the `graph.txt` download from SNAP dataset.
`output_graph_file` will generate `<output_graph_file>_gv.bin`, `<output_graph_file>_nl.bin` and `<output_graph_file>_orig_nl.bin`.
`num_of_vertex`: max vertex id.
`max_degree` controls the maximum degree after the splitting argument. A good number for a scale 28 RMAT graph is 512.

This program will output the split graph in a binary file named `<output_graph_file>_gv.bin`, `<output_graph_file>_nl.bin` and `<output_graph_file>_orig_nl.bin` in the same directory as the input graph file.

Example:

```bash
./snap ca-AstroPh.txt ca-AstroPh.txt 18772 512
```

## Push PageRank

```bash
OMP_NUM_THREADS=32 ./pagerankMSRsplit <graph_file_gv.bin> <graph_file_nl.bin> <num_nodes> <num_uds> <load_balance_parameter>
```

`graph_file` is the output of the vertex splitting program named `split_scale_<scale>_seed_1_edges.txt`.
`num_nodes` is the number of UpDown nodes running the PageRank computation. You also need to update `NUM_NODES` in splitPRMSRLinkableConfig.py and remake the udweave code.
`num_uds` is the number of UpDown accelerators running the PageRank computation on 1 node.
`load_balance_parameter` is the parameter to control the load balance, the higher the more aggressive it load balance within the accelerator level. In current version, it must be 1.

Example:

```bash
OMP_NUM_THREADS=32 ./pagerankMSRsplit ca-AstroPh.txt_gv.bin ca-AstroPh.txt_nl.bin 1 32 1
```

## Data-Driven PageRank

```bash
OMP_NUM_THREADS=32 ./partialPagerankDataDriven <graph_file_path> <num_nodes> <num_top_iterations> <num_ud_iterations>
```

`graph_file_path` is the path to the graph file, which is the output of the vertex splitting program named `split_scale_<scale>_seed_1_edges.txt`.
`num_nodes` is the number of UpDown nodes running the PageRank computation.
`num_top_iterations` is the number of iterations to run the PageRank computation on the cpu cores.
`num_ud_iterations` is the number of iterations to run the PageRank computation on the UpDown accelerators.

Example:

```bash
OMP_NUM_THREADS=32 ./partialPagerankDataDriven ca-AstroPh.txt 4 2 35
```
