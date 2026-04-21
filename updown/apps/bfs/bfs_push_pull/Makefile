### The following variables are used in this Makefile:
UPDOWN_ROOT=../../../
LINKER_DIR = $(UPDOWN_ROOT)/linker/
LINKER = $(LINKER_DIR)EFAlinker.py

INSTALL_DIR = $(UPDOWN_ROOT)install
.DEFAULT_GOAL := all

push_pull_exe: GenBfsPushPullEFA.py pull_bfs_phase.py
	mkdir -p out
	python3 $(LINKER) -L./ -L$(UPDOWN_ROOT) -L$(UPDOWN_ROOT)/libraries/UDMapShuffleReduce -L$(UPDOWN_ROOT)/libraries/UDMapShuffleReduce/linkable/LinkableGlobalSync.py   -o ./out/$@ $(UPDOWN_ROOT)/libraries/dramalloc/dramalloc_linkable.py $^

all: push_pull_exe 

clean:
	rm -f *.exe *.out *.o ./out/*.py ./out/*.hpp