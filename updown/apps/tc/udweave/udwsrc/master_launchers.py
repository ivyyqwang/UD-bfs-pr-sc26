from linker.EFAProgram import efaProgram

## UDWeave version: 02d7c60 (2026-01-27)

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
  ## This is all metadata information
  ## #define DEBUG
  ## #define PRINT_intersect_result
  ## #define NO_ADVANCED_STOP
  ## This is all metadata information
  ## Total threads used in TC
  ## #define WORKER_THREADS 120
  ## #define NUM_MASTERS 8
  ## #define NUM_INTERSECTORS 112
  ## Each threads in the same lane shared the following scratchpad
  ## send buffer 4 - 18 (15 words)
  ## master, intersection launcher offsets
  ## Each thread's own private scratchpad size: [(THREAD_STATUS << 3) + TID * THREAD_LM_SIZE, (THREAD_STATUS << 3) + (TID+1) * THREAD_LM_SIZE]
  
  #####################################################
  ###### Writing code for thread master_launcher ######
  #####################################################
  # Writing code for event master_launcher::init
  tranmaster_launcher__init = efa.writeEvent('master_launcher::init')
  tranmaster_launcher__init.writeAction(f"__entry: subi X11 X20 8") 
  tranmaster_launcher__init.writeAction(f"send_dmlm_ld_wret X20 master_launcher::read_master_dram_length 1 X21") 
  tranmaster_launcher__init.writeAction(f"movir X20 0") 
  tranmaster_launcher__init.writeAction(f"evlb X20 intersection_launcher__intersection_init") 
  tranmaster_launcher__init.writeAction(f"evi X20 X20 255 4") 
  tranmaster_launcher__init.writeAction(f"ev X20 X20 X0 X0 8") 
  tranmaster_launcher__init.writeAction(f"sendr3_wret X20 master_launcher::intersection_init_done X10 X13 X14 X21") 
  tranmaster_launcher__init.writeAction(f"movir X16 2") 
  tranmaster_launcher__init.writeAction(f"movir X20 65504") 
  tranmaster_launcher__init.writeAction(f"add X7 X20 X19") 
  tranmaster_launcher__init.writeAction(f"sri X2 X20 24") 
  tranmaster_launcher__init.writeAction(f"andi X20 X20 255") 
  tranmaster_launcher__init.writeAction(f"movrl X20 0(X19) 0 8") 
  tranmaster_launcher__init.writeAction(f"addi X7 X19 160") 
  tranmaster_launcher__init.writeAction(f"movir X20 0") 
  tranmaster_launcher__init.writeAction(f"movrl X20 8(X19) 0 8") 
  tranmaster_launcher__init.writeAction(f"movrl X1 0(X19) 0 8") 
  tranmaster_launcher__init.writeAction(f"movrl X11 16(X19) 0 8") 
  tranmaster_launcher__init.writeAction(f"add X11 X12 X20") 
  tranmaster_launcher__init.writeAction(f"movrl X20 24(X19) 0 8") 
  tranmaster_launcher__init.writeAction(f"addi X11 X17 0") 
  tranmaster_launcher__init.writeAction(f"addi X11 X18 0") 
  tranmaster_launcher__init.writeAction(f"addi X7 X20 0") 
  tranmaster_launcher__init.writeAction(f"movrl X9 136(X20) 0 8") 
  tranmaster_launcher__init.writeAction(f"movir X21 0") 
  tranmaster_launcher__init.writeAction(f"movrl X21 144(X20) 0 8") 
  tranmaster_launcher__init.writeAction(f"movir X21 0") 
  tranmaster_launcher__init.writeAction(f"movrl X21 8(X20) 0 8") 
  tranmaster_launcher__init.writeAction(f"movrl X15 16(X20) 0 8") 
  tranmaster_launcher__init.writeAction(f"movrl X8 24(X20) 0 8") 
  tranmaster_launcher__init.writeAction(f"yield") 
  
  # Writing code for event master_launcher::read_master_dram_length
  tranmaster_launcher__read_master_dram_length = efa.writeEvent('master_launcher::read_master_dram_length')
  tranmaster_launcher__read_master_dram_length.writeAction(f"__entry: subi X16 X16 1") 
  tranmaster_launcher__read_master_dram_length.writeAction(f"bnei X16 0 __if_read_master_dram_length_2_post") 
  ## return to global master after both launchers have been started

  tranmaster_launcher__read_master_dram_length.writeAction(f"__if_read_master_dram_length_0_true: movlr 0(X19) X20 0 8") 
  tranmaster_launcher__read_master_dram_length.writeAction(f"movir X21 -1") 
  tranmaster_launcher__read_master_dram_length.writeAction(f"sri X21 X21 1") 
  tranmaster_launcher__read_master_dram_length.writeAction(f"sendr_wcont X20 X21 X0 X0") 
  tranmaster_launcher__read_master_dram_length.writeAction(f"movir X20 1") 
  tranmaster_launcher__read_master_dram_length.writeAction(f"movrl X20 8(X19) 0 8") 
  tranmaster_launcher__read_master_dram_length.writeAction(f"__if_read_master_dram_length_2_post: sli X8 X20 3") 
  tranmaster_launcher__read_master_dram_length.writeAction(f"add X18 X20 X17") 
  tranmaster_launcher__read_master_dram_length.writeAction(f"yield") 
  
  # Writing code for event master_launcher::intersection_init_done
  tranmaster_launcher__intersection_init_done = efa.writeEvent('master_launcher::intersection_init_done')
  tranmaster_launcher__intersection_init_done.writeAction(f"__entry: subi X16 X16 1") 
  tranmaster_launcher__intersection_init_done.writeAction(f"bnei X16 0 __if_intersection_init_done_2_post") 
  ## return to global master after both launchers have been started

  tranmaster_launcher__intersection_init_done.writeAction(f"__if_intersection_init_done_0_true: movlr 0(X19) X20 0 8") 
  tranmaster_launcher__intersection_init_done.writeAction(f"movir X21 -1") 
  tranmaster_launcher__intersection_init_done.writeAction(f"sri X21 X21 1") 
  tranmaster_launcher__intersection_init_done.writeAction(f"sendr_wcont X20 X21 X0 X0") 
  tranmaster_launcher__intersection_init_done.writeAction(f"movir X20 1") 
  tranmaster_launcher__intersection_init_done.writeAction(f"movrl X20 8(X19) 0 8") 
  tranmaster_launcher__intersection_init_done.writeAction(f"__if_intersection_init_done_2_post: yield") 
  
  # Writing code for event master_launcher::launch_v
  tranmaster_launcher__launch_v = efa.writeEvent('master_launcher::launch_v')
  tranmaster_launcher__launch_v.writeAction(f"__entry: addi X7 X20 0") 
  tranmaster_launcher__launch_v.writeAction(f"subi X8 X21 1") 
  tranmaster_launcher__launch_v.writeAction(f"movrl X21 152(X20) 0 8") 
  tranmaster_launcher__launch_v.writeAction(f"movlr 136(X20) X20 0 8") 
  tranmaster_launcher__launch_v.writeAction(f"movrl X1 0(X19) 0 8") 
  tranmaster_launcher__launch_v.writeAction(f"addi X17 X21 0") 
  tranmaster_launcher__launch_v.writeAction(f"addi X18 X22 0") 
  tranmaster_launcher__launch_v.writeAction(f"sub X21 X22 X21") 
  tranmaster_launcher__launch_v.writeAction(f"sari X21 X21 3") 
  tranmaster_launcher__launch_v.writeAction(f"movir X16 0") 
  tranmaster_launcher__launch_v.writeAction(f"__while_launch_v_0_condition: clt X16 X20 X22") 
  tranmaster_launcher__launch_v.writeAction(f"clt X16 X21 X23") 
  tranmaster_launcher__launch_v.writeAction(f"and X22 X23 X22") 
  tranmaster_launcher__launch_v.writeAction(f"beqi X22 0 __while_launch_v_2_post") 
  tranmaster_launcher__launch_v.writeAction(f"__while_launch_v_1_body: send_dmlm_ld_wret X18 master_launcher::receive_dram 1 X22") 
  tranmaster_launcher__launch_v.writeAction(f"addi X18 X18 8") 
  tranmaster_launcher__launch_v.writeAction(f"addi X16 X16 1") 
  tranmaster_launcher__launch_v.writeAction(f"jmp __while_launch_v_0_condition") 
  tranmaster_launcher__launch_v.writeAction(f"__while_launch_v_2_post: bnei X21 0 __if_launch_v_5_post") 
  tranmaster_launcher__launch_v.writeAction(f"__if_launch_v_3_true: movlr 0(X19) X20 0 8") 
  tranmaster_launcher__launch_v.writeAction(f"movir X22 -1") 
  tranmaster_launcher__launch_v.writeAction(f"sri X22 X22 1") 
  tranmaster_launcher__launch_v.writeAction(f"sendr_wcont X20 X22 X0 X0") 
  tranmaster_launcher__launch_v.writeAction(f"movir X20 2") 
  tranmaster_launcher__launch_v.writeAction(f"movrl X20 8(X19) 0 8") 
  tranmaster_launcher__launch_v.writeAction(f"__if_launch_v_5_post: bne X16 X21 __if_launch_v_8_post") 
  tranmaster_launcher__launch_v.writeAction(f"__if_launch_v_6_true: movir X21 2") 
  tranmaster_launcher__launch_v.writeAction(f"movrl X21 8(X19) 0 8") 
  tranmaster_launcher__launch_v.writeAction(f"__if_launch_v_8_post: yield") 
  
  # Writing code for event master_launcher::receive_dram
  tranmaster_launcher__receive_dram = efa.writeEvent('master_launcher::receive_dram')
  tranmaster_launcher__receive_dram.writeAction(f"__entry: movir X21 0") 
  tranmaster_launcher__receive_dram.writeAction(f"evlb X21 vertex_master__launch") 
  tranmaster_launcher__receive_dram.writeAction(f"evi X21 X21 255 4") 
  tranmaster_launcher__receive_dram.writeAction(f"ev X21 X21 X0 X0 8") 
  tranmaster_launcher__receive_dram.writeAction(f"addi X7 X20 0") 
  tranmaster_launcher__receive_dram.writeAction(f"movlr 16(X20) X20 0 8") 
  tranmaster_launcher__receive_dram.writeAction(f"sendr_wret X21 master_launcher::vertex_term X20 X8 X22") 
  tranmaster_launcher__receive_dram.writeAction(f"yield") 
  
  # Writing code for event master_launcher::vertex_term
  tranmaster_launcher__vertex_term = efa.writeEvent('master_launcher::vertex_term')
  ## vertex thread terminated

  tranmaster_launcher__vertex_term.writeAction(f"__entry: subi X16 X16 1") 
  tranmaster_launcher__vertex_term.writeAction(f"bneu X18 X17 __if_vertex_term_2_post") 
  ## head == tail So nothing more to launch! 

  tranmaster_launcher__vertex_term.writeAction(f"__if_vertex_term_0_true: movir X21 2") 
  tranmaster_launcher__vertex_term.writeAction(f"movrl X21 8(X19) 0 8") 
  tranmaster_launcher__vertex_term.writeAction(f"bnei X16 0 __if_vertex_term_5_post") 
  tranmaster_launcher__vertex_term.writeAction(f"__if_vertex_term_3_true: movlr 0(X19) X21 0 8") 
  tranmaster_launcher__vertex_term.writeAction(f"movir X20 -1") 
  tranmaster_launcher__vertex_term.writeAction(f"sri X20 X20 1") 
  tranmaster_launcher__vertex_term.writeAction(f"sendr_wcont X21 X20 X0 X0") 
  tranmaster_launcher__vertex_term.writeAction(f"__if_vertex_term_5_post: yield") 
  ## Check if there's stuff in memory

  tranmaster_launcher__vertex_term.writeAction(f"__if_vertex_term_2_post: addi X7 X21 0") 
  tranmaster_launcher__vertex_term.writeAction(f"movlr 136(X21) X21 0 8") 
  tranmaster_launcher__vertex_term.writeAction(f"__while_vertex_term_6_condition: ceq X18 X17 X20") 
  tranmaster_launcher__vertex_term.writeAction(f"xori X20 X20 1") 
  tranmaster_launcher__vertex_term.writeAction(f"clt X16 X21 X22") 
  tranmaster_launcher__vertex_term.writeAction(f"and X20 X22 X20") 
  tranmaster_launcher__vertex_term.writeAction(f"beqi X20 0 __while_vertex_term_8_post") 
  tranmaster_launcher__vertex_term.writeAction(f"__while_vertex_term_7_body: send_dmlm_ld_wret X18 master_launcher::receive_dram 1 X20") 
  tranmaster_launcher__vertex_term.writeAction(f"addi X18 X18 8") 
  tranmaster_launcher__vertex_term.writeAction(f"addi X16 X16 1") 
  tranmaster_launcher__vertex_term.writeAction(f"jmp __while_vertex_term_6_condition") 
  tranmaster_launcher__vertex_term.writeAction(f"__while_vertex_term_8_post: bneu X18 X17 __if_vertex_term_11_post") 
  tranmaster_launcher__vertex_term.writeAction(f"__if_vertex_term_9_true: movir X21 2") 
  tranmaster_launcher__vertex_term.writeAction(f"movrl X21 8(X19) 0 8") 
  ## if(NETID == 0){

  ##     print("[DEBUG][NWID %lu] <vertex_term> test 0x%lx 0x%lx %lu %lu", NETID, master_dram_head_ptr, master_dram_tail_ptr, num_threads_active , num_threads_total);

  ## }

  tranmaster_launcher__vertex_term.writeAction(f"__if_vertex_term_11_post: yield") 
  
  # Writing code for event master_launcher::relaunch
  tranmaster_launcher__relaunch = efa.writeEvent('master_launcher::relaunch')
  tranmaster_launcher__relaunch.writeAction(f"__entry: addi X7 X21 0") 
  tranmaster_launcher__relaunch.writeAction(f"movlr 136(X21) X21 0 8") 
  tranmaster_launcher__relaunch.writeAction(f"__while_relaunch_0_condition: ceq X18 X17 X20") 
  tranmaster_launcher__relaunch.writeAction(f"xori X20 X20 1") 
  tranmaster_launcher__relaunch.writeAction(f"clt X16 X21 X22") 
  tranmaster_launcher__relaunch.writeAction(f"and X20 X22 X20") 
  tranmaster_launcher__relaunch.writeAction(f"beqi X20 0 __while_relaunch_2_post") 
  tranmaster_launcher__relaunch.writeAction(f"__while_relaunch_1_body: send_dmlm_ld_wret X18 master_launcher::receive_dram 1 X20") 
  tranmaster_launcher__relaunch.writeAction(f"addi X18 X18 8") 
  tranmaster_launcher__relaunch.writeAction(f"addi X16 X16 1") 
  tranmaster_launcher__relaunch.writeAction(f"jmp __while_relaunch_0_condition") 
  tranmaster_launcher__relaunch.writeAction(f"__while_relaunch_2_post: bneu X18 X17 __if_relaunch_5_post") 
  tranmaster_launcher__relaunch.writeAction(f"__if_relaunch_3_true: movir X21 2") 
  tranmaster_launcher__relaunch.writeAction(f"movrl X21 8(X19) 0 8") 
  ## if(NETID == 0){

  ##     print("[DEBUG][NWID %lu] <relaunch> test 0x%lx 0x%lx %lu %lu", NETID, master_dram_head_ptr, master_dram_tail_ptr, num_threads_active , num_threads_total);

  ## }

  tranmaster_launcher__relaunch.writeAction(f"__if_relaunch_5_post: yield") 
  
  # Writing code for event master_launcher::all_launched
  tranmaster_launcher__all_launched = efa.writeEvent('master_launcher::all_launched')
  tranmaster_launcher__all_launched.writeAction(f"__entry: movir X21 3") 
  tranmaster_launcher__all_launched.writeAction(f"movrl X21 8(X19) 0 8") 
  tranmaster_launcher__all_launched.writeAction(f"addi X7 X21 0") 
  tranmaster_launcher__all_launched.writeAction(f"movlr 144(X21) X21 0 8") 
  tranmaster_launcher__all_launched.writeAction(f"movrl X1 0(X19) 0 8") 
  tranmaster_launcher__all_launched.writeAction(f"bneiu X21 0 __if_all_launched_2_post") 
  tranmaster_launcher__all_launched.writeAction(f"__if_all_launched_0_true: movir X20 -1") 
  tranmaster_launcher__all_launched.writeAction(f"sri X20 X20 1") 
  tranmaster_launcher__all_launched.writeAction(f"sendr_wcont X1 X20 X21 X21") 
  ## print("[DEBUG][NWID %lu] <all_launched>: num_int = %lu", NETID, num_int);

  tranmaster_launcher__all_launched.writeAction(f"yield_terminate") 
  tranmaster_launcher__all_launched.writeAction(f"__if_all_launched_2_post: yield") 
  
  # Writing code for event master_launcher::reduce_num_int
  tranmaster_launcher__reduce_num_int = efa.writeEvent('master_launcher::reduce_num_int')
  tranmaster_launcher__reduce_num_int.writeAction(f"__entry: addi X7 X21 0") 
  tranmaster_launcher__reduce_num_int.writeAction(f"movlr 144(X21) X20 0 8") 
  tranmaster_launcher__reduce_num_int.writeAction(f"subi X20 X20 1") 
  tranmaster_launcher__reduce_num_int.writeAction(f"movrl X20 144(X21) 0 8") 
  tranmaster_launcher__reduce_num_int.writeAction(f"movlr 8(X21) X22 0 8") 
  tranmaster_launcher__reduce_num_int.writeAction(f"add X22 X8 X22") 
  tranmaster_launcher__reduce_num_int.writeAction(f"movrl X22 8(X21) 0 8") 
  ## if(NETID == 47){

  ##     print("[DEBUG][NWID %lu] <reduce_num_int>: num_int = %lu", NETID, num_int);

  ## }

  tranmaster_launcher__reduce_num_int.writeAction(f"bneiu X20 0 __if_reduce_num_int_2_post") 
  tranmaster_launcher__reduce_num_int.writeAction(f"__if_reduce_num_int_0_true: movlr 8(X19) X21 0 8") 
  tranmaster_launcher__reduce_num_int.writeAction(f"bneiu X21 3 __if_reduce_num_int_2_post") 
  tranmaster_launcher__reduce_num_int.writeAction(f"__if_reduce_num_int_3_true: movlr 0(X19) X21 0 8") 
  tranmaster_launcher__reduce_num_int.writeAction(f"movir X22 -1") 
  tranmaster_launcher__reduce_num_int.writeAction(f"sri X22 X22 1") 
  tranmaster_launcher__reduce_num_int.writeAction(f"sendr_wcont X21 X22 X20 X20") 
  ## print("[DEBUG][NWID %lu] <reduce_num_int>: num_int = %lu", NETID, num_int);

  tranmaster_launcher__reduce_num_int.writeAction(f"yield_terminate") 
  tranmaster_launcher__reduce_num_int.writeAction(f"__if_reduce_num_int_2_post: yield") 
  
  # Writing code for event master_launcher::send_to_master_thread1
  tranmaster_launcher__send_to_master_thread1 = efa.writeEvent('master_launcher::send_to_master_thread1')
  tranmaster_launcher__send_to_master_thread1.writeAction(f"__entry: movir X20 65504") 
  tranmaster_launcher__send_to_master_thread1.writeAction(f"add X7 X20 X20") 
  tranmaster_launcher__send_to_master_thread1.writeAction(f"movlr 0(X20) X20 0 8") 
  tranmaster_launcher__send_to_master_thread1.writeAction(f"addi X20 X20 0")  # This is for casting. May be used later on
  tranmaster_launcher__send_to_master_thread1.writeAction(f"ev X8 X20 X20 X20 4") 
  tranmaster_launcher__send_to_master_thread1.writeAction(f"sendr_wcont X20 X1 X9 X9") 
  tranmaster_launcher__send_to_master_thread1.writeAction(f"yield_terminate") 
  
  ##     event send_to_master_thread2(long op0, long op1, long op2){
  ##         unsigned long* local tmp_lmbuff = LMBASE + MASTER_THREADID_OFFSET;
  ##         int tid = tmp_lmbuff[0];
  ## #ifdef DEBUG
  ##         print("[DEBUG][NWID %lu] <send_to_worker_thread2> tid:%ld, CCONT=%lu", NETID, tid, CCONT);
  ## #endif
  ##         unsigned long evword = evw_update_thread(op0, tid);
  ##         send_event(evword, op1, op2, CCONT);
  ## #ifdef DEBUG
  ##         print("[DEBUG][NWID %lu] <send_to_worker_thread2> op1:%lu, op2=%lu", NETID, op1, op2);
  ## #endif
  ##         yield_terminate;
  ##     }