### The following variables are used in this Makefile:

UPDOWN_SRC_DIR = ../../../

LINKER_DIR = $(UPDOWN_SRC_DIR)/linker/
LINKER = $(LINKER_DIR)EFAlinker.py

UDWEAVE_DIR = $(UPDOWN_SRC_DIR)/udweave
UDWEAVE = $(UDWEAVE_DIR)/UDweave.py

LIBRARIES_DIR = $(UPDOWN_SRC_DIR)/libraries
LMSTATICMAP_DIR = ${LIBRARIES_DIR}/LMStaticMaps


DRAMALLOC_DIR = ${LIBRARIES_DIR}/dramalloc

UDKVMSR_DIR = ${LIBRARIES_DIR}/UDMapShuffleReduce
UDKVMSR_LINKABLE_DIR = ${UDKVMSR_DIR}/linkable
UDKVMSR_UTILS_DIR = ${UDKVMSR_DIR}/utils

GLOBAL_BCST_DIR = ${LIBRARIES_DIR}/UDMapShuffleReduce/udweave

Broadcast: Broadcast.udw
	python3 ${UDWEAVE} -i Broadcast.udw -o Broadcast.py -I ${UDKVMSR_LINKABLE_DIR} -I ${LMSTATICMAP_DIR} -I ${UDKVMSR_DIR}

LinkableBroadcast: Broadcast.py
	python3 $(LINKER) -f linkable-module -L./ -L${UDKVMSR_LINKABLE_DIR} -L${UDKVMSR_DIR} -L${LMSTATICMAP_DIR} -o ./LinkableBroadcast.py $^

all: Broadcast LinkableBroadcast
