from linker.EFAProgram import efaProgram

## UDWeave version: 7808cc0 (2026-04-24)

## Global constants

@efaProgram
def EFA_quality(efa):
  efa.code_level = 'machine'
  state0 = efa.State("udweave_init") #Only one state code 
  efa.add_initId(state0.state_id)
  ## Static declarations
  ## Scoped Variable "num_map_done" uses Register X16, scope (0)
  ## Scoped Variable "num_map" uses Register X17, scope (0)
  ## Scoped Variable "num_lanes_per_control" uses Register X18, scope (0)
  ## Scoped Variable "control_level" uses Register X19, scope (0)
  ## Scoped Variable "cont" uses Register X20, scope (0)
  ## Scoped Variable "q" uses Register X21, scope (0)
  ## Scoped Variable "m" uses Register X22, scope (0)
  ## Scoped Variable "q" uses Register X16, scope (0)
  ## Scoped Variable "m" uses Register X17, scope (0)
  ## Scoped Variable "vid" uses Register X18, scope (0)
  ## Scoped Variable "num_verts" uses Register X19, scope (0)
  ## Scoped Variable "outstanding" uses Register X20, scope (0)
  ## Scoped Variable "total_lanes" uses Register X21, scope (0)
  ## Scoped Variable "gv" uses Register X22, scope (0)
  ## Scoped Variable "cont" uses Register X23, scope (0)
  ## #define DEBUG
  
  ####################################################
  ###### Writing code for thread quality_master ######
  ####################################################
  # Writing code for event quality_master::init
  tranquality_master__init = efa.writeEvent('quality_master::init')
  tranquality_master__init.writeAction(f"__entry: addi X7 X23 0") 
  tranquality_master__init.writeAction(f"bneiu X14 0 __if_init_2_post") 
  tranquality_master__init.writeAction(f"__if_init_0_true: print 'Quality Start'") 
  tranquality_master__init.writeAction(f"movir X24 0") 
  tranquality_master__init.writeAction(f"movrl X24 0(X23) 0 8") 
  tranquality_master__init.writeAction(f"__if_init_2_post: movir X21 0") 
  tranquality_master__init.writeAction(f"addi X9 X22 0") 
  tranquality_master__init.writeAction(f"addi X1 X20 0") 
  tranquality_master__init.writeAction(f"addi X14 X19 0") 
  tranquality_master__init.writeAction(f"movir X24 1") 
  tranquality_master__init.writeAction(f"sl X24 X13 X24") 
  tranquality_master__init.writeAction(f"subi X8 X18 1") 
  tranquality_master__init.writeAction(f"sr X18 X13 X25") 
  tranquality_master__init.writeAction(f"addi X25 X18 1") 
  tranquality_master__init.writeAction(f"bneiu X18 1 __if_init_4_false") 
  tranquality_master__init.writeAction(f"__if_init_3_true: addi X8 X17 0") 
  ## start init 

  tranquality_master__init.writeAction(f"addi X7 X23 16") 
  tranquality_master__init.writeAction(f"movrl X10 0(X23) 0 8") 
  tranquality_master__init.writeAction(f"movrl X12 8(X23) 0 8") 
  tranquality_master__init.writeAction(f"movrl X11 16(X23) 0 8") 
  tranquality_master__init.writeAction(f"movrl X9 24(X23) 0 8") 
  tranquality_master__init.writeAction(f"addi X0 X25 0") 
  tranquality_master__init.writeAction(f"add X25 X8 X26") 
  tranquality_master__init.writeAction(f"__while_init_6_condition: ble X26 X25 __while_init_8_post") 
  tranquality_master__init.writeAction(f"__while_init_7_body: movir X27 0") 
  tranquality_master__init.writeAction(f"evlb X27 quality_worker__init") 
  tranquality_master__init.writeAction(f"evi X27 X27 255 4") 
  tranquality_master__init.writeAction(f"ev X27 X27 X25 X25 8") 
  tranquality_master__init.writeAction(f"send_wret X27 quality_master::init_done X23 4 X28") 
  tranquality_master__init.writeAction(f"addi X25 X25 1") 
  tranquality_master__init.writeAction(f"jmp __while_init_6_condition") 
  tranquality_master__init.writeAction(f"__while_init_8_post: jmp __if_init_5_post") 
  tranquality_master__init.writeAction(f"__if_init_4_false: addi X7 X23 16") 
  tranquality_master__init.writeAction(f"movrl X18 0(X23) 0 8") 
  tranquality_master__init.writeAction(f"movrl X9 8(X23) 0 8") 
  tranquality_master__init.writeAction(f"movrl X10 16(X23) 0 8") 
  tranquality_master__init.writeAction(f"movrl X11 24(X23) 0 8") 
  tranquality_master__init.writeAction(f"movrl X12 32(X23) 0 8") 
  tranquality_master__init.writeAction(f"movrl X13 40(X23) 0 8") 
  tranquality_master__init.writeAction(f"addi X14 X26 1") 
  tranquality_master__init.writeAction(f"movrl X26 48(X23) 0 8") 
  tranquality_master__init.writeAction(f"addi X0 X26 0") 
  tranquality_master__init.writeAction(f"addi X24 X17 0") 
  tranquality_master__init.writeAction(f"mul X18 X24 X25") 
  tranquality_master__init.writeAction(f"add X25 X26 X25") 
  tranquality_master__init.writeAction(f"__while_init_9_condition: ble X25 X26 __if_init_5_post") 
  tranquality_master__init.writeAction(f"__while_init_10_body: movir X27 0") 
  tranquality_master__init.writeAction(f"evlb X27 quality_master::init") 
  tranquality_master__init.writeAction(f"evi X27 X27 255 4") 
  tranquality_master__init.writeAction(f"ev X27 X27 X26 X26 8") 
  tranquality_master__init.writeAction(f"send_wret X27 quality_master::init_done X23 7 X28") 
  tranquality_master__init.writeAction(f"add X26 X18 X26") 
  tranquality_master__init.writeAction(f"jmp __while_init_9_condition") 
  tranquality_master__init.writeAction(f"__if_init_5_post: movir X16 0") 
  tranquality_master__init.writeAction(f"yield") 
  
  # Writing code for event quality_master::init_done
  tranquality_master__init_done = efa.writeEvent('quality_master::init_done')
  tranquality_master__init_done.writeAction(f"__entry: addi X16 X16 1") 
  tranquality_master__init_done.writeAction(f"fadd.64 X21 X9 X21") 
  ## print("%lu %lu", _q, q);

  tranquality_master__init_done.writeAction(f"bneu X16 X17 __if_init_done_2_post") 
  tranquality_master__init_done.writeAction(f"__if_init_done_0_true: movir X16 0") 
  tranquality_master__init_done.writeAction(f"bneiu X19 0 __if_init_done_4_false") 
  tranquality_master__init_done.writeAction(f"__if_init_done_3_true: fdiv.64 X21 X22 X21") 
  tranquality_master__init_done.writeAction(f"print 'Quality End'") 
  tranquality_master__init_done.writeAction(f"addi X7 X24 0") 
  tranquality_master__init_done.writeAction(f"movrl X21 8(X24) 0 8") 
  tranquality_master__init_done.writeAction(f"movir X23 1") 
  tranquality_master__init_done.writeAction(f"movrl X23 0(X24) 0 8") 
  tranquality_master__init_done.writeAction(f"yield_terminate") 
  tranquality_master__init_done.writeAction(f"jmp __if_init_done_2_post") 
  tranquality_master__init_done.writeAction(f"__if_init_done_4_false: movir X24 -1") 
  tranquality_master__init_done.writeAction(f"sri X24 X24 1") 
  tranquality_master__init_done.writeAction(f"sendr_wcont X20 X24 X0 X21") 
  tranquality_master__init_done.writeAction(f"yield_terminate") 
  tranquality_master__init_done.writeAction(f"__if_init_done_2_post: yield") 
  
  
  ####################################################
  ###### Writing code for thread quality_worker ######
  ####################################################
  # Writing code for event quality_worker::init
  tranquality_worker__init = efa.writeEvent('quality_worker::init')
  tranquality_worker__init.writeAction(f"__entry: addi X11 X17 0") 
  tranquality_worker__init.writeAction(f"movir X16 0") 
  tranquality_worker__init.writeAction(f"addi X0 X18 0") 
  tranquality_worker__init.writeAction(f"addi X10 X19 0") 
  tranquality_worker__init.writeAction(f"movir X20 0") 
  tranquality_worker__init.writeAction(f"addi X9 X21 0") 
  tranquality_worker__init.writeAction(f"addi X8 X22 40") 
  tranquality_worker__init.writeAction(f"addi X1 X23 0") 
  tranquality_worker__init.writeAction(f"addi X0 X18 0") 
  tranquality_worker__init.writeAction(f"__for_init_0_condition: ble X19 X18 __for_init_2_post") 
  tranquality_worker__init.writeAction(f"__for_init_1_body: sli X18 X24 7") 
  tranquality_worker__init.writeAction(f"add X22 X24 X24") 
  ## 16 words

  tranquality_worker__init.writeAction(f"send_dmlm_ld_wret X24 quality_worker::v_return 2 X25") 
  tranquality_worker__init.writeAction(f"addi X20 X20 1") 
  tranquality_worker__init.writeAction(f"movir X24 1024") 
  tranquality_worker__init.writeAction(f"bgt X24 X20 __if_init_5_post") 
  tranquality_worker__init.writeAction(f"__if_init_3_true: add X18 X9 X18") 
  tranquality_worker__init.writeAction(f"jmp __for_init_2_post") 
  tranquality_worker__init.writeAction(f"__if_init_5_post: add X18 X9 X18") 
  tranquality_worker__init.writeAction(f"jmp __for_init_0_condition") 
  tranquality_worker__init.writeAction(f"__for_init_2_post: bnei X20 0 __if_init_8_post") 
  tranquality_worker__init.writeAction(f"__if_init_6_true: movir X24 -1") 
  tranquality_worker__init.writeAction(f"sri X24 X24 1") 
  tranquality_worker__init.writeAction(f"sendr_wcont X23 X24 X0 X16") 
  tranquality_worker__init.writeAction(f"yield_terminate") 
  tranquality_worker__init.writeAction(f"__if_init_8_post: yield") 
  
  # Writing code for event quality_worker::v_return
  tranquality_worker__v_return = efa.writeEvent('quality_worker::v_return')
  tranquality_worker__v_return.writeAction(f"__entry: ble X19 X18 __if_v_return_1_false") 
  tranquality_worker__v_return.writeAction(f"__if_v_return_0_true: sli X18 X24 7") 
  tranquality_worker__v_return.writeAction(f"add X22 X24 X24") 
  ## 16 words

  tranquality_worker__v_return.writeAction(f"send_dmlm_ld_wret X24 quality_worker::v_return 2 X25") 
  tranquality_worker__v_return.writeAction(f"add X18 X21 X18") 
  tranquality_worker__v_return.writeAction(f"jmp __if_v_return_2_post") 
  tranquality_worker__v_return.writeAction(f"__if_v_return_1_false: subi X20 X20 1") 
  tranquality_worker__v_return.writeAction(f"__if_v_return_2_post: blei X8 0 __if_v_return_5_post") 
  tranquality_worker__v_return.writeAction(f"__if_v_return_3_true: fmul.64 X8 X8 X24") 
  tranquality_worker__v_return.writeAction(f"fdiv.64 X24 X17 X24") 
  tranquality_worker__v_return.writeAction(f"fsub.64 X9 X24 X24") 
  tranquality_worker__v_return.writeAction(f"fadd.64 X16 X24 X16") 
  tranquality_worker__v_return.writeAction(f"__if_v_return_5_post: bnei X20 0 __if_v_return_8_post") 
  tranquality_worker__v_return.writeAction(f"__if_v_return_6_true: movir X24 -1") 
  tranquality_worker__v_return.writeAction(f"sri X24 X24 1") 
  tranquality_worker__v_return.writeAction(f"sendr_wcont X23 X24 X0 X16") 
  tranquality_worker__v_return.writeAction(f"yield_terminate") 
  tranquality_worker__v_return.writeAction(f"__if_v_return_8_post: yield") 
  