# Push PR README

## Files

| Name | Description|
|-----------|---------|
| out/pr_exe.py | PR updown assembly code |
| pagerankMSRsplit.cpp | pr top code |

## Input graph

Input file is in ai-cluster /net/scratch2/jiya/dataset/pr_test/


## Compile

In current version, the number of UpDown nodes is hard code in `NUM_NODES` in splitPRMSRLinkableConfig.py, default is 4. So if you change the number of UpDown nodes, you need to change `NUM_NODES` and recompile the udweave code.

``` bash
cd updown/apps/fastsim3/push_pr/
make
```


## Run Command

``` bash
mpirun -np n --tag-output --report-bindings --map-by numa -x OMP_NUM_THREADS ./pagerankMSRsplit <graph_bfs_gv.bin> <graph_nl.bin>
```

eg:

``` bash
time mpirun -np 4 --tag-output --report-bindings --bind-to core --map-by socket -x OMP_NUM_THREADS /pagerankMSRsplit /net/scratch2/jiya/dataset/pr_test/s22_bfs_gv.bin /net/scratch2/jiya/dataset/pr_test/s22_nl.bin 4
```

### Valiate

PR will run UpDown and CPU version to validate results if define `VALIDATE_RESULT` in pagerankMSRsplit.cpp.
