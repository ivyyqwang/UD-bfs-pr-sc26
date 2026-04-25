from linker.EFAProgram import efaProgram

## UDWeave version: 7808cc0 (2026-04-24)

## Global constants

@efaProgram
def EFA_delete_vertices(efa):
  efa.code_level = 'machine'
  state0 = efa.State("udweave_init") #Only one state code 
  efa.add_initId(state0.state_id)
  ## Static declarations
  ## Scoped Variable "counter" uses Register X16, scope (0)
  ## Scoped Variable "verticesValid" uses Register X17, scope (0)
  ## Scoped Variable "verticesDeleted" uses Register X18, scope (0)
  ## Scoped Variable "verticesIgnored" uses Register X19, scope (0)
  ## Scoped Variable "srcBase" uses Register X16, scope (0)
  ## Scoped Variable "srcCurrentPointer" uses Register X17, scope (0)
  ## Scoped Variable "dstBase" uses Register X18, scope (0)
  ## Scoped Variable "numVertices" uses Register X19, scope (0)
  ## Scoped Variable "counter" uses Register X20, scope (0)
  ## Scoped Variable "sumLeft" uses Register X21, scope (0)
  ## Scoped Variable "sumDeleted" uses Register X22, scope (0)
  ## Scoped Variable "sumIgnored" uses Register X23, scope (0)
  
  from LinkableGlobalSync import Broadcast
  Broadcast(state=state0, identifier='BROADCAST', debug_flag=False)
  
  ## Here, the number of updates performed by the BFS is stored
  ## 8 children each with three words of data each taking 8 bytes
  ## can also be 6 children each with 4 words of data each taking 8 bytes
  ## can also be 6 childen with 5 words each
  ## A macro which declares a local pointer and writes a 1 to the address
  ## LMBASE + TOP_FLAG_OFFSET indicating to the TOP core, that we completed
  ## UpDown program execution.
  ## #define DEBUG_DELETE_VERTICES
  
  ####################################################
  ###### Writing code for thread DeleteVertices ######
  ####################################################
  # Writing code for event DeleteVertices::start
  tranDeleteVertices__start = efa.writeEvent('DeleteVertices::start')
  ## distribute the work among all lanes available

  tranDeleteVertices__start.writeAction(f"__entry: movir X20 0") 
  tranDeleteVertices__start.writeAction(f"evlb X20 BroadcastReduction::start") 
  tranDeleteVertices__start.writeAction(f"evi X20 X20 255 4") 
  tranDeleteVertices__start.writeAction(f"ev X20 X20 X0 X0 8") 
  tranDeleteVertices__start.writeAction(f"evi X2 X21 DeleteVertices::doneCollectInformation 1") 
  tranDeleteVertices__start.writeAction(f"movir X22 0") 
  tranDeleteVertices__start.writeAction(f"evlb X22 BroadcastDeleteWorker::start") 
  tranDeleteVertices__start.writeAction(f"evi X22 X22 255 4") 
  tranDeleteVertices__start.writeAction(f"ev X22 X22 X0 X0 8") 
  tranDeleteVertices__start.writeAction(f"addi X7 X23 1664") 
  tranDeleteVertices__start.writeAction(f"movrl X12 0(X23) 0 8") 
  tranDeleteVertices__start.writeAction(f"movrl X22 8(X23) 0 8") 
  tranDeleteVertices__start.writeAction(f"movrl X8 16(X23) 0 8") 
  tranDeleteVertices__start.writeAction(f"movrl X11 24(X23) 0 8") 
  tranDeleteVertices__start.writeAction(f"movrl X12 32(X23) 0 8") 
  ## length and destination address in the LM is configured in the Broadcast receiver

  tranDeleteVertices__start.writeAction(f"send_wcont X20 X21 X23 8") 
  tranDeleteVertices__start.writeAction(f"evi X2 X21 DeleteVertices::doneDiscardInformation 1") 
  tranDeleteVertices__start.writeAction(f"movrl X9 16(X23) 0 8") 
  tranDeleteVertices__start.writeAction(f"send_wcont X20 X21 X23 8") 
  tranDeleteVertices__start.writeAction(f"movrl X10 16(X23) 0 8") 
  tranDeleteVertices__start.writeAction(f"send_wcont X20 X21 X23 8") 
  tranDeleteVertices__start.writeAction(f"movir X16 3") 
  tranDeleteVertices__start.writeAction(f"yield") 
  
  # Writing code for event DeleteVertices::doneCollectInformation
  tranDeleteVertices__doneCollectInformation = efa.writeEvent('DeleteVertices::doneCollectInformation')
  tranDeleteVertices__doneCollectInformation.writeAction(f"__entry: subi X16 X16 1") 
  tranDeleteVertices__doneCollectInformation.writeAction(f"bneiu X16 0 __if_doneCollectInformation_1_false") 
  tranDeleteVertices__doneCollectInformation.writeAction(f"__if_doneCollectInformation_0_true: addi X7 X20 0") 
  tranDeleteVertices__doneCollectInformation.writeAction(f"movrl X8 8(X20) 0 8") 
  tranDeleteVertices__doneCollectInformation.writeAction(f"movrl X9 16(X20) 0 8") 
  tranDeleteVertices__doneCollectInformation.writeAction(f"movrl X10 24(X20) 0 8") 
  tranDeleteVertices__doneCollectInformation.writeAction(f"movir X21 1") 
  tranDeleteVertices__doneCollectInformation.writeAction(f"movrl X21 0(X20) 0 8") 
  tranDeleteVertices__doneCollectInformation.writeAction(f"yield_terminate") 
  tranDeleteVertices__doneCollectInformation.writeAction(f"jmp __if_doneCollectInformation_2_post") 
  tranDeleteVertices__doneCollectInformation.writeAction(f"__if_doneCollectInformation_1_false: addi X8 X17 0") 
  tranDeleteVertices__doneCollectInformation.writeAction(f"addi X9 X18 0") 
  tranDeleteVertices__doneCollectInformation.writeAction(f"addi X10 X19 0") 
  tranDeleteVertices__doneCollectInformation.writeAction(f"__if_doneCollectInformation_2_post: yield") 
  
  # Writing code for event DeleteVertices::doneDiscardInformation
  tranDeleteVertices__doneDiscardInformation = efa.writeEvent('DeleteVertices::doneDiscardInformation')
  tranDeleteVertices__doneDiscardInformation.writeAction(f"__entry: subi X16 X16 1") 
  tranDeleteVertices__doneDiscardInformation.writeAction(f"bneiu X16 0 __if_doneDiscardInformation_2_post") 
  tranDeleteVertices__doneDiscardInformation.writeAction(f"__if_doneDiscardInformation_0_true: addi X7 X20 0") 
  tranDeleteVertices__doneDiscardInformation.writeAction(f"movrl X17 8(X20) 0 8") 
  tranDeleteVertices__doneDiscardInformation.writeAction(f"movrl X18 16(X20) 0 8") 
  tranDeleteVertices__doneDiscardInformation.writeAction(f"movrl X19 24(X20) 0 8") 
  tranDeleteVertices__doneDiscardInformation.writeAction(f"movir X21 1") 
  tranDeleteVertices__doneDiscardInformation.writeAction(f"movrl X21 0(X20) 0 8") 
  tranDeleteVertices__doneDiscardInformation.writeAction(f"yield_terminate") 
  tranDeleteVertices__doneDiscardInformation.writeAction(f"__if_doneDiscardInformation_2_post: yield") 
  
  
  ###########################################################
  ###### Writing code for thread BroadcastDeleteWorker ######
  ###########################################################
  ## valid vertices (degree != 0 && color != -1)
  ## deleted vertices
  ## ignored vertices
  # Writing code for event BroadcastDeleteWorker::start
  tranBroadcastDeleteWorker__start = efa.writeEvent('BroadcastDeleteWorker::start')
  ## determine the numVertices

  tranBroadcastDeleteWorker__start.writeAction(f"__entry: div X9 X10 X24") 
  tranBroadcastDeleteWorker__start.writeAction(f"mod X9 X10 X25") 
  tranBroadcastDeleteWorker__start.writeAction(f"bleu X25 X0 __if_start_1_false") 
  tranBroadcastDeleteWorker__start.writeAction(f"__if_start_0_true: addi X24 X19 1") 
  tranBroadcastDeleteWorker__start.writeAction(f"addi X0 X26 0") 
  tranBroadcastDeleteWorker__start.writeAction(f"jmp __if_start_2_post") 
  tranBroadcastDeleteWorker__start.writeAction(f"__if_start_1_false: addi X24 X19 0") 
  tranBroadcastDeleteWorker__start.writeAction(f"addi X25 X26 0") 
  tranBroadcastDeleteWorker__start.writeAction(f"__if_start_2_post: bneiu X19 0 __if_start_5_post") 
  ## #ifdef DEBUG_DELETE_VERTICES

  ## 	print("Returning sum: 0");

  ## #endif

  tranBroadcastDeleteWorker__start.writeAction(f"__if_start_3_true: movir X25 0") 
  tranBroadcastDeleteWorker__start.writeAction(f"movir X27 -1") 
  tranBroadcastDeleteWorker__start.writeAction(f"sri X27 X27 1") 
  tranBroadcastDeleteWorker__start.writeAction(f"sendr3_wcont X1 X27 X25 X25 X25") 
  tranBroadcastDeleteWorker__start.writeAction(f"yield_terminate") 
  ## set the base addresses

  tranBroadcastDeleteWorker__start.writeAction(f"__if_start_5_post: mul X0 X24 X24") 
  tranBroadcastDeleteWorker__start.writeAction(f"add X24 X26 X26") 
  tranBroadcastDeleteWorker__start.writeAction(f"sli X26 X26 3") 
  tranBroadcastDeleteWorker__start.writeAction(f"sli X26 X26 3") 
  ## size of vertex_t

  tranBroadcastDeleteWorker__start.writeAction(f"add X8 X26 X16") 
  tranBroadcastDeleteWorker__start.writeAction(f"addi X16 X17 8") 
  ## point to where the degree is

  tranBroadcastDeleteWorker__start.writeAction(f"movir X20 0") 
  tranBroadcastDeleteWorker__start.writeAction(f"movir X21 0") 
  tranBroadcastDeleteWorker__start.writeAction(f"movir X22 0") 
  tranBroadcastDeleteWorker__start.writeAction(f"movir X23 0") 
  tranBroadcastDeleteWorker__start.writeAction(f"movir X26 0") 
  tranBroadcastDeleteWorker__start.writeAction(f"__for_start_6_condition: clti X26 X24 10") 
  tranBroadcastDeleteWorker__start.writeAction(f"cgti X19 X25 0") 
  tranBroadcastDeleteWorker__start.writeAction(f"and X24 X25 X24") 
  tranBroadcastDeleteWorker__start.writeAction(f"beqiu X24 0 __for_start_8_post") 
  tranBroadcastDeleteWorker__start.writeAction(f"__for_start_7_body: send_dmlm_ld_wret X17 BroadcastDeleteWorker::returnFromRead 4 X24") 
  tranBroadcastDeleteWorker__start.writeAction(f"addi X17 X17 64") 
  tranBroadcastDeleteWorker__start.writeAction(f"subi X19 X19 1") 
  tranBroadcastDeleteWorker__start.writeAction(f"addi X20 X20 1") 
  tranBroadcastDeleteWorker__start.writeAction(f"addi X26 X26 1") 
  tranBroadcastDeleteWorker__start.writeAction(f"jmp __for_start_6_condition") 
  tranBroadcastDeleteWorker__start.writeAction(f"__for_start_8_post: yield") 
  
  # Writing code for event BroadcastDeleteWorker::returnFromRead
  tranBroadcastDeleteWorker__returnFromRead = efa.writeEvent('BroadcastDeleteWorker::returnFromRead')
  tranBroadcastDeleteWorker__returnFromRead.writeAction(f"__entry: ceqi X11 X26 -1") 
  tranBroadcastDeleteWorker__returnFromRead.writeAction(f"ceqi X8 X24 0") 
  tranBroadcastDeleteWorker__returnFromRead.writeAction(f"xori X24 X24 1") 
  tranBroadcastDeleteWorker__returnFromRead.writeAction(f"and X26 X24 X26") 
  tranBroadcastDeleteWorker__returnFromRead.writeAction(f"beqi X26 0 __if_returnFromRead_1_false") 
  tranBroadcastDeleteWorker__returnFromRead.writeAction(f"__if_returnFromRead_0_true: movir X26 0") 
  tranBroadcastDeleteWorker__returnFromRead.writeAction(f"sendr_dmlm_wret X12 BroadcastDeleteWorker::returnFromWrite X26 X24") 
  tranBroadcastDeleteWorker__returnFromRead.writeAction(f"addi X20 X20 1") 
  tranBroadcastDeleteWorker__returnFromRead.writeAction(f"addi X22 X22 1") 
  tranBroadcastDeleteWorker__returnFromRead.writeAction(f"jmp __if_returnFromRead_2_post") 
  tranBroadcastDeleteWorker__returnFromRead.writeAction(f"__if_returnFromRead_1_false: beqiu X8 0 __if_returnFromRead_4_false") 
  tranBroadcastDeleteWorker__returnFromRead.writeAction(f"__if_returnFromRead_3_true: addi X12 X26 24") 
  tranBroadcastDeleteWorker__returnFromRead.writeAction(f"sendr_dmlm_wret X26 BroadcastDeleteWorker::returnFromWrite X10 X24") 
  tranBroadcastDeleteWorker__returnFromRead.writeAction(f"addi X20 X20 1") 
  tranBroadcastDeleteWorker__returnFromRead.writeAction(f"addi X21 X21 1") 
  tranBroadcastDeleteWorker__returnFromRead.writeAction(f"jmp __if_returnFromRead_2_post") 
  ## degree == 0

  tranBroadcastDeleteWorker__returnFromRead.writeAction(f"__if_returnFromRead_4_false: addi X23 X23 1") 
  tranBroadcastDeleteWorker__returnFromRead.writeAction(f"__if_returnFromRead_2_post: beqiu X19 0 __if_returnFromRead_7_false") 
  tranBroadcastDeleteWorker__returnFromRead.writeAction(f"__if_returnFromRead_6_true: send_dmlm_ld X17 X2 4") 
  tranBroadcastDeleteWorker__returnFromRead.writeAction(f"addi X17 X17 64") 
  tranBroadcastDeleteWorker__returnFromRead.writeAction(f"subi X19 X19 1") 
  tranBroadcastDeleteWorker__returnFromRead.writeAction(f"jmp __if_returnFromRead_8_post") 
  tranBroadcastDeleteWorker__returnFromRead.writeAction(f"__if_returnFromRead_7_false: subi X20 X20 1") 
  tranBroadcastDeleteWorker__returnFromRead.writeAction(f"bneiu X20 0 __if_returnFromRead_8_post") 
  ## inform the broadcast library that we are done

  tranBroadcastDeleteWorker__returnFromRead.writeAction(f"__if_returnFromRead_9_true: movir X26 -1") 
  tranBroadcastDeleteWorker__returnFromRead.writeAction(f"sri X26 X26 1") 
  tranBroadcastDeleteWorker__returnFromRead.writeAction(f"sendr3_wcont X1 X26 X21 X22 X23") 
  tranBroadcastDeleteWorker__returnFromRead.writeAction(f"yield_terminate") 
  tranBroadcastDeleteWorker__returnFromRead.writeAction(f"__if_returnFromRead_8_post: yield") 
  
  # Writing code for event BroadcastDeleteWorker::returnFromWrite
  tranBroadcastDeleteWorker__returnFromWrite = efa.writeEvent('BroadcastDeleteWorker::returnFromWrite')
  tranBroadcastDeleteWorker__returnFromWrite.writeAction(f"__entry: subi X20 X20 1") 
  tranBroadcastDeleteWorker__returnFromWrite.writeAction(f"bneiu X20 0 __if_returnFromWrite_2_post") 
  ## inform the broadcast library that we are done

  tranBroadcastDeleteWorker__returnFromWrite.writeAction(f"__if_returnFromWrite_0_true: movir X26 -1") 
  tranBroadcastDeleteWorker__returnFromWrite.writeAction(f"sri X26 X26 1") 
  tranBroadcastDeleteWorker__returnFromWrite.writeAction(f"sendr3_wcont X1 X26 X21 X22 X23") 
  tranBroadcastDeleteWorker__returnFromWrite.writeAction(f"yield_terminate") 
  tranBroadcastDeleteWorker__returnFromWrite.writeAction(f"__if_returnFromWrite_2_post: yield") 
  