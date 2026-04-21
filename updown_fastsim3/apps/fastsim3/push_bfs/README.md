# Sync BFS using udweave README

There are two executable programs, bfs_udweave and bfs_udweave_global. 

bfs_udweave will store frontier in local memory;

 bfs_udweave_global will store frontier in global memory.



## Compile BFS
``` bash
cd updown/
source setup_env.sh
mkdir -p build/
cd build/
cmake $UPDOWN_SOURCE_CODE -DUPDOWNRT_ENABLE_TESTS=ON -DUPDOWNRT_ENABLE_UBENCH=ON -DUPDOWNRT_ENABLE_LIBRARIES=ON -DCMAKE_INSTALL_PREFIX=$UPDOWN_INSTALL_DIR -DUPDOWNRT_ENABLE_APPS=ON -DUPDOWN_ENABLE_DEBUG=OFF -DDEBUG_SYMBOLS=ON -DUPDOWN_ENABLE_FASTSIM=ON -DUPDOWN_ENABLE_BASIM=ON -DUPDOWN_NODES=1 -DUPDOWN_INST_TRACE=OFF -DUPDOWN_DETAIL_STATS=ON -DUPDOWN_SENDPOLICY=OFF -DUPDOWN_FASTSIM_NETWOORK_TRACE_MSG=OFF -DUPDOWN_NETWORK_STATS=ON
make -j
make install
```


## Preprocess
Use the preprocess in te/isb/bfs

## Compile udweave code
``` bash
cd updown/
source setup_env.sh
cd apps/network_test/sync_bfs/udwsrc/
make
```
## Run Command
``` bash
cd updown/install/updown/apps/
OMP_NUM_THREADS=<omp_threads> ./bfs_udweave <graph.bin> <num_lanes> <num_lanes_controlled_by_master> <root_vid> or
OMP_NUM_THREADS=<omp_threads> ./bfs_udweave_global <graph.bin> <num_lanes> <num_lanes_controlled_by_master> <root_vid>
```
### Example:
``` bash
OMP_NUM_THREADS=32 ./bfs_udweave /net/projects/updown/jiya/dataset/graphs/bfs/scale_24_seed_5_edges_max_deg_2048.bin 8192 32 28 0 or
OMP_NUM_THREADS=32 ./bfs_udweave_global /net/projects/updown/jiya/dataset/graphs/bfs/scale_24_seed_5_edges_max_deg_2048.bin 8192 32 28 0
```

`<omp_threads>`: the number of OpenMP threads assigned to this program. The simulator uses OpenMP to parallelize execution.

`<graph_bin>`: path to the graphs outputted by preprocessing program.

`<num_lanes>`: number of UpDown lanes. One UpDown node has 2048 lanes, so, for example, 8192 corresponds to the 4 UpDown nodes.

`<num_lanes_controlled_by_master>`: the number of UpDown lanes controlled by a single master. The UpDown system, which ranges from 1 node to 512 nodes, requires multi-level control for synchronization and broadcast to reduce synchronization and broadcast overhead. At each level, one control lane manages `<num_lanes_controlled_by_master>` lanes.  If the number of control lanes exceeds  `<num_lanes_controlled_by_master>`, higher-level control lanes are introduced to manage them, and the hierarchy expands as needed.In exameple, we set `<num_lanes_controlled_by_master>` to 32.

`<root_vid>`: root vertex ID of the output BFS tree. 