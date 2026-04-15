### The following variables are used in this Makefile:
UPDOWN_DIR = ../../../../

LINKER_DIR = $(UPDOWN_DIR)linker/
LINKER = $(LINKER_DIR)EFAlinker.py

UDWEAVE_DIR = $(UPDOWN_DIR)udweave
UDWEAVE = $(UDWEAVE_DIR)/UDweave.py

INSTALL_DIR = $(UPDOWN_DIR)install
.DEFAULT_GOAL := all

three_clique_mm_exe:   
	python3 $(UDWEAVE) --input v1v2intersection.udw -o v1v2intersection.py
	python3 $(UDWEAVE) --input vertex_master.udw -o vertex_master.py
	python3 $(UDWEAVE) --input intersection_launchers.udw -o intersection_launchers.py
	python3 $(UDWEAVE) --input master_launchers.udw -o master_launchers.py
	python3 $(UDWEAVE) --input main_master.udw -o main_master.py
	python3 $(LINKER) -L$(UPDOWN_DIR)libraries/UDMapShuffleReduce -L$(UPDOWN_DIR)libraries/dramalloc $(UPDOWN_DIR)libraries/dramalloc/dramalloc_linkable.py v1v2intersection.py vertex_master.py intersection_launchers.py master_launchers.py main_master.py dram_copy.py -o ../$@ $^


all: three_clique_mm_exe

clean:
	rm -f *.exe 