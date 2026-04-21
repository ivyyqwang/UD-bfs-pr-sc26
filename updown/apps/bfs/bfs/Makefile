### The following variables are used in this Makefile:
LINKER_DIR = ../../../linker/
LINKER = $(LINKER_DIR)EFAlinker.py

INSTALL_DIR = ../../../install
.DEFAULT_GOAL := all

push_pull_exe: GenBfsPushPullEFA.py pull_bfs_phase.py
	mkdir -p out
	python3 $(LINKER) -L./ -L../../../ -L../../../libraries/UDMapShuffleReduce -L../../../libraries/UDMapShuffleReduce/linkable/LinkableGlobalSync.py   -o ./out/$@ ../../../libraries/dramalloc/dramalloc_linkable.py $^

all: push_pull_exe 

clean:
	rm -f *.exe *.out *.o ./out/*.py ./out/*.hpp