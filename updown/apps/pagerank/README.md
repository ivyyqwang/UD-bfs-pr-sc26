# PageRank README

## Preprocessing

### Generate input graph

```bash
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

## Push PageRank

```bash
cd install/updown/apps/
./pr_udweave <graph_file_gv.bin> <graph_file_nl.bin> <num_nodes>  (<network_latency> <network_bandwidth>)
```

eg:

```
cd install/updown/apps/
./pr_udweave ../../../apps/push_pr/preprocess/RMAT_s12_pr.txt_gv.bin  ../../../apps/push_pr/preprocess/RMAT_s12_pr.txt_nl.bin 1
```

## Data-Driven PageRank

```bash
OMP_NUM_THREADS=32 ./partialPagerankDataDriven <graph_file_path> <num_nodes> <num_top_iterations> <num_ud_iterations>
```

`graph_file_path` is the path to the graph file, which is the output of the vertex splitting program.
`num_nodes` is the number of UpDown nodes running the PageRank computation.
`num_top_iterations` is the number of iterations to run the PageRank computation on the cpu cores.
`num_ud_iterations` is the number of iterations to run the PageRank computation on the UpDown accelerators.

Example:

```bash
OMP_NUM_THREADS=32 ./partialPagerankDataDriven ca-AstroPh.txt 4 2 35
```
