from linker.EFAProgram import efaProgram

## UDWeave version: 7808cc0 (2026-04-24)

## Global constants

@efaProgram
def EFA_prefixSumDown(efa):
  efa.code_level = 'machine'
  state0 = efa.State("udweave_init") #Only one state code 
  efa.add_initId(state0.state_id)
  ## Static declarations
  ## Scoped Variable "counter" uses Register X16, scope (0)
  ## Scoped Variable "maxDegree" uses Register X17, scope (0)
  ## Scoped Variable "counter" uses Register X16, scope (0)
  ## Scoped Variable "maxDegree" uses Register X17, scope (0)
  ## Scoped Variable "counter" uses Register X16, scope (0)
  ## Scoped Variable "maxDegree" uses Register X17, scope (0)
  ## Scoped Variable "curAddressBlock" uses Register X16, scope (0)
  ## Scoped Variable "curVertexID" uses Register X17, scope (0)
  ## Scoped Variable "numVertices" uses Register X18, scope (0)
  ## Scoped Variable "counter" uses Register X19, scope (0)
  ## Scoped Variable "expectedReturnValues" uses Register X20, scope (0)
  ## Scoped Variable "prefixSum" uses Register X21, scope (0)
  ## Scoped Variable "maxDegree" uses Register X22, scope (0)
  ## Here, the number of updates performed by the BFS is stored
  ## 8 children each with three words of data each taking 8 bytes
  ## can also be 6 children each with 4 words of data each taking 8 bytes
  ## can also be 6 childen with 5 words each
  ## A macro which declares a local pointer and writes a 1 to the address
  ## LMBASE + TOP_FLAG_OFFSET indicating to the TOP core, that we completed
  ## UpDown program execution.
  ## #define DEBUG_PREFIXSUM
  ## size: (max (16384 / THRESHOLD_NODE_BC) + 1) * 8 Bytes each entries
  ## Address: 128-383 used by UDKVMSR for the BFS (256 Bytes)
  ## size: 1 entry per node + 1 (max THRESHOLD_NODE_BC * 8 Bytes)
  ## size: (32 + 1) (UDs) * 8
  ## size: (64 + 1) (Lanes/UD) * 8
  ## size: (MAX_OUTSTANDING_READ_REQUESTS + 1) * 8
  ## how many vertices to load in the lane in a batch
  ## distribute to the nodes
  
  #################################################################
  ###### Writing code for thread PrefixSumDownAboveNodeLevel ######
  #################################################################
  # Writing code for event PrefixSumDownAboveNodeLevel::start
  tranPrefixSumDownAboveNodeLevel__start = efa.writeEvent('PrefixSumDownAboveNodeLevel::start')
  tranPrefixSumDownAboveNodeLevel__start.writeAction(f"__entry: movir X16 0") 
  tranPrefixSumDownAboveNodeLevel__start.writeAction(f"movir X17 0") 
  tranPrefixSumDownAboveNodeLevel__start.writeAction(f"addi X11 X18 0") 
  tranPrefixSumDownAboveNodeLevel__start.writeAction(f"addi X7 X19 2440") 
  tranPrefixSumDownAboveNodeLevel__start.writeAction(f"addi X7 X20 8") 
  tranPrefixSumDownAboveNodeLevel__start.writeAction(f"bcpyoli X8 X20 3") 
  tranPrefixSumDownAboveNodeLevel__start.writeAction(f"evi X2 X21 PrefixSumDownAboveNodeLevel::returnFromChild 1") 
  tranPrefixSumDownAboveNodeLevel__start.writeAction(f"movir X22 131072") 
  tranPrefixSumDownAboveNodeLevel__start.writeAction(f"bleu X22 X10 __if_start_2_post") 
  tranPrefixSumDownAboveNodeLevel__start.writeAction(f"__if_start_0_true: addi X10 X22 0") 
  tranPrefixSumDownAboveNodeLevel__start.writeAction(f"__if_start_2_post: movir X23 0") 
  tranPrefixSumDownAboveNodeLevel__start.writeAction(f"__for_start_3_condition: bleu X22 X23 __for_start_5_post") 
  tranPrefixSumDownAboveNodeLevel__start.writeAction(f"__for_start_4_body: movwlr X19(X16,0,0) X24") 
  tranPrefixSumDownAboveNodeLevel__start.writeAction(f"add X18 X24 X18") 
  tranPrefixSumDownAboveNodeLevel__start.writeAction(f"movrl X18 24(X20) 0 8") 
  tranPrefixSumDownAboveNodeLevel__start.writeAction(f"add X0 X23 X24") 
  tranPrefixSumDownAboveNodeLevel__start.writeAction(f"movir X25 0") 
  tranPrefixSumDownAboveNodeLevel__start.writeAction(f"evlb X25 PrefixSumDownNodeLevel::start") 
  tranPrefixSumDownAboveNodeLevel__start.writeAction(f"evi X25 X25 255 4") 
  tranPrefixSumDownAboveNodeLevel__start.writeAction(f"ev X25 X25 X24 X24 8") 
  tranPrefixSumDownAboveNodeLevel__start.writeAction(f"send_wcont X25 X21 X20 4") 
  tranPrefixSumDownAboveNodeLevel__start.writeAction(f"addi X16 X16 1") 
  tranPrefixSumDownAboveNodeLevel__start.writeAction(f"addi X23 X23 2048") 
  tranPrefixSumDownAboveNodeLevel__start.writeAction(f"jmp __for_start_3_condition") 
  tranPrefixSumDownAboveNodeLevel__start.writeAction(f"__for_start_5_post: yield") 
  
  # Writing code for event PrefixSumDownAboveNodeLevel::returnFromChild
  tranPrefixSumDownAboveNodeLevel__returnFromChild = efa.writeEvent('PrefixSumDownAboveNodeLevel::returnFromChild')
  tranPrefixSumDownAboveNodeLevel__returnFromChild.writeAction(f"__entry: bleu X8 X17 __if_returnFromChild_2_post") 
  tranPrefixSumDownAboveNodeLevel__returnFromChild.writeAction(f"__if_returnFromChild_0_true: addi X8 X17 0") 
  tranPrefixSumDownAboveNodeLevel__returnFromChild.writeAction(f"__if_returnFromChild_2_post: subi X16 X16 1") 
  tranPrefixSumDownAboveNodeLevel__returnFromChild.writeAction(f"bneiu X16 0 __if_returnFromChild_5_post") 
  tranPrefixSumDownAboveNodeLevel__returnFromChild.writeAction(f"__if_returnFromChild_3_true: movir X19 -1") 
  tranPrefixSumDownAboveNodeLevel__returnFromChild.writeAction(f"sri X19 X19 1") 
  tranPrefixSumDownAboveNodeLevel__returnFromChild.writeAction(f"sendr_wcont X1 X19 X17 X17") 
  tranPrefixSumDownAboveNodeLevel__returnFromChild.writeAction(f"yield_terminate") 
  tranPrefixSumDownAboveNodeLevel__returnFromChild.writeAction(f"__if_returnFromChild_5_post: yield") 
  
  ## distribute among UDs
  
  ############################################################
  ###### Writing code for thread PrefixSumDownNodeLevel ######
  ############################################################
  # Writing code for event PrefixSumDownNodeLevel::start
  tranPrefixSumDownNodeLevel__start = efa.writeEvent('PrefixSumDownNodeLevel::start')
  tranPrefixSumDownNodeLevel__start.writeAction(f"__entry: movir X16 0") 
  tranPrefixSumDownNodeLevel__start.writeAction(f"movir X17 0") 
  tranPrefixSumDownNodeLevel__start.writeAction(f"addi X11 X18 0") 
  tranPrefixSumDownNodeLevel__start.writeAction(f"addi X7 X19 2960") 
  tranPrefixSumDownNodeLevel__start.writeAction(f"addi X7 X20 8") 
  tranPrefixSumDownNodeLevel__start.writeAction(f"bcpyoli X8 X20 3") 
  tranPrefixSumDownNodeLevel__start.writeAction(f"evi X2 X21 PrefixSumDownNodeLevel::returnFromChild 1") 
  tranPrefixSumDownNodeLevel__start.writeAction(f"movir X22 2048") 
  tranPrefixSumDownNodeLevel__start.writeAction(f"movir X23 0") 
  tranPrefixSumDownNodeLevel__start.writeAction(f"__for_start_0_condition: bleu X22 X23 __for_start_2_post") 
  tranPrefixSumDownNodeLevel__start.writeAction(f"__for_start_1_body: movwlr X19(X16,0,0) X24") 
  tranPrefixSumDownNodeLevel__start.writeAction(f"add X18 X24 X18") 
  tranPrefixSumDownNodeLevel__start.writeAction(f"movrl X18 24(X20) 0 8") 
  tranPrefixSumDownNodeLevel__start.writeAction(f"add X0 X23 X24") 
  tranPrefixSumDownNodeLevel__start.writeAction(f"movir X25 0") 
  tranPrefixSumDownNodeLevel__start.writeAction(f"evlb X25 PrefixSumDownUDLevel::start") 
  tranPrefixSumDownNodeLevel__start.writeAction(f"evi X25 X25 255 4") 
  tranPrefixSumDownNodeLevel__start.writeAction(f"ev X25 X25 X24 X24 8") 
  tranPrefixSumDownNodeLevel__start.writeAction(f"send_wcont X25 X21 X20 4") 
  tranPrefixSumDownNodeLevel__start.writeAction(f"addi X16 X16 1") 
  tranPrefixSumDownNodeLevel__start.writeAction(f"addi X23 X23 64") 
  tranPrefixSumDownNodeLevel__start.writeAction(f"jmp __for_start_0_condition") 
  tranPrefixSumDownNodeLevel__start.writeAction(f"__for_start_2_post: yield") 
  
  # Writing code for event PrefixSumDownNodeLevel::returnFromChild
  tranPrefixSumDownNodeLevel__returnFromChild = efa.writeEvent('PrefixSumDownNodeLevel::returnFromChild')
  tranPrefixSumDownNodeLevel__returnFromChild.writeAction(f"__entry: bleu X8 X17 __if_returnFromChild_2_post") 
  tranPrefixSumDownNodeLevel__returnFromChild.writeAction(f"__if_returnFromChild_0_true: addi X8 X17 0") 
  tranPrefixSumDownNodeLevel__returnFromChild.writeAction(f"__if_returnFromChild_2_post: subi X16 X16 1") 
  tranPrefixSumDownNodeLevel__returnFromChild.writeAction(f"bneiu X16 0 __if_returnFromChild_5_post") 
  tranPrefixSumDownNodeLevel__returnFromChild.writeAction(f"__if_returnFromChild_3_true: movir X18 -1") 
  tranPrefixSumDownNodeLevel__returnFromChild.writeAction(f"sri X18 X18 1") 
  tranPrefixSumDownNodeLevel__returnFromChild.writeAction(f"sendr_wcont X1 X18 X17 X17") 
  tranPrefixSumDownNodeLevel__returnFromChild.writeAction(f"yield_terminate") 
  tranPrefixSumDownNodeLevel__returnFromChild.writeAction(f"__if_returnFromChild_5_post: yield") 
  
  ## distribute among the lanes
  
  ##########################################################
  ###### Writing code for thread PrefixSumDownUDLevel ######
  ##########################################################
  # Writing code for event PrefixSumDownUDLevel::start
  tranPrefixSumDownUDLevel__start = efa.writeEvent('PrefixSumDownUDLevel::start')
  tranPrefixSumDownUDLevel__start.writeAction(f"__entry: movir X16 64") 
  tranPrefixSumDownUDLevel__start.writeAction(f"movir X17 0") 
  tranPrefixSumDownUDLevel__start.writeAction(f"addi X11 X18 0") 
  tranPrefixSumDownUDLevel__start.writeAction(f"addi X7 X19 3224") 
  tranPrefixSumDownUDLevel__start.writeAction(f"addi X7 X20 8") 
  tranPrefixSumDownUDLevel__start.writeAction(f"bcpyoli X8 X20 3") 
  tranPrefixSumDownUDLevel__start.writeAction(f"evi X2 X21 PrefixSumDownUDLevel::returnFromChild 1") 
  tranPrefixSumDownUDLevel__start.writeAction(f"movir X22 64") 
  tranPrefixSumDownUDLevel__start.writeAction(f"movir X23 0") 
  tranPrefixSumDownUDLevel__start.writeAction(f"__for_start_0_condition: bleu X22 X23 __for_start_2_post") 
  tranPrefixSumDownUDLevel__start.writeAction(f"__for_start_1_body: movwlr X19(X23,0,0) X24") 
  tranPrefixSumDownUDLevel__start.writeAction(f"add X18 X24 X18") 
  tranPrefixSumDownUDLevel__start.writeAction(f"movrl X18 24(X20) 0 8") 
  tranPrefixSumDownUDLevel__start.writeAction(f"add X0 X23 X24") 
  tranPrefixSumDownUDLevel__start.writeAction(f"movir X25 0") 
  tranPrefixSumDownUDLevel__start.writeAction(f"evlb X25 PrefixSumDownWorker::start") 
  tranPrefixSumDownUDLevel__start.writeAction(f"evi X25 X25 255 4") 
  tranPrefixSumDownUDLevel__start.writeAction(f"ev X25 X25 X24 X24 8") 
  tranPrefixSumDownUDLevel__start.writeAction(f"send_wcont X25 X21 X20 4") 
  tranPrefixSumDownUDLevel__start.writeAction(f"addi X23 X23 1") 
  tranPrefixSumDownUDLevel__start.writeAction(f"jmp __for_start_0_condition") 
  tranPrefixSumDownUDLevel__start.writeAction(f"__for_start_2_post: yield") 
  
  # Writing code for event PrefixSumDownUDLevel::returnFromChild
  tranPrefixSumDownUDLevel__returnFromChild = efa.writeEvent('PrefixSumDownUDLevel::returnFromChild')
  tranPrefixSumDownUDLevel__returnFromChild.writeAction(f"__entry: bleu X8 X17 __if_returnFromChild_2_post") 
  tranPrefixSumDownUDLevel__returnFromChild.writeAction(f"__if_returnFromChild_0_true: addi X8 X17 0") 
  tranPrefixSumDownUDLevel__returnFromChild.writeAction(f"__if_returnFromChild_2_post: subi X16 X16 1") 
  tranPrefixSumDownUDLevel__returnFromChild.writeAction(f"bneiu X16 0 __if_returnFromChild_5_post") 
  tranPrefixSumDownUDLevel__returnFromChild.writeAction(f"__if_returnFromChild_3_true: movir X18 -1") 
  tranPrefixSumDownUDLevel__returnFromChild.writeAction(f"sri X18 X18 1") 
  tranPrefixSumDownUDLevel__returnFromChild.writeAction(f"sendr_wcont X1 X18 X17 X17") 
  tranPrefixSumDownUDLevel__returnFromChild.writeAction(f"yield_terminate") 
  tranPrefixSumDownUDLevel__returnFromChild.writeAction(f"__if_returnFromChild_5_post: yield") 
  
  
  #########################################################
  ###### Writing code for thread PrefixSumDownWorker ######
  #########################################################
  # Writing code for event PrefixSumDownWorker::start
  tranPrefixSumDownWorker__start = efa.writeEvent('PrefixSumDownWorker::start')
  ## determine the numVertices

  tranPrefixSumDownWorker__start.writeAction(f"__entry: div X9 X10 X23") 
  tranPrefixSumDownWorker__start.writeAction(f"mod X9 X10 X24") 
  tranPrefixSumDownWorker__start.writeAction(f"bleu X24 X0 __if_start_1_false") 
  tranPrefixSumDownWorker__start.writeAction(f"__if_start_0_true: addi X23 X18 1") 
  tranPrefixSumDownWorker__start.writeAction(f"addi X0 X25 0") 
  tranPrefixSumDownWorker__start.writeAction(f"jmp __if_start_2_post") 
  tranPrefixSumDownWorker__start.writeAction(f"__if_start_1_false: addi X23 X18 0") 
  tranPrefixSumDownWorker__start.writeAction(f"addi X24 X25 0") 
  tranPrefixSumDownWorker__start.writeAction(f"__if_start_2_post: bneiu X18 0 __if_start_5_post") 
  tranPrefixSumDownWorker__start.writeAction(f"__if_start_3_true: movir X24 0") 
  tranPrefixSumDownWorker__start.writeAction(f"movir X26 -1") 
  tranPrefixSumDownWorker__start.writeAction(f"sri X26 X26 1") 
  tranPrefixSumDownWorker__start.writeAction(f"sendr_wcont X1 X26 X24 X24") 
  tranPrefixSumDownWorker__start.writeAction(f"yield_terminate") 
  tranPrefixSumDownWorker__start.writeAction(f"__if_start_5_post: addi X11 X21 0") 
  ## set the base addresses

  tranPrefixSumDownWorker__start.writeAction(f"mul X0 X23 X23") 
  tranPrefixSumDownWorker__start.writeAction(f"add X23 X25 X17") 
  tranPrefixSumDownWorker__start.writeAction(f"sli X17 X25 6") 
  tranPrefixSumDownWorker__start.writeAction(f"add X8 X25 X16") 
  tranPrefixSumDownWorker__start.writeAction(f"addi X16 X25 8") 
  ## point to where the degree is

  tranPrefixSumDownWorker__start.writeAction(f"movir X19 0") 
  tranPrefixSumDownWorker__start.writeAction(f"movir X22 0") 
  tranPrefixSumDownWorker__start.writeAction(f"evi X2 X23 PrefixSumDownWorker::returnFromRead 1") 
  tranPrefixSumDownWorker__start.writeAction(f"movir X24 0") 
  tranPrefixSumDownWorker__start.writeAction(f"__for_start_6_condition: clti X24 X26 32") 
  tranPrefixSumDownWorker__start.writeAction(f"cgti X18 X27 0") 
  tranPrefixSumDownWorker__start.writeAction(f"and X26 X27 X26") 
  tranPrefixSumDownWorker__start.writeAction(f"beqiu X26 0 __for_start_8_post") 
  tranPrefixSumDownWorker__start.writeAction(f"__for_start_7_body: send_dmlm_ld X25 X23 1") 
  tranPrefixSumDownWorker__start.writeAction(f"addi X25 X25 64") 
  tranPrefixSumDownWorker__start.writeAction(f"subi X18 X18 1") 
  tranPrefixSumDownWorker__start.writeAction(f"addi X19 X19 1") 
  tranPrefixSumDownWorker__start.writeAction(f"addi X24 X24 1") 
  tranPrefixSumDownWorker__start.writeAction(f"jmp __for_start_6_condition") 
  tranPrefixSumDownWorker__start.writeAction(f"__for_start_8_post: addi X19 X20 0") 
  tranPrefixSumDownWorker__start.writeAction(f"yield") 
  
  # Writing code for event PrefixSumDownWorker::returnFromRead
  tranPrefixSumDownWorker__returnFromRead = efa.writeEvent('PrefixSumDownWorker::returnFromRead')
  ## determine, which vertex has been read

  tranPrefixSumDownWorker__returnFromRead.writeAction(f"__entry: sub X9 X16 X24") 
  tranPrefixSumDownWorker__returnFromRead.writeAction(f"sari X24 X23 6") 
  tranPrefixSumDownWorker__returnFromRead.writeAction(f"addi X23 X24 1") 
  ## shift by 1, since the first element of the prefix sum should be 0

  tranPrefixSumDownWorker__returnFromRead.writeAction(f"addi X7 X23 3744") 
  tranPrefixSumDownWorker__returnFromRead.writeAction(f"movwrl X8 X23(X24,0,0)") 
  tranPrefixSumDownWorker__returnFromRead.writeAction(f"subi X19 X19 1") 
  tranPrefixSumDownWorker__returnFromRead.writeAction(f"bleu X8 X22 __if_returnFromRead_2_post") 
  tranPrefixSumDownWorker__returnFromRead.writeAction(f"__if_returnFromRead_0_true: addi X8 X22 0") 
  tranPrefixSumDownWorker__returnFromRead.writeAction(f"__if_returnFromRead_2_post: bneiu X19 0 __if_returnFromRead_5_post") 
  tranPrefixSumDownWorker__returnFromRead.writeAction(f"__if_returnFromRead_3_true: addi X7 X24 8") 
  tranPrefixSumDownWorker__returnFromRead.writeAction(f"movir X25 -1") 
  tranPrefixSumDownWorker__returnFromRead.writeAction(f"movrl X25 24(X24) 0 8") 
  ## scc ID

  tranPrefixSumDownWorker__returnFromRead.writeAction(f"movir X25 0") 
  tranPrefixSumDownWorker__returnFromRead.writeAction(f"movrl X25 32(X24) 0 8") 
  ## vert->unused0 = 0;

  tranPrefixSumDownWorker__returnFromRead.writeAction(f"movir X25 0") 
  tranPrefixSumDownWorker__returnFromRead.writeAction(f"movrl X25 40(X24) 0 8") 
  ## vert->unused1 = 0;

  tranPrefixSumDownWorker__returnFromRead.writeAction(f"evi X2 X25 PrefixSumDownWorker::returnFromWrite 1") 
  ## compute the prefixSum

  tranPrefixSumDownWorker__returnFromRead.writeAction(f"movir X26 0") 
  tranPrefixSumDownWorker__returnFromRead.writeAction(f"__for_returnFromRead_6_condition: bleu X20 X26 __for_returnFromRead_8_post") 
  tranPrefixSumDownWorker__returnFromRead.writeAction(f"__for_returnFromRead_7_body: movwlr X23(X26,0,0) X27") 
  tranPrefixSumDownWorker__returnFromRead.writeAction(f"add X21 X27 X21") 
  tranPrefixSumDownWorker__returnFromRead.writeAction(f"movrl X21 0(X24) 0 8") 
  tranPrefixSumDownWorker__returnFromRead.writeAction(f"add X17 X26 X27") 
  tranPrefixSumDownWorker__returnFromRead.writeAction(f"movrl X27 8(X24) 0 8") 
  ## rewrite the vertexID (should be the same)

  tranPrefixSumDownWorker__returnFromRead.writeAction(f"movrl X27 16(X24) 0 8") 
  ## color = vertex ID initially

  ## write the data

  ## FOR DEBUGGING. You can store the data into the scratch fields and then compare it with the existing data

  ## send_dram_write(curAddressBlock + 32 /* point to edges_before */, spPtrSend, 2, cont);

  tranPrefixSumDownWorker__returnFromRead.writeAction(f"addi X16 X27 16") 
  tranPrefixSumDownWorker__returnFromRead.writeAction(f"send_dmlm X27 X25 X24 6") 
  tranPrefixSumDownWorker__returnFromRead.writeAction(f"addi X16 X16 64") 
  tranPrefixSumDownWorker__returnFromRead.writeAction(f"addi X26 X26 1") 
  tranPrefixSumDownWorker__returnFromRead.writeAction(f"jmp __for_returnFromRead_6_condition") 
  tranPrefixSumDownWorker__returnFromRead.writeAction(f"__for_returnFromRead_8_post: addi X20 X19 0") 
  tranPrefixSumDownWorker__returnFromRead.writeAction(f"movwlr X23(X20,0,0) X24") 
  tranPrefixSumDownWorker__returnFromRead.writeAction(f"add X21 X24 X21") 
  ## move up the block

  tranPrefixSumDownWorker__returnFromRead.writeAction(f"add X17 X20 X17") 
  tranPrefixSumDownWorker__returnFromRead.writeAction(f"__if_returnFromRead_5_post: yield") 
  
  # Writing code for event PrefixSumDownWorker::returnFromWrite
  tranPrefixSumDownWorker__returnFromWrite = efa.writeEvent('PrefixSumDownWorker::returnFromWrite')
  tranPrefixSumDownWorker__returnFromWrite.writeAction(f"__entry: subi X19 X19 1") 
  tranPrefixSumDownWorker__returnFromWrite.writeAction(f"bneiu X19 0 __if_returnFromWrite_2_post") 
  ## send the next batch

  tranPrefixSumDownWorker__returnFromWrite.writeAction(f"__if_returnFromWrite_0_true: bleiu X18 0 __if_returnFromWrite_5_post") 
  tranPrefixSumDownWorker__returnFromWrite.writeAction(f"__if_returnFromWrite_3_true: addi X16 X23 8") 
  ## point to where the degree is

  tranPrefixSumDownWorker__returnFromWrite.writeAction(f"evi X2 X24 PrefixSumDownWorker::returnFromRead 1") 
  tranPrefixSumDownWorker__returnFromWrite.writeAction(f"movir X26 0") 
  tranPrefixSumDownWorker__returnFromWrite.writeAction(f"__for_returnFromWrite_6_condition: clti X26 X25 32") 
  tranPrefixSumDownWorker__returnFromWrite.writeAction(f"cgti X18 X27 0") 
  tranPrefixSumDownWorker__returnFromWrite.writeAction(f"and X25 X27 X25") 
  tranPrefixSumDownWorker__returnFromWrite.writeAction(f"beqiu X25 0 __for_returnFromWrite_8_post") 
  tranPrefixSumDownWorker__returnFromWrite.writeAction(f"__for_returnFromWrite_7_body: send_dmlm_ld X23 X24 1") 
  tranPrefixSumDownWorker__returnFromWrite.writeAction(f"addi X23 X23 64") 
  tranPrefixSumDownWorker__returnFromWrite.writeAction(f"subi X18 X18 1") 
  tranPrefixSumDownWorker__returnFromWrite.writeAction(f"addi X19 X19 1") 
  tranPrefixSumDownWorker__returnFromWrite.writeAction(f"addi X26 X26 1") 
  tranPrefixSumDownWorker__returnFromWrite.writeAction(f"jmp __for_returnFromWrite_6_condition") 
  tranPrefixSumDownWorker__returnFromWrite.writeAction(f"__for_returnFromWrite_8_post: addi X19 X20 0") 
  tranPrefixSumDownWorker__returnFromWrite.writeAction(f"yield") 
  ## we are done

  tranPrefixSumDownWorker__returnFromWrite.writeAction(f"__if_returnFromWrite_5_post: movir X26 -1") 
  tranPrefixSumDownWorker__returnFromWrite.writeAction(f"sri X26 X26 1") 
  tranPrefixSumDownWorker__returnFromWrite.writeAction(f"sendr_wcont X1 X26 X22 X22") 
  tranPrefixSumDownWorker__returnFromWrite.writeAction(f"yield_terminate") 
  tranPrefixSumDownWorker__returnFromWrite.writeAction(f"__if_returnFromWrite_2_post: yield") 
  