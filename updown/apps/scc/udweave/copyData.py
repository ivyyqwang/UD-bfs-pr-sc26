from linker.EFAProgram import efaProgram

## UDWeave version: 7808cc0 (2026-04-24)

## Global constants

@efaProgram
def EFA_copyData(efa):
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
  ## #define DEBUG_COPYDATA
  
  ##############################################
  ###### Writing code for thread CopyData ######
  ##############################################
  # Writing code for event CopyData::start
  tranCopyData__start = efa.writeEvent('CopyData::start')
  ## distribute the work among all lanes available

  tranCopyData__start.writeAction(f"__entry: movir X16 0") 
  tranCopyData__start.writeAction(f"evlb X16 BROADCAST__broadcast_global") 
  tranCopyData__start.writeAction(f"evi X16 X16 255 4") 
  tranCopyData__start.writeAction(f"ev X16 X16 X0 X0 8") 
  tranCopyData__start.writeAction(f"evi X2 X17 CopyData::done 1") 
  tranCopyData__start.writeAction(f"movir X18 0") 
  tranCopyData__start.writeAction(f"evlb X18 BroadcastDataWorker::start") 
  tranCopyData__start.writeAction(f"evi X18 X18 255 4") 
  tranCopyData__start.writeAction(f"ev X18 X18 X0 X0 8") 
  tranCopyData__start.writeAction(f"addi X7 X19 1664") 
  tranCopyData__start.writeAction(f"movrl X11 0(X19) 0 8") 
  tranCopyData__start.writeAction(f"movrl X18 8(X19) 0 8") 
  tranCopyData__start.writeAction(f"addi X19 X18 16") 
  tranCopyData__start.writeAction(f"bcpyoli X8 X18 4") 
  ## length and destination address in the LM is configured in the Broadcast receiver

  tranCopyData__start.writeAction(f"send_wcont X16 X17 X19 8") 
  tranCopyData__start.writeAction(f"yield") 
  
  # Writing code for event CopyData::done
  tranCopyData__done = efa.writeEvent('CopyData::done')
  tranCopyData__done.writeAction(f"__entry: addi X7 X16 0") 
  tranCopyData__done.writeAction(f"movir X17 1") 
  tranCopyData__done.writeAction(f"movrl X17 0(X16) 0 8") 
  tranCopyData__done.writeAction(f"yield_terminate") 
  
  
  #########################################################
  ###### Writing code for thread BroadcastDataWorker ######
  #########################################################
  # Writing code for event BroadcastDataWorker::start
  tranBroadcastDataWorker__start = efa.writeEvent('BroadcastDataWorker::start')
  ## determine the numVertices

  tranBroadcastDataWorker__start.writeAction(f"__entry: div X10 X11 X21") 
  tranBroadcastDataWorker__start.writeAction(f"mod X10 X11 X22") 
  tranBroadcastDataWorker__start.writeAction(f"bleu X22 X0 __if_start_1_false") 
  tranBroadcastDataWorker__start.writeAction(f"__if_start_0_true: addi X21 X19 1") 
  tranBroadcastDataWorker__start.writeAction(f"addi X0 X23 0") 
  tranBroadcastDataWorker__start.writeAction(f"jmp __if_start_2_post") 
  tranBroadcastDataWorker__start.writeAction(f"__if_start_1_false: addi X21 X19 0") 
  tranBroadcastDataWorker__start.writeAction(f"addi X22 X23 0") 
  tranBroadcastDataWorker__start.writeAction(f"__if_start_2_post: bneiu X19 0 __if_start_5_post") 
  tranBroadcastDataWorker__start.writeAction(f"__if_start_3_true: movir X22 -1") 
  tranBroadcastDataWorker__start.writeAction(f"sri X22 X22 1") 
  tranBroadcastDataWorker__start.writeAction(f"sendr_wcont X1 X22 X1 X1") 
  tranBroadcastDataWorker__start.writeAction(f"yield_terminate") 
  ## set the base addresses

  tranBroadcastDataWorker__start.writeAction(f"__if_start_5_post: mul X0 X21 X21") 
  tranBroadcastDataWorker__start.writeAction(f"add X21 X23 X23") 
  tranBroadcastDataWorker__start.writeAction(f"sli X23 X23 3") 
  tranBroadcastDataWorker__start.writeAction(f"sli X23 X23 3") 
  ## size of vertex_t

  tranBroadcastDataWorker__start.writeAction(f"add X8 X23 X16") 
  tranBroadcastDataWorker__start.writeAction(f"add X9 X23 X18") 
  tranBroadcastDataWorker__start.writeAction(f"addi X16 X17 32") 
  ## point to where the color is

  tranBroadcastDataWorker__start.writeAction(f"movir X20 0") 
  tranBroadcastDataWorker__start.writeAction(f"movir X23 0") 
  tranBroadcastDataWorker__start.writeAction(f"__for_start_6_condition: clti X23 X21 10") 
  tranBroadcastDataWorker__start.writeAction(f"cgti X19 X22 0") 
  tranBroadcastDataWorker__start.writeAction(f"and X21 X22 X21") 
  tranBroadcastDataWorker__start.writeAction(f"beqiu X21 0 __for_start_8_post") 
  tranBroadcastDataWorker__start.writeAction(f"__for_start_7_body: send_dmlm_ld_wret X17 BroadcastDataWorker::returnFromRead 2 X21") 
  tranBroadcastDataWorker__start.writeAction(f"addi X17 X17 64") 
  tranBroadcastDataWorker__start.writeAction(f"subi X19 X19 1") 
  tranBroadcastDataWorker__start.writeAction(f"addi X20 X20 1") 
  tranBroadcastDataWorker__start.writeAction(f"addi X23 X23 1") 
  tranBroadcastDataWorker__start.writeAction(f"jmp __for_start_6_condition") 
  tranBroadcastDataWorker__start.writeAction(f"__for_start_8_post: yield") 
  
  # Writing code for event BroadcastDataWorker::returnFromRead
  tranBroadcastDataWorker__returnFromRead = efa.writeEvent('BroadcastDataWorker::returnFromRead')
  tranBroadcastDataWorker__returnFromRead.writeAction(f"__entry: sub X10 X16 X23") 
  tranBroadcastDataWorker__returnFromRead.writeAction(f"add X18 X23 X23") 
  tranBroadcastDataWorker__returnFromRead.writeAction(f"sendops_dmlm_wret X23 BroadcastDataWorker::returnFromWrite X8 2 X21") 
  tranBroadcastDataWorker__returnFromRead.writeAction(f"yield") 
  
  # Writing code for event BroadcastDataWorker::returnFromWrite
  tranBroadcastDataWorker__returnFromWrite = efa.writeEvent('BroadcastDataWorker::returnFromWrite')
  tranBroadcastDataWorker__returnFromWrite.writeAction(f"__entry: beqiu X19 0 __if_returnFromWrite_1_false") 
  tranBroadcastDataWorker__returnFromWrite.writeAction(f"__if_returnFromWrite_0_true: send_dmlm_ld_wret X17 BroadcastDataWorker::returnFromRead 2 X23") 
  tranBroadcastDataWorker__returnFromWrite.writeAction(f"addi X17 X17 64") 
  tranBroadcastDataWorker__returnFromWrite.writeAction(f"subi X19 X19 1") 
  tranBroadcastDataWorker__returnFromWrite.writeAction(f"jmp __if_returnFromWrite_2_post") 
  tranBroadcastDataWorker__returnFromWrite.writeAction(f"__if_returnFromWrite_1_false: subi X20 X20 1") 
  tranBroadcastDataWorker__returnFromWrite.writeAction(f"bneiu X20 0 __if_returnFromWrite_2_post") 
  ## inform the broadcast library that we are done

  tranBroadcastDataWorker__returnFromWrite.writeAction(f"__if_returnFromWrite_3_true: movir X23 -1") 
  tranBroadcastDataWorker__returnFromWrite.writeAction(f"sri X23 X23 1") 
  tranBroadcastDataWorker__returnFromWrite.writeAction(f"sendr_wcont X1 X23 X1 X1") 
  tranBroadcastDataWorker__returnFromWrite.writeAction(f"yield_terminate") 
  tranBroadcastDataWorker__returnFromWrite.writeAction(f"__if_returnFromWrite_2_post: yield") 
  