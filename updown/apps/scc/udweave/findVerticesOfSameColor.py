from linker.EFAProgram import efaProgram

## UDWeave version: 7808cc0 (2026-04-24)

## Global constants

@efaProgram
def EFA_findVerticesOfSameColor(efa):
  efa.code_level = 'machine'
  state0 = efa.State("udweave_init") #Only one state code 
  efa.add_initId(state0.state_id)
  ## Static declarations
  ## Scoped Variable "verticesBase" uses Register X16, scope (0)
  ## Scoped Variable "verticesCurrentPointer" uses Register X17, scope (0)
  ## Scoped Variable "edges" uses Register X18, scope (0)
  ## Scoped Variable "numVerticesPerLane" uses Register X19, scope (0)
  ## Scoped Variable "counter" uses Register X20, scope (0)
  
  from LinkableGlobalSync import Broadcast
  Broadcast(state=state0, identifier='BROADCAST', debug_flag=False)
  
  ## Here, the number of updates performed by the BFS is stored
  ## 8 children each with three words of data each taking 8 bytes
  ## can also be 6 children each with 4 words of data each taking 8 bytes
  ## can also be 6 childen with 5 words each
  ## A macro which declares a local pointer and writes a 1 to the address
  ## LMBASE + TOP_FLAG_OFFSET indicating to the TOP core, that we completed
  ## UpDown program execution.
  ## #define DEBUG_FINDVERTICES
  
  #############################################################
  ###### Writing code for thread FindVerticesOfSameColor ######
  #############################################################
  # Writing code for event FindVerticesOfSameColor::start
  tranFindVerticesOfSameColor__start = efa.writeEvent('FindVerticesOfSameColor::start')
  ## distribute the work among all lanes available

  tranFindVerticesOfSameColor__start.writeAction(f"__entry: movir X16 0") 
  tranFindVerticesOfSameColor__start.writeAction(f"evlb X16 BROADCAST__broadcast_global") 
  tranFindVerticesOfSameColor__start.writeAction(f"evi X16 X16 255 4") 
  tranFindVerticesOfSameColor__start.writeAction(f"ev X16 X16 X0 X0 8") 
  tranFindVerticesOfSameColor__start.writeAction(f"evi X2 X17 FindVerticesOfSameColor::done 1") 
  tranFindVerticesOfSameColor__start.writeAction(f"movir X18 0") 
  tranFindVerticesOfSameColor__start.writeAction(f"evlb X18 BroadcastFindVertexWorker::start") 
  tranFindVerticesOfSameColor__start.writeAction(f"evi X18 X18 255 4") 
  tranFindVerticesOfSameColor__start.writeAction(f"ev X18 X18 X0 X0 8") 
  tranFindVerticesOfSameColor__start.writeAction(f"addi X7 X19 8") 
  tranFindVerticesOfSameColor__start.writeAction(f"movrl X10 0(X19) 0 8") 
  tranFindVerticesOfSameColor__start.writeAction(f"movrl X18 8(X19) 0 8") 
  tranFindVerticesOfSameColor__start.writeAction(f"addi X19 X18 16") 
  tranFindVerticesOfSameColor__start.writeAction(f"bcpyoli X8 X18 3") 
  ## length and destination address in the LM is configured in the Broadcast receiver

  tranFindVerticesOfSameColor__start.writeAction(f"send_wcont X16 X17 X19 8") 
  tranFindVerticesOfSameColor__start.writeAction(f"yield") 
  
  # Writing code for event FindVerticesOfSameColor::done
  tranFindVerticesOfSameColor__done = efa.writeEvent('FindVerticesOfSameColor::done')
  tranFindVerticesOfSameColor__done.writeAction(f"__entry: addi X7 X16 0") 
  tranFindVerticesOfSameColor__done.writeAction(f"movir X17 1") 
  tranFindVerticesOfSameColor__done.writeAction(f"movrl X17 0(X16) 0 8") 
  tranFindVerticesOfSameColor__done.writeAction(f"yield_terminate") 
  
  
  ###############################################################
  ###### Writing code for thread BroadcastFindVertexWorker ######
  ###############################################################
  # Writing code for event BroadcastFindVertexWorker::start
  tranBroadcastFindVertexWorker__start = efa.writeEvent('BroadcastFindVertexWorker::start')
  ## determine the numVertices that the lane should handle

  tranBroadcastFindVertexWorker__start.writeAction(f"__entry: div X9 X10 X21") 
  tranBroadcastFindVertexWorker__start.writeAction(f"mod X9 X10 X22") 
  tranBroadcastFindVertexWorker__start.writeAction(f"bleu X22 X0 __if_start_1_false") 
  tranBroadcastFindVertexWorker__start.writeAction(f"__if_start_0_true: addi X21 X19 1") 
  tranBroadcastFindVertexWorker__start.writeAction(f"addi X0 X23 0") 
  tranBroadcastFindVertexWorker__start.writeAction(f"jmp __if_start_2_post") 
  tranBroadcastFindVertexWorker__start.writeAction(f"__if_start_1_false: addi X21 X19 0") 
  tranBroadcastFindVertexWorker__start.writeAction(f"addi X22 X23 0") 
  tranBroadcastFindVertexWorker__start.writeAction(f"__if_start_2_post: bneiu X19 0 __if_start_5_post") 
  tranBroadcastFindVertexWorker__start.writeAction(f"__if_start_3_true: movir X22 -1") 
  tranBroadcastFindVertexWorker__start.writeAction(f"sri X22 X22 1") 
  tranBroadcastFindVertexWorker__start.writeAction(f"sendr_wcont X1 X22 X1 X1") 
  tranBroadcastFindVertexWorker__start.writeAction(f"yield") 
  ## set the base addresses

  tranBroadcastFindVertexWorker__start.writeAction(f"__if_start_5_post: mul X0 X21 X21") 
  tranBroadcastFindVertexWorker__start.writeAction(f"add X21 X23 X23") 
  tranBroadcastFindVertexWorker__start.writeAction(f"sli X23 X23 6") 
  tranBroadcastFindVertexWorker__start.writeAction(f"add X8 X23 X16") 
  tranBroadcastFindVertexWorker__start.writeAction(f"addi X16 X17 8") 
  ## point to where the degree is (loading the ID and the color)

  tranBroadcastFindVertexWorker__start.writeAction(f"movir X20 0") 
  tranBroadcastFindVertexWorker__start.writeAction(f"movir X23 0") 
  tranBroadcastFindVertexWorker__start.writeAction(f"__for_start_6_condition: clti X23 X21 10") 
  tranBroadcastFindVertexWorker__start.writeAction(f"cgti X19 X22 0") 
  tranBroadcastFindVertexWorker__start.writeAction(f"and X21 X22 X21") 
  tranBroadcastFindVertexWorker__start.writeAction(f"beqiu X21 0 __for_start_8_post") 
  tranBroadcastFindVertexWorker__start.writeAction(f"__for_start_7_body: send_dmlm_ld_wret X17 BroadcastFindVertexWorker::returnFromRead 4 X21") 
  tranBroadcastFindVertexWorker__start.writeAction(f"addi X17 X17 64") 
  tranBroadcastFindVertexWorker__start.writeAction(f"subi X19 X19 1") 
  tranBroadcastFindVertexWorker__start.writeAction(f"addi X20 X20 1") 
  tranBroadcastFindVertexWorker__start.writeAction(f"addi X23 X23 1") 
  tranBroadcastFindVertexWorker__start.writeAction(f"jmp __for_start_6_condition") 
  tranBroadcastFindVertexWorker__start.writeAction(f"__for_start_8_post: yield") 
  
  # Writing code for event BroadcastFindVertexWorker::returnFromRead
  tranBroadcastFindVertexWorker__returnFromRead = efa.writeEvent('BroadcastFindVertexWorker::returnFromRead')
  tranBroadcastFindVertexWorker__returnFromRead.writeAction(f"__entry: ceqi X11 X23 -1") 
  tranBroadcastFindVertexWorker__returnFromRead.writeAction(f"xori X23 X23 1") 
  tranBroadcastFindVertexWorker__returnFromRead.writeAction(f"ceq X10 X11 X21") 
  tranBroadcastFindVertexWorker__returnFromRead.writeAction(f"and X23 X21 X23") 
  tranBroadcastFindVertexWorker__returnFromRead.writeAction(f"beqi X23 0 __if_returnFromRead_2_post") 
  ## mark this vertex as visited by setting the color to -1

  ## and the SCC ID to the color;

  tranBroadcastFindVertexWorker__returnFromRead.writeAction(f"__if_returnFromRead_0_true: addi X12 X23 24") 
  ## skip over degree, edges_before and vertex_id

  tranBroadcastFindVertexWorker__returnFromRead.writeAction(f"movir X21 -1") 
  tranBroadcastFindVertexWorker__returnFromRead.writeAction(f"sendr2_dmlm_wret X23 BroadcastFindVertexWorker::returnFromWrite X21 X11 X22") 
  tranBroadcastFindVertexWorker__returnFromRead.writeAction(f"addi X20 X20 1") 
  ## check for more data to be loaded

  tranBroadcastFindVertexWorker__returnFromRead.writeAction(f"__if_returnFromRead_2_post: beqiu X19 0 __if_returnFromRead_4_false") 
  tranBroadcastFindVertexWorker__returnFromRead.writeAction(f"__if_returnFromRead_3_true: send_dmlm_ld X17 X2 4") 
  tranBroadcastFindVertexWorker__returnFromRead.writeAction(f"addi X17 X17 64") 
  tranBroadcastFindVertexWorker__returnFromRead.writeAction(f"subi X19 X19 1") 
  tranBroadcastFindVertexWorker__returnFromRead.writeAction(f"jmp __if_returnFromRead_5_post") 
  tranBroadcastFindVertexWorker__returnFromRead.writeAction(f"__if_returnFromRead_4_false: subi X20 X20 1") 
  tranBroadcastFindVertexWorker__returnFromRead.writeAction(f"bneiu X20 0 __if_returnFromRead_5_post") 
  ## inform the broadcast library that we are done

  tranBroadcastFindVertexWorker__returnFromRead.writeAction(f"__if_returnFromRead_6_true: movir X23 -1") 
  tranBroadcastFindVertexWorker__returnFromRead.writeAction(f"sri X23 X23 1") 
  tranBroadcastFindVertexWorker__returnFromRead.writeAction(f"sendr_wcont X1 X23 X1 X1") 
  tranBroadcastFindVertexWorker__returnFromRead.writeAction(f"__if_returnFromRead_5_post: yield") 
  
  # Writing code for event BroadcastFindVertexWorker::returnFromWrite
  tranBroadcastFindVertexWorker__returnFromWrite = efa.writeEvent('BroadcastFindVertexWorker::returnFromWrite')
  tranBroadcastFindVertexWorker__returnFromWrite.writeAction(f"__entry: subi X20 X20 1") 
  tranBroadcastFindVertexWorker__returnFromWrite.writeAction(f"bneiu X20 0 __if_returnFromWrite_2_post") 
  ## inform the broadcast library that we are done

  tranBroadcastFindVertexWorker__returnFromWrite.writeAction(f"__if_returnFromWrite_0_true: movir X23 -1") 
  tranBroadcastFindVertexWorker__returnFromWrite.writeAction(f"sri X23 X23 1") 
  tranBroadcastFindVertexWorker__returnFromWrite.writeAction(f"sendr_wcont X1 X23 X1 X1") 
  tranBroadcastFindVertexWorker__returnFromWrite.writeAction(f"__if_returnFromWrite_2_post: yield") 
  