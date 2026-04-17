# SCC

## Description
A strongly connected graph is a directed graph in which every vertex is reachable from every other vertex - that is, for any two vertices $u$ and $v$, there exists a directed path from $u$ to $v$ and from $v$ to $u$. A maximal subgraph satisfying this property is called a strongly connected component (SCC). The algorithm operates by coloring all vertices. In a second step, a parallel BFS is performed on the transposed graph starting from the root vertices. If a vertex is reachable from the root node, they form a SCC and are deleted from the graph. For vertices that could not be reached, the color is reset, and the algorithm restarts with the coloring of the remaining vertices. The algorithm terminates if all vertices have been assigned an SCC.
Reference: [https://ieeexplore.ieee.org/abstract/document/6877288](https://ieeexplore.ieee.org/abstract/document/6877288)

## Performance
The performance for k-core is documented [here](https://docs.google.com/document/d/15iNX0ijOYj3RNy30tRpZ2cvCUFghpgOR2DNV4EXkHyQ/edit?tab=t.0).


## Files

| Name | Description|
|-----------|---------|
| preprocess.cpp | preprocess file |
| scc_exe.py | SCC assembly code |
| scc.cpp | SCC top code |
| prefixSum.udw | Aggregate the degrees from all vertices to compute the prefix sum required for the load balancing framework. |
| prefixSumDown.udw | Communicate the prefix sum down to the vertices. |
| coloring.udw | Color the vertices using the load balancing framework. |
| copyData.udw | Since the coloring phase uses a different memory address for read and updates of the vectors, and not every vector is touched by the load balancing framework, the gaps need to be filled. copyData.udw performs this task. |
| findVerticesOfSameColor.udw | This UpDown program search for vertices, which are not marked as deleted and whose $color = vertex ID$. Thise vertices are marked as visited. |
| initVertices.udw | Initialize the vertex fields. |
| bfs_load_balanced.udw | Performing a BFS using the load balancing framework starting from the marked vertices by `findVerticesOfSameColor.udw` |


## Compile

First, you need to compile whole Fastsim2:

``` bash
cd updown/
source setup_env.sh
mkdir -p build
cd build/
cmake $UPDOWN_SOURCE_CODE -DUPDOWNRT_ENABLE_TESTS=ON -DUPDOWNRT_ENABLE_UBENCH=ON -DUPDOWNRT_ENABLE_LIBRARIES=ON -DCMAKE_INSTALL_PREFIX=$UPDOWN_INSTALL_DIR -DUPDOWNRT_ENABLE_APPS=ON -DUPDOWN_ENABLE_DEBUG=OFF -DDEBUG_SYMBOLS=ON -DUPDOWN_ENABLE_FASTSIM=ON -DUPDOWN_ENABLE_BASIM=ON -DUPDOWN_NODES=1 -DUPDOWN_INST_TRACE=OFF -DUPDOWN_DETAIL_STATS=OFF -DUPDOWN_SENDPOLICY=OFF -DUPDOWN_FASTSIM_NETWOORK_TRACE_MSG=OFF -DUPDOWN_NETWORK_STATS=OFF -DUPDOWNRT_ENABLE_TE=OFF
make -j
make install
```

Then go to the folder `./updown/apps/scc`, compile udweave and top code

``` bash
cd ./updown/apps/scc
make
```

## Preprocess

Generate input graph binary file, input is a [SNAP](https://snap.stanford.edu/) graph.

``` bash
cd ./updown/apps/scc
./preprocess <input_filename> <output_filename>
```
This program generates input files for SCC (`<output_filename>_gv.bin` and `<output_filename>_nl.bin`). The transposed graph is stored in `<output_filename>_T_gv.bin` and `<output_filename>_T_nl.bin`

Example:
``` bash
./preprocess ca-AstroPh.txt ca-AstroPh
```


## SCC Run

``` bash
cd ./updown/apps/scc
./scc <gv_bin> <nl_bin> <num_lanes>
```

Example:
``` bash
cd ./updown/apps/scc
./scc AstroPh_gv.bin AstroPh_nl.bin 4096
```

## Validate

A SCC computation is included in the TOP code. At every stage (coloring and BFS) the graphs modified by UpDown are compared to the one created in the TOP code by the CPU. If the graphs are equal, "Graphs equal" is printed. If an error occured, the program terminates automatically. The final line should read "All vertices deleted, converged at iteration $num$.
