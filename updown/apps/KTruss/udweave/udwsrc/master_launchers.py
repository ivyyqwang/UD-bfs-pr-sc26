from linker.EFAProgram import efaProgram

## UDWeave version: unknown

## Global constants

@efaProgram
def EFA_master_launchers(efa):
  efa.code_level = 'machine'
  state0 = efa.State("udweave_init") #Only one state code 
  efa.add_initId(state0.state_id)
  ## Static declarations
  ## Scoped Variable "num_threads_active" uses Register X16, scope (0)
  ## Scoped Variable "master_dram_tail_ptr" uses Register X17, scope (0)
  ## Scoped Variable "master_dram_head_ptr" uses Register X18, scope (0)
  ## Scoped Variable "lmbuff" uses Register X19, scope (0)
  ## Scoped Variable "num_combine" uses Register X20, scope (0)
  ## Scoped Variable "num_v" uses Register X21, scope (0)
  ## Scoped Variable "master_dram_write_ptr" uses Register X22, scope (0)
  ## Scoped Variable "count" uses Register X23, scope (0)
  ## Scoped Variable "tc" uses Register X24, scope (0)
  ## Scoped Variable "num_int" uses Register X25, scope (0)
  ## This is all metadata information
  ## #define DEBUG
  ## This is all metadata information
  ## Each threads in the same lane shared the following scratchpad
  ## #define TOP_TC_OUTPUT 1
  ## send buffer 4 - 13 (9 words)
  ## #define NUM_WRITE 16
  ## #define NUM_INT 18
  ## master, intersection launcher offsets
  ## Each thread's own private scratchpad size: [(THREAD_STATUS << 3) + TID * THREAD_LM_SIZE, (THREAD_STATUS << 3) + (TID+1) * THREAD_LM_SIZE]
  
  #####################################################
  ###### Writing code for thread master_launcher ######
  #####################################################
  # Writing code for event master_launcher::init
  tranmaster_launcher__init = efa.writeEvent('master_launcher::init')
  tranmaster_launcher__init.writeAction(f"__entry: mul X0 X11 X26") 
  tranmaster_launcher__init.writeAction(f"add X10 X26 X26") 
  tranmaster_launcher__init.writeAction(f"movir X27 0") 
  tranmaster_launcher__init.writeAction(f"evlb X27 intersection_launcher__intersection_init") 
  tranmaster_launcher__init.writeAction(f"evi X27 X27 255 4") 
  tranmaster_launcher__init.writeAction(f"ev X27 X27 X0 X0 8") 
  tranmaster_launcher__init.writeAction(f"sendr_wcont X27 X1 X26 X11") 
  tranmaster_launcher__init.writeAction(f"movir X27 65504") 
  tranmaster_launcher__init.writeAction(f"add X7 X27 X19") 
  tranmaster_launcher__init.writeAction(f"sri X2 X27 24") 
  tranmaster_launcher__init.writeAction(f"andi X27 X27 255") 
  tranmaster_launcher__init.writeAction(f"movrl X27 0(X19) 0 8") 
  tranmaster_launcher__init.writeAction(f"addi X7 X19 0") 
  tranmaster_launcher__init.writeAction(f"movir X27 4") 
  tranmaster_launcher__init.writeAction(f"movrl X27 136(X19) 0 8") 
  tranmaster_launcher__init.writeAction(f"movrl X12 16(X19) 0 8") 
  tranmaster_launcher__init.writeAction(f"subi X13 X27 1") 
  tranmaster_launcher__init.writeAction(f"movrl X27 152(X19) 0 8") 
  tranmaster_launcher__init.writeAction(f"movrl X9 120(X19) 0 8") 
  ## print("[DEBUG][NWID %lu] NUM_LANES_TOTAL:%lu", NETID, num_lanes_total);

  tranmaster_launcher__init.writeAction(f"addi X7 X19 0") 
  tranmaster_launcher__init.writeAction(f"subi X14 X27 1") 
  tranmaster_launcher__init.writeAction(f"movrl X27 0(X19) 0 8") 
  tranmaster_launcher__init.writeAction(f"movir X24 0") 
  tranmaster_launcher__init.writeAction(f"movir X25 0") 
  ## print("[DEBUG][NWID %lu] cache_len:%lu", NETID, cache_len);

  tranmaster_launcher__init.writeAction(f"mul X9 X15 X26") 
  tranmaster_launcher__init.writeAction(f"mul X26 X0 X26") 
  tranmaster_launcher__init.writeAction(f"add X8 X26 X18") 
  tranmaster_launcher__init.writeAction(f"addi X7 X19 160") 
  tranmaster_launcher__init.writeAction(f"movir X27 0") 
  tranmaster_launcher__init.writeAction(f"movrl X27 8(X19) 0 8") 
  tranmaster_launcher__init.writeAction(f"bnei X15 1 __if_init_1_false") 
  tranmaster_launcher__init.writeAction(f"__if_init_0_true: movir X20 1") 
  tranmaster_launcher__init.writeAction(f"sli X20 X20 32") 
  tranmaster_launcher__init.writeAction(f"jmp __if_init_2_post") 
  tranmaster_launcher__init.writeAction(f"__if_init_1_false: addi X15 X20 0") 
  tranmaster_launcher__init.writeAction(f"add X3 X26 X22") 
  tranmaster_launcher__init.writeAction(f"movir X27 65256") 
  tranmaster_launcher__init.writeAction(f"add X7 X27 X27") 
  tranmaster_launcher__init.writeAction(f"movrl X22 0(X27) 0 8") 
  tranmaster_launcher__init.writeAction(f"mul X0 X20 X26") 
  tranmaster_launcher__init.writeAction(f"movrl X26 24(X19) 0 8") 
  tranmaster_launcher__init.writeAction(f"add X18 X9 X27") 
  tranmaster_launcher__init.writeAction(f"movrl X27 16(X19) 0 8") 
  tranmaster_launcher__init.writeAction(f"__if_init_2_post: movir X21 0") 
  tranmaster_launcher__init.writeAction(f"movir X16 0") 
  tranmaster_launcher__init.writeAction(f"yield") 
  
  # Writing code for event master_launcher::launch_v
  tranmaster_launcher__launch_v = efa.writeEvent('master_launcher::launch_v')
  tranmaster_launcher__launch_v.writeAction(f"__entry: sari X20 X26 32") 
  tranmaster_launcher__launch_v.writeAction(f"bnei X26 1 __if_launch_v_1_false") 
  ## no compaction

  tranmaster_launcher__launch_v.writeAction(f"__if_launch_v_0_true: send_dmlm_ld_wret X18 master_launcher::read_master_dram_length 1 X26") 
  tranmaster_launcher__launch_v.writeAction(f"addi X18 X18 8") 
  tranmaster_launcher__launch_v.writeAction(f"jmp __if_launch_v_2_post") 
  tranmaster_launcher__launch_v.writeAction(f"__if_launch_v_1_false: movlr 24(X19) X26 0 8") 
  tranmaster_launcher__launch_v.writeAction(f"movir X27 0") 
  tranmaster_launcher__launch_v.writeAction(f"evlb X27 master_launcher::read_remote_data") 
  tranmaster_launcher__launch_v.writeAction(f"evi X27 X27 255 4") 
  tranmaster_launcher__launch_v.writeAction(f"ev X27 X27 X26 X26 8") 
  tranmaster_launcher__launch_v.writeAction(f"sendr_wret X27 master_launcher::read_master_dram_length_compact X18 X18 X26") 
  tranmaster_launcher__launch_v.writeAction(f"addi X18 X18 8") 
  tranmaster_launcher__launch_v.writeAction(f"addi X22 X22 8") 
  tranmaster_launcher__launch_v.writeAction(f"addi X18 X17 0") 
  tranmaster_launcher__launch_v.writeAction(f"sli X20 X20 1") 
  tranmaster_launcher__launch_v.writeAction(f"subi X20 X20 1") 
  tranmaster_launcher__launch_v.writeAction(f"movir X23 1") 
  tranmaster_launcher__launch_v.writeAction(f"__if_launch_v_2_post: movrl X1 0(X19) 0 8") 
  tranmaster_launcher__launch_v.writeAction(f"yield") 
  
  # Writing code for event master_launcher::read_master_dram_length
  tranmaster_launcher__read_master_dram_length = efa.writeEvent('master_launcher::read_master_dram_length')
  tranmaster_launcher__read_master_dram_length.writeAction(f"__entry: movir X27 1") 
  tranmaster_launcher__read_master_dram_length.writeAction(f"movrl X27 8(X19) 0 8") 
  tranmaster_launcher__read_master_dram_length.writeAction(f"add X21 X8 X21") 
  tranmaster_launcher__read_master_dram_length.writeAction(f"bnei X8 0 __if_read_master_dram_length_2_post") 
  tranmaster_launcher__read_master_dram_length.writeAction(f"__if_read_master_dram_length_0_true: movir X27 2") 
  tranmaster_launcher__read_master_dram_length.writeAction(f"movrl X27 8(X19) 0 8") 
  tranmaster_launcher__read_master_dram_length.writeAction(f"movir X27 65504") 
  tranmaster_launcher__read_master_dram_length.writeAction(f"add X7 X27 X27") 
  tranmaster_launcher__read_master_dram_length.writeAction(f"movir X26 -1") 
  tranmaster_launcher__read_master_dram_length.writeAction(f"movrl X26 0(X27) 0 8") 
  tranmaster_launcher__read_master_dram_length.writeAction(f"movlr 0(X19) X27 0 8") 
  tranmaster_launcher__read_master_dram_length.writeAction(f"movir X26 -1") 
  tranmaster_launcher__read_master_dram_length.writeAction(f"sri X26 X26 1") 
  tranmaster_launcher__read_master_dram_length.writeAction(f"sendr_wcont X27 X26 X21 X0") 
  tranmaster_launcher__read_master_dram_length.writeAction(f"yield_terminate") 
  ## print("[DEBUG][NWID %lu] <read_master_dram_length> length = %lu, num_combine = %lu, addr = 0x%lX", NETID, length, num_combine, read_addr);

  tranmaster_launcher__read_master_dram_length.writeAction(f"__if_read_master_dram_length_2_post: sli X8 X27 3") 
  tranmaster_launcher__read_master_dram_length.writeAction(f"add X18 X27 X17") 
  tranmaster_launcher__read_master_dram_length.writeAction(f"addi X7 X26 0") 
  tranmaster_launcher__read_master_dram_length.writeAction(f"movlr 136(X26) X26 0 8") 
  tranmaster_launcher__read_master_dram_length.writeAction(f"add X16 X8 X27") 
  tranmaster_launcher__read_master_dram_length.writeAction(f"ble X26 X27 __if_read_master_dram_length_5_post") 
  tranmaster_launcher__read_master_dram_length.writeAction(f"__if_read_master_dram_length_3_true: addi X27 X26 0") 
  tranmaster_launcher__read_master_dram_length.writeAction(f"__if_read_master_dram_length_5_post: addi X17 X22 0") 
  tranmaster_launcher__read_master_dram_length.writeAction(f"__while_read_master_dram_length_6_condition: ble X26 X16 __while_read_master_dram_length_8_post") 
  tranmaster_launcher__read_master_dram_length.writeAction(f"__while_read_master_dram_length_7_body: send_dmlm_ld_wret X18 master_launcher::receive_dram 1 X28") 
  tranmaster_launcher__read_master_dram_length.writeAction(f"addi X18 X18 8") 
  tranmaster_launcher__read_master_dram_length.writeAction(f"addi X16 X16 1") 
  ## num_v = num_v + 1;

  tranmaster_launcher__read_master_dram_length.writeAction(f"jmp __while_read_master_dram_length_6_condition") 
  tranmaster_launcher__read_master_dram_length.writeAction(f"__while_read_master_dram_length_8_post: bneu X18 X17 __if_read_master_dram_length_11_post") 
  tranmaster_launcher__read_master_dram_length.writeAction(f"__if_read_master_dram_length_9_true: movir X27 2") 
  tranmaster_launcher__read_master_dram_length.writeAction(f"movrl X27 8(X19) 0 8") 
  tranmaster_launcher__read_master_dram_length.writeAction(f"yield") 
  tranmaster_launcher__read_master_dram_length.writeAction(f"__if_read_master_dram_length_11_post: yield") 
  
  # Writing code for event master_launcher::receive_dram
  tranmaster_launcher__receive_dram = efa.writeEvent('master_launcher::receive_dram')
  ## #ifdef DEBUG

  ## print("[DEBUG][NWID %lu] <receive_dram> received %lu, addr = 0x%lX", NETID, v1, addr);

  ## #endif

  tranmaster_launcher__receive_dram.writeAction(f"__entry: movir X27 0") 
  tranmaster_launcher__receive_dram.writeAction(f"evlb X27 vertex_master__launch") 
  tranmaster_launcher__receive_dram.writeAction(f"evi X27 X27 255 4") 
  tranmaster_launcher__receive_dram.writeAction(f"ev X27 X27 X0 X0 8") 
  tranmaster_launcher__receive_dram.writeAction(f"addi X7 X26 0") 
  tranmaster_launcher__receive_dram.writeAction(f"movlr 16(X26) X26 0 8") 
  tranmaster_launcher__receive_dram.writeAction(f"sendr_wret X27 master_launcher::vertex_term X26 X8 X28") 
  tranmaster_launcher__receive_dram.writeAction(f"yield") 
  
  # Writing code for event master_launcher::read_remote_data
  tranmaster_launcher__read_remote_data = efa.writeEvent('master_launcher::read_remote_data')
  tranmaster_launcher__read_remote_data.writeAction(f"__entry: send_dmlm_ld X8 X1 1") 
  tranmaster_launcher__read_remote_data.writeAction(f"yield_terminate") 
  
  # Writing code for event master_launcher::read_master_dram_length_compact
  tranmaster_launcher__read_master_dram_length_compact = efa.writeEvent('master_launcher::read_master_dram_length_compact')
  ## unsigned long temp = master_dram_tail_ptr;

  ## unsigned long temp2 = master_dram_head_ptr;

  tranmaster_launcher__read_master_dram_length_compact.writeAction(f"__entry: movir X27 1") 
  tranmaster_launcher__read_master_dram_length_compact.writeAction(f"movrl X27 8(X19) 0 8") 
  tranmaster_launcher__read_master_dram_length_compact.writeAction(f"add X21 X8 X21") 
  tranmaster_launcher__read_master_dram_length_compact.writeAction(f"subi X20 X20 1") 
  tranmaster_launcher__read_master_dram_length_compact.writeAction(f"bnei X8 0 __if_read_master_dram_length_compact_2_post") 
  tranmaster_launcher__read_master_dram_length_compact.writeAction(f"__if_read_master_dram_length_compact_0_true: bnei X20 0 __if_read_master_dram_length_compact_4_false") 
  tranmaster_launcher__read_master_dram_length_compact.writeAction(f"__if_read_master_dram_length_compact_3_true: movir X27 2") 
  tranmaster_launcher__read_master_dram_length_compact.writeAction(f"movrl X27 8(X19) 0 8") 
  tranmaster_launcher__read_master_dram_length_compact.writeAction(f"bnei X16 0 __if_read_master_dram_length_compact_8_post") 
  tranmaster_launcher__read_master_dram_length_compact.writeAction(f"__if_read_master_dram_length_compact_6_true: movir X27 65256") 
  tranmaster_launcher__read_master_dram_length_compact.writeAction(f"add X7 X27 X27") 
  tranmaster_launcher__read_master_dram_length_compact.writeAction(f"movlr 0(X27) X27 0 8") 
  tranmaster_launcher__read_master_dram_length_compact.writeAction(f"sendr_dmlm_wret X27 master_launcher::write_return X21 X26") 
  ## print("[DEBUG][NWID %lu] length = %lu, addr = 0x%lX", NETID, num_v, addr);

  tranmaster_launcher__read_master_dram_length_compact.writeAction(f"yield") 
  tranmaster_launcher__read_master_dram_length_compact.writeAction(f"__if_read_master_dram_length_compact_8_post: jmp __if_read_master_dram_length_compact_5_post") 
  tranmaster_launcher__read_master_dram_length_compact.writeAction(f"__if_read_master_dram_length_compact_4_false: movlr 16(X19) X27 0 8") 
  tranmaster_launcher__read_master_dram_length_compact.writeAction(f"movlr 24(X19) X26 0 8") 
  tranmaster_launcher__read_master_dram_length_compact.writeAction(f"addi X26 X26 1") 
  tranmaster_launcher__read_master_dram_length_compact.writeAction(f"movir X28 0") 
  tranmaster_launcher__read_master_dram_length_compact.writeAction(f"evlb X28 master_launcher::read_remote_data") 
  tranmaster_launcher__read_master_dram_length_compact.writeAction(f"evi X28 X28 255 4") 
  tranmaster_launcher__read_master_dram_length_compact.writeAction(f"ev X28 X28 X26 X26 8") 
  tranmaster_launcher__read_master_dram_length_compact.writeAction(f"sendr_wret X28 master_launcher::read_master_dram_length_compact X27 X27 X29") 
  tranmaster_launcher__read_master_dram_length_compact.writeAction(f"movrl X26 24(X19) 0 8") 
  tranmaster_launcher__read_master_dram_length_compact.writeAction(f"addi X27 X18 8") 
  tranmaster_launcher__read_master_dram_length_compact.writeAction(f"addi X18 X17 0") 
  tranmaster_launcher__read_master_dram_length_compact.writeAction(f"addi X7 X26 0") 
  tranmaster_launcher__read_master_dram_length_compact.writeAction(f"movlr 120(X26) X28 0 8") 
  tranmaster_launcher__read_master_dram_length_compact.writeAction(f"add X27 X28 X28") 
  tranmaster_launcher__read_master_dram_length_compact.writeAction(f"movrl X28 16(X19) 0 8") 
  tranmaster_launcher__read_master_dram_length_compact.writeAction(f"subi X20 X20 1") 
  tranmaster_launcher__read_master_dram_length_compact.writeAction(f"yield") 
  tranmaster_launcher__read_master_dram_length_compact.writeAction(f"__if_read_master_dram_length_compact_5_post: yield") 
  ## print("[DEBUG][NWID %lu] <read_master_dram_length> length = %lu, num_combine = %lu, addr = 0x%lX", NETID, length, num_combine, read_addr);

  tranmaster_launcher__read_master_dram_length_compact.writeAction(f"__if_read_master_dram_length_compact_2_post: sli X8 X28 3") 
  tranmaster_launcher__read_master_dram_length_compact.writeAction(f"add X18 X28 X17") 
  tranmaster_launcher__read_master_dram_length_compact.writeAction(f"addi X7 X27 0") 
  tranmaster_launcher__read_master_dram_length_compact.writeAction(f"movlr 136(X27) X26 0 8") 
  tranmaster_launcher__read_master_dram_length_compact.writeAction(f"add X16 X8 X28") 
  tranmaster_launcher__read_master_dram_length_compact.writeAction(f"ble X26 X28 __if_read_master_dram_length_compact_11_post") 
  tranmaster_launcher__read_master_dram_length_compact.writeAction(f"__if_read_master_dram_length_compact_9_true: addi X28 X26 0") 
  tranmaster_launcher__read_master_dram_length_compact.writeAction(f"__if_read_master_dram_length_compact_11_post: movlr 24(X19) X29 0 8") 
  tranmaster_launcher__read_master_dram_length_compact.writeAction(f"movir X28 0") 
  tranmaster_launcher__read_master_dram_length_compact.writeAction(f"evlb X28 master_launcher::read_remote_data") 
  tranmaster_launcher__read_master_dram_length_compact.writeAction(f"evi X28 X28 255 4") 
  tranmaster_launcher__read_master_dram_length_compact.writeAction(f"ev X28 X28 X29 X29 8") 
  tranmaster_launcher__read_master_dram_length_compact.writeAction(f"__while_read_master_dram_length_compact_12_condition: ble X26 X16 __while_read_master_dram_length_compact_14_post") 
  tranmaster_launcher__read_master_dram_length_compact.writeAction(f"__while_read_master_dram_length_compact_13_body: sendr_wret X28 master_launcher::receive_dram_remote X18 X18 X30") 
  tranmaster_launcher__read_master_dram_length_compact.writeAction(f"addi X18 X18 8") 
  tranmaster_launcher__read_master_dram_length_compact.writeAction(f"addi X16 X16 1") 
  ## num_v = num_v + 1;

  tranmaster_launcher__read_master_dram_length_compact.writeAction(f"jmp __while_read_master_dram_length_compact_12_condition") 
  tranmaster_launcher__read_master_dram_length_compact.writeAction(f"__while_read_master_dram_length_compact_14_post: bneu X18 X17 __if_read_master_dram_length_compact_17_post") 
  tranmaster_launcher__read_master_dram_length_compact.writeAction(f"__if_read_master_dram_length_compact_15_true: bnei X20 0 __if_read_master_dram_length_compact_19_false") 
  tranmaster_launcher__read_master_dram_length_compact.writeAction(f"__if_read_master_dram_length_compact_18_true: movir X28 2") 
  tranmaster_launcher__read_master_dram_length_compact.writeAction(f"movrl X28 8(X19) 0 8") 
  tranmaster_launcher__read_master_dram_length_compact.writeAction(f"yield") 
  tranmaster_launcher__read_master_dram_length_compact.writeAction(f"jmp __if_read_master_dram_length_compact_17_post") 
  tranmaster_launcher__read_master_dram_length_compact.writeAction(f"__if_read_master_dram_length_compact_19_false: movlr 16(X19) X28 0 8") 
  tranmaster_launcher__read_master_dram_length_compact.writeAction(f"addi X29 X29 1") 
  tranmaster_launcher__read_master_dram_length_compact.writeAction(f"movrl X29 24(X19) 0 8") 
  tranmaster_launcher__read_master_dram_length_compact.writeAction(f"movir X26 0") 
  tranmaster_launcher__read_master_dram_length_compact.writeAction(f"evlb X26 master_launcher::read_remote_data") 
  tranmaster_launcher__read_master_dram_length_compact.writeAction(f"evi X26 X26 255 4") 
  tranmaster_launcher__read_master_dram_length_compact.writeAction(f"ev X26 X26 X29 X29 8") 
  tranmaster_launcher__read_master_dram_length_compact.writeAction(f"sendr_wret X26 master_launcher::read_master_dram_length_compact X28 X28 X30") 
  tranmaster_launcher__read_master_dram_length_compact.writeAction(f"addi X28 X18 8") 
  tranmaster_launcher__read_master_dram_length_compact.writeAction(f"addi X18 X17 0") 
  tranmaster_launcher__read_master_dram_length_compact.writeAction(f"addi X7 X27 0") 
  tranmaster_launcher__read_master_dram_length_compact.writeAction(f"movlr 120(X27) X29 0 8") 
  tranmaster_launcher__read_master_dram_length_compact.writeAction(f"add X28 X29 X29") 
  tranmaster_launcher__read_master_dram_length_compact.writeAction(f"movrl X29 16(X19) 0 8") 
  tranmaster_launcher__read_master_dram_length_compact.writeAction(f"subi X20 X20 1") 
  tranmaster_launcher__read_master_dram_length_compact.writeAction(f"yield") 
  tranmaster_launcher__read_master_dram_length_compact.writeAction(f"__if_read_master_dram_length_compact_17_post: yield") 
  
  # Writing code for event master_launcher::receive_dram_remote
  tranmaster_launcher__receive_dram_remote = efa.writeEvent('master_launcher::receive_dram_remote')
  ## #ifdef DEBUG

  tranmaster_launcher__receive_dram_remote.writeAction(f"__entry: bnei X8 5 __if_receive_dram_remote_2_post") 
  tranmaster_launcher__receive_dram_remote.writeAction(f"__if_receive_dram_remote_0_true: movlr 24(X19) X28 0 8") 
  tranmaster_launcher__receive_dram_remote.writeAction(f"print '[DEBUG][NWID %lu] <receive_dram_remote> received %lu, addr = 0x%lX, netid %lu, master = 0x%lx, 0x%lx' X0 X8 X9 X28 X18 X17") 
  ## #endif

  tranmaster_launcher__receive_dram_remote.writeAction(f"__if_receive_dram_remote_2_post: movir X28 0") 
  tranmaster_launcher__receive_dram_remote.writeAction(f"evlb X28 vertex_master__launch") 
  tranmaster_launcher__receive_dram_remote.writeAction(f"evi X28 X28 255 4") 
  tranmaster_launcher__receive_dram_remote.writeAction(f"ev X28 X28 X0 X0 8") 
  tranmaster_launcher__receive_dram_remote.writeAction(f"addi X7 X29 0") 
  tranmaster_launcher__receive_dram_remote.writeAction(f"movlr 16(X29) X29 0 8") 
  tranmaster_launcher__receive_dram_remote.writeAction(f"sendr_wret X28 master_launcher::vertex_term X29 X8 X26") 
  tranmaster_launcher__receive_dram_remote.writeAction(f"addi X23 X23 1") 
  tranmaster_launcher__receive_dram_remote.writeAction(f"sendr_dmlm_wret X22 master_launcher::write_return X8 X28") 
  tranmaster_launcher__receive_dram_remote.writeAction(f"addi X22 X22 8") 
  tranmaster_launcher__receive_dram_remote.writeAction(f"yield") 
  
  # Writing code for event master_launcher::vertex_term
  tranmaster_launcher__vertex_term = efa.writeEvent('master_launcher::vertex_term')
  ## vertex thread terminated

  tranmaster_launcher__vertex_term.writeAction(f"__entry: subi X16 X16 1") 
  tranmaster_launcher__vertex_term.writeAction(f"add X25 X8 X25") 
  tranmaster_launcher__vertex_term.writeAction(f"sari X20 X28 32") 
  tranmaster_launcher__vertex_term.writeAction(f"bnei X28 1 __if_vertex_term_2_post") 
  ## no compact

  tranmaster_launcher__vertex_term.writeAction(f"__if_vertex_term_0_true: bneu X18 X17 __if_vertex_term_5_post") 
  ## head == tail So nothing more to launch! 

  tranmaster_launcher__vertex_term.writeAction(f"__if_vertex_term_3_true: movir X29 2") 
  tranmaster_launcher__vertex_term.writeAction(f"movrl X29 8(X19) 0 8") 
  tranmaster_launcher__vertex_term.writeAction(f"bnei X16 0 __if_vertex_term_8_post") 
  tranmaster_launcher__vertex_term.writeAction(f"__if_vertex_term_6_true: movlr 0(X19) X29 0 8") 
  tranmaster_launcher__vertex_term.writeAction(f"movir X26 -1") 
  tranmaster_launcher__vertex_term.writeAction(f"sri X26 X26 1") 
  tranmaster_launcher__vertex_term.writeAction(f"sendr_wcont X29 X26 X21 X0") 
  tranmaster_launcher__vertex_term.writeAction(f"__if_vertex_term_8_post: yield") 
  tranmaster_launcher__vertex_term.writeAction(f"__if_vertex_term_5_post: addi X7 X29 0") 
  tranmaster_launcher__vertex_term.writeAction(f"movlr 136(X29) X28 0 8") 
  tranmaster_launcher__vertex_term.writeAction(f"__while_vertex_term_9_condition: clt X16 X28 X29") 
  tranmaster_launcher__vertex_term.writeAction(f"ceq X18 X17 X26") 
  tranmaster_launcher__vertex_term.writeAction(f"xori X26 X26 1") 
  tranmaster_launcher__vertex_term.writeAction(f"and X29 X26 X29") 
  tranmaster_launcher__vertex_term.writeAction(f"beqi X29 0 __while_vertex_term_11_post") 
  tranmaster_launcher__vertex_term.writeAction(f"__while_vertex_term_10_body: send_dmlm_ld_wret X18 master_launcher::receive_dram 1 X29") 
  tranmaster_launcher__vertex_term.writeAction(f"addi X18 X18 8") 
  tranmaster_launcher__vertex_term.writeAction(f"addi X16 X16 1") 
  tranmaster_launcher__vertex_term.writeAction(f"jmp __while_vertex_term_9_condition") 
  tranmaster_launcher__vertex_term.writeAction(f"__while_vertex_term_11_post: yield") 
  tranmaster_launcher__vertex_term.writeAction(f"__if_vertex_term_2_post: bneu X18 X17 __if_vertex_term_14_post") 
  ## head == tail So nothing more to launch! 

  tranmaster_launcher__vertex_term.writeAction(f"__if_vertex_term_12_true: bnei X20 0 __if_vertex_term_17_post") 
  tranmaster_launcher__vertex_term.writeAction(f"__if_vertex_term_15_true: movir X29 2") 
  tranmaster_launcher__vertex_term.writeAction(f"movrl X29 8(X19) 0 8") 
  tranmaster_launcher__vertex_term.writeAction(f"bnei X16 0 __if_vertex_term_20_post") 
  tranmaster_launcher__vertex_term.writeAction(f"__if_vertex_term_18_true: movir X29 65256") 
  tranmaster_launcher__vertex_term.writeAction(f"add X7 X29 X29") 
  tranmaster_launcher__vertex_term.writeAction(f"movlr 0(X29) X29 0 8") 
  tranmaster_launcher__vertex_term.writeAction(f"sendr_dmlm_wret X29 master_launcher::write_return X21 X26") 
  ## print("[DEBUG][NWID %lu] length = %lu, addr = 0x%lX", NETID, num_v, addr);

  tranmaster_launcher__vertex_term.writeAction(f"__if_vertex_term_20_post: yield") 
  tranmaster_launcher__vertex_term.writeAction(f"__if_vertex_term_17_post: yield") 
  ## Check if there's stuff in memory

  tranmaster_launcher__vertex_term.writeAction(f"__if_vertex_term_14_post: addi X7 X29 0") 
  tranmaster_launcher__vertex_term.writeAction(f"movlr 24(X19) X28 0 8") 
  tranmaster_launcher__vertex_term.writeAction(f"movir X26 0") 
  tranmaster_launcher__vertex_term.writeAction(f"evlb X26 master_launcher::read_remote_data") 
  tranmaster_launcher__vertex_term.writeAction(f"evi X26 X26 255 4") 
  tranmaster_launcher__vertex_term.writeAction(f"ev X26 X26 X28 X28 8") 
  tranmaster_launcher__vertex_term.writeAction(f"movlr 136(X29) X28 0 8") 
  tranmaster_launcher__vertex_term.writeAction(f"__while_vertex_term_21_condition: ceq X18 X17 X27") 
  tranmaster_launcher__vertex_term.writeAction(f"xori X27 X27 1") 
  tranmaster_launcher__vertex_term.writeAction(f"clt X16 X28 X30") 
  tranmaster_launcher__vertex_term.writeAction(f"and X27 X30 X27") 
  tranmaster_launcher__vertex_term.writeAction(f"beqi X27 0 __while_vertex_term_23_post") 
  tranmaster_launcher__vertex_term.writeAction(f"__while_vertex_term_22_body: sendr_wret X26 master_launcher::receive_dram_remote X18 X18 X27") 
  tranmaster_launcher__vertex_term.writeAction(f"addi X18 X18 8") 
  tranmaster_launcher__vertex_term.writeAction(f"addi X16 X16 1") 
  ## num_v = num_v + 1;

  tranmaster_launcher__vertex_term.writeAction(f"jmp __while_vertex_term_21_condition") 
  tranmaster_launcher__vertex_term.writeAction(f"__while_vertex_term_23_post: bneu X18 X17 __if_vertex_term_26_post") 
  tranmaster_launcher__vertex_term.writeAction(f"__if_vertex_term_24_true: bnei X20 0 __if_vertex_term_28_false") 
  tranmaster_launcher__vertex_term.writeAction(f"__if_vertex_term_27_true: movir X28 2") 
  tranmaster_launcher__vertex_term.writeAction(f"movrl X28 8(X19) 0 8") 
  tranmaster_launcher__vertex_term.writeAction(f"yield") 
  tranmaster_launcher__vertex_term.writeAction(f"jmp __if_vertex_term_26_post") 
  tranmaster_launcher__vertex_term.writeAction(f"__if_vertex_term_28_false: andi X20 X28 1") 
  tranmaster_launcher__vertex_term.writeAction(f"bnei X28 0 __if_vertex_term_26_post") 
  tranmaster_launcher__vertex_term.writeAction(f"__if_vertex_term_30_true: movlr 16(X19) X28 0 8") 
  tranmaster_launcher__vertex_term.writeAction(f"movlr 24(X19) X27 0 8") 
  tranmaster_launcher__vertex_term.writeAction(f"addi X27 X27 1") 
  tranmaster_launcher__vertex_term.writeAction(f"movir X26 0") 
  tranmaster_launcher__vertex_term.writeAction(f"evlb X26 master_launcher::read_remote_data") 
  tranmaster_launcher__vertex_term.writeAction(f"evi X26 X26 255 4") 
  tranmaster_launcher__vertex_term.writeAction(f"ev X26 X26 X27 X27 8") 
  tranmaster_launcher__vertex_term.writeAction(f"sendr_wret X26 master_launcher::read_master_dram_length_compact X28 X28 X30") 
  tranmaster_launcher__vertex_term.writeAction(f"movrl X27 24(X19) 0 8") 
  tranmaster_launcher__vertex_term.writeAction(f"addi X28 X18 8") 
  tranmaster_launcher__vertex_term.writeAction(f"addi X18 X17 0") 
  tranmaster_launcher__vertex_term.writeAction(f"addi X7 X29 0") 
  tranmaster_launcher__vertex_term.writeAction(f"movlr 120(X29) X26 0 8") 
  tranmaster_launcher__vertex_term.writeAction(f"add X28 X26 X26") 
  tranmaster_launcher__vertex_term.writeAction(f"movrl X26 16(X19) 0 8") 
  tranmaster_launcher__vertex_term.writeAction(f"subi X20 X20 1") 
  tranmaster_launcher__vertex_term.writeAction(f"yield") 
  ## if(NETID == 0){

  ##     print("[DEBUG][NWID %lu] <vertex_term> test 0x%lx 0x%lx %lu %lu", NETID, master_dram_head_ptr, master_dram_tail_ptr, num_threads_active , num_threads_total);

  ## }

  tranmaster_launcher__vertex_term.writeAction(f"__if_vertex_term_26_post: yield") 
  
  # Writing code for event master_launcher::relaunch
  tranmaster_launcher__relaunch = efa.writeEvent('master_launcher::relaunch')
  tranmaster_launcher__relaunch.writeAction(f"__entry: addi X7 X29 0") 
  tranmaster_launcher__relaunch.writeAction(f"sari X20 X26 32") 
  tranmaster_launcher__relaunch.writeAction(f"bnei X26 1 __if_relaunch_2_post") 
  ## no compact

  tranmaster_launcher__relaunch.writeAction(f"__if_relaunch_0_true: movlr 136(X29) X26 0 8") 
  tranmaster_launcher__relaunch.writeAction(f"__while_relaunch_3_condition: clt X16 X26 X28") 
  tranmaster_launcher__relaunch.writeAction(f"ceq X18 X17 X27") 
  tranmaster_launcher__relaunch.writeAction(f"xori X27 X27 1") 
  tranmaster_launcher__relaunch.writeAction(f"and X28 X27 X28") 
  tranmaster_launcher__relaunch.writeAction(f"beqi X28 0 __while_relaunch_5_post") 
  tranmaster_launcher__relaunch.writeAction(f"__while_relaunch_4_body: send_dmlm_ld_wret X18 master_launcher::receive_dram 1 X28") 
  tranmaster_launcher__relaunch.writeAction(f"addi X18 X18 8") 
  tranmaster_launcher__relaunch.writeAction(f"addi X16 X16 1") 
  tranmaster_launcher__relaunch.writeAction(f"jmp __while_relaunch_3_condition") 
  tranmaster_launcher__relaunch.writeAction(f"__while_relaunch_5_post: yield") 
  tranmaster_launcher__relaunch.writeAction(f"__if_relaunch_2_post: movlr 24(X19) X26 0 8") 
  tranmaster_launcher__relaunch.writeAction(f"movir X28 0") 
  tranmaster_launcher__relaunch.writeAction(f"evlb X28 master_launcher::read_remote_data") 
  tranmaster_launcher__relaunch.writeAction(f"evi X28 X28 255 4") 
  tranmaster_launcher__relaunch.writeAction(f"ev X28 X28 X26 X26 8") 
  tranmaster_launcher__relaunch.writeAction(f"__while_relaunch_6_condition: ceq X18 X17 X27") 
  tranmaster_launcher__relaunch.writeAction(f"xori X27 X27 1") 
  tranmaster_launcher__relaunch.writeAction(f"clt X16 X26 X30") 
  tranmaster_launcher__relaunch.writeAction(f"and X27 X30 X27") 
  tranmaster_launcher__relaunch.writeAction(f"beqi X27 0 __while_relaunch_8_post") 
  tranmaster_launcher__relaunch.writeAction(f"__while_relaunch_7_body: sendr_wret X28 master_launcher::receive_dram_remote X18 X18 X27") 
  tranmaster_launcher__relaunch.writeAction(f"addi X18 X18 8") 
  tranmaster_launcher__relaunch.writeAction(f"addi X16 X16 1") 
  ## num_v = num_v + 1;

  tranmaster_launcher__relaunch.writeAction(f"jmp __while_relaunch_6_condition") 
  tranmaster_launcher__relaunch.writeAction(f"__while_relaunch_8_post: bneu X18 X17 __if_relaunch_11_post") 
  tranmaster_launcher__relaunch.writeAction(f"__if_relaunch_9_true: bnei X20 0 __if_relaunch_13_false") 
  tranmaster_launcher__relaunch.writeAction(f"__if_relaunch_12_true: movir X26 2") 
  tranmaster_launcher__relaunch.writeAction(f"movrl X26 8(X19) 0 8") 
  tranmaster_launcher__relaunch.writeAction(f"yield") 
  tranmaster_launcher__relaunch.writeAction(f"jmp __if_relaunch_11_post") 
  tranmaster_launcher__relaunch.writeAction(f"__if_relaunch_13_false: andi X20 X26 1") 
  tranmaster_launcher__relaunch.writeAction(f"bnei X26 0 __if_relaunch_11_post") 
  tranmaster_launcher__relaunch.writeAction(f"__if_relaunch_15_true: movlr 16(X19) X26 0 8") 
  tranmaster_launcher__relaunch.writeAction(f"movlr 24(X19) X27 0 8") 
  tranmaster_launcher__relaunch.writeAction(f"addi X27 X27 1") 
  tranmaster_launcher__relaunch.writeAction(f"movir X28 0") 
  tranmaster_launcher__relaunch.writeAction(f"evlb X28 master_launcher::read_remote_data") 
  tranmaster_launcher__relaunch.writeAction(f"evi X28 X28 255 4") 
  tranmaster_launcher__relaunch.writeAction(f"ev X28 X28 X27 X27 8") 
  tranmaster_launcher__relaunch.writeAction(f"sendr_wret X28 master_launcher::read_master_dram_length_compact X26 X26 X30") 
  tranmaster_launcher__relaunch.writeAction(f"movrl X27 24(X19) 0 8") 
  tranmaster_launcher__relaunch.writeAction(f"addi X26 X18 8") 
  tranmaster_launcher__relaunch.writeAction(f"addi X18 X17 0") 
  ## temp_lmbuff = LMBASE;

  tranmaster_launcher__relaunch.writeAction(f"movlr 120(X29) X28 0 8") 
  tranmaster_launcher__relaunch.writeAction(f"add X26 X28 X28") 
  tranmaster_launcher__relaunch.writeAction(f"movrl X28 16(X19) 0 8") 
  tranmaster_launcher__relaunch.writeAction(f"subi X20 X20 1") 
  tranmaster_launcher__relaunch.writeAction(f"yield") 
  tranmaster_launcher__relaunch.writeAction(f"__if_relaunch_11_post: yield") 
  
  # Writing code for event master_launcher::write_return
  tranmaster_launcher__write_return = efa.writeEvent('master_launcher::write_return')
  tranmaster_launcher__write_return.writeAction(f"__entry: subi X23 X23 1") 
  tranmaster_launcher__write_return.writeAction(f"bnei X23 0 __if_write_return_2_post") 
  tranmaster_launcher__write_return.writeAction(f"__if_write_return_0_true: movlr 0(X19) X28 0 8") 
  tranmaster_launcher__write_return.writeAction(f"movir X29 -1") 
  tranmaster_launcher__write_return.writeAction(f"sri X29 X29 1") 
  tranmaster_launcher__write_return.writeAction(f"sendr_wcont X28 X29 X21 X0") 
  tranmaster_launcher__write_return.writeAction(f"bnei X21 0 __if_write_return_2_post") 
  tranmaster_launcher__write_return.writeAction(f"__if_write_return_3_true: movir X28 65504") 
  tranmaster_launcher__write_return.writeAction(f"add X7 X28 X28") 
  tranmaster_launcher__write_return.writeAction(f"movir X29 -1") 
  tranmaster_launcher__write_return.writeAction(f"movrl X29 0(X28) 0 8") 
  ## print("[DEBUG][NWID %lu] <write_return>: num_v = %ld", NETID, num_v);

  tranmaster_launcher__write_return.writeAction(f"yield_terminate") 
  tranmaster_launcher__write_return.writeAction(f"__if_write_return_2_post: yield") 
  
  # Writing code for event master_launcher::all_launched
  tranmaster_launcher__all_launched = efa.writeEvent('master_launcher::all_launched')
  tranmaster_launcher__all_launched.writeAction(f"__entry: movir X28 3") 
  tranmaster_launcher__all_launched.writeAction(f"movrl X28 8(X19) 0 8") 
  tranmaster_launcher__all_launched.writeAction(f"movrl X1 0(X19) 0 8") 
  tranmaster_launcher__all_launched.writeAction(f"bnei X25 0 __if_all_launched_2_post") 
  tranmaster_launcher__all_launched.writeAction(f"__if_all_launched_0_true: movir X28 -1") 
  tranmaster_launcher__all_launched.writeAction(f"sri X28 X28 1") 
  tranmaster_launcher__all_launched.writeAction(f"sendr_wcont X1 X28 X24 X24") 
  ## print("[DEBUG][NWID %lu] <all_launched>: num_int = %lu", NETID, num_int);

  tranmaster_launcher__all_launched.writeAction(f"yield_terminate") 
  tranmaster_launcher__all_launched.writeAction(f"__if_all_launched_2_post: yield") 
  
  # Writing code for event master_launcher::reduce_num_int
  tranmaster_launcher__reduce_num_int = efa.writeEvent('master_launcher::reduce_num_int')
  tranmaster_launcher__reduce_num_int.writeAction(f"__entry: subi X25 X25 1") 
  tranmaster_launcher__reduce_num_int.writeAction(f"add X24 X8 X24") 
  ## print("[DEBUG][NWID %lu] <reduce_num_int>: tc = %ld, num_int = %lu", NETID, tc, num_int);

  ##         if(_tc > 0){

  ##             unsigned long* local tmp_lmbuff2 = LMBASE + WORKER_THREADID_OFFSET;

  ##             int tid = tmp_lmbuff2[0];

  ##             unsigned long evword = evw_update_event(CEVNT, intersection_launcher__add_value);

  ##             evword = evw_update_thread(evword, tid);

  ##             send_event(evword, addr, _tc, IGNRCONT);

  ##             evword = temp_lmbuff[NUM_WRITE];

  ##             evword = evword + 1;

  ##             temp_lmbuff[NUM_WRITE] = evword;

  ## #ifdef DEBUG

  ##             print("<reduce_num_int> addr = 0x%lx, NUM_WRITE = %lu", addr, temp + 1);

  ## #endif

  ##         }

  tranmaster_launcher__reduce_num_int.writeAction(f"bnei X25 0 __if_reduce_num_int_2_post") 
  tranmaster_launcher__reduce_num_int.writeAction(f"__if_reduce_num_int_0_true: movlr 8(X19) X28 0 8") 
  tranmaster_launcher__reduce_num_int.writeAction(f"bneiu X28 3 __if_reduce_num_int_2_post") 
  tranmaster_launcher__reduce_num_int.writeAction(f"__if_reduce_num_int_3_true: movlr 0(X19) X28 0 8") 
  tranmaster_launcher__reduce_num_int.writeAction(f"movir X29 -1") 
  tranmaster_launcher__reduce_num_int.writeAction(f"sri X29 X29 1") 
  tranmaster_launcher__reduce_num_int.writeAction(f"sendr_wcont X28 X29 X24 X24") 
  ## print("[DEBUG][NWID %lu] <reduce_num_int>: tc = %ld", NETID, tc);

  tranmaster_launcher__reduce_num_int.writeAction(f"yield_terminate") 
  tranmaster_launcher__reduce_num_int.writeAction(f"__if_reduce_num_int_2_post: yield") 
  
  # Writing code for event master_launcher::send_to_master_thread1
  tranmaster_launcher__send_to_master_thread1 = efa.writeEvent('master_launcher::send_to_master_thread1')
  tranmaster_launcher__send_to_master_thread1.writeAction(f"__entry: movir X28 65504") 
  tranmaster_launcher__send_to_master_thread1.writeAction(f"add X7 X28 X28") 
  tranmaster_launcher__send_to_master_thread1.writeAction(f"movlr 0(X28) X28 0 8") 
  tranmaster_launcher__send_to_master_thread1.writeAction(f"bnei X28 -1 __if_send_to_master_thread1_2_post") 
  tranmaster_launcher__send_to_master_thread1.writeAction(f"__if_send_to_master_thread1_0_true: movir X29 0") 
  tranmaster_launcher__send_to_master_thread1.writeAction(f"movir X26 -1") 
  tranmaster_launcher__send_to_master_thread1.writeAction(f"sri X26 X26 1") 
  tranmaster_launcher__send_to_master_thread1.writeAction(f"sendr_wcont X1 X26 X29 X29") 
  tranmaster_launcher__send_to_master_thread1.writeAction(f"yield_terminate") 
  tranmaster_launcher__send_to_master_thread1.writeAction(f"__if_send_to_master_thread1_2_post: ev X8 X28 X28 X28 4") 
  tranmaster_launcher__send_to_master_thread1.writeAction(f"sendr_wcont X28 X1 X9 X9") 
  tranmaster_launcher__send_to_master_thread1.writeAction(f"yield_terminate") 
  
  # Writing code for event master_launcher::send_to_master_thread2
  tranmaster_launcher__send_to_master_thread2 = efa.writeEvent('master_launcher::send_to_master_thread2')
  tranmaster_launcher__send_to_master_thread2.writeAction(f"__entry: movir X28 65504") 
  tranmaster_launcher__send_to_master_thread2.writeAction(f"add X7 X28 X28") 
  tranmaster_launcher__send_to_master_thread2.writeAction(f"movlr 0(X28) X28 0 8") 
  ## if(tid == -1){

  ##     send_event(CCONT, 0, IGNRCONT);

  ##     yield_terminate;

  ## }

  tranmaster_launcher__send_to_master_thread2.writeAction(f"ev X8 X28 X28 X28 4") 
  tranmaster_launcher__send_to_master_thread2.writeAction(f"sendr_wcont X28 X1 X9 X10") 
  tranmaster_launcher__send_to_master_thread2.writeAction(f"yield_terminate") 
  