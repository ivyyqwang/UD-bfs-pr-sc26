
# For compiling inside the container environment...
UPDOWN_ROOT=../../..

EXEC = scc

UDWEAVE_DIR = $(UPDOWN_ROOT)/udweave
UDWEAVE = $(UDWEAVE_DIR)/UDweave.py

LINKER_DIR = $(UPDOWN_ROOT)/linker/
LINKER = $(LINKER_DIR)EFAlinker.py

UDASM_DIR=$(UPDOWN_ROOT)/udbasim/assembler
UDASM=efa2bin.py

INSTALL_DIR = $(UPDOWN_ROOT)/install/apps
INSTALLED_DIR = $(UPDOWN_ROOT)/install/updown
UPDOWN_BUILD_ROOT=$(UPDOWN_ROOT)/build

# DEP_FILES=coloring.py copyColors.py initVertices.py findVerticesOfSameColor.py \
# 		  bfs.py bfs_wrapper.py prefixSum.py prefixSumDown.py \
# 		  broadcastReduction.py

DEP_FILES=coloring.py copyData.py initVertices.py findVerticesOfSameColor.py \
		  bfs_load_balanced.py prefixSum.py prefixSumDown.py \
		  broadcastReduction.py delete_vertices.py
PYTHON=python3
CC=c++
CCFLAGS=-DBASE_PATH=\"$(UPDOWN_ROOT)/install\" \
		-DBASIM=1 \
		-DFASTSIM=1 \
		-DNODE1=1 \
		-DENABLE_SQLITE=1 \
		-DDETAIL_STATS=1 \
		-DMAX_BINS=2000 \
		-DBUCKET_SIZE=20 \
		-DMAX_COUNT_BINS=2000 \
		-DCOUNT_BUCKET_SIZE=1 \
		-DMAX_BYTES_BINS=4096 \
		-DBYTES_BUCKET_SIZE=64 \
		-I./include \
		-I$(HOME)/gem5/include \
		-I$(UPDOWN_ROOT)/include \
		-I$(UPDOWN_ROOT)/linkable \
		-I$(UPDOWN_ROOT)/basimruntime/include \
		-I$(UPDOWN_ROOT)/simruntime/include \
		-I$(UPDOWN_ROOT)/runtime/include \
		-I$(UPDOWN_ROOT)/common/include \
		-I$(UPDOWN_ROOT)/udbasim/isa/include \
		-I$(UPDOWN_ROOT)/udbasim/lane/include \
		-I$(UPDOWN_ROOT)/udbasim/accel/include \
		-I$(UPDOWN_ROOT)/udbasim/common/include \
		-I$(UPDOWN_ROOT)/udbasim/mem/include \
		-I$(UPDOWN_ROOT)/apps/common/glib-adv \
		-I$(UPDOWN_ROOT)/apps/common/glib-core \
		-I$(UPDOWN_ROOT)/apps/common/snap-adv \
		-I$(UPDOWN_ROOT)/apps/common/snap-core \
		-I$(UPDOWN_ROOT)/ext/sqlite3/include \
		-I$(UPDOWN_ROOT)/apps/common/snap-exp \
		-I$(UPDOWN_ROOT)/libraries/dramalloc \
		-I$(UPDOWN_ROOT)/libraries \
		-I$(INSTALLED_DIR)/libraries \
		-c \
		-std=c++17 \
		-fopenmp \
		# -O3


# LDFLAGS=$(UPDOWN_ROOT)/apps/common/snap-core/Snap.o \
# 		-L$(INSTALLED_DIR)/libraries/dramalloc \
# 		-Wl,-rpath,$(INSTALLED_DIR)/libraries/dramalloc: \
# 			$(INSTALLED_DIR)/lib/libUpDownBASimRuntimeStatic.a \
# 			$(INSTALLED_DIR)/lib/libUpDownSimRuntimeStatic.a \
# 		/usr/lib/x86_64-linux-gnu/libpython3.10.so \
# 		$(INSTALLED_DIR)/lib/libUpDownRuntimeStatic.a \
# 		$(INSTALLED_DIR)/lib/libUDAcceleratorStatic.a \
# 		$(INSTALLED_DIR)/lib/libUDMemoryStatic.a \
# 		$(INSTALLED_DIR)/lib/libLaneElementsStatic.a \
# 		$(INSTALLED_DIR)/lib/libISAElementsStatic.a \
# 		$(wildcard $(UPDOWN_BUILD_ROOT)/udbasim/mem/libUDMemoryStatic.a) \
# 		-std=c++17 \
# 		-fopenmp \
# 		-lpthread \
# 		-O3

