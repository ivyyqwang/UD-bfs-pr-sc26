# K-core Compact

## Compile

First, you need to compile whole Fastsim2

The following command is how to compile fastsim2

``` bash
cd updown/
source setup_env.sh
mkdir -p build
cd build/
cmake $UPDOWN_SOURCE_CODE -DUPDOWNRT_ENABLE_TESTS=ON -DUPDOWNRT_ENABLE_UBENCH=ON -DUPDOWNRT_ENABLE_LIBRARIES=ON -DCMAKE_INSTALL_PREFIX=$UPDOWN_INSTALL_DIR -DUPDOWNRT_ENABLE_APPS=ON -DUPDOWN_ENABLE_DEBUG=OFF -DDEBUG_SYMBOLS=ON -DUPDOWN_ENABLE_FASTSIM=ON -DUPDOWN_ENABLE_BASIM=ON -DUPDOWN_NODES=1 -DUPDOWN_INST_TRACE=OFF -DUPDOWN_DETAIL_STATS=OFF -DUPDOWN_SENDPOLICY=OFF -DUPDOWN_FASTSIM_NETWOORK_TRACE_MSG=OFF -DUPDOWN_NETWORK_STATS=OFF -DUPDOWNRT_ENABLE_TE=ON
make -j
make install
```

Then go to `updown/apps/kcore/original` folder, compile udweave and top code

``` bash
cd updown/apps/kcore/compact
make
```

## preprocess

Generate input graph binary file, input is a SNAP graph.

``` bash
cd updown/apps/kcore/compact
./preprocess <input_filename> <output_filename>
```
This program generates input files for the Ktruss (`<output_filename>_gv.bin` and `<output_filename>_nl.bin`). 

Example:
``` bash
./preprocess ca-AstroPh.txt ./ca-AstroPh.txt
```


## Kcore Run

``` bash
cd updown/apps/kcore/compact
./compac <gv_bin> <nl_bin> <num_lanes> <k>
./reset <gv_bin> <nl_bin> <num_lanes> <k>
```

Example:
``` bash
cd updown/apps/kcore/original
./compact AstroPh_gv.bin AstroPh_nl.bin 2048 10
./resett AstroPh_gv.bin AstroPh_nl.bin 2048 10
```

## Valiate

Kcore will compare UpDown results with CPU results, output "xxx Finished (No Errors!)".
