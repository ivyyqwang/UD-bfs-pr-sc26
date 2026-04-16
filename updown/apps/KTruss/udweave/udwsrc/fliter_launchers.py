from linker.EFAProgram import efaProgram

## UDWeave version: unknown

## Global constants

@efaProgram
def EFA_fliter_launchers(efa):
  efa.code_level = 'machine'
  state0 = efa.State("udweave_init") #Only one state code 
  efa.add_initId(state0.state_id)
  ## Static declarations
  ## Scoped Variable "num_threads_active" uses Register X16, scope (0)
  ## Scoped Variable "master_dram_tail_ptr" uses Register X17, scope (0)
  ## Scoped Variable "master_dram_head_ptr" uses Register X18, scope (0)
  ## Scoped Variable "num_v" uses Register X19, scope (0)
  ## Scoped Variable "deleted_edges" uses Register X20, scope (0)
  ## Scoped Variable "k" uses Register X21, scope (0)
  ## Scoped Variable "g_v" uses Register X22, scope (0)
  ## Scoped Variable "g_v_write" uses Register X23, scope (0)
  ## Scoped Variable "master_dram_write_ptr" uses Register X24, scope (0)
  ## Scoped Variable "cont" uses Register X25, scope (0)
  ## Scoped Variable "count" uses Register X26, scope (0)
  ## Scoped Variable "updated_edges" uses Register X27, scope (0)
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
  ###### Writing code for thread filter_launcher ######
  #####################################################
  # Writing code for event filter_launcher::start
  tranfilter_launcher__start = efa.writeEvent('filter_launcher::start')
  ## send_event(CCONT, 0, NETID, IGNRCONT);

  ## yield_terminate;

  tranfilter_launcher__start.writeAction(f"__entry: mul X15 X0 X28") 
  tranfilter_launcher__start.writeAction(f"add X10 X28 X29") 
  tranfilter_launcher__start.writeAction(f"send_dmlm_ld_wret X29 filter_launcher::read_master_dram_length 1 X30") 
  tranfilter_launcher__start.writeAction(f"movir X16 0") 
  tranfilter_launcher__start.writeAction(f"addi X29 X17 8") 
  tranfilter_launcher__start.writeAction(f"addi X17 X18 0") 
  tranfilter_launcher__start.writeAction(f"add X11 X28 X24") 
  tranfilter_launcher__start.writeAction(f"addi X24 X24 8") 
  tranfilter_launcher__start.writeAction(f"movir X19 0") 
  tranfilter_launcher__start.writeAction(f"movir X20 0") 
  tranfilter_launcher__start.writeAction(f"movir X27 0") 
  tranfilter_launcher__start.writeAction(f"addi X8 X21 0") 
  tranfilter_launcher__start.writeAction(f"addi X9 X22 0") 
  tranfilter_launcher__start.writeAction(f"addi X1 X25 0") 
  tranfilter_launcher__start.writeAction(f"movir X26 1") 
  tranfilter_launcher__start.writeAction(f"addi X9 X23 0") 
  tranfilter_launcher__start.writeAction(f"bnei X13 1 __if_start_2_post") 
  tranfilter_launcher__start.writeAction(f"__if_start_0_true: addi X14 X23 0") 
  tranfilter_launcher__start.writeAction(f"__if_start_2_post: yield") 
  
  # Writing code for event filter_launcher::read_master_dram_length
  tranfilter_launcher__read_master_dram_length = efa.writeEvent('filter_launcher::read_master_dram_length')
  tranfilter_launcher__read_master_dram_length.writeAction(f"__entry: bnei X8 0 __if_read_master_dram_length_2_post") 
  tranfilter_launcher__read_master_dram_length.writeAction(f"__if_read_master_dram_length_0_true: movir X28 -1") 
  tranfilter_launcher__read_master_dram_length.writeAction(f"sri X28 X28 1") 
  tranfilter_launcher__read_master_dram_length.writeAction(f"sendr3_wcont X25 X28 X20 X27 X19") 
  tranfilter_launcher__read_master_dram_length.writeAction(f"yield_terminate") 
  tranfilter_launcher__read_master_dram_length.writeAction(f"__if_read_master_dram_length_2_post: sli X8 X28 3") 
  tranfilter_launcher__read_master_dram_length.writeAction(f"add X18 X28 X17") 
  tranfilter_launcher__read_master_dram_length.writeAction(f"movir X29 64") 
  tranfilter_launcher__read_master_dram_length.writeAction(f"ble X29 X8 __if_read_master_dram_length_5_post") 
  tranfilter_launcher__read_master_dram_length.writeAction(f"__if_read_master_dram_length_3_true: addi X8 X29 0") 
  tranfilter_launcher__read_master_dram_length.writeAction(f"__if_read_master_dram_length_5_post: addi X7 X30 32") 
  tranfilter_launcher__read_master_dram_length.writeAction(f"movrl X22 0(X30) 0 8") 
  tranfilter_launcher__read_master_dram_length.writeAction(f"movrl X21 16(X30) 0 8") 
  tranfilter_launcher__read_master_dram_length.writeAction(f"bneu X22 X23 __if_read_master_dram_length_7_false") 
  tranfilter_launcher__read_master_dram_length.writeAction(f"__if_read_master_dram_length_6_true: movir X28 0") 
  tranfilter_launcher__read_master_dram_length.writeAction(f"evlb X28 vertex_filter_master__launch") 
  tranfilter_launcher__read_master_dram_length.writeAction(f"evi X28 X28 255 4") 
  tranfilter_launcher__read_master_dram_length.writeAction(f"ev X28 X28 X0 X0 8") 
  tranfilter_launcher__read_master_dram_length.writeAction(f"__while_read_master_dram_length_9_condition: ble X29 X16 __while_read_master_dram_length_11_post") 
  tranfilter_launcher__read_master_dram_length.writeAction(f"__while_read_master_dram_length_10_body: movrl X18 8(X30) 0 8") 
  tranfilter_launcher__read_master_dram_length.writeAction(f"movrl X16 24(X30) 0 8") 
  tranfilter_launcher__read_master_dram_length.writeAction(f"send_wret X28 filter_launcher::vertex_term X30 4 X31") 
  ## send_dram_read(master_dram_head_ptr, 1, receive_dram);

  tranfilter_launcher__read_master_dram_length.writeAction(f"addi X18 X18 8") 
  tranfilter_launcher__read_master_dram_length.writeAction(f"addi X16 X16 1") 
  tranfilter_launcher__read_master_dram_length.writeAction(f"jmp __while_read_master_dram_length_9_condition") 
  tranfilter_launcher__read_master_dram_length.writeAction(f"__while_read_master_dram_length_11_post: jmp __if_read_master_dram_length_8_post") 
  tranfilter_launcher__read_master_dram_length.writeAction(f"__if_read_master_dram_length_7_false: movrl X23 32(X30) 0 8") 
  tranfilter_launcher__read_master_dram_length.writeAction(f"movir X28 0") 
  tranfilter_launcher__read_master_dram_length.writeAction(f"evlb X28 vertex_filter_master_local__launch") 
  tranfilter_launcher__read_master_dram_length.writeAction(f"evi X28 X28 255 4") 
  tranfilter_launcher__read_master_dram_length.writeAction(f"ev X28 X28 X0 X0 8") 
  tranfilter_launcher__read_master_dram_length.writeAction(f"__while_read_master_dram_length_12_condition: ble X29 X16 __if_read_master_dram_length_8_post") 
  tranfilter_launcher__read_master_dram_length.writeAction(f"__while_read_master_dram_length_13_body: movrl X18 8(X30) 0 8") 
  tranfilter_launcher__read_master_dram_length.writeAction(f"movrl X16 24(X30) 0 8") 
  tranfilter_launcher__read_master_dram_length.writeAction(f"send_wret X28 filter_launcher::vertex_term X30 5 X31") 
  ## send_dram_read(master_dram_head_ptr, 1, receive_dram);

  tranfilter_launcher__read_master_dram_length.writeAction(f"addi X18 X18 8") 
  tranfilter_launcher__read_master_dram_length.writeAction(f"addi X16 X16 1") 
  tranfilter_launcher__read_master_dram_length.writeAction(f"jmp __while_read_master_dram_length_12_condition") 
  tranfilter_launcher__read_master_dram_length.writeAction(f"__if_read_master_dram_length_8_post: yield") 
  
  # Writing code for event filter_launcher::vertex_term
  tranfilter_launcher__vertex_term = efa.writeEvent('filter_launcher::vertex_term')
  ## vertex thread terminated

  tranfilter_launcher__vertex_term.writeAction(f"__entry: subi X16 X16 1") 
  tranfilter_launcher__vertex_term.writeAction(f"blei X9 0 __if_vertex_term_2_post") 
  tranfilter_launcher__vertex_term.writeAction(f"__if_vertex_term_0_true: addi X19 X19 1") 
  tranfilter_launcher__vertex_term.writeAction(f"sendr_dmlm_wret X24 filter_launcher::write_return X10 X30") 
  tranfilter_launcher__vertex_term.writeAction(f"addi X24 X24 8") 
  tranfilter_launcher__vertex_term.writeAction(f"addi X26 X26 1") 
  ## print("[DEBUG][NWID %lu] <vertex_term> _deleted_edges = %lu, v1:%lu, deg:%lu", NETID, _deleted_edges, _v, _deg);

  tranfilter_launcher__vertex_term.writeAction(f"__if_vertex_term_2_post: add X20 X8 X20") 
  tranfilter_launcher__vertex_term.writeAction(f"add X27 X9 X27") 
  tranfilter_launcher__vertex_term.writeAction(f"bneu X18 X17 __if_vertex_term_5_post") 
  ## head == tail So nothing more to launch! 

  tranfilter_launcher__vertex_term.writeAction(f"__if_vertex_term_3_true: bneiu X16 0 __if_vertex_term_8_post") 
  tranfilter_launcher__vertex_term.writeAction(f"__if_vertex_term_6_true: sli X19 X30 3") 
  tranfilter_launcher__vertex_term.writeAction(f"addi X30 X30 8") 
  tranfilter_launcher__vertex_term.writeAction(f"sub X24 X30 X30") 
  tranfilter_launcher__vertex_term.writeAction(f"sendr_dmlm_wret X30 filter_launcher::write_return X19 X28") 
  ## print("[DEBUG][NWID %lu] master_dram_len_ptr = 0x%lx, length = %lu", NETID, master_dram_len_ptr, num_v);

  tranfilter_launcher__vertex_term.writeAction(f"__if_vertex_term_8_post: yield") 
  ## Check if there's stuff in memory

  tranfilter_launcher__vertex_term.writeAction(f"__if_vertex_term_5_post: bequ X18 X17 __if_vertex_term_11_post") 
  tranfilter_launcher__vertex_term.writeAction(f"__if_vertex_term_9_true: addi X7 X30 32") 
  tranfilter_launcher__vertex_term.writeAction(f"movrl X22 0(X30) 0 8") 
  tranfilter_launcher__vertex_term.writeAction(f"movrl X18 8(X30) 0 8") 
  tranfilter_launcher__vertex_term.writeAction(f"movrl X21 16(X30) 0 8") 
  tranfilter_launcher__vertex_term.writeAction(f"movrl X11 24(X30) 0 8") 
  tranfilter_launcher__vertex_term.writeAction(f"bneu X22 X23 __if_vertex_term_13_false") 
  tranfilter_launcher__vertex_term.writeAction(f"__if_vertex_term_12_true: movir X28 0") 
  tranfilter_launcher__vertex_term.writeAction(f"evlb X28 vertex_filter_master__launch") 
  tranfilter_launcher__vertex_term.writeAction(f"evi X28 X28 255 4") 
  tranfilter_launcher__vertex_term.writeAction(f"ev X28 X28 X0 X0 8") 
  tranfilter_launcher__vertex_term.writeAction(f"send_wret X28 filter_launcher::vertex_term X30 4 X29") 
  tranfilter_launcher__vertex_term.writeAction(f"jmp __if_vertex_term_14_post") 
  tranfilter_launcher__vertex_term.writeAction(f"__if_vertex_term_13_false: movrl X23 32(X30) 0 8") 
  tranfilter_launcher__vertex_term.writeAction(f"movir X28 0") 
  tranfilter_launcher__vertex_term.writeAction(f"evlb X28 vertex_filter_master_local__launch") 
  tranfilter_launcher__vertex_term.writeAction(f"evi X28 X28 255 4") 
  tranfilter_launcher__vertex_term.writeAction(f"ev X28 X28 X0 X0 8") 
  tranfilter_launcher__vertex_term.writeAction(f"send_wret X28 filter_launcher::vertex_term X30 5 X29") 
  ## send_dram_read(master_dram_head_ptr, 1, receive_dram);

  tranfilter_launcher__vertex_term.writeAction(f"__if_vertex_term_14_post: addi X18 X18 8") 
  tranfilter_launcher__vertex_term.writeAction(f"addi X16 X16 1") 
  tranfilter_launcher__vertex_term.writeAction(f"__if_vertex_term_11_post: yield") 
  
  # Writing code for event filter_launcher::write_return
  tranfilter_launcher__write_return = efa.writeEvent('filter_launcher::write_return')
  tranfilter_launcher__write_return.writeAction(f"__entry: subi X26 X26 1") 
  tranfilter_launcher__write_return.writeAction(f"bnei X26 0 __if_write_return_2_post") 
  tranfilter_launcher__write_return.writeAction(f"__if_write_return_0_true: movir X30 -1") 
  tranfilter_launcher__write_return.writeAction(f"sri X30 X30 1") 
  tranfilter_launcher__write_return.writeAction(f"sendr3_wcont X25 X30 X20 X27 X19") 
  tranfilter_launcher__write_return.writeAction(f"yield_terminate") 
  tranfilter_launcher__write_return.writeAction(f"__if_write_return_2_post: yield") 
  