LDFLAGS=$(UPDOWN_ROOT)/apps/common/snap-core/Snap.o \
		-L$(UPDOWN_ROOT)/libraries/dramalloc \
		-Wl,-rpath,$(UPDOWN_ROOT)/libraries/dramalloc: \
			$(UPDOWN_BUILD_ROOT)/libraries/libUDLibs.a \
			$(UPDOWN_BUILD_ROOT)/basimruntime/libUpDownBASimRuntimeStatic.a \
			$(UPDOWN_BUILD_ROOT)/simruntime/libUpDownSimRuntimeStatic.a \
		$(UPDOWN_BUILD_ROOT)/runtime/libUpDownRuntimeStatic.a \
		$(UPDOWN_BUILD_ROOT)/udbasim/accel/libUDAcceleratorStatic.a \
		$(UPDOWN_BUILD_ROOT)/udbasim/lane/libLaneElementsStatic.a \
		$(wildcard $(UPDOWN_BUILD_ROOT)/udbasim/mem/libUDMemoryStatic.a) \
		$(UPDOWN_BUILD_ROOT)/udbasim/isa/libISAElementsStatic.a \
		$(wildcard $(UPDOWN_BUILD_ROOT)/ext/sqlite3/libsqlite3.a) \
		-ldl \
		-std=c++17 \
		-fopenmp \
		-O3
		

.DEFAULT_GOAL := all
.PHONY:
all: $(EXEC)_exe.bin $(EXEC) preprocess

$(EXEC)_exe.bin: $(EXEC)_exe.py
	cd $(UDASM_DIR) && \
	$(PYTHON) $(UDASM) \
		--efa ${CURDIR}/$<  \
		--outpath ${CURDIR}/${dir $@} \
		--toplinker --text-symbol-table

# Linker
$(EXEC)_exe.py: $(DEP_FILES) #GenBfsPullEFA.py
	python3 $(LINKER) -L./ \
		-L$(UPDOWN_ROOT)/libraries/dramalloc \
		-L$(UPDOWN_ROOT)/libraries/UDMapShuffleReduce/linkable/modules/Broadcast.py \
		-L$(UPDOWN_ROOT)/libraries/UDMapShuffleReduce/linkable/ \
		-L$(UPDOWN_ROOT)/libraries/UDMapShuffleReduce/ \
		-L$(UPDOWN_ROOT)/libraries/UDMapShuffleReduce/utils/ \
		-L$(UPDOWN_ROOT) \
		-L./ \
		-o ./$@ $^ $(UPDOWN_ROOT)/libraries/dramalloc/dramalloc_linkable.py \
	 	           $(UPDOWN_ROOT)/libraries/UDMapShuffleReduce/udweave/LinkableBroadcast.py

%.py: %.udw scc.udwh
	$(UDWEAVE) -i $< \
			   -I $(INSTALLED_DIR)/libraries/ \
			   -I $(UPDOWN_ROOT)/libraries/LMStaticMaps/ \
			   -o $(EXEC).assembly -E 
	$(UDWEAVE) -i $< \
			   -I $(INSTALLED_DIR)/libraries/ \
			   -I $(UPDOWN_ROOT)/libraries/LMStaticMaps/ \
			   -o $@  

$(EXEC).o: $(EXEC).cpp
	$(CXX) $(CCFLAGS) $(EXTRA_C_FLAGS) -o $@ $<

$(EXEC): $(EXEC).o
	$(CXX) $< -o $@ $(LDFLAGS)

preprocess: preprocess.cpp 
	$(CXX) -O3 preprocess.cpp -o preprocess

# all: $(EXEC) $(EXEC)_exe.bin preprocess

clean:
	rm -f $(EXEC)
	rm -f $(EXEC).o
# 	rm -f $(EXEC).py $(DEP_FILES)
# 	rm -f $(EXEC)_exe.hpp
# 	rm -f $(EXEC)_exe.py
	rm -f $(EXEC)_exe.bin
	rm -f $(EXEC).assembly
	rm -Rf __pycache__
	rm -f $(EXEC)_exe.symbol_table
	rm -f preprocess
