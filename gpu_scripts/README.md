This folder contains the programs we use to benchmark GPU performance using the CuGraph library. 

The scripts take two inputs: graph file directory and graph name list with run parameters (e.g., start vertex for BFS or k-value for k-truss). An example command is shown below.

``` python3 <app>_batch.py <graph_dir> <graph_list>```

Each row in the graph list file contain a pair of graph name and run parameter. If the application does not require a run parameter, that field will be ignored. However, a placeholder value has to be entered for the parser to work correctly. The code will search for ```graph_name.tsv``` and ```graph_name.txt``` in the ```graph_dir```. The rows in these files contain start and end vertex indices. An example file (test_snap_list.txt) is included.

The txt files follow the format of SNAP datasets from https://snap.stanford.edu/data/. The tsv files follow the format of https://graphchallenge.mit.edu/data-sets/.