from linker.EFAProgram import efaProgram

## UDWeave version: 7808cc0 (2026-04-24)

## Global constants

@efaProgram
def EFA_broadcastReduction(efa):
  efa.code_level = 'machine'
  state0 = efa.State("udweave_init") #Only one state code 
  efa.add_initId(state0.state_id)
  ## Static declarations
  ## Scoped Variable "counter" uses Register X16, scope (0)
  ## Scoped Variable "sum0" uses Register X17, scope (0)
  ## Scoped Variable "sum1" uses Register X18, scope (0)
  ## Scoped Variable "sum2" uses Register X19, scope (0)
  ## Scoped Variable "counter" uses Register X16, scope (0)
  ## Scoped Variable "sum0" uses Register X17, scope (0)
  ## Scoped Variable "sum1" uses Register X18, scope (0)
  ## Scoped Variable "sum2" uses Register X19, scope (0)
  ## Scoped Variable "counter" uses Register X16, scope (0)
  ## Scoped Variable "sum0" uses Register X17, scope (0)
  ## Scoped Variable "sum1" uses Register X18, scope (0)
  ## Scoped Variable "sum2" uses Register X19, scope (0)
  ## Scoped Variable "counter" uses Register X16, scope (0)
  ## Scoped Variable "sum0" uses Register X17, scope (0)
  ## Scoped Variable "sum1" uses Register X18, scope (0)
  ## Scoped Variable "sum2" uses Register X19, scope (0)
  ## Here, the number of updates performed by the BFS is stored
  ## 8 children each with three words of data each taking 8 bytes
  ## can also be 6 children each with 4 words of data each taking 8 bytes
  ## can also be 6 childen with 5 words each
  ## A macro which declares a local pointer and writes a 1 to the address
  ## LMBASE + TOP_FLAG_OFFSET indicating to the TOP core, that we completed
  ## UpDown program execution.
  ## #define DEBUG_BROADCAST
  
  ########################################################
  ###### Writing code for thread BroadcastReduction ######
  ########################################################
  # Writing code for event BroadcastReduction::start
  tranBroadcastReduction__start = efa.writeEvent('BroadcastReduction::start')
  tranBroadcastReduction__start.writeAction(f"__entry: addi X7 X20 1664") 
  tranBroadcastReduction__start.writeAction(f"addi X20 X21 8") 
  tranBroadcastReduction__start.writeAction(f"bcpyoli X9 X21 7") 
  tranBroadcastReduction__start.writeAction(f"movir X17 0") 
  tranBroadcastReduction__start.writeAction(f"movir X18 0") 
  tranBroadcastReduction__start.writeAction(f"movir X19 0") 
  tranBroadcastReduction__start.writeAction(f"evi X2 X21 BroadcastReduction::returnFromChild 1") 
  tranBroadcastReduction__start.writeAction(f"movir X22 65536") 
  tranBroadcastReduction__start.writeAction(f"bgtu X22 X8 __if_start_2_post") 
  ## determine the number of lanes that the next level of tree nodes have to handle each

  tranBroadcastReduction__start.writeAction(f"__if_start_0_true: sari X8 X22 5") 
  tranBroadcastReduction__start.writeAction(f"movrl X22 0(X20) 0 8") 
  tranBroadcastReduction__start.writeAction(f"movir X16 0") 
  tranBroadcastReduction__start.writeAction(f"movir X23 0") 
  tranBroadcastReduction__start.writeAction(f"__for_start_3_condition: bleu X8 X23 __for_start_5_post") 
  tranBroadcastReduction__start.writeAction(f"__for_start_4_body: add X0 X23 X24") 
  tranBroadcastReduction__start.writeAction(f"movir X25 0") 
  tranBroadcastReduction__start.writeAction(f"evlb X25 BroadcastAboveNodeLevel::start") 
  tranBroadcastReduction__start.writeAction(f"evi X25 X25 255 4") 
  tranBroadcastReduction__start.writeAction(f"ev X25 X25 X24 X24 8") 
  tranBroadcastReduction__start.writeAction(f"send_wcont X25 X21 X20 8") 
  tranBroadcastReduction__start.writeAction(f"addi X16 X16 1") 
  tranBroadcastReduction__start.writeAction(f"add X23 X22 X23") 
  tranBroadcastReduction__start.writeAction(f"jmp __for_start_3_condition") 
  tranBroadcastReduction__start.writeAction(f"__for_start_5_post: yield") 
  tranBroadcastReduction__start.writeAction(f"__if_start_2_post: movir X16 1") 
  tranBroadcastReduction__start.writeAction(f"movir X23 0") 
  tranBroadcastReduction__start.writeAction(f"evlb X23 BroadcastAboveNodeLevel::start") 
  tranBroadcastReduction__start.writeAction(f"evi X23 X23 255 4") 
  tranBroadcastReduction__start.writeAction(f"ev X23 X23 X0 X0 8") 
  tranBroadcastReduction__start.writeAction(f"movrl X8 0(X20) 0 8") 
  tranBroadcastReduction__start.writeAction(f"send_wcont X23 X21 X20 8") 
  tranBroadcastReduction__start.writeAction(f"yield") 
  
  # Writing code for event BroadcastReduction::returnFromChild
  tranBroadcastReduction__returnFromChild = efa.writeEvent('BroadcastReduction::returnFromChild')
  tranBroadcastReduction__returnFromChild.writeAction(f"__entry: subi X16 X16 1") 
  tranBroadcastReduction__returnFromChild.writeAction(f"add X17 X8 X17") 
  tranBroadcastReduction__returnFromChild.writeAction(f"add X18 X9 X18") 
  tranBroadcastReduction__returnFromChild.writeAction(f"add X19 X10 X19") 
  tranBroadcastReduction__returnFromChild.writeAction(f"bneiu X16 0 __if_returnFromChild_2_post") 
  tranBroadcastReduction__returnFromChild.writeAction(f"__if_returnFromChild_0_true: movir X20 -1") 
  tranBroadcastReduction__returnFromChild.writeAction(f"sri X20 X20 1") 
  tranBroadcastReduction__returnFromChild.writeAction(f"sendr3_wcont X1 X20 X17 X18 X19") 
  tranBroadcastReduction__returnFromChild.writeAction(f"yield_terminate") 
  tranBroadcastReduction__returnFromChild.writeAction(f"__if_returnFromChild_2_post: yield") 
  
  ## distribute to the nodes
  
  #############################################################
  ###### Writing code for thread BroadcastAboveNodeLevel ######
  #############################################################
  # Writing code for event BroadcastAboveNodeLevel::start
  tranBroadcastAboveNodeLevel__start = efa.writeEvent('BroadcastAboveNodeLevel::start')
  tranBroadcastAboveNodeLevel__start.writeAction(f"__entry: addi X7 X20 1664") 
  tranBroadcastAboveNodeLevel__start.writeAction(f"addi X20 X21 8") 
  tranBroadcastAboveNodeLevel__start.writeAction(f"bcpyoli X9 X21 7") 
  tranBroadcastAboveNodeLevel__start.writeAction(f"movir X21 2048") 
  tranBroadcastAboveNodeLevel__start.writeAction(f"movrl X21 0(X20) 0 8") 
  tranBroadcastAboveNodeLevel__start.writeAction(f"movir X16 0") 
  tranBroadcastAboveNodeLevel__start.writeAction(f"movir X17 0") 
  tranBroadcastAboveNodeLevel__start.writeAction(f"movir X18 0") 
  tranBroadcastAboveNodeLevel__start.writeAction(f"movir X19 0") 
  tranBroadcastAboveNodeLevel__start.writeAction(f"evi X2 X21 BroadcastAboveNodeLevel::returnFromChild 1") 
  tranBroadcastAboveNodeLevel__start.writeAction(f"movir X22 65536") 
  tranBroadcastAboveNodeLevel__start.writeAction(f"bleu X22 X8 __if_start_2_post") 
  tranBroadcastAboveNodeLevel__start.writeAction(f"__if_start_0_true: addi X8 X22 0") 
  tranBroadcastAboveNodeLevel__start.writeAction(f"__if_start_2_post: movir X23 0") 
  tranBroadcastAboveNodeLevel__start.writeAction(f"__for_start_3_condition: bleu X22 X23 __for_start_5_post") 
  tranBroadcastAboveNodeLevel__start.writeAction(f"__for_start_4_body: add X0 X23 X24") 
  tranBroadcastAboveNodeLevel__start.writeAction(f"movir X25 0") 
  tranBroadcastAboveNodeLevel__start.writeAction(f"evlb X25 BroadcastNodeLevel::start") 
  tranBroadcastAboveNodeLevel__start.writeAction(f"evi X25 X25 255 4") 
  tranBroadcastAboveNodeLevel__start.writeAction(f"ev X25 X25 X24 X24 8") 
  tranBroadcastAboveNodeLevel__start.writeAction(f"send_wcont X25 X21 X20 8") 
  tranBroadcastAboveNodeLevel__start.writeAction(f"addi X16 X16 1") 
  tranBroadcastAboveNodeLevel__start.writeAction(f"addi X23 X23 2048") 
  tranBroadcastAboveNodeLevel__start.writeAction(f"jmp __for_start_3_condition") 
  tranBroadcastAboveNodeLevel__start.writeAction(f"__for_start_5_post: yield") 
  
  # Writing code for event BroadcastAboveNodeLevel::returnFromChild
  tranBroadcastAboveNodeLevel__returnFromChild = efa.writeEvent('BroadcastAboveNodeLevel::returnFromChild')
  tranBroadcastAboveNodeLevel__returnFromChild.writeAction(f"__entry: subi X16 X16 1") 
  tranBroadcastAboveNodeLevel__returnFromChild.writeAction(f"add X17 X8 X17") 
  tranBroadcastAboveNodeLevel__returnFromChild.writeAction(f"add X18 X9 X18") 
  tranBroadcastAboveNodeLevel__returnFromChild.writeAction(f"add X19 X10 X19") 
  tranBroadcastAboveNodeLevel__returnFromChild.writeAction(f"bneiu X16 0 __if_returnFromChild_2_post") 
  tranBroadcastAboveNodeLevel__returnFromChild.writeAction(f"__if_returnFromChild_0_true: movir X23 -1") 
  tranBroadcastAboveNodeLevel__returnFromChild.writeAction(f"sri X23 X23 1") 
  tranBroadcastAboveNodeLevel__returnFromChild.writeAction(f"sendr3_wcont X1 X23 X17 X18 X19") 
  tranBroadcastAboveNodeLevel__returnFromChild.writeAction(f"yield_terminate") 
  tranBroadcastAboveNodeLevel__returnFromChild.writeAction(f"__if_returnFromChild_2_post: yield") 
  
  ## distribute among UDs
  
  ########################################################
  ###### Writing code for thread BroadcastNodeLevel ######
  ########################################################
  # Writing code for event BroadcastNodeLevel::start
  tranBroadcastNodeLevel__start = efa.writeEvent('BroadcastNodeLevel::start')
  tranBroadcastNodeLevel__start.writeAction(f"__entry: addi X7 X20 1664") 
  tranBroadcastNodeLevel__start.writeAction(f"addi X20 X21 8") 
  tranBroadcastNodeLevel__start.writeAction(f"bcpyoli X9 X21 7") 
  tranBroadcastNodeLevel__start.writeAction(f"movir X21 64") 
  tranBroadcastNodeLevel__start.writeAction(f"movrl X21 0(X20) 0 8") 
  tranBroadcastNodeLevel__start.writeAction(f"movir X16 0") 
  tranBroadcastNodeLevel__start.writeAction(f"movir X17 0") 
  tranBroadcastNodeLevel__start.writeAction(f"movir X18 0") 
  tranBroadcastNodeLevel__start.writeAction(f"movir X19 0") 
  tranBroadcastNodeLevel__start.writeAction(f"evi X2 X21 BroadcastNodeLevel::returnFromChild 1") 
  tranBroadcastNodeLevel__start.writeAction(f"movir X22 0") 
  tranBroadcastNodeLevel__start.writeAction(f"__for_start_0_condition: bleu X8 X22 __for_start_2_post") 
  tranBroadcastNodeLevel__start.writeAction(f"__for_start_1_body: add X0 X22 X23") 
  tranBroadcastNodeLevel__start.writeAction(f"movir X24 0") 
  tranBroadcastNodeLevel__start.writeAction(f"evlb X24 BroadcastUDLevel::start") 
  tranBroadcastNodeLevel__start.writeAction(f"evi X24 X24 255 4") 
  tranBroadcastNodeLevel__start.writeAction(f"ev X24 X24 X23 X23 8") 
  tranBroadcastNodeLevel__start.writeAction(f"send_wcont X24 X21 X20 8") 
  tranBroadcastNodeLevel__start.writeAction(f"addi X16 X16 1") 
  tranBroadcastNodeLevel__start.writeAction(f"addi X22 X22 64") 
  tranBroadcastNodeLevel__start.writeAction(f"jmp __for_start_0_condition") 
  tranBroadcastNodeLevel__start.writeAction(f"__for_start_2_post: yield") 
  
  # Writing code for event BroadcastNodeLevel::returnFromChild
  tranBroadcastNodeLevel__returnFromChild = efa.writeEvent('BroadcastNodeLevel::returnFromChild')
  tranBroadcastNodeLevel__returnFromChild.writeAction(f"__entry: subi X16 X16 1") 
  tranBroadcastNodeLevel__returnFromChild.writeAction(f"add X17 X8 X17") 
  tranBroadcastNodeLevel__returnFromChild.writeAction(f"add X18 X9 X18") 
  tranBroadcastNodeLevel__returnFromChild.writeAction(f"add X19 X10 X19") 
  tranBroadcastNodeLevel__returnFromChild.writeAction(f"bneiu X16 0 __if_returnFromChild_2_post") 
  tranBroadcastNodeLevel__returnFromChild.writeAction(f"__if_returnFromChild_0_true: movir X20 -1") 
  tranBroadcastNodeLevel__returnFromChild.writeAction(f"sri X20 X20 1") 
  tranBroadcastNodeLevel__returnFromChild.writeAction(f"sendr3_wcont X1 X20 X17 X18 X19") 
  tranBroadcastNodeLevel__returnFromChild.writeAction(f"yield_terminate") 
  tranBroadcastNodeLevel__returnFromChild.writeAction(f"__if_returnFromChild_2_post: yield") 
  
  ## distribute among the lanes
  
  ######################################################
  ###### Writing code for thread BroadcastUDLevel ######
  ######################################################
  # Writing code for event BroadcastUDLevel::start
  tranBroadcastUDLevel__start = efa.writeEvent('BroadcastUDLevel::start')
  tranBroadcastUDLevel__start.writeAction(f"__entry: movir X17 0") 
  tranBroadcastUDLevel__start.writeAction(f"movir X18 0") 
  tranBroadcastUDLevel__start.writeAction(f"movir X19 0") 
  tranBroadcastUDLevel__start.writeAction(f"addi X8 X16 0") 
  tranBroadcastUDLevel__start.writeAction(f"evi X2 X20 BroadcastUDLevel::returnFromChild 1") 
  tranBroadcastUDLevel__start.writeAction(f"movir X21 0") 
  tranBroadcastUDLevel__start.writeAction(f"__for_start_0_condition: bleu X8 X21 __for_start_2_post") 
  tranBroadcastUDLevel__start.writeAction(f"__for_start_1_body: add X21 X0 X22") 
  tranBroadcastUDLevel__start.writeAction(f"ev X9 X22 X22 X22 8") 
  tranBroadcastUDLevel__start.writeAction(f"sendops_wcont X22 X20 X10 8") 
  tranBroadcastUDLevel__start.writeAction(f"addi X21 X21 1") 
  tranBroadcastUDLevel__start.writeAction(f"jmp __for_start_0_condition") 
  tranBroadcastUDLevel__start.writeAction(f"__for_start_2_post: yield") 
  
  # Writing code for event BroadcastUDLevel::returnFromChild
  tranBroadcastUDLevel__returnFromChild = efa.writeEvent('BroadcastUDLevel::returnFromChild')
  tranBroadcastUDLevel__returnFromChild.writeAction(f"__entry: subi X16 X16 1") 
  tranBroadcastUDLevel__returnFromChild.writeAction(f"add X17 X8 X17") 
  tranBroadcastUDLevel__returnFromChild.writeAction(f"add X18 X9 X18") 
  tranBroadcastUDLevel__returnFromChild.writeAction(f"add X19 X10 X19") 
  tranBroadcastUDLevel__returnFromChild.writeAction(f"bneiu X16 0 __if_returnFromChild_2_post") 
  tranBroadcastUDLevel__returnFromChild.writeAction(f"__if_returnFromChild_0_true: movir X21 -1") 
  tranBroadcastUDLevel__returnFromChild.writeAction(f"sri X21 X21 1") 
  tranBroadcastUDLevel__returnFromChild.writeAction(f"sendr3_wcont X1 X21 X17 X18 X19") 
  tranBroadcastUDLevel__returnFromChild.writeAction(f"yield_terminate") 
  tranBroadcastUDLevel__returnFromChild.writeAction(f"__if_returnFromChild_2_post: yield") 
  