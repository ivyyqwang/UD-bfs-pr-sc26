### The following variables are used in this Makefile:
LINKER_DIR = ../../../linker/
LINKER = $(LINKER_DIR)EFAlinker.py

UDWEAVE_DIR = ../../../udweave
UDWEAVE = $(UDWEAVE_DIR)/UDweave.py
UDWEAVE = /net/projects/updown/jiya/Updown_project/new_test/updown/udweave/UDweave.py 

INSTALL_DIR = ../../../install
.DEFAULT_GOAL := all

msrUDW: splitPRMSRLinkableModule.py
	mkdir -p ./out 
	python3 $(LINKER) -f linkable-module -L./ -L../../../libraries/UDMapShuffleReduce/linkable -L../../../libraries/LMStaticMaps -L../../../libraries/UDMapShuffleReduce -L../../../ -o ./out/$@ $^

prUDW: splitPagerankMSR.udw
	python3 $(UDWEAVE) --input splitPagerankMSR.udw -o ./out/splitPagerankMSR.py 

pr_exe: ./out/msrUDW.py ./out/splitPagerankMSR.py 
	python3 $(LINKER) -L./ -L../../../libraries/UDMapShuffleReduce/linkable  -L../../../libraries/dramalloc -L../../../libraries/LMStaticMaps  -L../../../libraries/UDMapShuffleReduce -L../../../ -o ./out/$@  ../../../libraries/dramalloc/dramalloc_linkable.py ../../../libraries/UDMapShuffleReduce/udweave/LinkableBroadcast.py $^ 


all: msrUDW prUDW pr_exe

clean:
	rm -f *.exe *.out *.o 