from linker.EFAProgram import efaProgram

## UDWeave version: unknown

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
  ## Scoped Variable "lmbuff_read_offset" uses Register X23, scope (0)
  ## Scoped Variable "lmbuff_write_offset" uses Register X24, scope (0)
  ## Scoped Variable "num_write" uses Register X25, scope (0)
  ## Scoped Variable "cont" uses Register X16, scope (0)
  ## Scoped Variable "cache_lmbuff" uses Register X17, scope (0)
  ## Scoped Variable "count" uses Register X18, scope (0)
  ## Scoped Variable "new_val" uses Register X19, scope (0)
  ## Scoped Variable "new_addr" uses Register X20, scope (0)
  ## Scoped Variable "lmbuff" uses Register X21, scope (0)
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
  
  ###########################################################
  ###### Writing code for thread intersection_launcher ######
  ###########################################################
  # Writing code for event intersection_launcher::intersection_init
  tranintersection_launcher__intersection_init = efa.writeEvent('intersection_launcher::intersection_init')
  ## #ifdef DEBUG

  ## print("[DEBUG][NWID %lu] Intersection launcher intersection_addr:0x%lx int_size:%lu ", NETID, intersection_addr, intersection_size);

  ## #endif

  tranintersection_launcher__intersection_init.writeAction(f"__entry: movir X26 -1") 
  tranintersection_launcher__intersection_init.writeAction(f"sri X26 X26 1") 
  tranintersection_launcher__intersection_init.writeAction(f"sendr_wcont X1 X26 X0 X0") 
  tranintersection_launcher__intersection_init.writeAction(f"movir X26 65512") 
  tranintersection_launcher__intersection_init.writeAction(f"add X7 X26 X21") 
  tranintersection_launcher__intersection_init.writeAction(f"sri X2 X26 24") 
  tranintersection_launcher__intersection_init.writeAction(f"andi X26 X26 255") 
  tranintersection_launcher__intersection_init.writeAction(f"movrl X26 0(X21) 0 8") 
  tranintersection_launcher__intersection_init.writeAction(f"addi X7 X21 0") 
  ## lmbuff[NUM_WRITE] = 0;

  tranintersection_launcher__intersection_init.writeAction(f"movir X26 0") 
  tranintersection_launcher__intersection_init.writeAction(f"movrl X26 24(X21) 0 8") 
  tranintersection_launcher__intersection_init.writeAction(f"addi X7 X23 1520") 
  tranintersection_launcher__intersection_init.writeAction(f"movrl X23 224(X21) 0 8") 
  tranintersection_launcher__intersection_init.writeAction(f"addi X7 X24 2000") 
  tranintersection_launcher__intersection_init.writeAction(f"movrl X24 232(X21) 0 8") 
  tranintersection_launcher__intersection_init.writeAction(f"addi X23 X24 0") 
  tranintersection_launcher__intersection_init.writeAction(f"movir X26 60") 
  tranintersection_launcher__intersection_init.writeAction(f"movir X27 0") 
  tranintersection_launcher__intersection_init.writeAction(f"__for_intersection_init_0_condition: ble X26 X27 __for_intersection_init_2_post") 
  tranintersection_launcher__intersection_init.writeAction(f"__for_intersection_init_1_body: movwrl X27 X23(X27,0,0)") 
  tranintersection_launcher__intersection_init.writeAction(f"addi X27 X27 1") 
  tranintersection_launcher__intersection_init.writeAction(f"jmp __for_intersection_init_0_condition") 
  tranintersection_launcher__intersection_init.writeAction(f"__for_intersection_init_2_post: addi X7 X21 192") 
  tranintersection_launcher__intersection_init.writeAction(f"movir X27 0") 
  tranintersection_launcher__intersection_init.writeAction(f"movrl X27 8(X21) 0 8") 
  ## lmbuff[MAINCONT] = CCONT;

  ## temp = intersection_addr;

  tranintersection_launcher__intersection_init.writeAction(f"movrl X8 16(X21) 0 8") 
  tranintersection_launcher__intersection_init.writeAction(f"add X8 X9 X26") 
  tranintersection_launcher__intersection_init.writeAction(f"movrl X26 24(X21) 0 8") 
  tranintersection_launcher__intersection_init.writeAction(f"addi X8 X18 0") 
  tranintersection_launcher__intersection_init.writeAction(f"addi X8 X19 0") 
  tranintersection_launcher__intersection_init.writeAction(f"movir X20 0") 
  tranintersection_launcher__intersection_init.writeAction(f"movir X16 60") 
  tranintersection_launcher__intersection_init.writeAction(f"movir X17 0") 
  tranintersection_launcher__intersection_init.writeAction(f"movir X25 0") 
  tranintersection_launcher__intersection_init.writeAction(f"sari X9 X22 7") 
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

  ## print("[DEBUG][NWID %lu] <intersection_receive> received (%lu, %lu, %lu, 0x%lx)", NETID, v1, v2, threshold, v1v2_addr);

  tranintersection_launcher__receive.writeAction(f"__entry: ble X16 X17 __if_receive_1_false") 
  tranintersection_launcher__receive.writeAction(f"__if_receive_0_true: addi X7 X26 0") 
  tranintersection_launcher__receive.writeAction(f"movlr 16(X26) X27 0 8") 
  tranintersection_launcher__receive.writeAction(f"addi X7 X26 32") 
  tranintersection_launcher__receive.writeAction(f"movlr 0(X23) X28 0 8") 
  tranintersection_launcher__receive.writeAction(f"movrl X28 0(X26) 0 8") 
  tranintersection_launcher__receive.writeAction(f"movrl X27 8(X26) 0 8") 
  ## temp_lmbuff[2] = v1;

  ## temp_lmbuff[3] = v2;

  ## temp_lmbuff[4] = threshold;

  ## temp_lmbuff[5] = return_nid;

  ## temp_lmbuff[6] = v1v2_addr;

  tranintersection_launcher__receive.writeAction(f"addi X26 X27 16") 
  tranintersection_launcher__receive.writeAction(f"bcpyoli X8 X27 5") 
  tranintersection_launcher__receive.writeAction(f"movir X28 0") 
  tranintersection_launcher__receive.writeAction(f"evlb X28 v1v2intersection__launch") 
  tranintersection_launcher__receive.writeAction(f"evi X28 X28 255 4") 
  tranintersection_launcher__receive.writeAction(f"ev X28 X28 X0 X0 8") 
  tranintersection_launcher__receive.writeAction(f"send_wret X28 intersection_launcher::intersection_term X26 7 X27") 
  tranintersection_launcher__receive.writeAction(f"addi X17 X17 1") 
  tranintersection_launcher__receive.writeAction(f"addi X23 X23 8") 
  tranintersection_launcher__receive.writeAction(f"addi X7 X26 0") 
  tranintersection_launcher__receive.writeAction(f"movlr 232(X26) X28 0 8") 
  tranintersection_launcher__receive.writeAction(f"bneu X23 X28 __if_receive_5_post") 
  tranintersection_launcher__receive.writeAction(f"__if_receive_3_true: movlr 224(X26) X23 0 8") 
  tranintersection_launcher__receive.writeAction(f"__if_receive_5_post: yield") 
  tranintersection_launcher__receive.writeAction(f"jmp __if_receive_2_post") 
  ## no thread active save in memory

  tranintersection_launcher__receive.writeAction(f"__if_receive_1_false: cgti X20 X26 0") 
  tranintersection_launcher__receive.writeAction(f"ceq X19 X18 X28") 
  tranintersection_launcher__receive.writeAction(f"and X26 X28 X26") 
  tranintersection_launcher__receive.writeAction(f"beqi X26 0 __if_receive_8_post") 
  tranintersection_launcher__receive.writeAction(f"__if_receive_6_true: print '[DEBUG][NWID %lu] buffer is full' X0") 
  tranintersection_launcher__receive.writeAction(f"addi X7 X26 32") 
  ## temp_lmbuff[0] = v1;

  ## temp_lmbuff[1] = v2;

  ## temp_lmbuff[2] = threshold;

  ## temp_lmbuff[3] = return_nid;

  ## temp_lmbuff[4] = v1v2_addr;

  tranintersection_launcher__receive.writeAction(f"bcpyoli X8 X26 5") 
  tranintersection_launcher__receive.writeAction(f"send_wcont X2 X1 X26 5") 
  tranintersection_launcher__receive.writeAction(f"yield") 
  tranintersection_launcher__receive.writeAction(f"__if_receive_8_post: addi X20 X20 1") 
  ##     print("[DEBUG][NWID %lu] <intersection_receive> buffer in dram:%lu (%lu,%lu), num_outstanding: %lu", NETID, int_dram_tail_ptr, dram_start, dram_end, num_outstanding);

  tranintersection_launcher__receive.writeAction(f"addi X7 X26 32") 
  ## temp_lmbuff[0] = v1;

  ## temp_lmbuff[1] = v2;

  ## temp_lmbuff[2] = threshold + 1;

  ## temp_lmbuff[3] = return_nid;

  ## temp_lmbuff[4] = v1v2_addr;

  tranintersection_launcher__receive.writeAction(f"bcpyoli X8 X26 5") 
  tranintersection_launcher__receive.writeAction(f"addi X10 X28 1") 
  tranintersection_launcher__receive.writeAction(f"movrl X28 16(X26) 0 8") 
  tranintersection_launcher__receive.writeAction(f"send_dmlm_wret X18 intersection_launcher::v1v2_write_return X26 5 X28") 
  tranintersection_launcher__receive.writeAction(f"addi X18 X18 64") 
  tranintersection_launcher__receive.writeAction(f"movlr 24(X21) X28 0 8") 
  tranintersection_launcher__receive.writeAction(f"bgtu X28 X18 __if_receive_11_post") 
  tranintersection_launcher__receive.writeAction(f"__if_receive_9_true: movlr 16(X21) X28 0 8") 
  tranintersection_launcher__receive.writeAction(f"addi X28 X18 0") 
  tranintersection_launcher__receive.writeAction(f"__if_receive_11_post: ble X20 X22 __if_receive_14_post") 
  tranintersection_launcher__receive.writeAction(f"__if_receive_12_true: addi X7 X26 0") 
  tranintersection_launcher__receive.writeAction(f"movir X28 0") 
  tranintersection_launcher__receive.writeAction(f"movrl X28 136(X26) 0 8") 
  ## print("<receive> add back pressure %lu:%lu, %lu", NETID, num_outstanding, half_intersection_len);

  tranintersection_launcher__receive.writeAction(f"__if_receive_14_post: yield") 
  tranintersection_launcher__receive.writeAction(f"__if_receive_2_post: yield") 
  
  # Writing code for event intersection_launcher::receive_from_dram
  tranintersection_launcher__receive_from_dram = efa.writeEvent('intersection_launcher::receive_from_dram')
  tranintersection_launcher__receive_from_dram.writeAction(f"__entry: bnei X10 0 __if_receive_from_dram_2_post") 
  tranintersection_launcher__receive_from_dram.writeAction(f"__if_receive_from_dram_0_true: send_dmlm_ld_wret X13 intersection_launcher::receive_from_dram 5 X26") 
  tranintersection_launcher__receive_from_dram.writeAction(f"yield") 
  ## print("[DEBUG][NWID %lu] addr 0x%lx", NETID, addr);

  tranintersection_launcher__receive_from_dram.writeAction(f"__if_receive_from_dram_2_post: addi X7 X26 32") 
  tranintersection_launcher__receive_from_dram.writeAction(f"movir X28 0") 
  tranintersection_launcher__receive_from_dram.writeAction(f"movrl X28 0(X26) 0 8") 
  tranintersection_launcher__receive_from_dram.writeAction(f"addi X13 X28 16") 
  tranintersection_launcher__receive_from_dram.writeAction(f"send_dmlm_wret X28 intersection_launcher::v1v2_write_return X26 1 X27") 
  ## if(return_nid == 47){

  ## 	print("[DEBUG][NWID %lu] <intersection_receive_dram> received (%lu, %lu, %lu)", NETID, v1, v2, threshold);

  ## }

  tranintersection_launcher__receive_from_dram.writeAction(f"ble X16 X17 __if_receive_from_dram_4_false") 
  tranintersection_launcher__receive_from_dram.writeAction(f"__if_receive_from_dram_3_true: addi X7 X26 0") 
  tranintersection_launcher__receive_from_dram.writeAction(f"movlr 16(X26) X28 0 8") 
  tranintersection_launcher__receive_from_dram.writeAction(f"addi X7 X26 32") 
  tranintersection_launcher__receive_from_dram.writeAction(f"movlr 0(X23) X27 0 8") 
  tranintersection_launcher__receive_from_dram.writeAction(f"movrl X27 0(X26) 0 8") 
  tranintersection_launcher__receive_from_dram.writeAction(f"movrl X28 8(X26) 0 8") 
  ## temp_lmbuff[2] = v1;

  ## temp_lmbuff[3] = v2;

  ## temp_lmbuff[4] = threshold-1;

  ## temp_lmbuff[5] = return_nid;

  ## temp_lmbuff[6] = v1v2_addr;

  tranintersection_launcher__receive_from_dram.writeAction(f"addi X26 X28 16") 
  tranintersection_launcher__receive_from_dram.writeAction(f"bcpyoli X8 X28 5") 
  tranintersection_launcher__receive_from_dram.writeAction(f"subi X10 X27 1") 
  tranintersection_launcher__receive_from_dram.writeAction(f"movrl X27 32(X26) 0 8") 
  tranintersection_launcher__receive_from_dram.writeAction(f"movir X27 0") 
  tranintersection_launcher__receive_from_dram.writeAction(f"evlb X27 v1v2intersection__launch") 
  tranintersection_launcher__receive_from_dram.writeAction(f"evi X27 X27 255 4") 
  tranintersection_launcher__receive_from_dram.writeAction(f"ev X27 X27 X0 X0 8") 
  tranintersection_launcher__receive_from_dram.writeAction(f"send_wret X27 intersection_launcher::intersection_term X26 7 X28") 
  tranintersection_launcher__receive_from_dram.writeAction(f"addi X17 X17 1") 
  tranintersection_launcher__receive_from_dram.writeAction(f"addi X23 X23 8") 
  tranintersection_launcher__receive_from_dram.writeAction(f"addi X7 X26 0") 
  tranintersection_launcher__receive_from_dram.writeAction(f"movlr 232(X26) X27 0 8") 
  tranintersection_launcher__receive_from_dram.writeAction(f"bneu X23 X27 __if_receive_from_dram_8_post") 
  tranintersection_launcher__receive_from_dram.writeAction(f"__if_receive_from_dram_6_true: movlr 224(X26) X23 0 8") 
  tranintersection_launcher__receive_from_dram.writeAction(f"__if_receive_from_dram_8_post: yield") 
  tranintersection_launcher__receive_from_dram.writeAction(f"jmp __if_receive_from_dram_5_post") 
  tranintersection_launcher__receive_from_dram.writeAction(f"__if_receive_from_dram_4_false: cgti X20 X27 0") 
  tranintersection_launcher__receive_from_dram.writeAction(f"ceq X19 X18 X28") 
  tranintersection_launcher__receive_from_dram.writeAction(f"and X27 X28 X27") 
  tranintersection_launcher__receive_from_dram.writeAction(f"beqi X27 0 __if_receive_from_dram_11_post") 
  tranintersection_launcher__receive_from_dram.writeAction(f"__if_receive_from_dram_9_true: print '[DEBUG][NWID %lu] buffer2 is full' X0") 
  tranintersection_launcher__receive_from_dram.writeAction(f"addi X7 X26 0") 
  tranintersection_launcher__receive_from_dram.writeAction(f"addi X7 X26 32") 
  tranintersection_launcher__receive_from_dram.writeAction(f"movrl X8 0(X26) 0 8") 
  tranintersection_launcher__receive_from_dram.writeAction(f"movrl X9 8(X26) 0 8") 
  tranintersection_launcher__receive_from_dram.writeAction(f"subi X10 X27 1") 
  tranintersection_launcher__receive_from_dram.writeAction(f"movrl X27 16(X26) 0 8") 
  tranintersection_launcher__receive_from_dram.writeAction(f"movrl X11 24(X26) 0 8") 
  tranintersection_launcher__receive_from_dram.writeAction(f"movrl X12 32(X26) 0 8") 
  tranintersection_launcher__receive_from_dram.writeAction(f"evi X2 X27 intersection_launcher::receive 1") 
  tranintersection_launcher__receive_from_dram.writeAction(f"send_wcont X27 X1 X26 5") 
  tranintersection_launcher__receive_from_dram.writeAction(f"yield") 
  tranintersection_launcher__receive_from_dram.writeAction(f"__if_receive_from_dram_11_post: addi X20 X20 1") 
  ##     print("[DEBUG][NWID %lu] <intersection_receive> buffer in dram:%lu (%lu,%lu), num_outstanding: %lu", NETID, int_dram_tail_ptr, dram_start, dram_end, num_outstanding);

  tranintersection_launcher__receive_from_dram.writeAction(f"addi X7 X26 32") 
  ## temp_lmbuff[0] = v1;

  ## temp_lmbuff[1] = v2;

  ## temp_lmbuff[2] = threshold;

  ## temp_lmbuff[3] = return_nid;

  ## temp_lmbuff[4] = v1v2_addr;

  tranintersection_launcher__receive_from_dram.writeAction(f"bcpyoli X8 X26 5") 
  tranintersection_launcher__receive_from_dram.writeAction(f"send_dmlm_wret X18 intersection_launcher::v1v2_write_return X26 5 X27") 
  tranintersection_launcher__receive_from_dram.writeAction(f"addi X18 X18 64") 
  tranintersection_launcher__receive_from_dram.writeAction(f"movlr 24(X21) X27 0 8") 
  tranintersection_launcher__receive_from_dram.writeAction(f"bgtu X27 X18 __if_receive_from_dram_14_post") 
  tranintersection_launcher__receive_from_dram.writeAction(f"__if_receive_from_dram_12_true: movlr 16(X21) X27 0 8") 
  tranintersection_launcher__receive_from_dram.writeAction(f"addi X27 X18 0") 
  tranintersection_launcher__receive_from_dram.writeAction(f"__if_receive_from_dram_14_post: ble X20 X22 __if_receive_from_dram_17_post") 
  tranintersection_launcher__receive_from_dram.writeAction(f"__if_receive_from_dram_15_true: addi X7 X26 0") 
  tranintersection_launcher__receive_from_dram.writeAction(f"movir X27 0") 
  tranintersection_launcher__receive_from_dram.writeAction(f"movrl X27 136(X26) 0 8") 
  ## print("<receive_from_dram> add back pressure %lu:%lu %lu", NETID, num_outstanding, half_intersection_len);

  tranintersection_launcher__receive_from_dram.writeAction(f"__if_receive_from_dram_17_post: yield") 
  tranintersection_launcher__receive_from_dram.writeAction(f"__if_receive_from_dram_5_post: yield") 
  
  # Writing code for event intersection_launcher::intersection_term
  tranintersection_launcher__intersection_term = efa.writeEvent('intersection_launcher::intersection_term')
  ## intersection thread terminated

  ## put the offset in a thread that has status == -1

  ## and then check if there are things to be launched and read from dram if there are

  ## If everything has been launched - check if num_threads_active == 0

  tranintersection_launcher__intersection_term.writeAction(f"__entry: subi X17 X17 1") 
  tranintersection_launcher__intersection_term.writeAction(f"add X25 X12 X25") 
  tranintersection_launcher__intersection_term.writeAction(f"evi X2 X26 master_launcher__reduce_num_int 1") 
  tranintersection_launcher__intersection_term.writeAction(f"ev X26 X27 X8 X8 8") 
  tranintersection_launcher__intersection_term.writeAction(f"movir X26 0") 
  tranintersection_launcher__intersection_term.writeAction(f"evlb X26 master_launcher__send_to_master_thread2") 
  tranintersection_launcher__intersection_term.writeAction(f"evi X26 X26 255 4") 
  tranintersection_launcher__intersection_term.writeAction(f"ev X26 X26 X8 X8 8") 
  tranintersection_launcher__intersection_term.writeAction(f"movir X28 -1") 
  tranintersection_launcher__intersection_term.writeAction(f"sri X28 X28 1") 
  tranintersection_launcher__intersection_term.writeAction(f"sendr3_wcont X26 X28 X27 X9 X10") 
  tranintersection_launcher__intersection_term.writeAction(f"blei X9 0 __if_intersection_term_2_post") 
  tranintersection_launcher__intersection_term.writeAction(f"__if_intersection_term_0_true: evi X2 X26 intersection_launcher::add_value 1") 
  tranintersection_launcher__intersection_term.writeAction(f"movir X28 -1") 
  tranintersection_launcher__intersection_term.writeAction(f"sri X28 X28 1") 
  tranintersection_launcher__intersection_term.writeAction(f"sendr_wcont X26 X28 X10 X9") 
  tranintersection_launcher__intersection_term.writeAction(f"addi X7 X31 0") 
  tranintersection_launcher__intersection_term.writeAction(f"addi X25 X25 1") 
  ## evword = temp_lmbuff[NUM_WRITE];

  ## evword = evword + 1;

  ## temp_lmbuff[NUM_WRITE] = evword;

  tranintersection_launcher__intersection_term.writeAction(f"__if_intersection_term_2_post: addi X7 X28 0") 
  tranintersection_launcher__intersection_term.writeAction(f"movrl X11 0(X24) 0 8") 
  tranintersection_launcher__intersection_term.writeAction(f"addi X24 X24 8") 
  tranintersection_launcher__intersection_term.writeAction(f"movlr 232(X28) X29 0 8") 
  tranintersection_launcher__intersection_term.writeAction(f"bneu X24 X29 __if_intersection_term_5_post") 
  tranintersection_launcher__intersection_term.writeAction(f"__if_intersection_term_3_true: movlr 224(X28) X24 0 8") 
  ## Check if there's stuff in memory

  tranintersection_launcher__intersection_term.writeAction(f"__if_intersection_term_5_post: blei X20 0 __if_intersection_term_7_false") 
  ## read from head ptr

  tranintersection_launcher__intersection_term.writeAction(f"__if_intersection_term_6_true: subi X20 X20 1") 
  ## send a read from memory

  tranintersection_launcher__intersection_term.writeAction(f"send_dmlm_ld_wret X19 intersection_launcher::receive_from_dram 5 X29") 
  tranintersection_launcher__intersection_term.writeAction(f"addi X19 X19 64") 
  tranintersection_launcher__intersection_term.writeAction(f"addi X19 X26 0") 
  tranintersection_launcher__intersection_term.writeAction(f"movlr 24(X21) X27 0 8") 
  tranintersection_launcher__intersection_term.writeAction(f"bgtu X27 X26 __if_intersection_term_11_post") 
  tranintersection_launcher__intersection_term.writeAction(f"__if_intersection_term_9_true: movlr 16(X21) X26 0 8") 
  tranintersection_launcher__intersection_term.writeAction(f"addi X26 X19 0") 
  ## long* local temp_lmbuff = LMBASE;

  ## temp_lmbuff[NUM_V_THREAD] = 0;

  tranintersection_launcher__intersection_term.writeAction(f"__if_intersection_term_11_post: jmp __if_intersection_term_8_post") 
  tranintersection_launcher__intersection_term.writeAction(f"__if_intersection_term_7_false: addi X7 X28 20") 
  tranintersection_launcher__intersection_term.writeAction(f"movlr 8(X28) X26 0 8") 
  tranintersection_launcher__intersection_term.writeAction(f"bneiu X26 1 __if_intersection_term_8_post") 
  tranintersection_launcher__intersection_term.writeAction(f"__if_intersection_term_12_true: addi X7 X28 0") 
  tranintersection_launcher__intersection_term.writeAction(f"movlr 136(X28) X29 0 8") 
  tranintersection_launcher__intersection_term.writeAction(f"bneiu X29 0 __if_intersection_term_8_post") 
  tranintersection_launcher__intersection_term.writeAction(f"__if_intersection_term_15_true: movir X29 4") 
  tranintersection_launcher__intersection_term.writeAction(f"movrl X29 136(X28) 0 8") 
  tranintersection_launcher__intersection_term.writeAction(f"movir X29 65504") 
  tranintersection_launcher__intersection_term.writeAction(f"add X7 X29 X28") 
  tranintersection_launcher__intersection_term.writeAction(f"movlr 0(X28) X29 0 8") 
  tranintersection_launcher__intersection_term.writeAction(f"evi X2 X26 master_launcher__relaunch 1") 
  tranintersection_launcher__intersection_term.writeAction(f"ev X26 X27 X29 X29 4") 
  tranintersection_launcher__intersection_term.writeAction(f"movir X30 -1") 
  tranintersection_launcher__intersection_term.writeAction(f"sri X30 X30 1") 
  tranintersection_launcher__intersection_term.writeAction(f"sendr_wcont X27 X30 X29 X29") 
  tranintersection_launcher__intersection_term.writeAction(f"__if_intersection_term_8_post: yield") 
  
  # Writing code for event intersection_launcher::cache_write_finish
  tranintersection_launcher__cache_write_finish = efa.writeEvent('intersection_launcher::cache_write_finish')
  tranintersection_launcher__cache_write_finish.writeAction(f"__entry: movir X27 4") 
  tranintersection_launcher__cache_write_finish.writeAction(f"movrl X27 8(X21) 0 8") 
  tranintersection_launcher__cache_write_finish.writeAction(f"movrl X1 0(X21) 0 8") 
  tranintersection_launcher__cache_write_finish.writeAction(f"bnei X25 0 __if_cache_write_finish_2_post") 
  tranintersection_launcher__cache_write_finish.writeAction(f"__if_cache_write_finish_0_true: movlr 0(X21) X27 0 8") 
  tranintersection_launcher__cache_write_finish.writeAction(f"movir X28 -1") 
  tranintersection_launcher__cache_write_finish.writeAction(f"sri X28 X28 1") 
  tranintersection_launcher__cache_write_finish.writeAction(f"sendr_wcont X27 X28 X0 X0") 
  tranintersection_launcher__cache_write_finish.writeAction(f"yield") 
  ## long* local tmp_lmbuff = LMBASE;

  ## if(tmp_lmbuff[NUM_WRITE] == 0){

  ##     send_event(lmbuff[MAINCONT], NETID, IGNRCONT);

  ##     // finally we can terminate

  ##     yield;

  ## }

  tranintersection_launcher__cache_write_finish.writeAction(f"__if_cache_write_finish_2_post: yield") 
  
  # Writing code for event intersection_launcher::send_to_worker_thread2
  tranintersection_launcher__send_to_worker_thread2 = efa.writeEvent('intersection_launcher::send_to_worker_thread2')
  tranintersection_launcher__send_to_worker_thread2.writeAction(f"__entry: movir X27 65512") 
  tranintersection_launcher__send_to_worker_thread2.writeAction(f"add X7 X27 X27") 
  tranintersection_launcher__send_to_worker_thread2.writeAction(f"movlr 0(X27) X27 0 8") 
  tranintersection_launcher__send_to_worker_thread2.writeAction(f"ev X8 X27 X27 X27 4") 
  tranintersection_launcher__send_to_worker_thread2.writeAction(f"sendr_wcont X27 X1 X9 X10") 
  tranintersection_launcher__send_to_worker_thread2.writeAction(f"yield_terminate") 
  
  # Writing code for event intersection_launcher::send_to_worker_thread5
  tranintersection_launcher__send_to_worker_thread5 = efa.writeEvent('intersection_launcher::send_to_worker_thread5')
  tranintersection_launcher__send_to_worker_thread5.writeAction(f"__entry: movir X27 65512") 
  tranintersection_launcher__send_to_worker_thread5.writeAction(f"add X7 X27 X27") 
  tranintersection_launcher__send_to_worker_thread5.writeAction(f"movlr 0(X27) X27 0 8") 
  tranintersection_launcher__send_to_worker_thread5.writeAction(f"evi X2 X28 intersection_launcher::receive 1") 
  tranintersection_launcher__send_to_worker_thread5.writeAction(f"ev X28 X27 X27 X27 4") 
  tranintersection_launcher__send_to_worker_thread5.writeAction(f"ev X27 X27 X0 X0 8") 
  tranintersection_launcher__send_to_worker_thread5.writeAction(f"movir X28 -1") 
  tranintersection_launcher__send_to_worker_thread5.writeAction(f"sri X28 X28 1") 
  tranintersection_launcher__send_to_worker_thread5.writeAction(f"sendops_wcont X27 X28 X8 5") 
  tranintersection_launcher__send_to_worker_thread5.writeAction(f"yield_terminate") 
  
  # Writing code for event intersection_launcher::v1v2_write_return
  tranintersection_launcher__v1v2_write_return = efa.writeEvent('intersection_launcher::v1v2_write_return')
  tranintersection_launcher__v1v2_write_return.writeAction(f"__entry: yield") 
  
  # Writing code for event intersection_launcher::add_one
  tranintersection_launcher__add_one = efa.writeEvent('intersection_launcher::add_one')
  tranintersection_launcher__add_one.writeAction(f"__entry: movir X27 0") 
  tranintersection_launcher__add_one.writeAction(f"sri X8 X28 3") 
  tranintersection_launcher__add_one.writeAction(f"hash X28 X27") 
  tranintersection_launcher__add_one.writeAction(f"sri X27 X28 11") 
  tranintersection_launcher__add_one.writeAction(f"addi X7 X26 0") 
  tranintersection_launcher__add_one.writeAction(f"movlr 152(X26) X29 0 8") 
  tranintersection_launcher__add_one.writeAction(f"and X28 X29 X28") 
  tranintersection_launcher__add_one.writeAction(f"movir X30 0") 
  tranintersection_launcher__add_one.writeAction(f"evlb X30 intersection_cache__add_val_dram_write") 
  tranintersection_launcher__add_one.writeAction(f"evi X30 X30 255 4") 
  tranintersection_launcher__add_one.writeAction(f"ev X30 X30 X28 X28 8") 
  ## nwid = nwid & CACHE_LEN_1;

  tranintersection_launcher__add_one.writeAction(f"movlr 0(X26) X29 0 8") 
  tranintersection_launcher__add_one.writeAction(f"and X27 X29 X27") 
  ## print("cache len = %lu", cache_len);

  tranintersection_launcher__add_one.writeAction(f"movir X28 1") 
  tranintersection_launcher__add_one.writeAction(f"sendr3_wret X30 intersection_launcher::add_return X27 X8 X28 X29") 
  tranintersection_launcher__add_one.writeAction(f"yield") 
  
  # Writing code for event intersection_launcher::add_value
  tranintersection_launcher__add_value = efa.writeEvent('intersection_launcher::add_value')
  tranintersection_launcher__add_value.writeAction(f"__entry: movir X27 0") 
  tranintersection_launcher__add_value.writeAction(f"sri X8 X28 3") 
  tranintersection_launcher__add_value.writeAction(f"hash X28 X27") 
  tranintersection_launcher__add_value.writeAction(f"sri X27 X28 11") 
  tranintersection_launcher__add_value.writeAction(f"addi X7 X30 0") 
  tranintersection_launcher__add_value.writeAction(f"movlr 152(X30) X29 0 8") 
  tranintersection_launcher__add_value.writeAction(f"and X28 X29 X28") 
  tranintersection_launcher__add_value.writeAction(f"movir X26 0") 
  tranintersection_launcher__add_value.writeAction(f"evlb X26 intersection_cache__add_val_dram_write") 
  tranintersection_launcher__add_value.writeAction(f"evi X26 X26 255 4") 
  tranintersection_launcher__add_value.writeAction(f"ev X26 X26 X28 X28 8") 
  ## nwid = nwid & CACHE_LEN_1;

  tranintersection_launcher__add_value.writeAction(f"movlr 0(X30) X29 0 8") 
  tranintersection_launcher__add_value.writeAction(f"and X27 X29 X27") 
  ## print("cache len = %lu", cache_len);

  tranintersection_launcher__add_value.writeAction(f"sendr3_wret X26 intersection_launcher::add_return X27 X8 X9 X29") 
  tranintersection_launcher__add_value.writeAction(f"yield") 
  
  # Writing code for event intersection_launcher::add_return
  tranintersection_launcher__add_return = efa.writeEvent('intersection_launcher::add_return')
  ## long* local tmp_lmbuff = LMBASE;

  ## long num_write = tmp_lmbuff[NUM_WRITE] - 1;

  ## tmp_lmbuff[NUM_WRITE] = num_write;

  tranintersection_launcher__add_return.writeAction(f"__entry: subi X25 X25 1") 
  tranintersection_launcher__add_return.writeAction(f"bnei X25 0 __if_add_return_2_post") 
  tranintersection_launcher__add_return.writeAction(f"__if_add_return_0_true: movlr 8(X21) X27 0 8") 
  tranintersection_launcher__add_return.writeAction(f"bneiu X27 4 __if_add_return_2_post") 
  tranintersection_launcher__add_return.writeAction(f"__if_add_return_3_true: movlr 0(X21) X27 0 8") 
  tranintersection_launcher__add_return.writeAction(f"movir X26 -1") 
  tranintersection_launcher__add_return.writeAction(f"sri X26 X26 1") 
  tranintersection_launcher__add_return.writeAction(f"sendr_wcont X27 X26 X0 X0") 
  ## finally we can terminate

  tranintersection_launcher__add_return.writeAction(f"yield") 
  tranintersection_launcher__add_return.writeAction(f"__if_add_return_2_post: yield") 
  
  # Writing code for event intersection_launcher::write_back_cache
  tranintersection_launcher__write_back_cache = efa.writeEvent('intersection_launcher::write_back_cache')
  tranintersection_launcher__write_back_cache.writeAction(f"__entry: movrl X1 0(X21) 0 8") 
  tranintersection_launcher__write_back_cache.writeAction(f"movir X22 0") 
  tranintersection_launcher__write_back_cache.writeAction(f"addi X7 X27 0") 
  tranintersection_launcher__write_back_cache.writeAction(f"movlr 0(X27) X26 0 8") 
  tranintersection_launcher__write_back_cache.writeAction(f"addi X26 X26 1") 
  tranintersection_launcher__write_back_cache.writeAction(f"movir X25 0") 
  tranintersection_launcher__write_back_cache.writeAction(f"addi X7 X27 15920") 
  tranintersection_launcher__write_back_cache.writeAction(f"muli X26 X29 24") 
  tranintersection_launcher__write_back_cache.writeAction(f"add X27 X29 X26") 
  tranintersection_launcher__write_back_cache.writeAction(f"__while_write_back_cache_0_condition: bleu X26 X27 __while_write_back_cache_2_post") 
  tranintersection_launcher__write_back_cache.writeAction(f"__while_write_back_cache_1_body: movlr 8(X27) X29 0 8") 
  tranintersection_launcher__write_back_cache.writeAction(f"beqiu X29 0 __if_write_back_cache_5_post") 
  tranintersection_launcher__write_back_cache.writeAction(f"__if_write_back_cache_3_true: movlr 0(X27) X30 0 8") 
  tranintersection_launcher__write_back_cache.writeAction(f"sendr_dmlm_wret X30 intersection_launcher::intersection_end X29 X28") 
  tranintersection_launcher__write_back_cache.writeAction(f"addi X22 X22 1") 
  tranintersection_launcher__write_back_cache.writeAction(f"movrl X25 0(X27) 0 8") 
  tranintersection_launcher__write_back_cache.writeAction(f"movrl X25 8(X27) 0 8") 
  ## tmp_lmbuff[2] = num_write;

  tranintersection_launcher__write_back_cache.writeAction(f"__if_write_back_cache_5_post: addi X27 X27 24") 
  tranintersection_launcher__write_back_cache.writeAction(f"jmp __while_write_back_cache_0_condition") 
  tranintersection_launcher__write_back_cache.writeAction(f"__while_write_back_cache_2_post: bneiu X22 0 __if_write_back_cache_8_post") 
  tranintersection_launcher__write_back_cache.writeAction(f"__if_write_back_cache_6_true: movlr 0(X21) X27 0 8") 
  tranintersection_launcher__write_back_cache.writeAction(f"movir X26 -1") 
  tranintersection_launcher__write_back_cache.writeAction(f"sri X26 X26 1") 
  tranintersection_launcher__write_back_cache.writeAction(f"sendr_wcont X27 X26 X0 X0") 
  ## finally we can terminate

  tranintersection_launcher__write_back_cache.writeAction(f"yield_terminate") 
  tranintersection_launcher__write_back_cache.writeAction(f"__if_write_back_cache_8_post: yield") 
  
  # Writing code for event intersection_launcher::intersection_end
  tranintersection_launcher__intersection_end = efa.writeEvent('intersection_launcher::intersection_end')
  tranintersection_launcher__intersection_end.writeAction(f"__entry: subi X22 X22 1") 
  tranintersection_launcher__intersection_end.writeAction(f"bneiu X22 0 __if_intersection_end_2_post") 
  tranintersection_launcher__intersection_end.writeAction(f"__if_intersection_end_0_true: movlr 0(X21) X27 0 8") 
  tranintersection_launcher__intersection_end.writeAction(f"movir X26 -1") 
  tranintersection_launcher__intersection_end.writeAction(f"sri X26 X26 1") 
  tranintersection_launcher__intersection_end.writeAction(f"sendr_wcont X27 X26 X0 X0") 
  ## finally we can terminate

  tranintersection_launcher__intersection_end.writeAction(f"yield_terminate") 
  tranintersection_launcher__intersection_end.writeAction(f"__if_intersection_end_2_post: yield") 
  
  
  ########################################################
  ###### Writing code for thread intersection_cache ######
  ########################################################
  # Writing code for event intersection_cache::add_val_dram_write
  tranintersection_cache__add_val_dram_write = efa.writeEvent('intersection_cache::add_val_dram_write')
  tranintersection_cache__add_val_dram_write.writeAction(f"__entry: addi X7 X17 15920") 
  tranintersection_cache__add_val_dram_write.writeAction(f"muli X8 X22 24") 
  tranintersection_cache__add_val_dram_write.writeAction(f"add X17 X22 X17") 
  tranintersection_cache__add_val_dram_write.writeAction(f"movlr 0(X17) X22 0 8") 
  tranintersection_cache__add_val_dram_write.writeAction(f"bneu X22 X9 __if_add_val_dram_write_2_post") 
  ## cache hit

  tranintersection_cache__add_val_dram_write.writeAction(f"__if_add_val_dram_write_0_true: movlr 8(X17) X23 0 8") 
  tranintersection_cache__add_val_dram_write.writeAction(f"add X23 X10 X23") 
  tranintersection_cache__add_val_dram_write.writeAction(f"movrl X23 8(X17) 0 8") 
  tranintersection_cache__add_val_dram_write.writeAction(f"movir X24 -1") 
  tranintersection_cache__add_val_dram_write.writeAction(f"sri X24 X24 1") 
  tranintersection_cache__add_val_dram_write.writeAction(f"sendr_wcont X1 X24 X9 X23") 
  tranintersection_cache__add_val_dram_write.writeAction(f"yield_terminate") 
  ## cache old miss

  tranintersection_cache__add_val_dram_write.writeAction(f"__if_add_val_dram_write_2_post: bneiu X22 0 __if_add_val_dram_write_5_post") 
  ## empty cache

  tranintersection_cache__add_val_dram_write.writeAction(f"__if_add_val_dram_write_3_true: movrl X9 0(X17) 0 8") 
  tranintersection_cache__add_val_dram_write.writeAction(f"movrl X10 8(X17) 0 8") 
  tranintersection_cache__add_val_dram_write.writeAction(f"movrl X22 16(X17) 0 8") 
  tranintersection_cache__add_val_dram_write.writeAction(f"movir X23 -1") 
  tranintersection_cache__add_val_dram_write.writeAction(f"sri X23 X23 1") 
  tranintersection_cache__add_val_dram_write.writeAction(f"sendr_wcont X1 X23 X9 X10") 
  tranintersection_cache__add_val_dram_write.writeAction(f"yield_terminate") 
  tranintersection_cache__add_val_dram_write.writeAction(f"__if_add_val_dram_write_5_post: movlr 16(X17) X23 0 8") 
  tranintersection_cache__add_val_dram_write.writeAction(f"beqiu X23 0 __if_add_val_dram_write_8_post") 
  ## occupied

  tranintersection_cache__add_val_dram_write.writeAction(f"__if_add_val_dram_write_6_true: movir X24 0") 
  tranintersection_cache__add_val_dram_write.writeAction(f"evlb X24 intersection_cache::add_val_dram_write") 
  tranintersection_cache__add_val_dram_write.writeAction(f"evi X24 X24 255 4") 
  tranintersection_cache__add_val_dram_write.writeAction(f"ev X24 X24 X0 X0 8") 
  ## #ifdef DEBUG

  ## print("occupied cache_idx=%lu, addr=0x%lx, val=%lu", cache_idx, addr, val);

  ## #endif

  tranintersection_cache__add_val_dram_write.writeAction(f"sendr3_wcont X24 X1 X8 X9 X10") 
  tranintersection_cache__add_val_dram_write.writeAction(f"yield_terminate") 
  tranintersection_cache__add_val_dram_write.writeAction(f"__if_add_val_dram_write_8_post: addi X7 X21 0") 
  tranintersection_cache__add_val_dram_write.writeAction(f"movlr 24(X21) X24 0 8") 
  tranintersection_cache__add_val_dram_write.writeAction(f"movir X25 180") 
  tranintersection_cache__add_val_dram_write.writeAction(f"bgt X25 X24 __if_add_val_dram_write_11_post") 
  tranintersection_cache__add_val_dram_write.writeAction(f"__if_add_val_dram_write_9_true: movir X25 0") 
  tranintersection_cache__add_val_dram_write.writeAction(f"evlb X25 intersection_cache::add_val_dram_write") 
  tranintersection_cache__add_val_dram_write.writeAction(f"evi X25 X25 255 4") 
  tranintersection_cache__add_val_dram_write.writeAction(f"ev X25 X25 X0 X0 8") 
  tranintersection_cache__add_val_dram_write.writeAction(f"sendr3_wcont X25 X1 X8 X9 X10") 
  tranintersection_cache__add_val_dram_write.writeAction(f"yield_terminate") 
  tranintersection_cache__add_val_dram_write.writeAction(f"__if_add_val_dram_write_11_post: addi X1 X16 0") 
  tranintersection_cache__add_val_dram_write.writeAction(f"movir X18 1") 
  ## print("cache miss: nwid:%lu, cache_idx=%lu, addr=0x%lx, val=%lu", NETID, cache_idx, addr, val);

  tranintersection_cache__add_val_dram_write.writeAction(f"movir X23 0") 
  tranintersection_cache__add_val_dram_write.writeAction(f"evlb X23 intersection_cache::add_value_dram_write_return") 
  tranintersection_cache__add_val_dram_write.writeAction(f"evi X23 X23 255 4") 
  tranintersection_cache__add_val_dram_write.writeAction(f"ev X23 X23 X0 X0 8") 
  tranintersection_cache__add_val_dram_write.writeAction(f"addi X22 X22 0") 
  tranintersection_cache__add_val_dram_write.writeAction(f"movrl X9 0(X17) 0 8") 
  tranintersection_cache__add_val_dram_write.writeAction(f"movlr 8(X17) X23 0 8") 
  tranintersection_cache__add_val_dram_write.writeAction(f"movrl X10 8(X17) 0 8") 
  tranintersection_cache__add_val_dram_write.writeAction(f"movrl X18 16(X17) 0 8") 
  tranintersection_cache__add_val_dram_write.writeAction(f"sendr_dmlm_wret X22 intersection_cache::add_value_dram_write_return X23 X25") 
  ## write old value back to DRAM;

  tranintersection_cache__add_val_dram_write.writeAction(f"send_dmlm_ld_wret X9 intersection_cache::add_value_dram_read_return 1 X22") 
  tranintersection_cache__add_val_dram_write.writeAction(f"addi X9 X20 0") 
  tranintersection_cache__add_val_dram_write.writeAction(f"addi X24 X24 1") 
  tranintersection_cache__add_val_dram_write.writeAction(f"movrl X24 24(X21) 0 8") 
  tranintersection_cache__add_val_dram_write.writeAction(f"yield") 
  
  # Writing code for event intersection_cache::add_value_dram_write_return
  tranintersection_cache__add_value_dram_write_return = efa.writeEvent('intersection_cache::add_value_dram_write_return')
  tranintersection_cache__add_value_dram_write_return.writeAction(f"__entry: bnei X18 1 __if_add_value_dram_write_return_1_false") 
  tranintersection_cache__add_value_dram_write_return.writeAction(f"__if_add_value_dram_write_return_0_true: movir X18 0") 
  tranintersection_cache__add_value_dram_write_return.writeAction(f"jmp __if_add_value_dram_write_return_2_post") 
  tranintersection_cache__add_value_dram_write_return.writeAction(f"__if_add_value_dram_write_return_1_false: movrl X18 16(X17) 0 8") 
  tranintersection_cache__add_value_dram_write_return.writeAction(f"movir X24 -1") 
  tranintersection_cache__add_value_dram_write_return.writeAction(f"sri X24 X24 1") 
  tranintersection_cache__add_value_dram_write_return.writeAction(f"sendr_wcont X16 X24 X20 X19") 
  tranintersection_cache__add_value_dram_write_return.writeAction(f"movlr 24(X21) X24 0 8") 
  tranintersection_cache__add_value_dram_write_return.writeAction(f"subi X24 X24 1") 
  tranintersection_cache__add_value_dram_write_return.writeAction(f"movrl X24 24(X21) 0 8") 
  tranintersection_cache__add_value_dram_write_return.writeAction(f"yield_terminate") 
  tranintersection_cache__add_value_dram_write_return.writeAction(f"__if_add_value_dram_write_return_2_post: yield") 
  
  # Writing code for event intersection_cache::add_value_dram_read_return
  tranintersection_cache__add_value_dram_read_return = efa.writeEvent('intersection_cache::add_value_dram_read_return')
  tranintersection_cache__add_value_dram_read_return.writeAction(f"__entry: movlr 8(X17) X19 0 8") 
  tranintersection_cache__add_value_dram_read_return.writeAction(f"add X8 X19 X19") 
  tranintersection_cache__add_value_dram_read_return.writeAction(f"movrl X19 8(X17) 0 8") 
  tranintersection_cache__add_value_dram_read_return.writeAction(f"bnei X18 1 __if_add_value_dram_read_return_1_false") 
  tranintersection_cache__add_value_dram_read_return.writeAction(f"__if_add_value_dram_read_return_0_true: movir X18 0") 
  tranintersection_cache__add_value_dram_read_return.writeAction(f"jmp __if_add_value_dram_read_return_2_post") 
  tranintersection_cache__add_value_dram_read_return.writeAction(f"__if_add_value_dram_read_return_1_false: movrl X18 16(X17) 0 8") 
  tranintersection_cache__add_value_dram_read_return.writeAction(f"movir X24 -1") 
  tranintersection_cache__add_value_dram_read_return.writeAction(f"sri X24 X24 1") 
  tranintersection_cache__add_value_dram_read_return.writeAction(f"sendr_wcont X16 X24 X20 X19") 
  tranintersection_cache__add_value_dram_read_return.writeAction(f"movlr 24(X21) X24 0 8") 
  tranintersection_cache__add_value_dram_read_return.writeAction(f"subi X24 X24 1") 
  tranintersection_cache__add_value_dram_read_return.writeAction(f"movrl X24 24(X21) 0 8") 
  tranintersection_cache__add_value_dram_read_return.writeAction(f"yield_terminate") 
  tranintersection_cache__add_value_dram_read_return.writeAction(f"__if_add_value_dram_read_return_2_post: yield") 
  