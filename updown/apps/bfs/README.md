# BFS Validation README

## Generate input

```bash
python3 ./RMAT.py --scale <scale> --seed <random_seed>
```

This will generate 1 file `<filename>` containing edges for an RMAT graph of scale `scale` with random seed set to `random_seed`.
The generated graph has two to the power `scale` number of vertices.
The output graph will be written to a file named `scale_<scale>_seed_<random_seed>_edges.txt` under the `graph` folder.

The RMAT graph generated and used for validation and performance experiments are https://drive.google.com/file/d/1lU61zWGhs0oYQw3HMfrmdEOVdSZ2Gauc/view?usp=drive_link.

```bash
./split_shuffle  -f <graph_file> -m <max_degree> -l (line offset) -d(directed) -s(stats) -n(no split)
```

This will take the `graph_file` in edge list format and convert it to a binary format file.
`<max_degree>` set the maximum degree of the graph after split.
`<directed>` is set if the graph is directed, i.e., has an edge between two vertices in both directions.

## Run BFS

```bash
./updown_bfs_push_pull  <graph_file> <num_uds> <root_vid> <partition_parameter>
```

`graph_file` is the output of the vertex splitting program named `<graph_file>_max_split_degree_<max_degree>.bin`.
`num_uds` is the number of UpDowns running the BFS computation.
`root_vid` is the root vertex id of the BFS tree to be computed.
`partition_parameter` is a parameter controlling the load balancing, a good choice is 3.
