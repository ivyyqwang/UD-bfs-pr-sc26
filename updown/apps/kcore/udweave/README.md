# K-core

## Description
The k-core of a graph $G = (V, E)$ is the maximal subgraph where every vertex has degree at least $k$. K-core decomposition identifies all such subgraphs for increasing values of $k$, assigning each vertex a coreness value $k[v]$ - the index of the highest k-core to which it belongs. The graph's coreness $k_{max}$ is the maximum coreness across all vertices. The algorithm computes this by repeatedly removing vertices of degree $\le k$ and updating the degrees of their neighbors until all remaining vertices have degree $\ge k+1$, then incrementing k and repeating. The figure shows an example of k-Core with $k_{max}=3$. Vertices and edges peeled in each subround are marked red. The algorithm completes when the graph is exhausted, i.e., all vertices have been removed and assigned a coreness value equal to the highest k-core to which they belonged before elimination.
Reference: [https://www.sciencedirect.com/science/article/abs/pii/S037015731930328X](https://www.sciencedirect.com/science/article/abs/pii/S037015731930328X)

## Performance
The performance for k-core is documented [here](https://docs.google.com/document/d/1vOqL0154ppxFPjgmjN_TxDxFZi_jeS8rKj3NcebO9ZY/edit?tab=t.0).

## Files

| Name | Description|
|-----------|---------|
| preprocess.cpp | preprocess file |
| kcore_exe.py | k-core assembly code |
| kcore.cpp | k-core top code |
| kcore.udw | Update the vertex degree depending on deleted neighbors |
| markVertices.udw | Mark vertices as deleted, if their $k < degree$ |
| prefixSum.udw | Aggregate the degrees from all vertices to compute the prefix sum required for the load balancing framework. |
| prefixSumDown.udw | Communicate the prefix sum down to the vertices. |

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

Then go to the folder `./updown/apps/kcore/`, compile udweave and top code

``` bash
cd ./updown/apps/kcore
make
```

## Preprocess

Generate input graph binary file, input is a [SNAP](https://snap.stanford.edu/) graph.

``` bash
cd ./updown/apps/kcore
./preprocess <input_filename> <output_filename>
```
This program generates input files for the k-core application (`<output_filename>_gv.bin` and `<output_filename>_nl.bin`). 

Example:
``` bash
./preprocess ca-AstroPh.txt ca-AstroPh
```


## K-core Run

``` bash
cd ./updown/apps/kcore
./kcore <gv_bin> <nl_bin> <num_lanes>
```

Example:
``` bash
cd ./updown/apps/kcore
./kcore AstroPh_gv.bin AstroPh_nl.bin 2048
```

## Validate
A k-core computation is included in the TOP code. The output of UpDown is compared against the results generated in the TOP code by the CPU. If no error is detected, the output "K-Core Finished (No Errors!)" is printed.
