#!/bin/bash
export UPDOWN_SOURCE_CODE=`pwd`
export UPDOWN_INSTALL_DIR=`pwd`/install
export PYTHONPATH=$PYTHONPATH:`pwd`
export PYTHONPATH=$PYTHONPATH:`pwd`/libraries/UDMapShuffleReduce
export LD_LIBRARY_PATH=/net/projects/updown/tssu/python/techstaff/3.8/lib:$LD_LIBRARY_PATH