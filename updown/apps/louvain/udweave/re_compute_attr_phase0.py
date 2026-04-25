from linker.EFAProgram import efaProgram

## UDWeave version: 7808cc0 (2026-04-24)

## Global constants

@efaProgram
def EFA_re_compute_attr_phase0(efa):
  efa.code_level = 'machine'
  state0 = efa.State("udweave_init") #Only one state code 
  efa.add_initId(state0.state_id)
  ## Static declarations
  ## Scoped Variable "num_map_done" uses Register X16, scope (0)
  ## Scoped Variable "num_map" uses Register X17, scope (0)
  ## Scoped Variable "num_lanes_per_control" uses Register X18, scope (0)
  ## Scoped Variable "control_level" uses Register X19, scope (0)
  ## Scoped Variable "cont" uses Register X20, scope (0)
  ## Scoped Variable "num_moves" uses Register X21, scope (0)
  ## Scoped Variable "vid" uses Register X16, scope (0)
  ## Scoped Variable "num_verts" uses Register X17, scope (0)
  ## Scoped Variable "outstanding" uses Register X18, scope (0)
  ## Scoped Variable "total_lanes" uses Register X19, scope (0)
  ## Scoped Variable "gv" uses Register X20, scope (0)
  ## Scoped Variable "cont" uses Register X21, scope (0)
  ## Scoped Variable "num_moves" uses Register X22, scope (0)
  ## Scoped Variable "flag" uses Register X23, scope (0)
  ## #define DEBUG
  
  ###################################################################
  ###### Writing code for thread re_compute_attr_phase0_master ######
  ###################################################################
  # Writing code for event re_compute_attr_phase0_master::init
  tranre_compute_attr_phase0_master__init = efa.writeEvent('re_compute_attr_phase0_master::init')
  tranre_compute_attr_phase0_master__init.writeAction(f"__entry: addi X7 X22 0") 
  tranre_compute_attr_phase0_master__init.writeAction(f"bneiu X13 0 __if_init_2_post") 
  tranre_compute_attr_phase0_master__init.writeAction(f"__if_init_0_true: print 're_compute_attr_phase0 Start'") 
  tranre_compute_attr_phase0_master__init.writeAction(f"movir X23 0") 
  tranre_compute_attr_phase0_master__init.writeAction(f"movrl X23 0(X22) 0 8") 
  tranre_compute_attr_phase0_master__init.writeAction(f"__if_init_2_post: addi X1 X20 0") 
  tranre_compute_attr_phase0_master__init.writeAction(f"addi X13 X19 0") 
  tranre_compute_attr_phase0_master__init.writeAction(f"movir X23 1") 
  tranre_compute_attr_phase0_master__init.writeAction(f"sl X23 X12 X23") 
  tranre_compute_attr_phase0_master__init.writeAction(f"subi X8 X18 1") 
  tranre_compute_attr_phase0_master__init.writeAction(f"sr X18 X12 X24") 
  tranre_compute_attr_phase0_master__init.writeAction(f"addi X24 X18 1") 
  tranre_compute_attr_phase0_master__init.writeAction(f"bneiu X18 1 __if_init_4_false") 
  tranre_compute_attr_phase0_master__init.writeAction(f"__if_init_3_true: addi X8 X17 0") 
  ## start init 

  tranre_compute_attr_phase0_master__init.writeAction(f"addi X7 X22 16") 
  tranre_compute_attr_phase0_master__init.writeAction(f"movrl X9 0(X22) 0 8") 
  tranre_compute_attr_phase0_master__init.writeAction(f"movrl X11 8(X22) 0 8") 
  tranre_compute_attr_phase0_master__init.writeAction(f"movrl X10 16(X22) 0 8") 
  tranre_compute_attr_phase0_master__init.writeAction(f"movrl X14 24(X22) 0 8") 
  tranre_compute_attr_phase0_master__init.writeAction(f"addi X0 X24 0") 
  tranre_compute_attr_phase0_master__init.writeAction(f"add X24 X8 X25") 
  tranre_compute_attr_phase0_master__init.writeAction(f"__while_init_6_condition: ble X25 X24 __while_init_8_post") 
  tranre_compute_attr_phase0_master__init.writeAction(f"__while_init_7_body: movir X26 0") 
  tranre_compute_attr_phase0_master__init.writeAction(f"evlb X26 re_compute_attr_phase0_worker__init") 
  tranre_compute_attr_phase0_master__init.writeAction(f"evi X26 X26 255 4") 
  tranre_compute_attr_phase0_master__init.writeAction(f"ev X26 X26 X24 X24 8") 
  tranre_compute_attr_phase0_master__init.writeAction(f"send_wret X26 re_compute_attr_phase0_master::init_done X22 4 X27") 
  tranre_compute_attr_phase0_master__init.writeAction(f"addi X24 X24 1") 
  tranre_compute_attr_phase0_master__init.writeAction(f"jmp __while_init_6_condition") 
  tranre_compute_attr_phase0_master__init.writeAction(f"__while_init_8_post: jmp __if_init_5_post") 
  tranre_compute_attr_phase0_master__init.writeAction(f"__if_init_4_false: addi X7 X22 16") 
  tranre_compute_attr_phase0_master__init.writeAction(f"movrl X18 0(X22) 0 8") 
  tranre_compute_attr_phase0_master__init.writeAction(f"movrl X9 8(X22) 0 8") 
  tranre_compute_attr_phase0_master__init.writeAction(f"movrl X10 16(X22) 0 8") 
  tranre_compute_attr_phase0_master__init.writeAction(f"movrl X11 24(X22) 0 8") 
  tranre_compute_attr_phase0_master__init.writeAction(f"movrl X12 32(X22) 0 8") 
  tranre_compute_attr_phase0_master__init.writeAction(f"addi X13 X24 1") 
  tranre_compute_attr_phase0_master__init.writeAction(f"movrl X24 40(X22) 0 8") 
  tranre_compute_attr_phase0_master__init.writeAction(f"movrl X14 48(X22) 0 8") 
  tranre_compute_attr_phase0_master__init.writeAction(f"addi X0 X24 0") 
  tranre_compute_attr_phase0_master__init.writeAction(f"addi X23 X17 0") 
  tranre_compute_attr_phase0_master__init.writeAction(f"mul X18 X23 X25") 
  tranre_compute_attr_phase0_master__init.writeAction(f"add X25 X24 X25") 
  tranre_compute_attr_phase0_master__init.writeAction(f"__while_init_9_condition: ble X25 X24 __if_init_5_post") 
  tranre_compute_attr_phase0_master__init.writeAction(f"__while_init_10_body: movir X26 0") 
  tranre_compute_attr_phase0_master__init.writeAction(f"evlb X26 re_compute_attr_phase0_master::init") 
  tranre_compute_attr_phase0_master__init.writeAction(f"evi X26 X26 255 4") 
  tranre_compute_attr_phase0_master__init.writeAction(f"ev X26 X26 X24 X24 8") 
  tranre_compute_attr_phase0_master__init.writeAction(f"send_wret X26 re_compute_attr_phase0_master::init_done X22 7 X27") 
  tranre_compute_attr_phase0_master__init.writeAction(f"add X24 X18 X24") 
  tranre_compute_attr_phase0_master__init.writeAction(f"jmp __while_init_9_condition") 
  tranre_compute_attr_phase0_master__init.writeAction(f"__if_init_5_post: movir X16 0") 
  tranre_compute_attr_phase0_master__init.writeAction(f"movir X21 0") 
  tranre_compute_attr_phase0_master__init.writeAction(f"yield") 
  
  # Writing code for event re_compute_attr_phase0_master::init_done
  tranre_compute_attr_phase0_master__init_done = efa.writeEvent('re_compute_attr_phase0_master::init_done')
  tranre_compute_attr_phase0_master__init_done.writeAction(f"__entry: addi X16 X16 1") 
  ## print("%lu %lu", _q, q);

  tranre_compute_attr_phase0_master__init_done.writeAction(f"add X21 X9 X21") 
  tranre_compute_attr_phase0_master__init_done.writeAction(f"bneu X16 X17 __if_init_done_2_post") 
  tranre_compute_attr_phase0_master__init_done.writeAction(f"__if_init_done_0_true: movir X16 0") 
  tranre_compute_attr_phase0_master__init_done.writeAction(f"bneiu X19 0 __if_init_done_4_false") 
  tranre_compute_attr_phase0_master__init_done.writeAction(f"__if_init_done_3_true: print 're_compute_attr_phase0 End'") 
  tranre_compute_attr_phase0_master__init_done.writeAction(f"addi X7 X22 0") 
  tranre_compute_attr_phase0_master__init_done.writeAction(f"movir X23 1") 
  tranre_compute_attr_phase0_master__init_done.writeAction(f"movrl X23 0(X22) 0 8") 
  tranre_compute_attr_phase0_master__init_done.writeAction(f"movrl X21 8(X22) 0 8") 
  tranre_compute_attr_phase0_master__init_done.writeAction(f"print 'num_moves = %lu' X21") 
  tranre_compute_attr_phase0_master__init_done.writeAction(f"yield_terminate") 
  tranre_compute_attr_phase0_master__init_done.writeAction(f"jmp __if_init_done_2_post") 
  tranre_compute_attr_phase0_master__init_done.writeAction(f"__if_init_done_4_false: movir X22 -1") 
  tranre_compute_attr_phase0_master__init_done.writeAction(f"sri X22 X22 1") 
  tranre_compute_attr_phase0_master__init_done.writeAction(f"sendr_wcont X20 X22 X0 X21") 
  tranre_compute_attr_phase0_master__init_done.writeAction(f"yield_terminate") 
  tranre_compute_attr_phase0_master__init_done.writeAction(f"__if_init_done_2_post: yield") 
  
  
  ###################################################################
  ###### Writing code for thread re_compute_attr_phase0_worker ######
  ###################################################################
  # Writing code for event re_compute_attr_phase0_worker::init
  tranre_compute_attr_phase0_worker__init = efa.writeEvent('re_compute_attr_phase0_worker::init')
  tranre_compute_attr_phase0_worker__init.writeAction(f"__entry: addi X0 X16 0") 
  tranre_compute_attr_phase0_worker__init.writeAction(f"addi X10 X17 0") 
  tranre_compute_attr_phase0_worker__init.writeAction(f"movir X18 0") 
  tranre_compute_attr_phase0_worker__init.writeAction(f"addi X9 X19 0") 
  tranre_compute_attr_phase0_worker__init.writeAction(f"addi X8 X20 32") 
  tranre_compute_attr_phase0_worker__init.writeAction(f"addi X1 X21 0") 
  tranre_compute_attr_phase0_worker__init.writeAction(f"movir X22 0") 
  tranre_compute_attr_phase0_worker__init.writeAction(f"addi X11 X23 0") 
  tranre_compute_attr_phase0_worker__init.writeAction(f"addi X0 X16 0") 
  tranre_compute_attr_phase0_worker__init.writeAction(f"__for_init_0_condition: ble X17 X16 __for_init_2_post") 
  tranre_compute_attr_phase0_worker__init.writeAction(f"__for_init_1_body: sli X16 X24 7") 
  tranre_compute_attr_phase0_worker__init.writeAction(f"add X20 X24 X24") 
  ## 16 words

  tranre_compute_attr_phase0_worker__init.writeAction(f"send_dmlm_ld_wret X24 re_compute_attr_phase0_worker::v_return 7 X25") 
  tranre_compute_attr_phase0_worker__init.writeAction(f"addi X18 X18 1") 
  tranre_compute_attr_phase0_worker__init.writeAction(f"movir X24 1024") 
  tranre_compute_attr_phase0_worker__init.writeAction(f"bgt X24 X18 __if_init_5_post") 
  tranre_compute_attr_phase0_worker__init.writeAction(f"__if_init_3_true: add X16 X9 X16") 
  tranre_compute_attr_phase0_worker__init.writeAction(f"jmp __for_init_2_post") 
  tranre_compute_attr_phase0_worker__init.writeAction(f"__if_init_5_post: add X16 X9 X16") 
  tranre_compute_attr_phase0_worker__init.writeAction(f"jmp __for_init_0_condition") 
  tranre_compute_attr_phase0_worker__init.writeAction(f"__for_init_2_post: bnei X18 0 __if_init_8_post") 
  tranre_compute_attr_phase0_worker__init.writeAction(f"__if_init_6_true: movir X24 -1") 
  tranre_compute_attr_phase0_worker__init.writeAction(f"sri X24 X24 1") 
  tranre_compute_attr_phase0_worker__init.writeAction(f"sendr_wcont X21 X24 X0 X22") 
  tranre_compute_attr_phase0_worker__init.writeAction(f"yield_terminate") 
  tranre_compute_attr_phase0_worker__init.writeAction(f"__if_init_8_post: yield") 
  
  # Writing code for event re_compute_attr_phase0_worker::v_return
  tranre_compute_attr_phase0_worker__v_return = efa.writeEvent('re_compute_attr_phase0_worker::v_return')
  tranre_compute_attr_phase0_worker__v_return.writeAction(f"__entry: beqi X23 0 __if_v_return_1_false") 
  tranre_compute_attr_phase0_worker__v_return.writeAction(f"__if_v_return_0_true: bleu X14 X8 __if_v_return_5_post") 
  tranre_compute_attr_phase0_worker__v_return.writeAction(f"__if_v_return_3_true: addi X22 X22 1") 
  tranre_compute_attr_phase0_worker__v_return.writeAction(f"__if_v_return_5_post: jmp __if_v_return_2_post") 
  tranre_compute_attr_phase0_worker__v_return.writeAction(f"__if_v_return_1_false: bleu X8 X14 __if_v_return_2_post") 
  tranre_compute_attr_phase0_worker__v_return.writeAction(f"__if_v_return_6_true: addi X22 X22 1") 
  tranre_compute_attr_phase0_worker__v_return.writeAction(f"__if_v_return_2_post: ble X17 X16 __if_v_return_10_false") 
  tranre_compute_attr_phase0_worker__v_return.writeAction(f"__if_v_return_9_true: sli X16 X24 7") 
  tranre_compute_attr_phase0_worker__v_return.writeAction(f"add X20 X24 X24") 
  ## 16 words

  tranre_compute_attr_phase0_worker__v_return.writeAction(f"send_dmlm_ld_wret X24 re_compute_attr_phase0_worker::v_return 7 X25") 
  tranre_compute_attr_phase0_worker__v_return.writeAction(f"add X16 X19 X16") 
  tranre_compute_attr_phase0_worker__v_return.writeAction(f"jmp __if_v_return_11_post") 
  tranre_compute_attr_phase0_worker__v_return.writeAction(f"__if_v_return_10_false: subi X18 X18 1") 
  tranre_compute_attr_phase0_worker__v_return.writeAction(f"__if_v_return_11_post: bnei X18 0 __if_v_return_14_post") 
  tranre_compute_attr_phase0_worker__v_return.writeAction(f"__if_v_return_12_true: movir X24 -1") 
  tranre_compute_attr_phase0_worker__v_return.writeAction(f"sri X24 X24 1") 
  tranre_compute_attr_phase0_worker__v_return.writeAction(f"sendr_wcont X21 X24 X0 X22") 
  tranre_compute_attr_phase0_worker__v_return.writeAction(f"yield_terminate") 
  tranre_compute_attr_phase0_worker__v_return.writeAction(f"__if_v_return_14_post: yield") 
  