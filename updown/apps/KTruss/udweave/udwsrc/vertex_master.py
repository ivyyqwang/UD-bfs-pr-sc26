from linker.EFAProgram import efaProgram

## UDWeave version: unknown

## Global constants

@efaProgram
def EFA_vertex_master(efa):
  efa.code_level = 'machine'
  state0 = efa.State("udweave_init") #Only one state code 
  efa.add_initId(state0.state_id)
  ## Static declarations
  ## Scoped Variable "v1" uses Register X16, scope (0)
  ## Scoped Variable "cont" uses Register X17, scope (0)
  ## Scoped Variable "count" uses Register X18, scope (0)
  ## Scoped Variable "nl_ptr_start" uses Register X19, scope (0)
  ## Scoped Variable "count_ptr_start" uses Register X20, scope (0)
  ## Scoped Variable "count_ptr_end" uses Register X21, scope (0)
  ## Scoped Variable "lmbuff" uses Register X22, scope (0)
  ## Scoped Variable "temp_lmbuff" uses Register X23, scope (0)
  ## Scoped Variable "num_int" uses Register X24, scope (0)
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
  
  ###################################################
  ###### Writing code for thread vertex_master ######
  ###################################################
  # Writing code for event vertex_master::launch
  tranvertex_master__launch = efa.writeEvent('vertex_master::launch')
  ## #ifdef DEBUG

  ## print("[DEBUG][NWID %lu] <vertex_master> inputs g_v:%lu, v1:%lu, thread:%lu", NETID, _g_v, _v1, TID);

  ## #endif

  tranvertex_master__launch.writeAction(f"__entry: addi X9 X16 0") 
  tranvertex_master__launch.writeAction(f"addi X1 X17 0") 
  tranvertex_master__launch.writeAction(f"movir X24 0") 
  tranvertex_master__launch.writeAction(f"movir X18 1") 
  ## Fetch V1 8 bytes from g_v[v1]

  tranvertex_master__launch.writeAction(f"sli X16 X25 6") 
  tranvertex_master__launch.writeAction(f"add X8 X25 X25") 
  tranvertex_master__launch.writeAction(f"send_dmlm_ld_wret X25 vertex_master::v1_return 4 X26") 
  tranvertex_master__launch.writeAction(f"yield") 
  
  # Writing code for event vertex_master::v1_return
  tranvertex_master__v1_return = efa.writeEvent('vertex_master::v1_return')
  ##deg, id, neigh, count_ptr

  tranvertex_master__v1_return.writeAction(f"__entry: subi X18 X18 1") 
  ## print("[DEBUG][NWID %lu] <vertex_master> inputs v1:%lu, deg:%lu, thread:%lu", NETID, op1, op0, TID);

  tranvertex_master__v1_return.writeAction(f"bgtiu X8 1 __if_v1_return_2_post") 
  ## thread can be returned to master_launcher 

  tranvertex_master__v1_return.writeAction(f"__if_v1_return_0_true: bneiu X18 0 __if_v1_return_5_post") 
  tranvertex_master__v1_return.writeAction(f"__if_v1_return_3_true: movir X25 -1") 
  tranvertex_master__v1_return.writeAction(f"sri X25 X25 1") 
  tranvertex_master__v1_return.writeAction(f"sendr_wcont X17 X25 X24 X24") 
  tranvertex_master__v1_return.writeAction(f"yield_terminate") 
  tranvertex_master__v1_return.writeAction(f"__if_v1_return_5_post: yield") 
  ## Vertex needs to be counted

  tranvertex_master__v1_return.writeAction(f"__if_v1_return_2_post: addi X10 X25 0") 
  tranvertex_master__v1_return.writeAction(f"sli X8 X26 3") 
  tranvertex_master__v1_return.writeAction(f"add X10 X26 X26") 
  tranvertex_master__v1_return.writeAction(f"__while_v1_return_6_condition: bleu X26 X25 __while_v1_return_8_post") 
  tranvertex_master__v1_return.writeAction(f"__while_v1_return_7_body: send_dmlm_ld_wret X25 vertex_master::v1_neighs 8 X27") 
  tranvertex_master__v1_return.writeAction(f"addi X18 X18 1") 
  tranvertex_master__v1_return.writeAction(f"addi X25 X25 64") 
  tranvertex_master__v1_return.writeAction(f"jmp __while_v1_return_6_condition") 
  tranvertex_master__v1_return.writeAction(f"__while_v1_return_8_post: addi X7 X22 0") 
  tranvertex_master__v1_return.writeAction(f"addi X7 X23 32") 
  tranvertex_master__v1_return.writeAction(f"addi X11 X20 0") 
  tranvertex_master__v1_return.writeAction(f"sli X8 X25 3") 
  tranvertex_master__v1_return.writeAction(f"add X11 X25 X21") 
  tranvertex_master__v1_return.writeAction(f"addi X10 X19 0") 
  tranvertex_master__v1_return.writeAction(f"yield") 
  
  # Writing code for event vertex_master::v1_neighs
  tranvertex_master__v1_neighs = efa.writeEvent('vertex_master::v1_neighs')
  ## Update the return count

  ## unsigned long num_int = lmbuff[NUM_INT];

  tranvertex_master__v1_neighs.writeAction(f"__entry: movlr 152(X22) X25 0 8") 
  tranvertex_master__v1_neighs.writeAction(f"sub X3 X19 X26") 
  tranvertex_master__v1_neighs.writeAction(f"add X26 X20 X26") 
  tranvertex_master__v1_neighs.writeAction(f"subi X18 X18 1") 
  tranvertex_master__v1_neighs.writeAction(f"movrl X16 0(X23) 0 8") 
  tranvertex_master__v1_neighs.writeAction(f"movrl X0 24(X23) 0 8") 
  tranvertex_master__v1_neighs.writeAction(f"bleu X21 X26 __if_v1_neighs_1_false") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_0_true: addi X8 X27 0") 
  tranvertex_master__v1_neighs.writeAction(f"ble X16 X27 __if_v1_neighs_4_false") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_3_true: addi X24 X24 1") 
  ## next_nwid = hash(v1, hash(v2, HASH_SEED))

  tranvertex_master__v1_neighs.writeAction(f"movir X28 0") 
  tranvertex_master__v1_neighs.writeAction(f"hash X27 X28") 
  tranvertex_master__v1_neighs.writeAction(f"hash X16 X28") 
  tranvertex_master__v1_neighs.writeAction(f"and X28 X25 X28") 
  ## next_nwid = next_nwid % total_lanes

  tranvertex_master__v1_neighs.writeAction(f"movir X29 0") 
  tranvertex_master__v1_neighs.writeAction(f"evlb X29 intersection_launcher__send_to_worker_thread5") 
  tranvertex_master__v1_neighs.writeAction(f"evi X29 X29 255 4") 
  tranvertex_master__v1_neighs.writeAction(f"ev X29 X29 X28 X28 8") 
  tranvertex_master__v1_neighs.writeAction(f"movrl X27 8(X23) 0 8") 
  tranvertex_master__v1_neighs.writeAction(f"movrl X27 16(X23) 0 8") 
  tranvertex_master__v1_neighs.writeAction(f"movrl X26 32(X23) 0 8") 
  tranvertex_master__v1_neighs.writeAction(f"movir X28 -1") 
  tranvertex_master__v1_neighs.writeAction(f"sri X28 X28 1") 
  tranvertex_master__v1_neighs.writeAction(f"send_wcont X29 X28 X23 5") 
  tranvertex_master__v1_neighs.writeAction(f"jmp __if_v1_neighs_5_post") 
  ## lmbuff[NUM_INT] = num_int;

  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_4_false: bneiu X18 0 __if_v1_neighs_8_post") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_6_true: movir X29 -1") 
  tranvertex_master__v1_neighs.writeAction(f"sri X29 X29 1") 
  tranvertex_master__v1_neighs.writeAction(f"sendr_wcont X17 X29 X24 X24") 
  tranvertex_master__v1_neighs.writeAction(f"yield_terminate") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_8_post: yield") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_5_post: addi X26 X26 8") 
  tranvertex_master__v1_neighs.writeAction(f"jmp __if_v1_neighs_2_post") 
  ## lmbuff[NUM_INT] = num_int;

  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_1_false: bneiu X18 0 __if_v1_neighs_11_post") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_9_true: movir X27 -1") 
  tranvertex_master__v1_neighs.writeAction(f"sri X27 X27 1") 
  tranvertex_master__v1_neighs.writeAction(f"sendr_wcont X17 X27 X24 X24") 
  tranvertex_master__v1_neighs.writeAction(f"yield_terminate") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_11_post: yield") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_2_post: bleu X21 X26 __if_v1_neighs_13_false") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_12_true: addi X9 X27 0") 
  tranvertex_master__v1_neighs.writeAction(f"ble X16 X27 __if_v1_neighs_16_false") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_15_true: addi X24 X24 1") 
  ## next_nwid = hash(v1, hash(v2, HASH_SEED))

  tranvertex_master__v1_neighs.writeAction(f"movir X29 0") 
  tranvertex_master__v1_neighs.writeAction(f"hash X27 X29") 
  tranvertex_master__v1_neighs.writeAction(f"hash X16 X29") 
  tranvertex_master__v1_neighs.writeAction(f"and X29 X25 X29") 
  ## next_nwid = next_nwid % total_lanes

  tranvertex_master__v1_neighs.writeAction(f"movir X28 0") 
  tranvertex_master__v1_neighs.writeAction(f"evlb X28 intersection_launcher__send_to_worker_thread5") 
  tranvertex_master__v1_neighs.writeAction(f"evi X28 X28 255 4") 
  tranvertex_master__v1_neighs.writeAction(f"ev X28 X28 X29 X29 8") 
  tranvertex_master__v1_neighs.writeAction(f"movrl X27 8(X23) 0 8") 
  tranvertex_master__v1_neighs.writeAction(f"movrl X27 16(X23) 0 8") 
  tranvertex_master__v1_neighs.writeAction(f"movrl X26 32(X23) 0 8") 
  tranvertex_master__v1_neighs.writeAction(f"movir X29 -1") 
  tranvertex_master__v1_neighs.writeAction(f"sri X29 X29 1") 
  tranvertex_master__v1_neighs.writeAction(f"send_wcont X28 X29 X23 5") 
  tranvertex_master__v1_neighs.writeAction(f"jmp __if_v1_neighs_17_post") 
  ## lmbuff[NUM_INT] = num_int;

  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_16_false: bneiu X18 0 __if_v1_neighs_20_post") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_18_true: movir X28 -1") 
  tranvertex_master__v1_neighs.writeAction(f"sri X28 X28 1") 
  tranvertex_master__v1_neighs.writeAction(f"sendr_wcont X17 X28 X24 X24") 
  tranvertex_master__v1_neighs.writeAction(f"yield_terminate") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_20_post: yield") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_17_post: addi X26 X26 8") 
  tranvertex_master__v1_neighs.writeAction(f"jmp __if_v1_neighs_14_post") 
  ## lmbuff[NUM_INT] = num_int;

  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_13_false: bneiu X18 0 __if_v1_neighs_23_post") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_21_true: movir X27 -1") 
  tranvertex_master__v1_neighs.writeAction(f"sri X27 X27 1") 
  tranvertex_master__v1_neighs.writeAction(f"sendr_wcont X17 X27 X24 X24") 
  tranvertex_master__v1_neighs.writeAction(f"yield_terminate") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_23_post: yield") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_14_post: bleu X21 X26 __if_v1_neighs_25_false") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_24_true: addi X10 X27 0") 
  tranvertex_master__v1_neighs.writeAction(f"ble X16 X27 __if_v1_neighs_28_false") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_27_true: addi X24 X24 1") 
  ## next_nwid = hash(v1, hash(v2, HASH_SEED))

  tranvertex_master__v1_neighs.writeAction(f"movir X28 0") 
  tranvertex_master__v1_neighs.writeAction(f"hash X27 X28") 
  tranvertex_master__v1_neighs.writeAction(f"hash X16 X28") 
  tranvertex_master__v1_neighs.writeAction(f"and X28 X25 X28") 
  ## next_nwid = next_nwid % total_lanes

  tranvertex_master__v1_neighs.writeAction(f"movir X29 0") 
  tranvertex_master__v1_neighs.writeAction(f"evlb X29 intersection_launcher__send_to_worker_thread5") 
  tranvertex_master__v1_neighs.writeAction(f"evi X29 X29 255 4") 
  tranvertex_master__v1_neighs.writeAction(f"ev X29 X29 X28 X28 8") 
  tranvertex_master__v1_neighs.writeAction(f"movrl X27 8(X23) 0 8") 
  tranvertex_master__v1_neighs.writeAction(f"movrl X27 16(X23) 0 8") 
  tranvertex_master__v1_neighs.writeAction(f"movrl X26 32(X23) 0 8") 
  tranvertex_master__v1_neighs.writeAction(f"movir X28 -1") 
  tranvertex_master__v1_neighs.writeAction(f"sri X28 X28 1") 
  tranvertex_master__v1_neighs.writeAction(f"send_wcont X29 X28 X23 5") 
  tranvertex_master__v1_neighs.writeAction(f"jmp __if_v1_neighs_29_post") 
  ## lmbuff[NUM_INT] = num_int;

  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_28_false: bneiu X18 0 __if_v1_neighs_32_post") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_30_true: movir X29 -1") 
  tranvertex_master__v1_neighs.writeAction(f"sri X29 X29 1") 
  tranvertex_master__v1_neighs.writeAction(f"sendr_wcont X17 X29 X24 X24") 
  tranvertex_master__v1_neighs.writeAction(f"yield_terminate") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_32_post: yield") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_29_post: addi X26 X26 8") 
  tranvertex_master__v1_neighs.writeAction(f"jmp __if_v1_neighs_26_post") 
  ## lmbuff[NUM_INT] = num_int;

  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_25_false: bneiu X18 0 __if_v1_neighs_35_post") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_33_true: movir X27 -1") 
  tranvertex_master__v1_neighs.writeAction(f"sri X27 X27 1") 
  tranvertex_master__v1_neighs.writeAction(f"sendr_wcont X17 X27 X24 X24") 
  tranvertex_master__v1_neighs.writeAction(f"yield_terminate") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_35_post: yield") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_26_post: bleu X21 X26 __if_v1_neighs_37_false") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_36_true: addi X11 X27 0") 
  tranvertex_master__v1_neighs.writeAction(f"ble X16 X27 __if_v1_neighs_40_false") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_39_true: addi X24 X24 1") 
  ## next_nwid = hash(v1, hash(v2, HASH_SEED))

  tranvertex_master__v1_neighs.writeAction(f"movir X29 0") 
  tranvertex_master__v1_neighs.writeAction(f"hash X27 X29") 
  tranvertex_master__v1_neighs.writeAction(f"hash X16 X29") 
  tranvertex_master__v1_neighs.writeAction(f"and X29 X25 X29") 
  ## next_nwid = next_nwid % total_lanes

  tranvertex_master__v1_neighs.writeAction(f"movir X28 0") 
  tranvertex_master__v1_neighs.writeAction(f"evlb X28 intersection_launcher__send_to_worker_thread5") 
  tranvertex_master__v1_neighs.writeAction(f"evi X28 X28 255 4") 
  tranvertex_master__v1_neighs.writeAction(f"ev X28 X28 X29 X29 8") 
  tranvertex_master__v1_neighs.writeAction(f"movrl X27 8(X23) 0 8") 
  tranvertex_master__v1_neighs.writeAction(f"movrl X27 16(X23) 0 8") 
  tranvertex_master__v1_neighs.writeAction(f"movrl X26 32(X23) 0 8") 
  tranvertex_master__v1_neighs.writeAction(f"movir X29 -1") 
  tranvertex_master__v1_neighs.writeAction(f"sri X29 X29 1") 
  tranvertex_master__v1_neighs.writeAction(f"send_wcont X28 X29 X23 5") 
  tranvertex_master__v1_neighs.writeAction(f"jmp __if_v1_neighs_41_post") 
  ## lmbuff[NUM_INT] = num_int;

  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_40_false: bneiu X18 0 __if_v1_neighs_44_post") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_42_true: movir X28 -1") 
  tranvertex_master__v1_neighs.writeAction(f"sri X28 X28 1") 
  tranvertex_master__v1_neighs.writeAction(f"sendr_wcont X17 X28 X24 X24") 
  tranvertex_master__v1_neighs.writeAction(f"yield_terminate") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_44_post: yield") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_41_post: addi X26 X26 8") 
  tranvertex_master__v1_neighs.writeAction(f"jmp __if_v1_neighs_38_post") 
  ## lmbuff[NUM_INT] = num_int;

  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_37_false: bneiu X18 0 __if_v1_neighs_47_post") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_45_true: movir X27 -1") 
  tranvertex_master__v1_neighs.writeAction(f"sri X27 X27 1") 
  tranvertex_master__v1_neighs.writeAction(f"sendr_wcont X17 X27 X24 X24") 
  tranvertex_master__v1_neighs.writeAction(f"yield_terminate") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_47_post: yield") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_38_post: bleu X21 X26 __if_v1_neighs_49_false") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_48_true: addi X12 X27 0") 
  tranvertex_master__v1_neighs.writeAction(f"ble X16 X27 __if_v1_neighs_52_false") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_51_true: addi X24 X24 1") 
  ## next_nwid = hash(v1, hash(v2, HASH_SEED))

  tranvertex_master__v1_neighs.writeAction(f"movir X28 0") 
  tranvertex_master__v1_neighs.writeAction(f"hash X27 X28") 
  tranvertex_master__v1_neighs.writeAction(f"hash X16 X28") 
  tranvertex_master__v1_neighs.writeAction(f"and X28 X25 X28") 
  ## next_nwid = next_nwid % total_lanes

  tranvertex_master__v1_neighs.writeAction(f"movir X29 0") 
  tranvertex_master__v1_neighs.writeAction(f"evlb X29 intersection_launcher__send_to_worker_thread5") 
  tranvertex_master__v1_neighs.writeAction(f"evi X29 X29 255 4") 
  tranvertex_master__v1_neighs.writeAction(f"ev X29 X29 X28 X28 8") 
  tranvertex_master__v1_neighs.writeAction(f"movrl X27 8(X23) 0 8") 
  tranvertex_master__v1_neighs.writeAction(f"movrl X27 16(X23) 0 8") 
  tranvertex_master__v1_neighs.writeAction(f"movrl X26 32(X23) 0 8") 
  tranvertex_master__v1_neighs.writeAction(f"movir X28 -1") 
  tranvertex_master__v1_neighs.writeAction(f"sri X28 X28 1") 
  tranvertex_master__v1_neighs.writeAction(f"send_wcont X29 X28 X23 5") 
  tranvertex_master__v1_neighs.writeAction(f"jmp __if_v1_neighs_53_post") 
  ## lmbuff[NUM_INT] = num_int;

  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_52_false: bneiu X18 0 __if_v1_neighs_56_post") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_54_true: movir X29 -1") 
  tranvertex_master__v1_neighs.writeAction(f"sri X29 X29 1") 
  tranvertex_master__v1_neighs.writeAction(f"sendr_wcont X17 X29 X24 X24") 
  tranvertex_master__v1_neighs.writeAction(f"yield_terminate") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_56_post: yield") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_53_post: addi X26 X26 8") 
  tranvertex_master__v1_neighs.writeAction(f"jmp __if_v1_neighs_50_post") 
  ## lmbuff[NUM_INT] = num_int;

  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_49_false: bneiu X18 0 __if_v1_neighs_59_post") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_57_true: movir X27 -1") 
  tranvertex_master__v1_neighs.writeAction(f"sri X27 X27 1") 
  tranvertex_master__v1_neighs.writeAction(f"sendr_wcont X17 X27 X24 X24") 
  tranvertex_master__v1_neighs.writeAction(f"yield_terminate") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_59_post: yield") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_50_post: bleu X21 X26 __if_v1_neighs_61_false") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_60_true: addi X13 X27 0") 
  tranvertex_master__v1_neighs.writeAction(f"ble X16 X27 __if_v1_neighs_64_false") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_63_true: addi X24 X24 1") 
  ## next_nwid = hash(v1, hash(v2, HASH_SEED))

  tranvertex_master__v1_neighs.writeAction(f"movir X29 0") 
  tranvertex_master__v1_neighs.writeAction(f"hash X27 X29") 
  tranvertex_master__v1_neighs.writeAction(f"hash X16 X29") 
  tranvertex_master__v1_neighs.writeAction(f"and X29 X25 X29") 
  ## next_nwid = next_nwid % total_lanes

  tranvertex_master__v1_neighs.writeAction(f"movir X28 0") 
  tranvertex_master__v1_neighs.writeAction(f"evlb X28 intersection_launcher__send_to_worker_thread5") 
  tranvertex_master__v1_neighs.writeAction(f"evi X28 X28 255 4") 
  tranvertex_master__v1_neighs.writeAction(f"ev X28 X28 X29 X29 8") 
  tranvertex_master__v1_neighs.writeAction(f"movrl X27 8(X23) 0 8") 
  tranvertex_master__v1_neighs.writeAction(f"movrl X27 16(X23) 0 8") 
  tranvertex_master__v1_neighs.writeAction(f"movrl X26 32(X23) 0 8") 
  tranvertex_master__v1_neighs.writeAction(f"movir X29 -1") 
  tranvertex_master__v1_neighs.writeAction(f"sri X29 X29 1") 
  tranvertex_master__v1_neighs.writeAction(f"send_wcont X28 X29 X23 5") 
  tranvertex_master__v1_neighs.writeAction(f"jmp __if_v1_neighs_65_post") 
  ## lmbuff[NUM_INT] = num_int;

  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_64_false: bneiu X18 0 __if_v1_neighs_68_post") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_66_true: movir X28 -1") 
  tranvertex_master__v1_neighs.writeAction(f"sri X28 X28 1") 
  tranvertex_master__v1_neighs.writeAction(f"sendr_wcont X17 X28 X24 X24") 
  tranvertex_master__v1_neighs.writeAction(f"yield_terminate") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_68_post: yield") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_65_post: addi X26 X26 8") 
  tranvertex_master__v1_neighs.writeAction(f"jmp __if_v1_neighs_62_post") 
  ## lmbuff[NUM_INT] = num_int;

  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_61_false: bneiu X18 0 __if_v1_neighs_71_post") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_69_true: movir X27 -1") 
  tranvertex_master__v1_neighs.writeAction(f"sri X27 X27 1") 
  tranvertex_master__v1_neighs.writeAction(f"sendr_wcont X17 X27 X24 X24") 
  tranvertex_master__v1_neighs.writeAction(f"yield_terminate") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_71_post: yield") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_62_post: bleu X21 X26 __if_v1_neighs_73_false") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_72_true: addi X14 X27 0") 
  tranvertex_master__v1_neighs.writeAction(f"ble X16 X27 __if_v1_neighs_76_false") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_75_true: addi X24 X24 1") 
  ## next_nwid = hash(v1, hash(v2, HASH_SEED))

  tranvertex_master__v1_neighs.writeAction(f"movir X28 0") 
  tranvertex_master__v1_neighs.writeAction(f"hash X27 X28") 
  tranvertex_master__v1_neighs.writeAction(f"hash X16 X28") 
  tranvertex_master__v1_neighs.writeAction(f"and X28 X25 X28") 
  ## next_nwid = next_nwid % total_lanes

  tranvertex_master__v1_neighs.writeAction(f"movir X29 0") 
  tranvertex_master__v1_neighs.writeAction(f"evlb X29 intersection_launcher__send_to_worker_thread5") 
  tranvertex_master__v1_neighs.writeAction(f"evi X29 X29 255 4") 
  tranvertex_master__v1_neighs.writeAction(f"ev X29 X29 X28 X28 8") 
  tranvertex_master__v1_neighs.writeAction(f"movrl X27 8(X23) 0 8") 
  tranvertex_master__v1_neighs.writeAction(f"movrl X27 16(X23) 0 8") 
  tranvertex_master__v1_neighs.writeAction(f"movrl X26 32(X23) 0 8") 
  tranvertex_master__v1_neighs.writeAction(f"movir X28 -1") 
  tranvertex_master__v1_neighs.writeAction(f"sri X28 X28 1") 
  tranvertex_master__v1_neighs.writeAction(f"send_wcont X29 X28 X23 5") 
  tranvertex_master__v1_neighs.writeAction(f"jmp __if_v1_neighs_77_post") 
  ## lmbuff[NUM_INT] = num_int;

  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_76_false: bneiu X18 0 __if_v1_neighs_80_post") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_78_true: movir X29 -1") 
  tranvertex_master__v1_neighs.writeAction(f"sri X29 X29 1") 
  tranvertex_master__v1_neighs.writeAction(f"sendr_wcont X17 X29 X24 X24") 
  tranvertex_master__v1_neighs.writeAction(f"yield_terminate") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_80_post: yield") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_77_post: addi X26 X26 8") 
  tranvertex_master__v1_neighs.writeAction(f"jmp __if_v1_neighs_74_post") 
  ## lmbuff[NUM_INT] = num_int;

  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_73_false: bneiu X18 0 __if_v1_neighs_83_post") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_81_true: movir X27 -1") 
  tranvertex_master__v1_neighs.writeAction(f"sri X27 X27 1") 
  tranvertex_master__v1_neighs.writeAction(f"sendr_wcont X17 X27 X24 X24") 
  tranvertex_master__v1_neighs.writeAction(f"yield_terminate") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_83_post: yield") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_74_post: bleu X21 X26 __if_v1_neighs_85_false") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_84_true: addi X15 X27 0") 
  tranvertex_master__v1_neighs.writeAction(f"ble X16 X27 __if_v1_neighs_88_false") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_87_true: addi X24 X24 1") 
  ## next_nwid = hash(v1, hash(v2, HASH_SEED))

  tranvertex_master__v1_neighs.writeAction(f"movir X29 0") 
  tranvertex_master__v1_neighs.writeAction(f"hash X27 X29") 
  tranvertex_master__v1_neighs.writeAction(f"hash X16 X29") 
  tranvertex_master__v1_neighs.writeAction(f"and X29 X25 X29") 
  ## next_nwid = next_nwid % total_lanes

  tranvertex_master__v1_neighs.writeAction(f"movir X28 0") 
  tranvertex_master__v1_neighs.writeAction(f"evlb X28 intersection_launcher__send_to_worker_thread5") 
  tranvertex_master__v1_neighs.writeAction(f"evi X28 X28 255 4") 
  tranvertex_master__v1_neighs.writeAction(f"ev X28 X28 X29 X29 8") 
  tranvertex_master__v1_neighs.writeAction(f"movrl X27 8(X23) 0 8") 
  tranvertex_master__v1_neighs.writeAction(f"movrl X27 16(X23) 0 8") 
  tranvertex_master__v1_neighs.writeAction(f"movrl X26 32(X23) 0 8") 
  tranvertex_master__v1_neighs.writeAction(f"movir X29 -1") 
  tranvertex_master__v1_neighs.writeAction(f"sri X29 X29 1") 
  tranvertex_master__v1_neighs.writeAction(f"send_wcont X28 X29 X23 5") 
  tranvertex_master__v1_neighs.writeAction(f"jmp __if_v1_neighs_89_post") 
  ## lmbuff[NUM_INT] = num_int;

  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_88_false: bneiu X18 0 __if_v1_neighs_92_post") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_90_true: movir X28 -1") 
  tranvertex_master__v1_neighs.writeAction(f"sri X28 X28 1") 
  tranvertex_master__v1_neighs.writeAction(f"sendr_wcont X17 X28 X24 X24") 
  tranvertex_master__v1_neighs.writeAction(f"yield_terminate") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_92_post: yield") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_89_post: addi X26 X26 8") 
  tranvertex_master__v1_neighs.writeAction(f"jmp __if_v1_neighs_86_post") 
  ## lmbuff[NUM_INT] = num_int;

  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_85_false: bneiu X18 0 __if_v1_neighs_95_post") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_93_true: movir X27 -1") 
  tranvertex_master__v1_neighs.writeAction(f"sri X27 X27 1") 
  tranvertex_master__v1_neighs.writeAction(f"sendr_wcont X17 X27 X24 X24") 
  tranvertex_master__v1_neighs.writeAction(f"yield_terminate") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_95_post: yield") 
  ## lmbuff[NUM_INT] = num_int;

  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_86_post: bneiu X18 0 __if_v1_neighs_98_post") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_96_true: movir X25 -1") 
  tranvertex_master__v1_neighs.writeAction(f"sri X25 X25 1") 
  tranvertex_master__v1_neighs.writeAction(f"sendr_wcont X17 X25 X24 X24") 
  tranvertex_master__v1_neighs.writeAction(f"yield_terminate") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_98_post: yield") 
  