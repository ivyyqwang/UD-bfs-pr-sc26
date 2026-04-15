from linker.EFAProgram import efaProgram

## UDWeave version: 02d7c60 (2026-01-27)

## Global constants

@efaProgram
def EFA_intersection_launchers(efa):
  efa.code_level = 'machine'
  state0 = efa.State("udweave_init") #Only one state code 
  efa.add_initId(state0.state_id)
  ## Static declarations
  ## Scoped Variable "num_threads_total" uses Register X16, scope (0)
  ## Scoped Variable "num_threads_active" uses Register X17, scope (0)
  ## Scoped Variable "int_dram_tail_ptr" uses Register X18, scope (0)
  ## Scoped Variable "int_dram_head_ptr" uses Register X19, scope (0)
  ## Scoped Variable "num_outstanding" uses Register X20, scope (0)
  ## Scoped Variable "lmbuff" uses Register X21, scope (0)
  ## Scoped Variable "half_intersection_len" uses Register X22, scope (0)
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
  ## #define DEBUG
  
  ###########################################################
  ###### Writing code for thread intersection_launcher ######
  ###########################################################
  # Writing code for event intersection_launcher::intersection_init
  tranintersection_launcher__intersection_init = efa.writeEvent('intersection_launcher::intersection_init')
  ## return to master launcher

  tranintersection_launcher__intersection_init.writeAction(f"__entry: movir X23 -1") 
  tranintersection_launcher__intersection_init.writeAction(f"sri X23 X23 1") 
  tranintersection_launcher__intersection_init.writeAction(f"sendr_wcont X1 X23 X8 X8") 
  tranintersection_launcher__intersection_init.writeAction(f"movir X23 65512") 
  tranintersection_launcher__intersection_init.writeAction(f"add X7 X23 X21") 
  tranintersection_launcher__intersection_init.writeAction(f"sri X2 X23 24") 
  tranintersection_launcher__intersection_init.writeAction(f"andi X23 X23 255") 
  tranintersection_launcher__intersection_init.writeAction(f"movrl X23 0(X21) 0 8") 
  tranintersection_launcher__intersection_init.writeAction(f"addi X7 X21 192") 
  tranintersection_launcher__intersection_init.writeAction(f"movir X23 0") 
  tranintersection_launcher__intersection_init.writeAction(f"movrl X23 8(X21) 0 8") 
  tranintersection_launcher__intersection_init.writeAction(f"movrl X1 0(X21) 0 8") 
  tranintersection_launcher__intersection_init.writeAction(f"addi X9 X23 0") 
  tranintersection_launcher__intersection_init.writeAction(f"movrl X23 16(X21) 0 8") 
  tranintersection_launcher__intersection_init.writeAction(f"add X9 X10 X23") 
  tranintersection_launcher__intersection_init.writeAction(f"movrl X23 24(X21) 0 8") 
  tranintersection_launcher__intersection_init.writeAction(f"addi X9 X18 0") 
  tranintersection_launcher__intersection_init.writeAction(f"addi X9 X19 0") 
  tranintersection_launcher__intersection_init.writeAction(f"movir X20 0") 
  tranintersection_launcher__intersection_init.writeAction(f"addi X8 X16 0") 
  tranintersection_launcher__intersection_init.writeAction(f"movir X17 0") 
  tranintersection_launcher__intersection_init.writeAction(f"sari X10 X22 7") 
  ## 4 words, 32 B (not half, now is 1/4)

  ## half_intersection_len = 0;  

  tranintersection_launcher__intersection_init.writeAction(f"yield") 
  
  # Writing code for event intersection_launcher::receive
  tranintersection_launcher__receive = efa.writeEvent('intersection_launcher::receive')
  ## check if all threads are active

  ## check for a free thread

  ## launch master 

  ## else save in dram 

  ## update pointers (check for roll over)

  ##  vertex_master --> event launch (long lm_offset, long* g_v, long v1){

  ##print("[DEBUG][NWID %lu] <intersection_receive> received (%lu, %lu)", NETID, v1, v2);

  ## if(return_nid == 47){

  ## 	print("[DEBUG][NWID %lu] <intersection_receive> received (%lu, %lu, %lu)", NETID, v1, v2, threshold);

  ## }

  tranintersection_launcher__receive.writeAction(f"__entry: ble X16 X17 __if_receive_1_false") 
  tranintersection_launcher__receive.writeAction(f"__if_receive_0_true: movir X23 0") 
  tranintersection_launcher__receive.writeAction(f"evlb X23 v1v2intersection__launch") 
  tranintersection_launcher__receive.writeAction(f"evi X23 X23 255 4") 
  tranintersection_launcher__receive.writeAction(f"ev X23 X23 X0 X0 8") 
  tranintersection_launcher__receive.writeAction(f"addi X7 X24 0") 
  tranintersection_launcher__receive.writeAction(f"movlr 16(X24) X25 0 8") 
  tranintersection_launcher__receive.writeAction(f"addi X7 X24 32") 
  tranintersection_launcher__receive.writeAction(f"movir X26 0") 
  tranintersection_launcher__receive.writeAction(f"movrl X26 0(X24) 0 8") 
  tranintersection_launcher__receive.writeAction(f"movrl X25 8(X24) 0 8") 
  ## temp_lmbuff[2] = v1;

  ## temp_lmbuff[3] = v2;

  ## temp_lmbuff[4] = threshold;

  ## temp_lmbuff[5] = return_nid;

  tranintersection_launcher__receive.writeAction(f"addi X24 X25 16") 
  tranintersection_launcher__receive.writeAction(f"bcpyoli X8 X25 4") 
  tranintersection_launcher__receive.writeAction(f"send_wret X23 intersection_launcher::intersection_term X24 6 X25") 
  tranintersection_launcher__receive.writeAction(f"addi X17 X17 1") 
  tranintersection_launcher__receive.writeAction(f"yield") 
  tranintersection_launcher__receive.writeAction(f"jmp __if_receive_2_post") 
  ## no thread active save in memory

  tranintersection_launcher__receive.writeAction(f"__if_receive_1_false: cgti X20 X23 0") 
  tranintersection_launcher__receive.writeAction(f"ceq X19 X18 X24") 
  tranintersection_launcher__receive.writeAction(f"and X23 X24 X23") 
  tranintersection_launcher__receive.writeAction(f"beqi X23 0 __if_receive_5_post") 
  tranintersection_launcher__receive.writeAction(f"__if_receive_3_true: print '[DEBUG][NWID %lu] buffer is full' X0") 
  tranintersection_launcher__receive.writeAction(f"addi X7 X23 32") 
  tranintersection_launcher__receive.writeAction(f"movrl X8 0(X23) 0 8") 
  tranintersection_launcher__receive.writeAction(f"movrl X9 8(X23) 0 8") 
  tranintersection_launcher__receive.writeAction(f"movrl X10 16(X23) 0 8") 
  tranintersection_launcher__receive.writeAction(f"movrl X11 24(X23) 0 8") 
  tranintersection_launcher__receive.writeAction(f"send_wcont X2 X1 X23 4") 
  tranintersection_launcher__receive.writeAction(f"yield") 
  tranintersection_launcher__receive.writeAction(f"__if_receive_5_post: addi X20 X20 1") 
  ##     print("[DEBUG][NWID %lu] <intersection_receive> buffer in dram:%lu (%lu,%lu), num_outstanding: %lu", NETID, int_dram_tail_ptr, dram_start, dram_end, num_outstanding);

  tranintersection_launcher__receive.writeAction(f"addi X7 X23 32") 
  tranintersection_launcher__receive.writeAction(f"movrl X8 0(X23) 0 8") 
  tranintersection_launcher__receive.writeAction(f"movrl X9 8(X23) 0 8") 
  tranintersection_launcher__receive.writeAction(f"addi X10 X24 1") 
  tranintersection_launcher__receive.writeAction(f"movrl X24 16(X23) 0 8") 
  tranintersection_launcher__receive.writeAction(f"movrl X11 24(X23) 0 8") 
  tranintersection_launcher__receive.writeAction(f"send_dmlm_wret X18 intersection_launcher::v1v2_write_return X23 4 X24") 
  tranintersection_launcher__receive.writeAction(f"addi X18 X18 32") 
  tranintersection_launcher__receive.writeAction(f"movlr 24(X21) X24 0 8") 
  tranintersection_launcher__receive.writeAction(f"bgtu X24 X18 __if_receive_8_post") 
  tranintersection_launcher__receive.writeAction(f"__if_receive_6_true: movlr 16(X21) X24 0 8") 
  tranintersection_launcher__receive.writeAction(f"addi X24 X18 0") 
  tranintersection_launcher__receive.writeAction(f"__if_receive_8_post: ble X20 X22 __if_receive_11_post") 
  tranintersection_launcher__receive.writeAction(f"__if_receive_9_true: addi X7 X23 0") 
  tranintersection_launcher__receive.writeAction(f"movir X24 0") 
  tranintersection_launcher__receive.writeAction(f"movrl X24 136(X23) 0 8") 
  tranintersection_launcher__receive.writeAction(f"__if_receive_11_post: yield") 
  tranintersection_launcher__receive.writeAction(f"__if_receive_2_post: yield") 
  
  # Writing code for event intersection_launcher::receive_from_dram
  tranintersection_launcher__receive_from_dram = efa.writeEvent('intersection_launcher::receive_from_dram')
  tranintersection_launcher__receive_from_dram.writeAction(f"__entry: bnei X10 0 __if_receive_from_dram_2_post") 
  tranintersection_launcher__receive_from_dram.writeAction(f"__if_receive_from_dram_0_true: send_dmlm_ld_wret X12 intersection_launcher::receive_from_dram 4 X23") 
  tranintersection_launcher__receive_from_dram.writeAction(f"yield") 
  ## print("[DEBUG][NWID %lu] addr 0x%lx", NETID, addr);

  tranintersection_launcher__receive_from_dram.writeAction(f"__if_receive_from_dram_2_post: addi X7 X23 32") 
  tranintersection_launcher__receive_from_dram.writeAction(f"movir X24 0") 
  tranintersection_launcher__receive_from_dram.writeAction(f"movrl X24 0(X23) 0 8") 
  tranintersection_launcher__receive_from_dram.writeAction(f"movir X24 0") 
  tranintersection_launcher__receive_from_dram.writeAction(f"movrl X24 8(X23) 0 8") 
  tranintersection_launcher__receive_from_dram.writeAction(f"movir X24 0") 
  tranintersection_launcher__receive_from_dram.writeAction(f"movrl X24 16(X23) 0 8") 
  tranintersection_launcher__receive_from_dram.writeAction(f"movir X24 0") 
  tranintersection_launcher__receive_from_dram.writeAction(f"movrl X24 24(X23) 0 8") 
  tranintersection_launcher__receive_from_dram.writeAction(f"send_dmlm_wret X12 intersection_launcher::v1v2_write_return X23 4 X24") 
  ## if(return_nid == 47){

  ## 	print("[DEBUG][NWID %lu] <intersection_receive_dram> received (%lu, %lu, %lu)", NETID, v1, v2, threshold);

  ## }

  tranintersection_launcher__receive_from_dram.writeAction(f"ble X16 X17 __if_receive_from_dram_4_false") 
  tranintersection_launcher__receive_from_dram.writeAction(f"__if_receive_from_dram_3_true: movir X24 0") 
  tranintersection_launcher__receive_from_dram.writeAction(f"evlb X24 v1v2intersection__launch") 
  tranintersection_launcher__receive_from_dram.writeAction(f"evi X24 X24 255 4") 
  tranintersection_launcher__receive_from_dram.writeAction(f"ev X24 X24 X0 X0 8") 
  tranintersection_launcher__receive_from_dram.writeAction(f"addi X7 X23 0") 
  tranintersection_launcher__receive_from_dram.writeAction(f"movlr 16(X23) X25 0 8") 
  tranintersection_launcher__receive_from_dram.writeAction(f"addi X7 X23 32") 
  tranintersection_launcher__receive_from_dram.writeAction(f"movir X26 0") 
  tranintersection_launcher__receive_from_dram.writeAction(f"movrl X26 0(X23) 0 8") 
  tranintersection_launcher__receive_from_dram.writeAction(f"movrl X25 8(X23) 0 8") 
  tranintersection_launcher__receive_from_dram.writeAction(f"movrl X8 16(X23) 0 8") 
  tranintersection_launcher__receive_from_dram.writeAction(f"movrl X9 24(X23) 0 8") 
  tranintersection_launcher__receive_from_dram.writeAction(f"subi X10 X25 1") 
  tranintersection_launcher__receive_from_dram.writeAction(f"movrl X25 32(X23) 0 8") 
  tranintersection_launcher__receive_from_dram.writeAction(f"movrl X11 40(X23) 0 8") 
  tranintersection_launcher__receive_from_dram.writeAction(f"send_wret X24 intersection_launcher::intersection_term X23 6 X25") 
  tranintersection_launcher__receive_from_dram.writeAction(f"addi X17 X17 1") 
  tranintersection_launcher__receive_from_dram.writeAction(f"yield") 
  tranintersection_launcher__receive_from_dram.writeAction(f"jmp __if_receive_from_dram_5_post") 
  tranintersection_launcher__receive_from_dram.writeAction(f"__if_receive_from_dram_4_false: cgti X20 X24 0") 
  tranintersection_launcher__receive_from_dram.writeAction(f"ceq X19 X18 X25") 
  tranintersection_launcher__receive_from_dram.writeAction(f"and X24 X25 X24") 
  tranintersection_launcher__receive_from_dram.writeAction(f"beqi X24 0 __if_receive_from_dram_8_post") 
  tranintersection_launcher__receive_from_dram.writeAction(f"__if_receive_from_dram_6_true: print '[DEBUG][NWID %lu] buffer2 is full' X0") 
  tranintersection_launcher__receive_from_dram.writeAction(f"addi X7 X23 0") 
  tranintersection_launcher__receive_from_dram.writeAction(f"addi X7 X23 32") 
  tranintersection_launcher__receive_from_dram.writeAction(f"movrl X8 0(X23) 0 8") 
  tranintersection_launcher__receive_from_dram.writeAction(f"movrl X9 8(X23) 0 8") 
  tranintersection_launcher__receive_from_dram.writeAction(f"subi X10 X24 1") 
  tranintersection_launcher__receive_from_dram.writeAction(f"movrl X24 16(X23) 0 8") 
  tranintersection_launcher__receive_from_dram.writeAction(f"movrl X11 24(X23) 0 8") 
  tranintersection_launcher__receive_from_dram.writeAction(f"evi X2 X24 intersection_launcher::receive 1") 
  tranintersection_launcher__receive_from_dram.writeAction(f"send_wcont X24 X1 X23 4") 
  tranintersection_launcher__receive_from_dram.writeAction(f"yield") 
  tranintersection_launcher__receive_from_dram.writeAction(f"__if_receive_from_dram_8_post: addi X20 X20 1") 
  ##     print("[DEBUG][NWID %lu] <intersection_receive> buffer in dram:%lu (%lu,%lu), num_outstanding: %lu", NETID, int_dram_tail_ptr, dram_start, dram_end, num_outstanding);

  tranintersection_launcher__receive_from_dram.writeAction(f"addi X7 X23 32") 
  tranintersection_launcher__receive_from_dram.writeAction(f"movrl X8 0(X23) 0 8") 
  tranintersection_launcher__receive_from_dram.writeAction(f"movrl X9 8(X23) 0 8") 
  tranintersection_launcher__receive_from_dram.writeAction(f"movrl X10 16(X23) 0 8") 
  tranintersection_launcher__receive_from_dram.writeAction(f"movrl X11 24(X23) 0 8") 
  tranintersection_launcher__receive_from_dram.writeAction(f"send_dmlm_wret X18 intersection_launcher::v1v2_write_return X23 4 X24") 
  tranintersection_launcher__receive_from_dram.writeAction(f"addi X18 X18 32") 
  tranintersection_launcher__receive_from_dram.writeAction(f"movlr 24(X21) X24 0 8") 
  tranintersection_launcher__receive_from_dram.writeAction(f"bgtu X24 X18 __if_receive_from_dram_11_post") 
  tranintersection_launcher__receive_from_dram.writeAction(f"__if_receive_from_dram_9_true: movlr 16(X21) X24 0 8") 
  tranintersection_launcher__receive_from_dram.writeAction(f"addi X24 X18 0") 
  tranintersection_launcher__receive_from_dram.writeAction(f"__if_receive_from_dram_11_post: ble X20 X22 __if_receive_from_dram_14_post") 
  tranintersection_launcher__receive_from_dram.writeAction(f"__if_receive_from_dram_12_true: addi X7 X23 0") 
  tranintersection_launcher__receive_from_dram.writeAction(f"movir X24 0") 
  tranintersection_launcher__receive_from_dram.writeAction(f"movrl X24 136(X23) 0 8") 
  tranintersection_launcher__receive_from_dram.writeAction(f"__if_receive_from_dram_14_post: yield") 
  tranintersection_launcher__receive_from_dram.writeAction(f"__if_receive_from_dram_5_post: yield") 
  
  # Writing code for event intersection_launcher::intersection_term
  tranintersection_launcher__intersection_term = efa.writeEvent('intersection_launcher::intersection_term')
  ## intersection thread terminated

  ## put the offset in a thread that has status == -1

  ## and then check if there are things to be launched and read from dram if there are

  ## If everything has been launched - check if num_threads_active == 0

  tranintersection_launcher__intersection_term.writeAction(f"__entry: subi X17 X17 1") 
  tranintersection_launcher__intersection_term.writeAction(f"evi X2 X23 master_launcher__reduce_num_int 1") 
  tranintersection_launcher__intersection_term.writeAction(f"addi X8 X24 0")  # This is for casting. May be used later on
  tranintersection_launcher__intersection_term.writeAction(f"ev X23 X25 X24 X24 8") 
  tranintersection_launcher__intersection_term.writeAction(f"movir X23 0") 
  tranintersection_launcher__intersection_term.writeAction(f"evlb X23 master_launcher__send_to_master_thread1") 
  tranintersection_launcher__intersection_term.writeAction(f"evi X23 X23 255 4") 
  tranintersection_launcher__intersection_term.writeAction(f"ev X23 X23 X24 X24 8") 
  tranintersection_launcher__intersection_term.writeAction(f"movir X24 -1") 
  tranintersection_launcher__intersection_term.writeAction(f"sri X24 X24 1") 
  tranintersection_launcher__intersection_term.writeAction(f"sendr_wcont X23 X24 X25 X9") 
  ## if(return_nid == 47){

  ## 	print("[DEBUG][NWID %lu] <intersection_term>", NETID);

  ## }

  ## Check if there's stuff in memory

  tranintersection_launcher__intersection_term.writeAction(f"blei X20 0 __if_intersection_term_1_false") 
  ## read from head ptr

  tranintersection_launcher__intersection_term.writeAction(f"__if_intersection_term_0_true: subi X20 X20 1") 
  ## send a read from memory

  tranintersection_launcher__intersection_term.writeAction(f"send_dmlm_ld_wret X19 intersection_launcher::receive_from_dram 4 X23") 
  tranintersection_launcher__intersection_term.writeAction(f"addi X19 X19 32") 
  tranintersection_launcher__intersection_term.writeAction(f"addi X19 X23 0") 
  tranintersection_launcher__intersection_term.writeAction(f"movlr 24(X21) X25 0 8") 
  tranintersection_launcher__intersection_term.writeAction(f"bgtu X25 X23 __if_intersection_term_5_post") 
  tranintersection_launcher__intersection_term.writeAction(f"__if_intersection_term_3_true: movlr 16(X21) X23 0 8") 
  tranintersection_launcher__intersection_term.writeAction(f"addi X23 X19 0") 
  ## long* local temp_lmbuff = LMBASE;

  ## temp_lmbuff[NUM_V_THREAD] = 0;

  tranintersection_launcher__intersection_term.writeAction(f"__if_intersection_term_5_post: jmp __if_intersection_term_2_post") 
  tranintersection_launcher__intersection_term.writeAction(f"__if_intersection_term_1_false: addi X7 X23 20") 
  tranintersection_launcher__intersection_term.writeAction(f"movlr 8(X23) X25 0 8") 
  tranintersection_launcher__intersection_term.writeAction(f"bgeiu X25 2 __if_intersection_term_2_post") 
  tranintersection_launcher__intersection_term.writeAction(f"__if_intersection_term_6_true: addi X7 X23 0") 
  tranintersection_launcher__intersection_term.writeAction(f"movlr 136(X23) X25 0 8") 
  tranintersection_launcher__intersection_term.writeAction(f"bneiu X25 0 __if_intersection_term_2_post") 
  tranintersection_launcher__intersection_term.writeAction(f"__if_intersection_term_9_true: movir X25 10") 
  tranintersection_launcher__intersection_term.writeAction(f"movrl X25 136(X23) 0 8") 
  tranintersection_launcher__intersection_term.writeAction(f"movir X25 65504") 
  tranintersection_launcher__intersection_term.writeAction(f"add X7 X25 X23") 
  tranintersection_launcher__intersection_term.writeAction(f"movlr 0(X23) X25 0 8") 
  tranintersection_launcher__intersection_term.writeAction(f"addi X25 X25 0")  # This is for casting. May be used later on
  tranintersection_launcher__intersection_term.writeAction(f"evi X2 X24 master_launcher__relaunch 1") 
  tranintersection_launcher__intersection_term.writeAction(f"ev X24 X24 X25 X25 4") 
  tranintersection_launcher__intersection_term.writeAction(f"movir X26 -1") 
  tranintersection_launcher__intersection_term.writeAction(f"sri X26 X26 1") 
  tranintersection_launcher__intersection_term.writeAction(f"sendr_wcont X24 X26 X25 X25") 
  ## if(NETID == 0){

  ## 	long* local temp_lmbuff = LMBASE;

  ## 	long dram_end = temp_lmbuff[NUM_V_THREAD];

  ##     print("[DEBUG][NWID %lu] <intersection_term> test %lu %lu %lu", NETID, dram_end, num_outstanding, num_threads_active);

  ## }

  tranintersection_launcher__intersection_term.writeAction(f"__if_intersection_term_2_post: yield") 
  
  # Writing code for event intersection_launcher::get_tc
  tranintersection_launcher__get_tc = efa.writeEvent('intersection_launcher::get_tc')
  tranintersection_launcher__get_tc.writeAction(f"__entry: addi X7 X21 0") 
  tranintersection_launcher__get_tc.writeAction(f"movlr 8(X21) X23 0 8") 
  tranintersection_launcher__get_tc.writeAction(f"movir X25 -1") 
  tranintersection_launcher__get_tc.writeAction(f"sri X25 X25 1") 
  tranintersection_launcher__get_tc.writeAction(f"sendr_wcont X1 X25 X23 X23") 
  ## finally we can terminate

  tranintersection_launcher__get_tc.writeAction(f"yield_terminate") 
  
  # Writing code for event intersection_launcher::send_to_worker_thread2
  tranintersection_launcher__send_to_worker_thread2 = efa.writeEvent('intersection_launcher::send_to_worker_thread2')
  tranintersection_launcher__send_to_worker_thread2.writeAction(f"__entry: movir X23 65512") 
  tranintersection_launcher__send_to_worker_thread2.writeAction(f"add X7 X23 X23") 
  tranintersection_launcher__send_to_worker_thread2.writeAction(f"movlr 0(X23) X23 0 8") 
  tranintersection_launcher__send_to_worker_thread2.writeAction(f"addi X23 X23 0")  # This is for casting. May be used later on
  tranintersection_launcher__send_to_worker_thread2.writeAction(f"ev X8 X23 X23 X23 4") 
  tranintersection_launcher__send_to_worker_thread2.writeAction(f"sendr_wcont X23 X1 X9 X10") 
  tranintersection_launcher__send_to_worker_thread2.writeAction(f"yield_terminate") 
  
  # Writing code for event intersection_launcher::send_to_worker_thread4
  tranintersection_launcher__send_to_worker_thread4 = efa.writeEvent('intersection_launcher::send_to_worker_thread4')
  tranintersection_launcher__send_to_worker_thread4.writeAction(f"__entry: movir X23 65512") 
  tranintersection_launcher__send_to_worker_thread4.writeAction(f"add X7 X23 X23") 
  tranintersection_launcher__send_to_worker_thread4.writeAction(f"movlr 0(X23) X23 0 8") 
  tranintersection_launcher__send_to_worker_thread4.writeAction(f"addi X23 X23 0")  # This is for casting. May be used later on
  tranintersection_launcher__send_to_worker_thread4.writeAction(f"evi X2 X25 intersection_launcher::receive 1") 
  tranintersection_launcher__send_to_worker_thread4.writeAction(f"ev X25 X23 X23 X23 4") 
  tranintersection_launcher__send_to_worker_thread4.writeAction(f"ev X23 X23 X0 X0 8") 
  tranintersection_launcher__send_to_worker_thread4.writeAction(f"movir X25 -1") 
  tranintersection_launcher__send_to_worker_thread4.writeAction(f"sri X25 X25 1") 
  tranintersection_launcher__send_to_worker_thread4.writeAction(f"sendops_wcont X23 X25 X8 4") 
  ## if(op3 == 47){

  ## 	print("[DEBUG][NWID %lu] <send_to_worker_thread4> op0:%lu, op1:%lu, op2=%lu", NETID, op0, op1, op2);

  ## }

  tranintersection_launcher__send_to_worker_thread4.writeAction(f"yield_terminate") 
  
  # Writing code for event intersection_launcher::v1v2_write_return
  tranintersection_launcher__v1v2_write_return = efa.writeEvent('intersection_launcher::v1v2_write_return')
  tranintersection_launcher__v1v2_write_return.writeAction(f"__entry: yield") 
  