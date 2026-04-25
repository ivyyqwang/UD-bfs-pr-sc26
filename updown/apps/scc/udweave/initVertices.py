from linker.EFAProgram import efaProgram

## UDWeave version: 7808cc0 (2026-04-24)

## Global constants

@efaProgram
def EFA_initVertices(efa):
  efa.code_level = 'machine'
  state0 = efa.State("udweave_init") #Only one state code 
  efa.add_initId(state0.state_id)
  ## Static declarations
  ## Scoped Variable "srcBase" uses Register X16, scope (0)
  ## Scoped Variable "srcCurrentPointer" uses Register X17, scope (0)
  ## Scoped Variable "dstBase" uses Register X18, scope (0)
  ## Scoped Variable "numVertices" uses Register X19, scope (0)
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
  ## #define DEBUG_INITVERTICES
  
  ##################################################
  ###### Writing code for thread InitVertices ######
  ##################################################
  # Writing code for event InitVertices::start
  tranInitVertices__start = efa.writeEvent('InitVertices::start')
  ## distribute the work among all lanes available

  tranInitVertices__start.writeAction(f"__entry: movir X16 0") 
  tranInitVertices__start.writeAction(f"evlb X16 BROADCAST__broadcast_global") 
  tranInitVertices__start.writeAction(f"evi X16 X16 255 4") 
  tranInitVertices__start.writeAction(f"ev X16 X16 X0 X0 8") 
  tranInitVertices__start.writeAction(f"evi X2 X17 InitVertices::done 1") 
  tranInitVertices__start.writeAction(f"movir X18 0") 
  tranInitVertices__start.writeAction(f"evlb X18 BroadcastInitVertexWorker::start") 
  tranInitVertices__start.writeAction(f"evi X18 X18 255 4") 
  tranInitVertices__start.writeAction(f"ev X18 X18 X0 X0 8") 
  tranInitVertices__start.writeAction(f"addi X7 X19 1664") 
  tranInitVertices__start.writeAction(f"movrl X11 0(X19) 0 8") 
  tranInitVertices__start.writeAction(f"movrl X18 8(X19) 0 8") 
  tranInitVertices__start.writeAction(f"addi X19 X18 16") 
  tranInitVertices__start.writeAction(f"bcpyoli X8 X18 4") 
  ## length and destination address in the LM is configured in the Broadcast receiver

  tranInitVertices__start.writeAction(f"send_wcont X16 X17 X19 8") 
  tranInitVertices__start.writeAction(f"yield") 
  
  # Writing code for event InitVertices::done
  tranInitVertices__done = efa.writeEvent('InitVertices::done')
  tranInitVertices__done.writeAction(f"__entry: addi X7 X16 0") 
  tranInitVertices__done.writeAction(f"movir X17 1") 
  tranInitVertices__done.writeAction(f"movrl X17 0(X16) 0 8") 
  tranInitVertices__done.writeAction(f"yield_terminate") 
  
  
  ###############################################################
  ###### Writing code for thread BroadcastInitVertexWorker ######
  ###############################################################
  # Writing code for event BroadcastInitVertexWorker::start
  tranBroadcastInitVertexWorker__start = efa.writeEvent('BroadcastInitVertexWorker::start')
  ## determine the numVertices

  tranBroadcastInitVertexWorker__start.writeAction(f"__entry: div X10 X11 X21") 
  tranBroadcastInitVertexWorker__start.writeAction(f"mod X10 X11 X22") 
  tranBroadcastInitVertexWorker__start.writeAction(f"bleu X22 X0 __if_start_1_false") 
  tranBroadcastInitVertexWorker__start.writeAction(f"__if_start_0_true: addi X21 X19 1") 
  tranBroadcastInitVertexWorker__start.writeAction(f"addi X0 X23 0") 
  tranBroadcastInitVertexWorker__start.writeAction(f"jmp __if_start_2_post") 
  tranBroadcastInitVertexWorker__start.writeAction(f"__if_start_1_false: addi X21 X19 0") 
  tranBroadcastInitVertexWorker__start.writeAction(f"addi X22 X23 0") 
  tranBroadcastInitVertexWorker__start.writeAction(f"__if_start_2_post: bneiu X19 0 __if_start_5_post") 
  tranBroadcastInitVertexWorker__start.writeAction(f"__if_start_3_true: movir X22 -1") 
  tranBroadcastInitVertexWorker__start.writeAction(f"sri X22 X22 1") 
  tranBroadcastInitVertexWorker__start.writeAction(f"sendr_wcont X1 X22 X1 X1") 
  tranBroadcastInitVertexWorker__start.writeAction(f"yield") 
  ## set the base addresses

  tranBroadcastInitVertexWorker__start.writeAction(f"__if_start_5_post: mul X0 X21 X21") 
  tranBroadcastInitVertexWorker__start.writeAction(f"add X21 X23 X23") 
  tranBroadcastInitVertexWorker__start.writeAction(f"sli X23 X23 3") 
  tranBroadcastInitVertexWorker__start.writeAction(f"sli X23 X23 3") 
  ## size of vertex_t

  tranBroadcastInitVertexWorker__start.writeAction(f"add X8 X23 X16") 
  tranBroadcastInitVertexWorker__start.writeAction(f"add X9 X23 X18") 
  tranBroadcastInitVertexWorker__start.writeAction(f"addi X16 X17 0") 
  tranBroadcastInitVertexWorker__start.writeAction(f"movir X20 0") 
  tranBroadcastInitVertexWorker__start.writeAction(f"movir X23 0") 
  tranBroadcastInitVertexWorker__start.writeAction(f"__for_start_6_condition: clti X23 X21 10") 
  tranBroadcastInitVertexWorker__start.writeAction(f"cgti X19 X22 0") 
  tranBroadcastInitVertexWorker__start.writeAction(f"and X21 X22 X21") 
  tranBroadcastInitVertexWorker__start.writeAction(f"beqiu X21 0 __for_start_8_post") 
  tranBroadcastInitVertexWorker__start.writeAction(f"__for_start_7_body: send_dmlm_ld_wret X17 BroadcastInitVertexWorker::returnFromRead 6 X21") 
  tranBroadcastInitVertexWorker__start.writeAction(f"addi X17 X17 64") 
  tranBroadcastInitVertexWorker__start.writeAction(f"subi X19 X19 1") 
  tranBroadcastInitVertexWorker__start.writeAction(f"addi X20 X20 1") 
  tranBroadcastInitVertexWorker__start.writeAction(f"addi X23 X23 1") 
  tranBroadcastInitVertexWorker__start.writeAction(f"jmp __for_start_6_condition") 
  tranBroadcastInitVertexWorker__start.writeAction(f"__for_start_8_post: yield") 
  
  # Writing code for event BroadcastInitVertexWorker::returnFromRead
  tranBroadcastInitVertexWorker__returnFromRead = efa.writeEvent('BroadcastInitVertexWorker::returnFromRead')
  tranBroadcastInitVertexWorker__returnFromRead.writeAction(f"__entry: sub X14 X16 X23") 
  tranBroadcastInitVertexWorker__returnFromRead.writeAction(f"add X18 X23 X23") 
  tranBroadcastInitVertexWorker__returnFromRead.writeAction(f"sendops_dmlm_wret X23 BroadcastInitVertexWorker::returnFromWrite X8 6 X21") 
  tranBroadcastInitVertexWorker__returnFromRead.writeAction(f"yield") 
  
  # Writing code for event BroadcastInitVertexWorker::returnFromWrite
  tranBroadcastInitVertexWorker__returnFromWrite = efa.writeEvent('BroadcastInitVertexWorker::returnFromWrite')
  tranBroadcastInitVertexWorker__returnFromWrite.writeAction(f"__entry: beqiu X19 0 __if_returnFromWrite_1_false") 
  tranBroadcastInitVertexWorker__returnFromWrite.writeAction(f"__if_returnFromWrite_0_true: send_dmlm_ld_wret X17 BroadcastInitVertexWorker::returnFromRead 6 X23") 
  tranBroadcastInitVertexWorker__returnFromWrite.writeAction(f"addi X17 X17 64") 
  tranBroadcastInitVertexWorker__returnFromWrite.writeAction(f"subi X19 X19 1") 
  tranBroadcastInitVertexWorker__returnFromWrite.writeAction(f"jmp __if_returnFromWrite_2_post") 
  tranBroadcastInitVertexWorker__returnFromWrite.writeAction(f"__if_returnFromWrite_1_false: subi X20 X20 1") 
  tranBroadcastInitVertexWorker__returnFromWrite.writeAction(f"bneiu X20 0 __if_returnFromWrite_2_post") 
  ## inform the broadcast library that we are done

  tranBroadcastInitVertexWorker__returnFromWrite.writeAction(f"__if_returnFromWrite_3_true: movir X23 -1") 
  tranBroadcastInitVertexWorker__returnFromWrite.writeAction(f"sri X23 X23 1") 
  tranBroadcastInitVertexWorker__returnFromWrite.writeAction(f"sendr_wcont X1 X23 X1 X1") 
  tranBroadcastInitVertexWorker__returnFromWrite.writeAction(f"__if_returnFromWrite_2_post: yield") 
  