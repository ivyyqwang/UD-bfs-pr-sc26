
# For compiling inside the container environment...
UPDOWN_ROOT=../../../../


UDWEAVE_DIR = $(UPDOWN_ROOT)/udweave
UDWEAVE = $(UDWEAVE_DIR)/UDweave.py

LINKER_DIR = $(UPDOWN_ROOT)/linker/
LINKER = $(LINKER_DIR)EFAlinker.py

UDASM_DIR=$(UPDOWN_ROOT)/udbasim/assembler
UDASM=efa2bin.py

INSTALL_DIR = $(UPDOWN_ROOT)/install/apps
INSTALLED_DIR = $(UPDOWN_ROOT)/install/updown
UPDOWN_BUILD_ROOT=$(UPDOWN_ROOT)/build


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
all: compact_exe.bin compact reset_deg_exe.bin reset_deg preprocess

compact_exe.bin: compact_exe.py
	cd $(UDASM_DIR) && \
	$(PYTHON) $(UDASM) \
		--efa ${CURDIR}/$<  \
		--outpath ${CURDIR}/${dir $@} \
		--toplinker --text-symbol-table

# Linker
compact_exe.py: compact.py \
					$(UPDOWN_ROOT)/libraries/dramalloc/dramalloc_linkable.py
	python3 $(LINKER) -L./ \
		-L$(UPDOWN_ROOT)/libraries/UDMapShuffleReduce/linkable/ \
		-L$(UPDOWN_ROOT)/libraries/UDMapShuffleReduce/ \
		-L$(UPDOWN_ROOT)/libraries/UDMapShuffleReduce/linkable/LinkableGlobalSync.py \
		-L$(UPDOWN_ROOT)/libraries/UDMapShuffleReduce/KVMSRMachineConfig.py \
		-L$(UPDOWN_ROOT)/libraries/dramalloc \
		-L$(UPDOWN_ROOT) \
		-L./ \
		-o ./$@ $^

compact.py: compact.udw
	$(UDWEAVE) -i $< \
			   -I $(INSTALLED_DIR)/libraries/ \
			   -o compact.assembly -E 
	$(UDWEAVE) -i $< \
			   -I $(INSTALLED_DIR)/libraries/ \
			   -o $@  

compact.o: compact.cpp
	$(CXX) $(CCFLAGS) $(EXTRA_C_FLAGS) -o $@ $<

compact: compact.o
	$(CXX) $< -o $@ $(LDFLAGS)

reset_deg_exe.bin: reset_deg_exe.py
	cd $(UDASM_DIR) && \
	$(PYTHON) $(UDASM) \
		--efa ${CURDIR}/$<  \
		--outpath ${CURDIR}/${dir $@} \
		--toplinker --text-symbol-table

# Linker
reset_deg_exe.py: reset_deg.py \
					$(UPDOWN_ROOT)/libraries/dramalloc/dramalloc_linkable.py
	python3 $(LINKER) -L./ \
		-L$(UPDOWN_ROOT)/libraries/UDMapShuffleReduce/linkable/ \
		-L$(UPDOWN_ROOT)/libraries/UDMapShuffleReduce/ \
		-L$(UPDOWN_ROOT)/libraries/UDMapShuffleReduce/linkable/LinkableGlobalSync.py \
		-L$(UPDOWN_ROOT)/libraries/UDMapShuffleReduce/KVMSRMachineConfig.py \
		-L$(UPDOWN_ROOT)/libraries/dramalloc \
		-L$(UPDOWN_ROOT) \
		-L./ \
		-o ./$@ $^

reset_deg.py: reset_deg.udw
	$(UDWEAVE) -i $< \
			   -I $(INSTALLED_DIR)/libraries/ \
			   -o reset_deg.assembly -E 
	$(UDWEAVE) -i $< \
			   -I $(INSTALLED_DIR)/libraries/ \
			   -o $@  

reset_deg.o: reset_deg.cpp
	$(CXX) $(CCFLAGS) $(EXTRA_C_FLAGS) -o $@ $<

reset_deg: reset_deg.o
	$(CXX) $< -o $@ $(LDFLAGS)

preprocess: preprocess.cpp 
	$(CXX) -O3 preprocess.cpp -o preprocess


clean:
	rm -f compact
	rm -f compact.o
	rm -f compact.py
	rm -f compact_exe.hpp
	rm -f compact_exe.py
	rm -f compact_exe.bin
	rm -f compact.assembly
	rm -f compact_exe.symbol_table
	rm -f reset_deg
	rm -f reset_deg.o
	rm -f reset_deg.py
	rm -f reset_deg_exe.hpp
	rm -f reset_deg_exe.py
	rm -f reset_deg_exe.bin
	rm -f reset_deg.assembly
	rm -f reset_deg_exe.symbol_table
	rm -Rf __pycache__
	rm -Rf __pycache__
	rm -f preprocess
