from linker.EFAProgram import efaProgram

## UDWeave version: 7808cc0 (2026-04-24)

## Global constants

@efaProgram
def EFA_re_compute_attr1_phase1(efa):
  efa.code_level = 'machine'
  state0 = efa.State("udweave_init") #Only one state code 
  efa.add_initId(state0.state_id)
  ## Static declarations
  ## Scoped Variable "num_map_done" uses Register X16, scope (0)
  ## Scoped Variable "num_map" uses Register X17, scope (0)
  ## Scoped Variable "num_lanes_per_control" uses Register X18, scope (0)
  ## Scoped Variable "control_level" uses Register X19, scope (0)
  ## Scoped Variable "cont" uses Register X20, scope (0)
  ## Scoped Variable "vid" uses Register X16, scope (0)
  ## Scoped Variable "num_verts" uses Register X17, scope (0)
  ## Scoped Variable "outstanding" uses Register X18, scope (0)
  ## Scoped Variable "total_lanes" uses Register X19, scope (0)
  ## Scoped Variable "gv" uses Register X20, scope (0)
  ## Scoped Variable "cont" uses Register X21, scope (0)
  ## Scoped Variable "flag" uses Register X22, scope (0)
  ## #define DEBUG
  
  ####################################################################
  ###### Writing code for thread re_compute_attr1_phase1_master ######
  ####################################################################
  # Writing code for event re_compute_attr1_phase1_master::init
  tranre_compute_attr1_phase1_master__init = efa.writeEvent('re_compute_attr1_phase1_master::init')
  tranre_compute_attr1_phase1_master__init.writeAction(f"__entry: addi X7 X21 0") 
  tranre_compute_attr1_phase1_master__init.writeAction(f"bneiu X13 0 __if_init_2_post") 
  tranre_compute_attr1_phase1_master__init.writeAction(f"__if_init_0_true: print 're_compute_attr1_phase1 Start'") 
  tranre_compute_attr1_phase1_master__init.writeAction(f"movir X22 0") 
  tranre_compute_attr1_phase1_master__init.writeAction(f"movrl X22 0(X21) 0 8") 
  tranre_compute_attr1_phase1_master__init.writeAction(f"__if_init_2_post: addi X1 X20 0") 
  tranre_compute_attr1_phase1_master__init.writeAction(f"addi X13 X19 0") 
  tranre_compute_attr1_phase1_master__init.writeAction(f"movir X22 1") 
  tranre_compute_attr1_phase1_master__init.writeAction(f"sl X22 X12 X22") 
  tranre_compute_attr1_phase1_master__init.writeAction(f"subi X8 X18 1") 
  tranre_compute_attr1_phase1_master__init.writeAction(f"sr X18 X12 X23") 
  tranre_compute_attr1_phase1_master__init.writeAction(f"addi X23 X18 1") 
  tranre_compute_attr1_phase1_master__init.writeAction(f"bneiu X18 1 __if_init_4_false") 
  tranre_compute_attr1_phase1_master__init.writeAction(f"__if_init_3_true: addi X8 X17 0") 
  ## start init 

  tranre_compute_attr1_phase1_master__init.writeAction(f"addi X7 X21 16") 
  tranre_compute_attr1_phase1_master__init.writeAction(f"movrl X9 0(X21) 0 8") 
  tranre_compute_attr1_phase1_master__init.writeAction(f"movrl X11 8(X21) 0 8") 
  tranre_compute_attr1_phase1_master__init.writeAction(f"movrl X10 16(X21) 0 8") 
  tranre_compute_attr1_phase1_master__init.writeAction(f"movrl X14 24(X21) 0 8") 
  tranre_compute_attr1_phase1_master__init.writeAction(f"addi X0 X23 0") 
  tranre_compute_attr1_phase1_master__init.writeAction(f"add X23 X8 X24") 
  tranre_compute_attr1_phase1_master__init.writeAction(f"__while_init_6_condition: ble X24 X23 __while_init_8_post") 
  tranre_compute_attr1_phase1_master__init.writeAction(f"__while_init_7_body: movir X25 0") 
  tranre_compute_attr1_phase1_master__init.writeAction(f"evlb X25 re_compute_attr1_phase1_worker__init") 
  tranre_compute_attr1_phase1_master__init.writeAction(f"evi X25 X25 255 4") 
  tranre_compute_attr1_phase1_master__init.writeAction(f"ev X25 X25 X23 X23 8") 
  tranre_compute_attr1_phase1_master__init.writeAction(f"send_wret X25 re_compute_attr1_phase1_master::init_done X21 4 X26") 
  tranre_compute_attr1_phase1_master__init.writeAction(f"addi X23 X23 1") 
  tranre_compute_attr1_phase1_master__init.writeAction(f"jmp __while_init_6_condition") 
  tranre_compute_attr1_phase1_master__init.writeAction(f"__while_init_8_post: jmp __if_init_5_post") 
  tranre_compute_attr1_phase1_master__init.writeAction(f"__if_init_4_false: addi X7 X21 16") 
  tranre_compute_attr1_phase1_master__init.writeAction(f"movrl X18 0(X21) 0 8") 
  tranre_compute_attr1_phase1_master__init.writeAction(f"movrl X9 8(X21) 0 8") 
  tranre_compute_attr1_phase1_master__init.writeAction(f"movrl X10 16(X21) 0 8") 
  tranre_compute_attr1_phase1_master__init.writeAction(f"movrl X11 24(X21) 0 8") 
  tranre_compute_attr1_phase1_master__init.writeAction(f"movrl X12 32(X21) 0 8") 
  tranre_compute_attr1_phase1_master__init.writeAction(f"addi X13 X24 1") 
  tranre_compute_attr1_phase1_master__init.writeAction(f"movrl X24 40(X21) 0 8") 
  tranre_compute_attr1_phase1_master__init.writeAction(f"movrl X14 48(X21) 0 8") 
  tranre_compute_attr1_phase1_master__init.writeAction(f"addi X0 X24 0") 
  tranre_compute_attr1_phase1_master__init.writeAction(f"addi X22 X17 0") 
  tranre_compute_attr1_phase1_master__init.writeAction(f"mul X18 X22 X23") 
  tranre_compute_attr1_phase1_master__init.writeAction(f"add X23 X24 X23") 
  tranre_compute_attr1_phase1_master__init.writeAction(f"__while_init_9_condition: ble X23 X24 __if_init_5_post") 
  tranre_compute_attr1_phase1_master__init.writeAction(f"__while_init_10_body: movir X25 0") 
  tranre_compute_attr1_phase1_master__init.writeAction(f"evlb X25 re_compute_attr1_phase1_master::init") 
  tranre_compute_attr1_phase1_master__init.writeAction(f"evi X25 X25 255 4") 
  tranre_compute_attr1_phase1_master__init.writeAction(f"ev X25 X25 X24 X24 8") 
  tranre_compute_attr1_phase1_master__init.writeAction(f"send_wret X25 re_compute_attr1_phase1_master::init_done X21 7 X26") 
  tranre_compute_attr1_phase1_master__init.writeAction(f"add X24 X18 X24") 
  tranre_compute_attr1_phase1_master__init.writeAction(f"jmp __while_init_9_condition") 
  tranre_compute_attr1_phase1_master__init.writeAction(f"__if_init_5_post: movir X16 0") 
  tranre_compute_attr1_phase1_master__init.writeAction(f"yield") 
  
  # Writing code for event re_compute_attr1_phase1_master::init_done
  tranre_compute_attr1_phase1_master__init_done = efa.writeEvent('re_compute_attr1_phase1_master::init_done')
  tranre_compute_attr1_phase1_master__init_done.writeAction(f"__entry: addi X16 X16 1") 
  ## print("%lu %lu", _q, q);

  tranre_compute_attr1_phase1_master__init_done.writeAction(f"bneu X16 X17 __if_init_done_2_post") 
  tranre_compute_attr1_phase1_master__init_done.writeAction(f"__if_init_done_0_true: movir X16 0") 
  tranre_compute_attr1_phase1_master__init_done.writeAction(f"bneiu X19 0 __if_init_done_4_false") 
  tranre_compute_attr1_phase1_master__init_done.writeAction(f"__if_init_done_3_true: print 're_compute_attr1_phase1 End'") 
  tranre_compute_attr1_phase1_master__init_done.writeAction(f"addi X7 X22 0") 
  tranre_compute_attr1_phase1_master__init_done.writeAction(f"movir X21 1") 
  tranre_compute_attr1_phase1_master__init_done.writeAction(f"movrl X21 0(X22) 0 8") 
  tranre_compute_attr1_phase1_master__init_done.writeAction(f"yield_terminate") 
  tranre_compute_attr1_phase1_master__init_done.writeAction(f"jmp __if_init_done_2_post") 
  tranre_compute_attr1_phase1_master__init_done.writeAction(f"__if_init_done_4_false: movir X22 -1") 
  tranre_compute_attr1_phase1_master__init_done.writeAction(f"sri X22 X22 1") 
  tranre_compute_attr1_phase1_master__init_done.writeAction(f"sendr_wcont X20 X22 X0 X0") 
  tranre_compute_attr1_phase1_master__init_done.writeAction(f"yield_terminate") 
  tranre_compute_attr1_phase1_master__init_done.writeAction(f"__if_init_done_2_post: yield") 
  
  
  ####################################################################
  ###### Writing code for thread re_compute_attr1_phase1_worker ######
  ####################################################################
  # Writing code for event re_compute_attr1_phase1_worker::init
  tranre_compute_attr1_phase1_worker__init = efa.writeEvent('re_compute_attr1_phase1_worker::init')
  tranre_compute_attr1_phase1_worker__init.writeAction(f"__entry: addi X0 X16 0") 
  tranre_compute_attr1_phase1_worker__init.writeAction(f"addi X10 X17 0") 
  tranre_compute_attr1_phase1_worker__init.writeAction(f"movir X18 0") 
  tranre_compute_attr1_phase1_worker__init.writeAction(f"addi X9 X19 0") 
  tranre_compute_attr1_phase1_worker__init.writeAction(f"addi X8 X20 80") 
  tranre_compute_attr1_phase1_worker__init.writeAction(f"addi X1 X21 0") 
  tranre_compute_attr1_phase1_worker__init.writeAction(f"addi X11 X22 0") 
  tranre_compute_attr1_phase1_worker__init.writeAction(f"addi X0 X16 0") 
  tranre_compute_attr1_phase1_worker__init.writeAction(f"__for_init_0_condition: ble X17 X16 __for_init_2_post") 
  tranre_compute_attr1_phase1_worker__init.writeAction(f"__for_init_1_body: sli X16 X23 7") 
  tranre_compute_attr1_phase1_worker__init.writeAction(f"add X20 X23 X23") 
  ## 16 words

  tranre_compute_attr1_phase1_worker__init.writeAction(f"send_dmlm_ld_wret X23 re_compute_attr1_phase1_worker::v_return 4 X24") 
  tranre_compute_attr1_phase1_worker__init.writeAction(f"addi X18 X18 1") 
  tranre_compute_attr1_phase1_worker__init.writeAction(f"movir X23 1024") 
  tranre_compute_attr1_phase1_worker__init.writeAction(f"bgt X23 X18 __if_init_5_post") 
  tranre_compute_attr1_phase1_worker__init.writeAction(f"__if_init_3_true: add X16 X9 X16") 
  tranre_compute_attr1_phase1_worker__init.writeAction(f"jmp __for_init_2_post") 
  tranre_compute_attr1_phase1_worker__init.writeAction(f"__if_init_5_post: add X16 X9 X16") 
  tranre_compute_attr1_phase1_worker__init.writeAction(f"jmp __for_init_0_condition") 
  tranre_compute_attr1_phase1_worker__init.writeAction(f"__for_init_2_post: bnei X18 0 __if_init_8_post") 
  tranre_compute_attr1_phase1_worker__init.writeAction(f"__if_init_6_true: movir X23 -1") 
  tranre_compute_attr1_phase1_worker__init.writeAction(f"sri X23 X23 1") 
  tranre_compute_attr1_phase1_worker__init.writeAction(f"sendr_wcont X21 X23 X0 X0") 
  tranre_compute_attr1_phase1_worker__init.writeAction(f"yield_terminate") 
  tranre_compute_attr1_phase1_worker__init.writeAction(f"__if_init_8_post: yield") 
  
  # Writing code for event re_compute_attr1_phase1_worker::v_return
  tranre_compute_attr1_phase1_worker__v_return = efa.writeEvent('re_compute_attr1_phase1_worker::v_return')
  tranre_compute_attr1_phase1_worker__v_return.writeAction(f"__entry: addi X7 X23 16") 
  tranre_compute_attr1_phase1_worker__v_return.writeAction(f"movir X24 0") 
  tranre_compute_attr1_phase1_worker__v_return.writeAction(f"movrl X24 8(X23) 0 8") 
  tranre_compute_attr1_phase1_worker__v_return.writeAction(f"movir X24 0") 
  tranre_compute_attr1_phase1_worker__v_return.writeAction(f"movrl X24 16(X23) 0 8") 
  tranre_compute_attr1_phase1_worker__v_return.writeAction(f"beqi X22 0 __if_v_return_1_false") 
  tranre_compute_attr1_phase1_worker__v_return.writeAction(f"__if_v_return_0_true: bleu X8 X11 __if_v_return_4_false") 
  tranre_compute_attr1_phase1_worker__v_return.writeAction(f"__if_v_return_3_true: movrl X8 0(X23) 0 8") 
  tranre_compute_attr1_phase1_worker__v_return.writeAction(f"jmp __if_v_return_5_post") 
  tranre_compute_attr1_phase1_worker__v_return.writeAction(f"__if_v_return_4_false: movrl X11 0(X23) 0 8") 
  tranre_compute_attr1_phase1_worker__v_return.writeAction(f"__if_v_return_5_post: jmp __if_v_return_2_post") 
  tranre_compute_attr1_phase1_worker__v_return.writeAction(f"__if_v_return_1_false: bleu X11 X8 __if_v_return_7_false") 
  tranre_compute_attr1_phase1_worker__v_return.writeAction(f"__if_v_return_6_true: movrl X8 0(X23) 0 8") 
  tranre_compute_attr1_phase1_worker__v_return.writeAction(f"jmp __if_v_return_2_post") 
  tranre_compute_attr1_phase1_worker__v_return.writeAction(f"__if_v_return_7_false: movrl X11 0(X23) 0 8") 
  tranre_compute_attr1_phase1_worker__v_return.writeAction(f"__if_v_return_2_post: subi X12 X24 48") 
  tranre_compute_attr1_phase1_worker__v_return.writeAction(f"send_dmlm_wret X24 re_compute_attr1_phase1_worker::write_done X23 3 X25") 
  tranre_compute_attr1_phase1_worker__v_return.writeAction(f"yield") 
  
  # Writing code for event re_compute_attr1_phase1_worker::write_done
  tranre_compute_attr1_phase1_worker__write_done = efa.writeEvent('re_compute_attr1_phase1_worker::write_done')
  tranre_compute_attr1_phase1_worker__write_done.writeAction(f"__entry: subi X18 X18 1") 
  tranre_compute_attr1_phase1_worker__write_done.writeAction(f"ble X17 X16 __if_write_done_2_post") 
  tranre_compute_attr1_phase1_worker__write_done.writeAction(f"__if_write_done_0_true: sli X16 X23 7") 
  tranre_compute_attr1_phase1_worker__write_done.writeAction(f"add X20 X23 X23") 
  ## 16 words

  tranre_compute_attr1_phase1_worker__write_done.writeAction(f"send_dmlm_ld_wret X23 re_compute_attr1_phase1_worker::v_return 4 X24") 
  tranre_compute_attr1_phase1_worker__write_done.writeAction(f"add X16 X19 X16") 
  tranre_compute_attr1_phase1_worker__write_done.writeAction(f"addi X18 X18 1") 
  tranre_compute_attr1_phase1_worker__write_done.writeAction(f"__if_write_done_2_post: bnei X18 0 __if_write_done_5_post") 
  tranre_compute_attr1_phase1_worker__write_done.writeAction(f"__if_write_done_3_true: movir X23 -1") 
  tranre_compute_attr1_phase1_worker__write_done.writeAction(f"sri X23 X23 1") 
  tranre_compute_attr1_phase1_worker__write_done.writeAction(f"sendr_wcont X21 X23 X0 X0") 
  tranre_compute_attr1_phase1_worker__write_done.writeAction(f"yield_terminate") 
  tranre_compute_attr1_phase1_worker__write_done.writeAction(f"__if_write_done_5_post: yield") 
  