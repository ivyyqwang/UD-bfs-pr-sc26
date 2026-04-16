from linker.EFAProgram import efaProgram

## UDWeave version: unknown

## Global constants

@efaProgram
def EFA_main_master(efa):
  efa.code_level = 'machine'
  state0 = efa.State("udweave_init") #Only one state code 
  efa.add_initId(state0.state_id)
  ## Static declarations
  ## Scoped Variable "tc_cumulative" uses Register X16, scope (0)
  ## Scoped Variable "num_lanes_per_control" uses Register X17, scope (0)
  ## Scoped Variable "control_level" uses Register X18, scope (0)
  ## Scoped Variable "num_map" uses Register X19, scope (0)
  ## Scoped Variable "num_map_done" uses Register X20, scope (0)
  ## Scoped Variable "num_vertices" uses Register X21, scope (0)
  ## Scoped Variable "num_combine" uses Register X22, scope (0)
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
  ## #define DEBUG
  ## master_buffer_start in LM[MASTER_BUFFER_START]
  ## g_v_local in LM[G_V_LOCAL]
  ## k in LM[K_OFFSET]
  ## iter in LM[ITERA]
  ## _num_lane_in = num_lanes << 32 + num_lanes_total
  ## _num_combine = num_combine << 32 + cache_size
  ## _log2_num_control_lane = log2_num_control_lane << 32 + control_level
  
  #################################################
  ###### Writing code for thread main_master ######
  #################################################
  ## unsigned long  master_start;
  # Writing code for event main_master::init_tc
  tranmain_master__init_tc = efa.writeEvent('main_master::init_tc')
  tranmain_master__init_tc.writeAction(f"__entry: addi X7 X23 0") 
  tranmain_master__init_tc.writeAction(f"movlr 240(X23) X24 0 8") 
  tranmain_master__init_tc.writeAction(f"sari X3 X25 32") 
  tranmain_master__init_tc.writeAction(f"sli X25 X18 32") 
  tranmain_master__init_tc.writeAction(f"sub X3 X18 X18") 
  tranmain_master__init_tc.writeAction(f"bneiu X24 0 __if_init_tc_2_post") 
  tranmain_master__init_tc.writeAction(f"__if_init_tc_0_true: bneiu X18 0 __if_init_tc_2_post") 
  tranmain_master__init_tc.writeAction(f"__if_init_tc_3_true: print 'K-Truss Start'") 
  tranmain_master__init_tc.writeAction(f"movir X26 65520") 
  tranmain_master__init_tc.writeAction(f"add X7 X26 X23") 
  tranmain_master__init_tc.writeAction(f"movrl X18 0(X23) 0 8") 
  tranmain_master__init_tc.writeAction(f"movrl X18 8(X23) 0 8") 
  tranmain_master__init_tc.writeAction(f"__if_init_tc_2_post: sari X8 X26 32") 
  tranmain_master__init_tc.writeAction(f"sari X9 X22 32") 
  tranmain_master__init_tc.writeAction(f"bneiu X18 0 __if_init_tc_8_post") 
  tranmain_master__init_tc.writeAction(f"__if_init_tc_6_true: movlr 240(X23) X27 0 8") 
  tranmain_master__init_tc.writeAction(f"print '[Itera %lu] start' X27") 
  tranmain_master__init_tc.writeAction(f"sli X26 X27 32") 
  tranmain_master__init_tc.writeAction(f"sub X8 X27 X27") 
  tranmain_master__init_tc.writeAction(f"sli X22 X28 32") 
  tranmain_master__init_tc.writeAction(f"sub X9 X28 X28") 
  tranmain_master__init_tc.writeAction(f"print 'num_lanes_in = %lu, num_lanes_total = %lu, num_combine = %lu, cache_len = %lu' X26 X27 X22 X28") 
  tranmain_master__init_tc.writeAction(f"print 'log2_num_control_lane = %lu, control_level = %lu, g_v_in = 0x%lx, intersection_start = 0x%lx, intersection_size = %lu' X25 X18 X10 X11 X12") 
  tranmain_master__init_tc.writeAction(f"print 'master_start0 = 0x%lx, master_start1 = 0x%lx, master_size = %lu' X13 X14 X15") 
  tranmain_master__init_tc.writeAction(f"__if_init_tc_8_post: movir X27 1") 
  tranmain_master__init_tc.writeAction(f"sl X27 X25 X24") 
  tranmain_master__init_tc.writeAction(f"subi X26 X17 1") 
  tranmain_master__init_tc.writeAction(f"sr X17 X25 X25") 
  tranmain_master__init_tc.writeAction(f"addi X25 X17 1") 
  tranmain_master__init_tc.writeAction(f"bneiu X17 1 __if_init_tc_10_false") 
  tranmain_master__init_tc.writeAction(f"__if_init_tc_9_true: addi X26 X19 0") 
  tranmain_master__init_tc.writeAction(f"addi X7 X23 32") 
  tranmain_master__init_tc.writeAction(f"movrl X13 0(X23) 0 8") 
  tranmain_master__init_tc.writeAction(f"movrl X15 8(X23) 0 8") 
  tranmain_master__init_tc.writeAction(f"movrl X11 16(X23) 0 8") 
  tranmain_master__init_tc.writeAction(f"movrl X12 24(X23) 0 8") 
  tranmain_master__init_tc.writeAction(f"movrl X10 32(X23) 0 8") 
  tranmain_master__init_tc.writeAction(f"sli X26 X25 32") 
  tranmain_master__init_tc.writeAction(f"sub X8 X25 X25") 
  tranmain_master__init_tc.writeAction(f"movrl X25 40(X23) 0 8") 
  ## num_lanes_total

  tranmain_master__init_tc.writeAction(f"sli X22 X25 32") 
  tranmain_master__init_tc.writeAction(f"sub X9 X25 X25") 
  tranmain_master__init_tc.writeAction(f"movrl X25 48(X23) 0 8") 
  ## cache_len

  tranmain_master__init_tc.writeAction(f"movrl X22 56(X23) 0 8") 
  tranmain_master__init_tc.writeAction(f"movrl X14 64(X23) 0 8") 
  tranmain_master__init_tc.writeAction(f"addi X0 X25 0") 
  tranmain_master__init_tc.writeAction(f"add X25 X26 X27") 
  tranmain_master__init_tc.writeAction(f"__while_init_tc_12_condition: ble X27 X25 __while_init_tc_14_post") 
  tranmain_master__init_tc.writeAction(f"__while_init_tc_13_body: movir X28 0") 
  tranmain_master__init_tc.writeAction(f"evlb X28 master_launcher__init") 
  tranmain_master__init_tc.writeAction(f"evi X28 X28 255 4") 
  tranmain_master__init_tc.writeAction(f"ev X28 X28 X25 X25 8") 
  tranmain_master__init_tc.writeAction(f"send_wret X28 main_master::init_done X23 9 X29") 
  tranmain_master__init_tc.writeAction(f"addi X25 X25 1") 
  tranmain_master__init_tc.writeAction(f"jmp __while_init_tc_12_condition") 
  tranmain_master__init_tc.writeAction(f"__while_init_tc_14_post: jmp __if_init_tc_11_post") 
  tranmain_master__init_tc.writeAction(f"__if_init_tc_10_false: addi X24 X19 0") 
  tranmain_master__init_tc.writeAction(f"addi X7 X23 32") 
  tranmain_master__init_tc.writeAction(f"sli X26 X25 32") 
  tranmain_master__init_tc.writeAction(f"sub X8 X25 X25") 
  ## num_lanes_total

  tranmain_master__init_tc.writeAction(f"sli X17 X27 32") 
  tranmain_master__init_tc.writeAction(f"add X27 X25 X25") 
  ## num_lanes_in : num_lanes_total

  tranmain_master__init_tc.writeAction(f"movrl X25 0(X23) 0 8") 
  tranmain_master__init_tc.writeAction(f"addi X23 X27 8") 
  tranmain_master__init_tc.writeAction(f"bcpyoli X9 X27 7") 
  tranmain_master__init_tc.writeAction(f"addi X3 X27 1") 
  tranmain_master__init_tc.writeAction(f"movrl X27 64(X23) 0 8") 
  tranmain_master__init_tc.writeAction(f"addi X0 X27 0") 
  tranmain_master__init_tc.writeAction(f"mul X17 X24 X25") 
  tranmain_master__init_tc.writeAction(f"add X25 X27 X25") 
  tranmain_master__init_tc.writeAction(f"__while_init_tc_15_condition: ble X25 X27 __if_init_tc_11_post") 
  tranmain_master__init_tc.writeAction(f"__while_init_tc_16_body: movir X28 0") 
  tranmain_master__init_tc.writeAction(f"evlb X28 main_master::init_tc") 
  tranmain_master__init_tc.writeAction(f"evi X28 X28 255 4") 
  tranmain_master__init_tc.writeAction(f"ev X28 X28 X27 X27 8") 
  tranmain_master__init_tc.writeAction(f"send_wret X28 main_master::init_done X23 9 X29") 
  tranmain_master__init_tc.writeAction(f"add X27 X17 X27") 
  tranmain_master__init_tc.writeAction(f"jmp __while_init_tc_15_condition") 
  tranmain_master__init_tc.writeAction(f"__if_init_tc_11_post: movir X16 0") 
  tranmain_master__init_tc.writeAction(f"movir X21 0") 
  tranmain_master__init_tc.writeAction(f"movir X20 0") 
  tranmain_master__init_tc.writeAction(f"movir X26 65264") 
  tranmain_master__init_tc.writeAction(f"add X7 X26 X23") 
  tranmain_master__init_tc.writeAction(f"sli X18 X26 1") 
  tranmain_master__init_tc.writeAction(f"sri X2 X24 24") 
  tranmain_master__init_tc.writeAction(f"andi X24 X24 255") 
  tranmain_master__init_tc.writeAction(f"movwrl X24 X23(X26,0,0)") 
  tranmain_master__init_tc.writeAction(f"addi X26 X26 1") 
  tranmain_master__init_tc.writeAction(f"movwrl X1 X23(X26,0,0)") 
  tranmain_master__init_tc.writeAction(f"movir X26 248") 
  tranmain_master__init_tc.writeAction(f"muli X18 X24 72") 
  tranmain_master__init_tc.writeAction(f"add X24 X26 X24") 
  tranmain_master__init_tc.writeAction(f"add X7 X24 X23") 
  tranmain_master__init_tc.writeAction(f"bcpyoli X8 X23 8") 
  tranmain_master__init_tc.writeAction(f"movrl X3 64(X23) 0 8") 
  tranmain_master__init_tc.writeAction(f"blei X22 1 __if_init_tc_20_post") 
  tranmain_master__init_tc.writeAction(f"__if_init_tc_18_true: movrl X14 40(X23) 0 8") 
  tranmain_master__init_tc.writeAction(f"movrl X13 48(X23) 0 8") 
  tranmain_master__init_tc.writeAction(f"__if_init_tc_20_post: yield") 
  
  # Writing code for event main_master::init_done
  tranmain_master__init_done = efa.writeEvent('main_master::init_done')
  tranmain_master__init_done.writeAction(f"__entry: addi X20 X20 1") 
  tranmain_master__init_done.writeAction(f"bneu X20 X19 __if_init_done_2_post") 
  tranmain_master__init_done.writeAction(f"__if_init_done_0_true: movir X20 0") 
  tranmain_master__init_done.writeAction(f"bneiu X18 0 __if_init_done_4_false") 
  tranmain_master__init_done.writeAction(f"__if_init_done_3_true: evi X2 X23 main_master::start 1") 
  tranmain_master__init_done.writeAction(f"sendr_wret X23 main_master::v_launcher_done X18 X18 X24") 
  tranmain_master__init_done.writeAction(f"print '[DEBUG][NWID %lu] <init_done> finsh' X0") 
  tranmain_master__init_done.writeAction(f"jmp __if_init_done_2_post") 
  tranmain_master__init_done.writeAction(f"__if_init_done_4_false: movir X23 65264") 
  tranmain_master__init_done.writeAction(f"add X7 X23 X23") 
  tranmain_master__init_done.writeAction(f"sli X18 X24 1") 
  tranmain_master__init_done.writeAction(f"addi X24 X24 1") 
  tranmain_master__init_done.writeAction(f"movwlr X23(X24,0,0) X23") 
  tranmain_master__init_done.writeAction(f"movir X24 -1") 
  tranmain_master__init_done.writeAction(f"sri X24 X24 1") 
  tranmain_master__init_done.writeAction(f"sendr_wcont X23 X24 X0 X0") 
  tranmain_master__init_done.writeAction(f"__if_init_done_2_post: yield") 
  
  # Writing code for event main_master::send_to_global_master_thread
  tranmain_master__send_to_global_master_thread = efa.writeEvent('main_master::send_to_global_master_thread')
  tranmain_master__send_to_global_master_thread.writeAction(f"__entry: movir X23 65264") 
  tranmain_master__send_to_global_master_thread.writeAction(f"add X7 X23 X23") 
  tranmain_master__send_to_global_master_thread.writeAction(f"sli X10 X24 1") 
  tranmain_master__send_to_global_master_thread.writeAction(f"movwlr X23(X24,0,0) X26") 
  tranmain_master__send_to_global_master_thread.writeAction(f"addi X24 X24 1") 
  tranmain_master__send_to_global_master_thread.writeAction(f"movwrl X1 X23(X24,0,0)") 
  tranmain_master__send_to_global_master_thread.writeAction(f"ev X8 X26 X26 X26 4") 
  tranmain_master__send_to_global_master_thread.writeAction(f"sendr_wcont X26 X1 X9 X9") 
  tranmain_master__send_to_global_master_thread.writeAction(f"yield_terminate") 
  
  # Writing code for event main_master::start
  tranmain_master__start = efa.writeEvent('main_master::start')
  tranmain_master__start.writeAction(f"__entry: addi X0 X26 0") 
  tranmain_master__start.writeAction(f"bneiu X17 1 __if_start_1_false") 
  tranmain_master__start.writeAction(f"__if_start_0_true: evi X2 X23 master_launcher__launch_v 1") 
  tranmain_master__start.writeAction(f"add X26 X19 X24") 
  tranmain_master__start.writeAction(f"__while_start_3_condition: ble X24 X26 __while_start_5_post") 
  tranmain_master__start.writeAction(f"__while_start_4_body: ev X23 X25 X26 X26 8") 
  tranmain_master__start.writeAction(f"movir X27 0") 
  tranmain_master__start.writeAction(f"evlb X27 master_launcher__send_to_master_thread1") 
  tranmain_master__start.writeAction(f"evi X27 X27 255 4") 
  tranmain_master__start.writeAction(f"ev X27 X27 X26 X26 8") 
  tranmain_master__start.writeAction(f"sendr_wret X27 main_master::v_launcher_done X25 X0 X28") 
  tranmain_master__start.writeAction(f"addi X26 X26 1") 
  tranmain_master__start.writeAction(f"jmp __while_start_3_condition") 
  tranmain_master__start.writeAction(f"__while_start_5_post: jmp __if_start_2_post") 
  tranmain_master__start.writeAction(f"__if_start_1_false: evi X2 X24 main_master::start 1") 
  tranmain_master__start.writeAction(f"mul X19 X17 X23") 
  tranmain_master__start.writeAction(f"add X26 X23 X23") 
  tranmain_master__start.writeAction(f"__while_start_6_condition: ble X23 X26 __if_start_2_post") 
  tranmain_master__start.writeAction(f"__while_start_7_body: ev X24 X25 X26 X26 8") 
  tranmain_master__start.writeAction(f"movir X27 0") 
  tranmain_master__start.writeAction(f"evlb X27 main_master::send_to_global_master_thread") 
  tranmain_master__start.writeAction(f"evi X27 X27 255 4") 
  tranmain_master__start.writeAction(f"ev X27 X27 X26 X26 8") 
  tranmain_master__start.writeAction(f"addi X18 X28 1") 
  tranmain_master__start.writeAction(f"sendr3_wret X27 main_master::v_launcher_done X25 X0 X28 X29") 
  tranmain_master__start.writeAction(f"add X26 X17 X26") 
  tranmain_master__start.writeAction(f"jmp __while_start_6_condition") 
  tranmain_master__start.writeAction(f"__if_start_2_post: yield") 
  
  # Writing code for event main_master::v_launcher_done
  tranmain_master__v_launcher_done = efa.writeEvent('main_master::v_launcher_done')
  tranmain_master__v_launcher_done.writeAction(f"__entry: addi X20 X20 1") 
  tranmain_master__v_launcher_done.writeAction(f"movir X16 0") 
  tranmain_master__v_launcher_done.writeAction(f"add X8 X21 X21") 
  ## #ifdef DEBUG

  ## print("[DEBUG][NWID %lu] <map_launcher_done> num_map_done:%lu from niwd %lu", NETID, num_map_done, nwid);

  ## #endif

  tranmain_master__v_launcher_done.writeAction(f"bneu X20 X19 __if_v_launcher_done_2_post") 
  tranmain_master__v_launcher_done.writeAction(f"__if_v_launcher_done_0_true: movir X20 0") 
  tranmain_master__v_launcher_done.writeAction(f"bneiu X18 0 __if_v_launcher_done_4_false") 
  tranmain_master__v_launcher_done.writeAction(f"__if_v_launcher_done_3_true: evi X2 X26 main_master::v_all_launched 1") 
  tranmain_master__v_launcher_done.writeAction(f"sendr_wret X26 main_master::int_launcher_done X18 X18 X23") 
  tranmain_master__v_launcher_done.writeAction(f"print '[DEBUG][NWID %lu] <v_launcher_done> num of vertices = %lu' X0 X21") 
  tranmain_master__v_launcher_done.writeAction(f"jmp __if_v_launcher_done_2_post") 
  tranmain_master__v_launcher_done.writeAction(f"__if_v_launcher_done_4_false: movir X26 65264") 
  tranmain_master__v_launcher_done.writeAction(f"add X7 X26 X26") 
  tranmain_master__v_launcher_done.writeAction(f"sli X18 X23 1") 
  tranmain_master__v_launcher_done.writeAction(f"addi X23 X23 1") 
  tranmain_master__v_launcher_done.writeAction(f"movwlr X26(X23,0,0) X26") 
  tranmain_master__v_launcher_done.writeAction(f"movir X23 -1") 
  tranmain_master__v_launcher_done.writeAction(f"sri X23 X23 1") 
  tranmain_master__v_launcher_done.writeAction(f"sendr_wcont X26 X23 X21 X21") 
  tranmain_master__v_launcher_done.writeAction(f"__if_v_launcher_done_2_post: yield") 
  
  # Writing code for event main_master::v_all_launched
  tranmain_master__v_all_launched = efa.writeEvent('main_master::v_all_launched')
  tranmain_master__v_all_launched.writeAction(f"__entry: addi X0 X26 0") 
  tranmain_master__v_all_launched.writeAction(f"bneiu X21 0 __if_v_all_launched_2_post") 
  ## no work

  tranmain_master__v_all_launched.writeAction(f"__if_v_all_launched_0_true: evi X2 X23 main_master::int_launcher_done 1") 
  tranmain_master__v_all_launched.writeAction(f"movir X24 -1") 
  tranmain_master__v_all_launched.writeAction(f"sri X24 X24 1") 
  tranmain_master__v_all_launched.writeAction(f"sendr_wcont X23 X24 X21 X21") 
  tranmain_master__v_all_launched.writeAction(f"subi X19 X20 1") 
  tranmain_master__v_all_launched.writeAction(f"yield") 
  tranmain_master__v_all_launched.writeAction(f"__if_v_all_launched_2_post: bneiu X17 1 __if_v_all_launched_4_false") 
  tranmain_master__v_all_launched.writeAction(f"__if_v_all_launched_3_true: evi X2 X23 master_launcher__all_launched 1") 
  ## int net_id = NETID;

  tranmain_master__v_all_launched.writeAction(f"add X26 X19 X24") 
  tranmain_master__v_all_launched.writeAction(f"__while_v_all_launched_6_condition: ble X24 X26 __while_v_all_launched_8_post") 
  tranmain_master__v_all_launched.writeAction(f"__while_v_all_launched_7_body: ev X23 X25 X26 X26 8") 
  tranmain_master__v_all_launched.writeAction(f"movir X27 0") 
  tranmain_master__v_all_launched.writeAction(f"evlb X27 master_launcher__send_to_master_thread1") 
  tranmain_master__v_all_launched.writeAction(f"evi X27 X27 255 4") 
  tranmain_master__v_all_launched.writeAction(f"ev X27 X27 X26 X26 8") 
  tranmain_master__v_all_launched.writeAction(f"sendr_wret X27 main_master::int_launcher_done X25 X0 X28") 
  tranmain_master__v_all_launched.writeAction(f"addi X26 X26 1") 
  tranmain_master__v_all_launched.writeAction(f"jmp __while_v_all_launched_6_condition") 
  tranmain_master__v_all_launched.writeAction(f"__while_v_all_launched_8_post: jmp __if_v_all_launched_5_post") 
  tranmain_master__v_all_launched.writeAction(f"__if_v_all_launched_4_false: evi X2 X23 main_master::v_all_launched 1") 
  ## int net_id = NETID;

  tranmain_master__v_all_launched.writeAction(f"mul X19 X17 X24") 
  tranmain_master__v_all_launched.writeAction(f"add X26 X24 X24") 
  tranmain_master__v_all_launched.writeAction(f"__while_v_all_launched_9_condition: ble X24 X26 __if_v_all_launched_5_post") 
  tranmain_master__v_all_launched.writeAction(f"__while_v_all_launched_10_body: ev X23 X25 X26 X26 8") 
  tranmain_master__v_all_launched.writeAction(f"movir X27 0") 
  tranmain_master__v_all_launched.writeAction(f"evlb X27 main_master::send_to_global_master_thread") 
  tranmain_master__v_all_launched.writeAction(f"evi X27 X27 255 4") 
  tranmain_master__v_all_launched.writeAction(f"ev X27 X27 X26 X26 8") 
  tranmain_master__v_all_launched.writeAction(f"addi X18 X28 1") 
  tranmain_master__v_all_launched.writeAction(f"sendr3_wret X27 main_master::int_launcher_done X25 X26 X28 X29") 
  tranmain_master__v_all_launched.writeAction(f"add X26 X17 X26") 
  tranmain_master__v_all_launched.writeAction(f"jmp __while_v_all_launched_9_condition") 
  tranmain_master__v_all_launched.writeAction(f"__if_v_all_launched_5_post: yield") 
  
  # Writing code for event main_master::int_launcher_done
  tranmain_master__int_launcher_done = efa.writeEvent('main_master::int_launcher_done')
  tranmain_master__int_launcher_done.writeAction(f"__entry: addi X20 X20 1") 
  tranmain_master__int_launcher_done.writeAction(f"add X16 X8 X16") 
  tranmain_master__int_launcher_done.writeAction(f"bneu X20 X19 __if_int_launcher_done_2_post") 
  tranmain_master__int_launcher_done.writeAction(f"__if_int_launcher_done_0_true: movir X20 0") 
  tranmain_master__int_launcher_done.writeAction(f"bneiu X18 0 __if_int_launcher_done_4_false") 
  tranmain_master__int_launcher_done.writeAction(f"__if_int_launcher_done_3_true: evi X2 X26 main_master::int_all_launched 1") 
  tranmain_master__int_launcher_done.writeAction(f"sendr_wret X26 main_master::tc_launcher_done X18 X18 X24") 
  tranmain_master__int_launcher_done.writeAction(f"print '[DEBUG][NWID %lu] <int_launcher_done>' X0") 
  tranmain_master__int_launcher_done.writeAction(f"jmp __if_int_launcher_done_2_post") 
  tranmain_master__int_launcher_done.writeAction(f"__if_int_launcher_done_4_false: movir X26 65264") 
  tranmain_master__int_launcher_done.writeAction(f"add X7 X26 X26") 
  tranmain_master__int_launcher_done.writeAction(f"sli X18 X24 1") 
  tranmain_master__int_launcher_done.writeAction(f"addi X24 X24 1") 
  tranmain_master__int_launcher_done.writeAction(f"movwlr X26(X24,0,0) X26") 
  tranmain_master__int_launcher_done.writeAction(f"movir X24 -1") 
  tranmain_master__int_launcher_done.writeAction(f"sri X24 X24 1") 
  tranmain_master__int_launcher_done.writeAction(f"sendr_wcont X26 X24 X16 X16") 
  tranmain_master__int_launcher_done.writeAction(f"__if_int_launcher_done_2_post: yield") 
  
  # Writing code for event main_master::int_all_launched
  tranmain_master__int_all_launched = efa.writeEvent('main_master::int_all_launched')
  tranmain_master__int_all_launched.writeAction(f"__entry: bneiu X17 1 __if_int_all_launched_1_false") 
  tranmain_master__int_all_launched.writeAction(f"__if_int_all_launched_0_true: evi X2 X26 intersection_launcher__cache_write_finish 1") 
  tranmain_master__int_all_launched.writeAction(f"addi X0 X24 0") 
  tranmain_master__int_all_launched.writeAction(f"add X24 X19 X23") 
  tranmain_master__int_all_launched.writeAction(f"__while_int_all_launched_3_condition: ble X23 X24 __while_int_all_launched_5_post") 
  tranmain_master__int_all_launched.writeAction(f"__while_int_all_launched_4_body: ev X26 X25 X24 X24 8") 
  tranmain_master__int_all_launched.writeAction(f"movir X27 0") 
  tranmain_master__int_all_launched.writeAction(f"evlb X27 intersection_launcher__send_to_worker_thread2") 
  tranmain_master__int_all_launched.writeAction(f"evi X27 X27 255 4") 
  tranmain_master__int_all_launched.writeAction(f"ev X27 X27 X24 X24 8") 
  tranmain_master__int_all_launched.writeAction(f"sendr3_wret X27 main_master::tc_launcher_done X25 X24 X0 X28") 
  tranmain_master__int_all_launched.writeAction(f"addi X24 X24 1") 
  tranmain_master__int_all_launched.writeAction(f"jmp __while_int_all_launched_3_condition") 
  tranmain_master__int_all_launched.writeAction(f"__while_int_all_launched_5_post: jmp __if_int_all_launched_2_post") 
  tranmain_master__int_all_launched.writeAction(f"__if_int_all_launched_1_false: evi X2 X26 main_master::int_all_launched 1") 
  tranmain_master__int_all_launched.writeAction(f"addi X0 X23 0") 
  tranmain_master__int_all_launched.writeAction(f"mul X19 X17 X24") 
  tranmain_master__int_all_launched.writeAction(f"add X23 X24 X24") 
  tranmain_master__int_all_launched.writeAction(f"__while_int_all_launched_6_condition: ble X24 X23 __if_int_all_launched_2_post") 
  tranmain_master__int_all_launched.writeAction(f"__while_int_all_launched_7_body: ev X26 X25 X23 X23 8") 
  tranmain_master__int_all_launched.writeAction(f"movir X27 0") 
  tranmain_master__int_all_launched.writeAction(f"evlb X27 main_master::send_to_global_master_thread") 
  tranmain_master__int_all_launched.writeAction(f"evi X27 X27 255 4") 
  tranmain_master__int_all_launched.writeAction(f"ev X27 X27 X23 X23 8") 
  tranmain_master__int_all_launched.writeAction(f"addi X18 X28 1") 
  tranmain_master__int_all_launched.writeAction(f"sendr3_wret X27 main_master::tc_launcher_done X25 X18 X28 X29") 
  tranmain_master__int_all_launched.writeAction(f"add X23 X17 X23") 
  tranmain_master__int_all_launched.writeAction(f"jmp __while_int_all_launched_6_condition") 
  tranmain_master__int_all_launched.writeAction(f"__if_int_all_launched_2_post: yield") 
  
  # Writing code for event main_master::tc_launcher_done
  tranmain_master__tc_launcher_done = efa.writeEvent('main_master::tc_launcher_done')
  tranmain_master__tc_launcher_done.writeAction(f"__entry: addi X20 X20 1") 
  tranmain_master__tc_launcher_done.writeAction(f"bneu X20 X19 __if_tc_launcher_done_2_post") 
  tranmain_master__tc_launcher_done.writeAction(f"__if_tc_launcher_done_0_true: movir X20 0") 
  tranmain_master__tc_launcher_done.writeAction(f"bneiu X18 0 __if_tc_launcher_done_4_false") 
  tranmain_master__tc_launcher_done.writeAction(f"__if_tc_launcher_done_3_true: evi X2 X24 main_master::tc_all_launched 1") 
  tranmain_master__tc_launcher_done.writeAction(f"addi X7 X23 0") 
  tranmain_master__tc_launcher_done.writeAction(f"movlr 104(X23) X23 0 8") 
  tranmain_master__tc_launcher_done.writeAction(f"sendr_wret X24 main_master::cache_launcher_done X23 X23 X26") 
  tranmain_master__tc_launcher_done.writeAction(f"print '[DEBUG][NWID %lu] <tc_launcher_done>' X0") 
  tranmain_master__tc_launcher_done.writeAction(f"jmp __if_tc_launcher_done_2_post") 
  tranmain_master__tc_launcher_done.writeAction(f"__if_tc_launcher_done_4_false: movir X24 65264") 
  tranmain_master__tc_launcher_done.writeAction(f"add X7 X24 X24") 
  tranmain_master__tc_launcher_done.writeAction(f"sli X18 X23 1") 
  tranmain_master__tc_launcher_done.writeAction(f"addi X23 X23 1") 
  tranmain_master__tc_launcher_done.writeAction(f"movwlr X24(X23,0,0) X24") 
  tranmain_master__tc_launcher_done.writeAction(f"movir X23 -1") 
  tranmain_master__tc_launcher_done.writeAction(f"sri X23 X23 1") 
  tranmain_master__tc_launcher_done.writeAction(f"sendr_wcont X24 X23 X0 X0") 
  tranmain_master__tc_launcher_done.writeAction(f"__if_tc_launcher_done_2_post: yield") 
  
  # Writing code for event main_master::tc_all_launched
  tranmain_master__tc_all_launched = efa.writeEvent('main_master::tc_all_launched')
  tranmain_master__tc_all_launched.writeAction(f"__entry: bneiu X17 1 __if_tc_all_launched_1_false") 
  tranmain_master__tc_all_launched.writeAction(f"__if_tc_all_launched_0_true: evi X2 X24 intersection_launcher__write_back_cache 1") 
  tranmain_master__tc_all_launched.writeAction(f"addi X0 X23 0") 
  tranmain_master__tc_all_launched.writeAction(f"add X23 X19 X26") 
  tranmain_master__tc_all_launched.writeAction(f"__while_tc_all_launched_3_condition: ble X26 X23 __while_tc_all_launched_5_post") 
  tranmain_master__tc_all_launched.writeAction(f"__while_tc_all_launched_4_body: ev X24 X25 X23 X23 8") 
  tranmain_master__tc_all_launched.writeAction(f"movir X27 0") 
  tranmain_master__tc_all_launched.writeAction(f"evlb X27 intersection_launcher__send_to_worker_thread2") 
  tranmain_master__tc_all_launched.writeAction(f"evi X27 X27 255 4") 
  tranmain_master__tc_all_launched.writeAction(f"ev X27 X27 X23 X23 8") 
  tranmain_master__tc_all_launched.writeAction(f"sendr3_wret X27 main_master::cache_launcher_done X25 X23 X0 X28") 
  tranmain_master__tc_all_launched.writeAction(f"addi X23 X23 1") 
  tranmain_master__tc_all_launched.writeAction(f"jmp __while_tc_all_launched_3_condition") 
  tranmain_master__tc_all_launched.writeAction(f"__while_tc_all_launched_5_post: addi X7 X26 0") 
  tranmain_master__tc_all_launched.writeAction(f"movrl X8 104(X26) 0 8") 
  tranmain_master__tc_all_launched.writeAction(f"jmp __if_tc_all_launched_2_post") 
  tranmain_master__tc_all_launched.writeAction(f"__if_tc_all_launched_1_false: evi X2 X26 main_master::tc_all_launched 1") 
  tranmain_master__tc_all_launched.writeAction(f"addi X0 X23 0") 
  tranmain_master__tc_all_launched.writeAction(f"mul X19 X17 X24") 
  tranmain_master__tc_all_launched.writeAction(f"add X23 X24 X24") 
  tranmain_master__tc_all_launched.writeAction(f"__while_tc_all_launched_6_condition: ble X24 X23 __if_tc_all_launched_2_post") 
  tranmain_master__tc_all_launched.writeAction(f"__while_tc_all_launched_7_body: ev X26 X25 X23 X23 8") 
  tranmain_master__tc_all_launched.writeAction(f"movir X27 0") 
  tranmain_master__tc_all_launched.writeAction(f"evlb X27 main_master::send_to_global_master_thread") 
  tranmain_master__tc_all_launched.writeAction(f"evi X27 X27 255 4") 
  tranmain_master__tc_all_launched.writeAction(f"ev X27 X27 X23 X23 8") 
  tranmain_master__tc_all_launched.writeAction(f"addi X18 X28 1") 
  tranmain_master__tc_all_launched.writeAction(f"sendr3_wret X27 main_master::cache_launcher_done X25 X8 X28 X29") 
  tranmain_master__tc_all_launched.writeAction(f"add X23 X17 X23") 
  tranmain_master__tc_all_launched.writeAction(f"jmp __while_tc_all_launched_6_condition") 
  tranmain_master__tc_all_launched.writeAction(f"__if_tc_all_launched_2_post: yield") 
  
  # Writing code for event main_master::cache_launcher_done
  tranmain_master__cache_launcher_done = efa.writeEvent('main_master::cache_launcher_done')
  tranmain_master__cache_launcher_done.writeAction(f"__entry: addi X20 X20 1") 
  tranmain_master__cache_launcher_done.writeAction(f"bneu X20 X19 __if_cache_launcher_done_2_post") 
  tranmain_master__cache_launcher_done.writeAction(f"__if_cache_launcher_done_0_true: movir X20 0") 
  tranmain_master__cache_launcher_done.writeAction(f"bneiu X18 0 __if_cache_launcher_done_4_false") 
  tranmain_master__cache_launcher_done.writeAction(f"__if_cache_launcher_done_3_true: print 'TC: %lu' X16") 
  tranmain_master__cache_launcher_done.writeAction(f"evi X2 X23 main_master::cache_all_launched 1") 
  tranmain_master__cache_launcher_done.writeAction(f"movir X26 65496") 
  tranmain_master__cache_launcher_done.writeAction(f"add X7 X26 X26") 
  tranmain_master__cache_launcher_done.writeAction(f"movlr 0(X26) X26 0 8") 
  tranmain_master__cache_launcher_done.writeAction(f"sendr_wret X23 main_master::filter_launcher_done X26 X26 X24") 
  tranmain_master__cache_launcher_done.writeAction(f"yield") 
  tranmain_master__cache_launcher_done.writeAction(f"jmp __if_cache_launcher_done_2_post") 
  tranmain_master__cache_launcher_done.writeAction(f"__if_cache_launcher_done_4_false: sli X18 X23 1") 
  tranmain_master__cache_launcher_done.writeAction(f"movir X26 65264") 
  tranmain_master__cache_launcher_done.writeAction(f"add X7 X26 X26") 
  tranmain_master__cache_launcher_done.writeAction(f"addi X23 X23 1") 
  tranmain_master__cache_launcher_done.writeAction(f"movwlr X26(X23,0,0) X26") 
  tranmain_master__cache_launcher_done.writeAction(f"movir X23 -1") 
  tranmain_master__cache_launcher_done.writeAction(f"sri X23 X23 1") 
  tranmain_master__cache_launcher_done.writeAction(f"sendr_wcont X26 X23 X0 X0") 
  tranmain_master__cache_launcher_done.writeAction(f"yield") 
  tranmain_master__cache_launcher_done.writeAction(f"__if_cache_launcher_done_2_post: yield") 
  
  # Writing code for event main_master::cache_all_launched
  tranmain_master__cache_all_launched = efa.writeEvent('main_master::cache_all_launched')
  tranmain_master__cache_all_launched.writeAction(f"__entry: movir X16 0") 
  ## if(num_vertices == 0){ // no work

  ##     unsigned long evword = evw_update_event(CEVNT, filter_launcher_done);

  ##     send_event(evword, num_vertices, num_vertices, IGNRCONT);

  ##     num_map_done = num_map - 1;

  ##     yield;

  ## }

  tranmain_master__cache_all_launched.writeAction(f"movir X21 0") 
  tranmain_master__cache_all_launched.writeAction(f"addi X0 X26 0") 
  tranmain_master__cache_all_launched.writeAction(f"bneiu X17 1 __if_cache_all_launched_1_false") 
  tranmain_master__cache_all_launched.writeAction(f"__if_cache_all_launched_0_true: movir X23 248") 
  tranmain_master__cache_all_launched.writeAction(f"add X7 X23 X24") 
  tranmain_master__cache_all_launched.writeAction(f"muli X18 X23 72") 
  tranmain_master__cache_all_launched.writeAction(f"add X24 X23 X24") 
  tranmain_master__cache_all_launched.writeAction(f"movir X23 -1") 
  tranmain_master__cache_all_launched.writeAction(f"sri X23 X23 32") 
  ## mask

  tranmain_master__cache_all_launched.writeAction(f"movlr 0(X24) X25 0 8") 
  tranmain_master__cache_all_launched.writeAction(f"and X25 X23 X25") 
  ## num_lane_total

  tranmain_master__cache_all_launched.writeAction(f"addi X7 X27 32") 
  tranmain_master__cache_all_launched.writeAction(f"movrl X8 0(X27) 0 8") 
  tranmain_master__cache_all_launched.writeAction(f"movlr 16(X24) X23 0 8") 
  ## gv

  tranmain_master__cache_all_launched.writeAction(f"movrl X23 8(X27) 0 8") 
  tranmain_master__cache_all_launched.writeAction(f"movlr 40(X24) X23 0 8") 
  ## master_start

  tranmain_master__cache_all_launched.writeAction(f"movrl X23 16(X27) 0 8") 
  tranmain_master__cache_all_launched.writeAction(f"movlr 48(X24) X23 0 8") 
  ## master_start_write

  tranmain_master__cache_all_launched.writeAction(f"movrl X23 24(X27) 0 8") 
  tranmain_master__cache_all_launched.writeAction(f"movrl X22 32(X27) 0 8") 
  tranmain_master__cache_all_launched.writeAction(f"movir X28 0") 
  tranmain_master__cache_all_launched.writeAction(f"movrl X28 40(X27) 0 8") 
  tranmain_master__cache_all_launched.writeAction(f"movlr 56(X24) X23 0 8") 
  ## master_size

  tranmain_master__cache_all_launched.writeAction(f"mul X23 X22 X23") 
  tranmain_master__cache_all_launched.writeAction(f"movrl X23 56(X27) 0 8") 
  tranmain_master__cache_all_launched.writeAction(f"addi X7 X24 0") 
  tranmain_master__cache_all_launched.writeAction(f"movlr 104(X24) X23 0 8") 
  tranmain_master__cache_all_launched.writeAction(f"movrl X23 48(X27) 0 8") 
  tranmain_master__cache_all_launched.writeAction(f"blei X22 1 __if_cache_all_launched_5_post") 
  tranmain_master__cache_all_launched.writeAction(f"__if_cache_all_launched_3_true: movir X24 2048") 
  tranmain_master__cache_all_launched.writeAction(f"bne X25 X24 __if_cache_all_launched_5_post") 
  ## 1 node

  tranmain_master__cache_all_launched.writeAction(f"__if_cache_all_launched_6_true: movir X24 1") 
  tranmain_master__cache_all_launched.writeAction(f"movrl X24 40(X27) 0 8") 
  ## net_id = NETID;

  tranmain_master__cache_all_launched.writeAction(f"__if_cache_all_launched_5_post: add X26 X19 X25") 
  tranmain_master__cache_all_launched.writeAction(f"__while_cache_all_launched_9_condition: ble X25 X26 __while_cache_all_launched_11_post") 
  tranmain_master__cache_all_launched.writeAction(f"__while_cache_all_launched_10_body: movir X23 0") 
  tranmain_master__cache_all_launched.writeAction(f"evlb X23 filter_launcher__start") 
  tranmain_master__cache_all_launched.writeAction(f"evi X23 X23 255 4") 
  tranmain_master__cache_all_launched.writeAction(f"ev X23 X23 X26 X26 8") 
  tranmain_master__cache_all_launched.writeAction(f"send_wret X23 main_master::filter_launcher_done X27 8 X24") 
  tranmain_master__cache_all_launched.writeAction(f"addi X26 X26 1") 
  tranmain_master__cache_all_launched.writeAction(f"jmp __while_cache_all_launched_9_condition") 
  tranmain_master__cache_all_launched.writeAction(f"__while_cache_all_launched_11_post: jmp __if_cache_all_launched_2_post") 
  tranmain_master__cache_all_launched.writeAction(f"__if_cache_all_launched_1_false: evi X2 X27 main_master::cache_all_launched 1") 
  ## int net_id = NETID;

  tranmain_master__cache_all_launched.writeAction(f"mul X19 X17 X23") 
  tranmain_master__cache_all_launched.writeAction(f"add X26 X23 X23") 
  tranmain_master__cache_all_launched.writeAction(f"__while_cache_all_launched_12_condition: ble X23 X26 __if_cache_all_launched_2_post") 
  tranmain_master__cache_all_launched.writeAction(f"__while_cache_all_launched_13_body: ev X27 X25 X26 X26 8") 
  tranmain_master__cache_all_launched.writeAction(f"movir X24 0") 
  tranmain_master__cache_all_launched.writeAction(f"evlb X24 main_master::send_to_global_master_thread") 
  tranmain_master__cache_all_launched.writeAction(f"evi X24 X24 255 4") 
  tranmain_master__cache_all_launched.writeAction(f"ev X24 X24 X26 X26 8") 
  tranmain_master__cache_all_launched.writeAction(f"addi X18 X28 1") 
  tranmain_master__cache_all_launched.writeAction(f"sendr3_wret X24 main_master::filter_launcher_done X25 X8 X28 X29") 
  tranmain_master__cache_all_launched.writeAction(f"add X26 X17 X26") 
  tranmain_master__cache_all_launched.writeAction(f"jmp __while_cache_all_launched_12_condition") 
  tranmain_master__cache_all_launched.writeAction(f"__if_cache_all_launched_2_post: yield") 
  
  # Writing code for event main_master::filter_launcher_done
  tranmain_master__filter_launcher_done = efa.writeEvent('main_master::filter_launcher_done')
  tranmain_master__filter_launcher_done.writeAction(f"__entry: addi X20 X20 1") 
  tranmain_master__filter_launcher_done.writeAction(f"add X16 X8 X16") 
  tranmain_master__filter_launcher_done.writeAction(f"add X21 X9 X21") 
  tranmain_master__filter_launcher_done.writeAction(f"addi X7 X26 0") 
  tranmain_master__filter_launcher_done.writeAction(f"bneu X20 X19 __if_filter_launcher_done_2_post") 
  tranmain_master__filter_launcher_done.writeAction(f"__if_filter_launcher_done_0_true: movir X20 0") 
  tranmain_master__filter_launcher_done.writeAction(f"bneiu X18 0 __if_filter_launcher_done_4_false") 
  tranmain_master__filter_launcher_done.writeAction(f"__if_filter_launcher_done_3_true: movlr 240(X26) X27 0 8") 
  tranmain_master__filter_launcher_done.writeAction(f"print '[Itera %lu]: deleted tc %lu, update edges %lu' X27 X16 X21") 
  tranmain_master__filter_launcher_done.writeAction(f"addi X27 X27 1") 
  tranmain_master__filter_launcher_done.writeAction(f"movrl X27 240(X26) 0 8") 
  tranmain_master__filter_launcher_done.writeAction(f"bneiu X16 0 __if_filter_launcher_done_8_post") 
  ## end

  ## if(itera == 1){

  tranmain_master__filter_launcher_done.writeAction(f"__if_filter_launcher_done_6_true: movir X23 65520") 
  tranmain_master__filter_launcher_done.writeAction(f"add X7 X23 X26") 
  tranmain_master__filter_launcher_done.writeAction(f"movrl X27 0(X26) 0 8") 
  tranmain_master__filter_launcher_done.writeAction(f"movir X23 1") 
  tranmain_master__filter_launcher_done.writeAction(f"movrl X23 8(X26) 0 8") 
  tranmain_master__filter_launcher_done.writeAction(f"yield_terminate") 
  ## lmbuff = LMBASE + K_OFFSET;

  ## long k = lmbuff[0];

  ## if(k == 1){

  ##     if(itera == 1){ // end in the first iteratio

  ##         lmbuff = LMBASE + MAIN_MASTER_OFFSET;

  ##         lmbuff[MAIN_TC] = itera;

  ##         lmbuff[MAIN_TOP_FLAG] = 1;

  ##         yield_terminate;

  ##     }

  ## }

  tranmain_master__filter_launcher_done.writeAction(f"__if_filter_launcher_done_8_post: movir X27 248") 
  tranmain_master__filter_launcher_done.writeAction(f"muli X18 X23 72") 
  tranmain_master__filter_launcher_done.writeAction(f"add X23 X27 X23") 
  tranmain_master__filter_launcher_done.writeAction(f"add X7 X23 X26") 
  tranmain_master__filter_launcher_done.writeAction(f"movlr 56(X26) X27 0 8") 
  ## master_size

  tranmain_master__filter_launcher_done.writeAction(f"mul X22 X27 X25") 
  tranmain_master__filter_launcher_done.writeAction(f"movrl X25 56(X26) 0 8") 
  tranmain_master__filter_launcher_done.writeAction(f"movlr 40(X26) X27 0 8") 
  tranmain_master__filter_launcher_done.writeAction(f"movlr 48(X26) X25 0 8") 
  tranmain_master__filter_launcher_done.writeAction(f"movrl X25 40(X26) 0 8") 
  tranmain_master__filter_launcher_done.writeAction(f"movrl X27 48(X26) 0 8") 
  ## exchange LM[5] and LM[6]

  tranmain_master__filter_launcher_done.writeAction(f"movir X27 -1") 
  tranmain_master__filter_launcher_done.writeAction(f"sri X27 X27 32") 
  ## mask

  tranmain_master__filter_launcher_done.writeAction(f"movlr 0(X26) X25 0 8") 
  tranmain_master__filter_launcher_done.writeAction(f"and X25 X27 X25") 
  ## num_lane_total

  tranmain_master__filter_launcher_done.writeAction(f"movir X24 256") 
  tranmain_master__filter_launcher_done.writeAction(f"sli X24 X24 16") 
  tranmain_master__filter_launcher_done.writeAction(f"bleu X21 X24 __if_filter_launcher_done_11_post") 
  ## not reduce

  ## if(evword == tmp){ // not reduce

  tranmain_master__filter_launcher_done.writeAction(f"__if_filter_launcher_done_9_true: evi X2 X25 main_master::init_tc 1") 
  tranmain_master__filter_launcher_done.writeAction(f"send_wret X25 main_master::init_done X26 9 X24") 
  tranmain_master__filter_launcher_done.writeAction(f"yield") 
  tranmain_master__filter_launcher_done.writeAction(f"__if_filter_launcher_done_11_post: blei X22 1 __if_filter_launcher_done_14_post") 
  tranmain_master__filter_launcher_done.writeAction(f"__if_filter_launcher_done_12_true: movir X24 2048") 
  tranmain_master__filter_launcher_done.writeAction(f"bneu X25 X24 __if_filter_launcher_done_14_post") 
  ## 1 node, switch to local

  tranmain_master__filter_launcher_done.writeAction(f"__if_filter_launcher_done_15_true: addi X7 X26 0") 
  tranmain_master__filter_launcher_done.writeAction(f"movlr 104(X26) X27 0 8") 
  tranmain_master__filter_launcher_done.writeAction(f"add X7 X23 X26") 
  tranmain_master__filter_launcher_done.writeAction(f"movrl X27 16(X26) 0 8") 
  ## switch gv to gv_local

  tranmain_master__filter_launcher_done.writeAction(f"__if_filter_launcher_done_14_post: movir X23 2048") 
  tranmain_master__filter_launcher_done.writeAction(f"bleu X25 X23 __if_filter_launcher_done_19_false") 
  ## reduce machine sizes to 1

  tranmain_master__filter_launcher_done.writeAction(f"__if_filter_launcher_done_18_true: sli X23 X24 32") 
  tranmain_master__filter_launcher_done.writeAction(f"add X24 X23 X27") 
  tranmain_master__filter_launcher_done.writeAction(f"movrl X27 0(X26) 0 8") 
  tranmain_master__filter_launcher_done.writeAction(f"div X25 X23 X27") 
  ## num_combine

  tranmain_master__filter_launcher_done.writeAction(f"movrl X27 8(X26) 0 8") 
  ## num_combine

  tranmain_master__filter_launcher_done.writeAction(f"jmp __if_filter_launcher_done_20_post") 
  tranmain_master__filter_launcher_done.writeAction(f"__if_filter_launcher_done_19_false: bneu X25 X23 __if_filter_launcher_done_22_false") 
  ## 1 node, reduce cache line

  tranmain_master__filter_launcher_done.writeAction(f"__if_filter_launcher_done_21_true: movir X24 1") 
  tranmain_master__filter_launcher_done.writeAction(f"movrl X24 8(X26) 0 8") 
  tranmain_master__filter_launcher_done.writeAction(f"addi X7 X26 0") 
  tranmain_master__filter_launcher_done.writeAction(f"movlr 0(X26) X24 0 8") 
  tranmain_master__filter_launcher_done.writeAction(f"addi X24 X27 1") 
  tranmain_master__filter_launcher_done.writeAction(f"mul X27 X23 X27") 
  ## total cache length

  tranmain_master__filter_launcher_done.writeAction(f"sli X21 X21 2") 
  tranmain_master__filter_launcher_done.writeAction(f"__while_filter_launcher_done_24_condition: ble X27 X21 __while_filter_launcher_done_26_post") 
  ## reduce cache size

  tranmain_master__filter_launcher_done.writeAction(f"__while_filter_launcher_done_25_body: sari X27 X27 1") 
  tranmain_master__filter_launcher_done.writeAction(f"jmp __while_filter_launcher_done_24_condition") 
  tranmain_master__filter_launcher_done.writeAction(f"__while_filter_launcher_done_26_post: div X27 X23 X27") 
  tranmain_master__filter_launcher_done.writeAction(f"bgti X27 4 __if_filter_launcher_done_28_false") 
  tranmain_master__filter_launcher_done.writeAction(f"__if_filter_launcher_done_27_true: movir X27 4") 
  tranmain_master__filter_launcher_done.writeAction(f"subi X27 X24 1") 
  tranmain_master__filter_launcher_done.writeAction(f"movrl X24 0(X26) 0 8") 
  tranmain_master__filter_launcher_done.writeAction(f"addi X25 X27 0") 
  tranmain_master__filter_launcher_done.writeAction(f"movir X24 2048") 
  tranmain_master__filter_launcher_done.writeAction(f"bgt X24 X27 __if_filter_launcher_done_31_false") 
  tranmain_master__filter_launcher_done.writeAction(f"__if_filter_launcher_done_30_true: movir X23 2048") 
  tranmain_master__filter_launcher_done.writeAction(f"jmp __if_filter_launcher_done_32_post") 
  tranmain_master__filter_launcher_done.writeAction(f"__if_filter_launcher_done_31_false: movir X24 1024") 
  tranmain_master__filter_launcher_done.writeAction(f"bgt X24 X27 __if_filter_launcher_done_34_false") 
  tranmain_master__filter_launcher_done.writeAction(f"__if_filter_launcher_done_33_true: movir X23 1024") 
  tranmain_master__filter_launcher_done.writeAction(f"jmp __if_filter_launcher_done_32_post") 
  tranmain_master__filter_launcher_done.writeAction(f"__if_filter_launcher_done_34_false: movir X24 512") 
  tranmain_master__filter_launcher_done.writeAction(f"bgt X24 X27 __if_filter_launcher_done_37_false") 
  tranmain_master__filter_launcher_done.writeAction(f"__if_filter_launcher_done_36_true: movir X23 512") 
  tranmain_master__filter_launcher_done.writeAction(f"jmp __if_filter_launcher_done_32_post") 
  tranmain_master__filter_launcher_done.writeAction(f"__if_filter_launcher_done_37_false: movir X24 256") 
  tranmain_master__filter_launcher_done.writeAction(f"bgt X24 X27 __if_filter_launcher_done_40_false") 
  tranmain_master__filter_launcher_done.writeAction(f"__if_filter_launcher_done_39_true: movir X23 256") 
  tranmain_master__filter_launcher_done.writeAction(f"jmp __if_filter_launcher_done_32_post") 
  tranmain_master__filter_launcher_done.writeAction(f"__if_filter_launcher_done_40_false: movir X24 128") 
  tranmain_master__filter_launcher_done.writeAction(f"bgt X24 X27 __if_filter_launcher_done_43_false") 
  tranmain_master__filter_launcher_done.writeAction(f"__if_filter_launcher_done_42_true: movir X23 128") 
  tranmain_master__filter_launcher_done.writeAction(f"jmp __if_filter_launcher_done_32_post") 
  tranmain_master__filter_launcher_done.writeAction(f"__if_filter_launcher_done_43_false: movir X24 64") 
  tranmain_master__filter_launcher_done.writeAction(f"bgt X24 X27 __if_filter_launcher_done_46_false") 
  tranmain_master__filter_launcher_done.writeAction(f"__if_filter_launcher_done_45_true: movir X23 64") 
  tranmain_master__filter_launcher_done.writeAction(f"jmp __if_filter_launcher_done_32_post") 
  tranmain_master__filter_launcher_done.writeAction(f"__if_filter_launcher_done_46_false: movir X24 32") 
  tranmain_master__filter_launcher_done.writeAction(f"bgt X24 X27 __if_filter_launcher_done_49_false") 
  tranmain_master__filter_launcher_done.writeAction(f"__if_filter_launcher_done_48_true: movir X23 32") 
  tranmain_master__filter_launcher_done.writeAction(f"jmp __if_filter_launcher_done_32_post") 
  tranmain_master__filter_launcher_done.writeAction(f"__if_filter_launcher_done_49_false: movir X24 16") 
  tranmain_master__filter_launcher_done.writeAction(f"bgt X24 X27 __if_filter_launcher_done_52_false") 
  tranmain_master__filter_launcher_done.writeAction(f"__if_filter_launcher_done_51_true: movir X23 16") 
  tranmain_master__filter_launcher_done.writeAction(f"jmp __if_filter_launcher_done_32_post") 
  tranmain_master__filter_launcher_done.writeAction(f"__if_filter_launcher_done_52_false: blti X27 8 __if_filter_launcher_done_55_false") 
  tranmain_master__filter_launcher_done.writeAction(f"__if_filter_launcher_done_54_true: movir X23 8") 
  tranmain_master__filter_launcher_done.writeAction(f"jmp __if_filter_launcher_done_32_post") 
  tranmain_master__filter_launcher_done.writeAction(f"__if_filter_launcher_done_55_false: blti X27 4 __if_filter_launcher_done_58_false") 
  tranmain_master__filter_launcher_done.writeAction(f"__if_filter_launcher_done_57_true: movir X23 4") 
  tranmain_master__filter_launcher_done.writeAction(f"jmp __if_filter_launcher_done_32_post") 
  tranmain_master__filter_launcher_done.writeAction(f"__if_filter_launcher_done_58_false: blti X27 2 __if_filter_launcher_done_32_post") 
  tranmain_master__filter_launcher_done.writeAction(f"__if_filter_launcher_done_60_true: movir X23 2") 
  tranmain_master__filter_launcher_done.writeAction(f"__if_filter_launcher_done_32_post: addi X7 X26 248") 
  tranmain_master__filter_launcher_done.writeAction(f"sli X23 X24 32") 
  tranmain_master__filter_launcher_done.writeAction(f"add X24 X23 X27") 
  tranmain_master__filter_launcher_done.writeAction(f"movrl X27 0(X26) 0 8") 
  tranmain_master__filter_launcher_done.writeAction(f"div X25 X23 X27") 
  ## num_combine

  tranmain_master__filter_launcher_done.writeAction(f"movrl X27 8(X26) 0 8") 
  ## num_combine

  tranmain_master__filter_launcher_done.writeAction(f"print 'previous lanes = %lu, next lanes = %lu' X25 X23") 
  tranmain_master__filter_launcher_done.writeAction(f"jmp __if_filter_launcher_done_29_post") 
  tranmain_master__filter_launcher_done.writeAction(f"__if_filter_launcher_done_28_false: subi X27 X24 1") 
  tranmain_master__filter_launcher_done.writeAction(f"movrl X24 0(X26) 0 8") 
  tranmain_master__filter_launcher_done.writeAction(f"__if_filter_launcher_done_29_post: jmp __if_filter_launcher_done_20_post") 
  tranmain_master__filter_launcher_done.writeAction(f"__if_filter_launcher_done_22_false: movir X24 2048") 
  tranmain_master__filter_launcher_done.writeAction(f"bgt X24 X27 __if_filter_launcher_done_64_false") 
  tranmain_master__filter_launcher_done.writeAction(f"__if_filter_launcher_done_63_true: movir X23 2048") 
  tranmain_master__filter_launcher_done.writeAction(f"jmp __if_filter_launcher_done_65_post") 
  tranmain_master__filter_launcher_done.writeAction(f"__if_filter_launcher_done_64_false: movir X24 1024") 
  tranmain_master__filter_launcher_done.writeAction(f"bgt X24 X27 __if_filter_launcher_done_67_false") 
  tranmain_master__filter_launcher_done.writeAction(f"__if_filter_launcher_done_66_true: movir X23 1024") 
  tranmain_master__filter_launcher_done.writeAction(f"jmp __if_filter_launcher_done_65_post") 
  tranmain_master__filter_launcher_done.writeAction(f"__if_filter_launcher_done_67_false: movir X24 512") 
  tranmain_master__filter_launcher_done.writeAction(f"bgt X24 X27 __if_filter_launcher_done_70_false") 
  tranmain_master__filter_launcher_done.writeAction(f"__if_filter_launcher_done_69_true: movir X23 512") 
  tranmain_master__filter_launcher_done.writeAction(f"jmp __if_filter_launcher_done_65_post") 
  tranmain_master__filter_launcher_done.writeAction(f"__if_filter_launcher_done_70_false: movir X24 256") 
  tranmain_master__filter_launcher_done.writeAction(f"bgt X24 X27 __if_filter_launcher_done_73_false") 
  tranmain_master__filter_launcher_done.writeAction(f"__if_filter_launcher_done_72_true: movir X23 256") 
  tranmain_master__filter_launcher_done.writeAction(f"jmp __if_filter_launcher_done_65_post") 
  tranmain_master__filter_launcher_done.writeAction(f"__if_filter_launcher_done_73_false: movir X24 128") 
  tranmain_master__filter_launcher_done.writeAction(f"bgt X24 X27 __if_filter_launcher_done_76_false") 
  tranmain_master__filter_launcher_done.writeAction(f"__if_filter_launcher_done_75_true: movir X23 128") 
  tranmain_master__filter_launcher_done.writeAction(f"jmp __if_filter_launcher_done_65_post") 
  tranmain_master__filter_launcher_done.writeAction(f"__if_filter_launcher_done_76_false: movir X24 64") 
  tranmain_master__filter_launcher_done.writeAction(f"bgt X24 X27 __if_filter_launcher_done_79_false") 
  tranmain_master__filter_launcher_done.writeAction(f"__if_filter_launcher_done_78_true: movir X23 64") 
  tranmain_master__filter_launcher_done.writeAction(f"jmp __if_filter_launcher_done_65_post") 
  tranmain_master__filter_launcher_done.writeAction(f"__if_filter_launcher_done_79_false: movir X24 32") 
  tranmain_master__filter_launcher_done.writeAction(f"bgt X24 X27 __if_filter_launcher_done_82_false") 
  tranmain_master__filter_launcher_done.writeAction(f"__if_filter_launcher_done_81_true: movir X23 32") 
  tranmain_master__filter_launcher_done.writeAction(f"jmp __if_filter_launcher_done_65_post") 
  tranmain_master__filter_launcher_done.writeAction(f"__if_filter_launcher_done_82_false: movir X24 16") 
  tranmain_master__filter_launcher_done.writeAction(f"bgt X24 X27 __if_filter_launcher_done_85_false") 
  tranmain_master__filter_launcher_done.writeAction(f"__if_filter_launcher_done_84_true: movir X23 16") 
  tranmain_master__filter_launcher_done.writeAction(f"jmp __if_filter_launcher_done_65_post") 
  tranmain_master__filter_launcher_done.writeAction(f"__if_filter_launcher_done_85_false: blti X27 8 __if_filter_launcher_done_88_false") 
  tranmain_master__filter_launcher_done.writeAction(f"__if_filter_launcher_done_87_true: movir X23 8") 
  tranmain_master__filter_launcher_done.writeAction(f"jmp __if_filter_launcher_done_65_post") 
  tranmain_master__filter_launcher_done.writeAction(f"__if_filter_launcher_done_88_false: blti X27 4 __if_filter_launcher_done_91_false") 
  tranmain_master__filter_launcher_done.writeAction(f"__if_filter_launcher_done_90_true: movir X23 4") 
  tranmain_master__filter_launcher_done.writeAction(f"jmp __if_filter_launcher_done_65_post") 
  tranmain_master__filter_launcher_done.writeAction(f"__if_filter_launcher_done_91_false: blti X27 2 __if_filter_launcher_done_65_post") 
  tranmain_master__filter_launcher_done.writeAction(f"__if_filter_launcher_done_93_true: movir X23 2") 
  tranmain_master__filter_launcher_done.writeAction(f"__if_filter_launcher_done_65_post: sli X23 X24 32") 
  tranmain_master__filter_launcher_done.writeAction(f"add X24 X23 X27") 
  tranmain_master__filter_launcher_done.writeAction(f"movrl X27 0(X26) 0 8") 
  tranmain_master__filter_launcher_done.writeAction(f"div X25 X23 X27") 
  ## num_combine

  tranmain_master__filter_launcher_done.writeAction(f"movrl X27 8(X26) 0 8") 
  ## num_combine

  tranmain_master__filter_launcher_done.writeAction(f"__if_filter_launcher_done_20_post: addi X7 X26 0") 
  tranmain_master__filter_launcher_done.writeAction(f"movlr 0(X26) X24 0 8") 
  tranmain_master__filter_launcher_done.writeAction(f"addi X24 X27 1") 
  tranmain_master__filter_launcher_done.writeAction(f"print 'cache len = %ld' X27") 
  tranmain_master__filter_launcher_done.writeAction(f"addi X7 X26 248") 
  tranmain_master__filter_launcher_done.writeAction(f"movlr 8(X26) X23 0 8") 
  ## num_combine

  tranmain_master__filter_launcher_done.writeAction(f"sli X23 X24 32") 
  tranmain_master__filter_launcher_done.writeAction(f"add X24 X27 X23") 
  ## num_combine: cache_size

  tranmain_master__filter_launcher_done.writeAction(f"movrl X23 8(X26) 0 8") 
  tranmain_master__filter_launcher_done.writeAction(f"evi X2 X25 main_master::init_tc 1") 
  tranmain_master__filter_launcher_done.writeAction(f"send_wret X25 main_master::init_done X26 9 X23") 
  tranmain_master__filter_launcher_done.writeAction(f"yield") 
  tranmain_master__filter_launcher_done.writeAction(f"jmp __if_filter_launcher_done_2_post") 
  ## if(num_lanes_per_control == 1){

  ##     print("deleted_edges %lu, update_edges %lu", tc_cumulative, num_vertices);

  ## }

  tranmain_master__filter_launcher_done.writeAction(f"__if_filter_launcher_done_4_false: sli X18 X25 1") 
  tranmain_master__filter_launcher_done.writeAction(f"movir X23 65264") 
  tranmain_master__filter_launcher_done.writeAction(f"add X7 X23 X26") 
  tranmain_master__filter_launcher_done.writeAction(f"addi X25 X25 1") 
  tranmain_master__filter_launcher_done.writeAction(f"movwlr X26(X25,0,0) X25") 
  tranmain_master__filter_launcher_done.writeAction(f"movir X23 -1") 
  tranmain_master__filter_launcher_done.writeAction(f"sri X23 X23 1") 
  tranmain_master__filter_launcher_done.writeAction(f"sendr_wcont X25 X23 X16 X21") 
  tranmain_master__filter_launcher_done.writeAction(f"yield_terminate") 
  tranmain_master__filter_launcher_done.writeAction(f"__if_filter_launcher_done_2_post: yield") 
  