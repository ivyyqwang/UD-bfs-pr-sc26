# UD-bfs-pr-sc26

This repository contains the UpDown accelerator simulator, UpDown application programs and the projection model for the full system design.

## Folder Structure

The folder structure of the respository

```
├── graph_analytics_and_modeling        # projection model.
│   ├── julia                           # random graph generators and serial algorithms used for producing work statistics
│   ├── python                          # projection code for BFS and PR.
│   ├── data
│   │   ├── julia_output                # precomputed graph/algorithm statistics used for projections
├── gpu_scripts                         # GPU baseline programs and scripts
├── network_modeling                    # discrete event network simulator
│   ├──	data                            # radix 22 PolarStar network adjacency list
│   │  	├── results                     # precomputed network simulation results used for generating Figure 8
│   ├── src                             # source code for the DiscreteEventNetworkSim julia module
│   ├──	test                            # testing code for julia module
│   ├──	plots                           # plotting code for generating Figure 8
├── updown                              # UpDown simulator
│   ├── apps                            # UpDown program code and top (CPU) drivers
│   ├── libraries                       # UpDown software libraries
│   ├── linker                          # UpDown program linker
│   ├── runtime                         # UpDown top (CPU) runtime
│   ├── udbasim                         # UpDown simulator
│   ├── udweave                         # UpDown UDWeave program compiler
│   ├── common                          # useful utility programs files
├── updown_fastsim3                     # full system scale UpDown simulator
│   ├── apps                            # UpDown program code and top (CPU) drivers
│   ├── runtime                         # UpDown runtime
└───└── udbasim                         # UpDown simulator
```
