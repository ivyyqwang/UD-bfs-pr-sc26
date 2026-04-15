from linker.EFAProgram import efaProgram

## UDWeave version: 02d7c60 (2026-01-27)

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
  ## Scoped Variable "nl_ptr_end" uses Register X19, scope (0)
  ## Scoped Variable "lmbuff" uses Register X20, scope (0)
  ## Scoped Variable "temp_lmbuff" uses Register X21, scope (0)
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
  
  ###################################################
  ###### Writing code for thread vertex_master ######
  ###################################################
  # Writing code for event vertex_master::launch
  tranvertex_master__launch = efa.writeEvent('vertex_master::launch')
  tranvertex_master__launch.writeAction(f"__entry: addi X9 X16 0") 
  tranvertex_master__launch.writeAction(f"addi X1 X17 0") 
  ## Fetch V1 8 bytes from g_v[v1]

  tranvertex_master__launch.writeAction(f"sli X16 X22 6") 
  tranvertex_master__launch.writeAction(f"add X8 X22 X22") 
  tranvertex_master__launch.writeAction(f"send_dmlm_ld_wret X22 vertex_master::v1_return 5 X23") 
  tranvertex_master__launch.writeAction(f"yield") 
  
  # Writing code for event vertex_master::v1_return
  tranvertex_master__v1_return = efa.writeEvent('vertex_master::v1_return')
  ##deg, id, neigh,

  tranvertex_master__v1_return.writeAction(f"__entry: bgtiu X8 1 __if_v1_return_2_post") 
  ## thread can be returned to master_launcher 

  tranvertex_master__v1_return.writeAction(f"__if_v1_return_0_true: movir X22 -1") 
  tranvertex_master__v1_return.writeAction(f"sri X22 X22 1") 
  tranvertex_master__v1_return.writeAction(f"sendr_wcont X17 X22 X8 X8") 
  tranvertex_master__v1_return.writeAction(f"yield_terminate") 
  tranvertex_master__v1_return.writeAction(f"__if_v1_return_2_post: addi X7 X20 0") 
  tranvertex_master__v1_return.writeAction(f"addi X7 X21 32") 
  tranvertex_master__v1_return.writeAction(f"movir X18 0") 
  tranvertex_master__v1_return.writeAction(f"movrl X16 0(X21) 0 8") 
  tranvertex_master__v1_return.writeAction(f"movrl X0 24(X21) 0 8") 
  ## if(op0 == 1){

  ##     long v2 = _min_vid;

  ##     unsigned long num_int = lmbuff[NUM_INT];

  ##     long num_total_lanes = lmbuff[NUM_LANES_TOTAL];

  ##     if(v1 > v2){

  ##         num_int = num_int + 1;

  ##         // next_nwid = hash(v1, hash(v2, HASH_SEED))

  ##         unsigned int next_nwid = HASH_SEED;

  ##         asm{

  ##             "hash %[src] %[dst]"

  ##         }: [src] "r" (v2), [dst] "r" (next_nwid);

  ##         asm{

  ##             "hash %[src] %[dst]"

  ##         }: [src] "r" (v1), [dst] "r" (next_nwid);

  ##         next_nwid = next_nwid & num_total_lanes;  // next_nwid = next_nwid % total_lanes

  ##         unsigned long evword = evw_new(next_nwid, intersection_launcher__send_to_worker_thread4);

  ##         temp_lmbuff[1] = v2;

  ##         temp_lmbuff[2] = v2;

  ##         send_event(evword, temp_lmbuff, 4, IGNRCONT);

  ##     }

  ##     lmbuff[NUM_INT] = num_int;

  ##     send_event(cont, count, IGNRCONT);

  ##     yield_terminate;

  ## }

  tranvertex_master__v1_return.writeAction(f"bneiu X8 2 __if_v1_return_5_post") 
  tranvertex_master__v1_return.writeAction(f"__if_v1_return_3_true: movlr 144(X20) X22 0 8") 
  tranvertex_master__v1_return.writeAction(f"movlr 152(X20) X23 0 8") 
  tranvertex_master__v1_return.writeAction(f"addi X12 X24 0") 
  tranvertex_master__v1_return.writeAction(f"ble X16 X24 __if_v1_return_8_post") 
  tranvertex_master__v1_return.writeAction(f"__if_v1_return_6_true: addi X22 X22 1") 
  ## next_nwid = hash(v1, hash(v2, HASH_SEED))

  tranvertex_master__v1_return.writeAction(f"movir X25 0") 
  tranvertex_master__v1_return.writeAction(f"hash X24 X25") 
  tranvertex_master__v1_return.writeAction(f"hash X16 X25") 
  tranvertex_master__v1_return.writeAction(f"addi X23 X26 0")  # This is for casting. May be used later on
  tranvertex_master__v1_return.writeAction(f"and X25 X26 X25") 
  ## next_nwid = next_nwid % total_lanes

  tranvertex_master__v1_return.writeAction(f"movir X26 0") 
  tranvertex_master__v1_return.writeAction(f"evlb X26 intersection_launcher__send_to_worker_thread4") 
  tranvertex_master__v1_return.writeAction(f"evi X26 X26 255 4") 
  tranvertex_master__v1_return.writeAction(f"ev X26 X26 X25 X25 8") 
  tranvertex_master__v1_return.writeAction(f"movrl X24 8(X21) 0 8") 
  tranvertex_master__v1_return.writeAction(f"movrl X24 16(X21) 0 8") 
  tranvertex_master__v1_return.writeAction(f"movir X25 -1") 
  tranvertex_master__v1_return.writeAction(f"sri X25 X25 1") 
  tranvertex_master__v1_return.writeAction(f"send_wcont X26 X25 X21 4") 
  tranvertex_master__v1_return.writeAction(f"__if_v1_return_8_post: movrl X22 144(X20) 0 8") 
  tranvertex_master__v1_return.writeAction(f"movir X22 -1") 
  tranvertex_master__v1_return.writeAction(f"sri X22 X22 1") 
  tranvertex_master__v1_return.writeAction(f"sendr_wcont X17 X22 X18 X18") 
  tranvertex_master__v1_return.writeAction(f"yield_terminate") 
  ## Vertex needs to be counted

  tranvertex_master__v1_return.writeAction(f"__if_v1_return_5_post: addi X10 X22 0") 
  tranvertex_master__v1_return.writeAction(f"sli X8 X24 3") 
  tranvertex_master__v1_return.writeAction(f"add X10 X24 X19") 
  tranvertex_master__v1_return.writeAction(f"__while_v1_return_9_condition: bleu X19 X22 __while_v1_return_11_post") 
  tranvertex_master__v1_return.writeAction(f"__while_v1_return_10_body: send_dmlm_ld_wret X22 vertex_master::v1_neighs 8 X24") 
  tranvertex_master__v1_return.writeAction(f"addi X18 X18 1") 
  tranvertex_master__v1_return.writeAction(f"addi X22 X22 64") 
  tranvertex_master__v1_return.writeAction(f"jmp __while_v1_return_9_condition") 
  tranvertex_master__v1_return.writeAction(f"__while_v1_return_11_post: yield") 
  
  # Writing code for event vertex_master::v1_neighs
  tranvertex_master__v1_neighs = efa.writeEvent('vertex_master::v1_neighs')
  ## Update the return count

  tranvertex_master__v1_neighs.writeAction(f"__entry: movlr 144(X20) X22 0 8") 
  tranvertex_master__v1_neighs.writeAction(f"movlr 152(X20) X24 0 8") 
  tranvertex_master__v1_neighs.writeAction(f"addi X3 X23 0") 
  tranvertex_master__v1_neighs.writeAction(f"movrl X16 0(X21) 0 8") 
  tranvertex_master__v1_neighs.writeAction(f"movrl X0 24(X21) 0 8") 
  tranvertex_master__v1_neighs.writeAction(f"bleu X19 X23 __if_v1_neighs_1_false") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_0_true: addi X8 X26 0") 
  tranvertex_master__v1_neighs.writeAction(f"ble X16 X26 __if_v1_neighs_4_false") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_3_true: addi X22 X22 1") 
  ## next_nwid = hash(v1, hash(v2, HASH_SEED))

  tranvertex_master__v1_neighs.writeAction(f"movir X25 0") 
  tranvertex_master__v1_neighs.writeAction(f"hash X26 X25") 
  tranvertex_master__v1_neighs.writeAction(f"hash X16 X25") 
  tranvertex_master__v1_neighs.writeAction(f"addi X24 X27 0")  # This is for casting. May be used later on
  tranvertex_master__v1_neighs.writeAction(f"and X25 X27 X25") 
  ## next_nwid = next_nwid % total_lanes

  tranvertex_master__v1_neighs.writeAction(f"movir X27 0") 
  tranvertex_master__v1_neighs.writeAction(f"evlb X27 intersection_launcher__send_to_worker_thread4") 
  tranvertex_master__v1_neighs.writeAction(f"evi X27 X27 255 4") 
  tranvertex_master__v1_neighs.writeAction(f"ev X27 X27 X25 X25 8") 
  tranvertex_master__v1_neighs.writeAction(f"movrl X26 8(X21) 0 8") 
  tranvertex_master__v1_neighs.writeAction(f"movrl X26 16(X21) 0 8") 
  tranvertex_master__v1_neighs.writeAction(f"movir X25 -1") 
  tranvertex_master__v1_neighs.writeAction(f"sri X25 X25 1") 
  tranvertex_master__v1_neighs.writeAction(f"send_wcont X27 X25 X21 4") 
  ## if(NETID == 47){

  ##     print("send (%lu %lu) to lane %lu", v1, v2, next_nwid);

  ## }

  tranvertex_master__v1_neighs.writeAction(f"jmp __if_v1_neighs_5_post") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_4_false: movrl X22 144(X20) 0 8") 
  tranvertex_master__v1_neighs.writeAction(f"subi X18 X18 1") 
  tranvertex_master__v1_neighs.writeAction(f"bneiu X18 0 __if_v1_neighs_8_post") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_6_true: movir X27 -1") 
  tranvertex_master__v1_neighs.writeAction(f"sri X27 X27 1") 
  tranvertex_master__v1_neighs.writeAction(f"sendr_wcont X17 X27 X18 X18") 
  tranvertex_master__v1_neighs.writeAction(f"yield_terminate") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_8_post: yield") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_5_post: addi X23 X23 8") 
  tranvertex_master__v1_neighs.writeAction(f"jmp __if_v1_neighs_2_post") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_1_false: movrl X22 144(X20) 0 8") 
  tranvertex_master__v1_neighs.writeAction(f"subi X18 X18 1") 
  tranvertex_master__v1_neighs.writeAction(f"bneiu X18 0 __if_v1_neighs_11_post") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_9_true: movir X26 -1") 
  tranvertex_master__v1_neighs.writeAction(f"sri X26 X26 1") 
  tranvertex_master__v1_neighs.writeAction(f"sendr_wcont X17 X26 X18 X18") 
  tranvertex_master__v1_neighs.writeAction(f"yield_terminate") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_11_post: yield") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_2_post: bleu X19 X23 __if_v1_neighs_13_false") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_12_true: addi X9 X26 0") 
  tranvertex_master__v1_neighs.writeAction(f"ble X16 X26 __if_v1_neighs_16_false") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_15_true: addi X22 X22 1") 
  ## next_nwid = hash(v1, hash(v2, HASH_SEED))

  tranvertex_master__v1_neighs.writeAction(f"movir X27 0") 
  tranvertex_master__v1_neighs.writeAction(f"hash X26 X27") 
  tranvertex_master__v1_neighs.writeAction(f"hash X16 X27") 
  tranvertex_master__v1_neighs.writeAction(f"addi X24 X25 0")  # This is for casting. May be used later on
  tranvertex_master__v1_neighs.writeAction(f"and X27 X25 X27") 
  ## next_nwid = next_nwid % total_lanes

  tranvertex_master__v1_neighs.writeAction(f"movir X25 0") 
  tranvertex_master__v1_neighs.writeAction(f"evlb X25 intersection_launcher__send_to_worker_thread4") 
  tranvertex_master__v1_neighs.writeAction(f"evi X25 X25 255 4") 
  tranvertex_master__v1_neighs.writeAction(f"ev X25 X25 X27 X27 8") 
  tranvertex_master__v1_neighs.writeAction(f"movrl X26 8(X21) 0 8") 
  tranvertex_master__v1_neighs.writeAction(f"movrl X26 16(X21) 0 8") 
  tranvertex_master__v1_neighs.writeAction(f"movir X27 -1") 
  tranvertex_master__v1_neighs.writeAction(f"sri X27 X27 1") 
  tranvertex_master__v1_neighs.writeAction(f"send_wcont X25 X27 X21 4") 
  ## if(NETID == 47){

  ##     print("send (%lu %lu) to lane %lu", v1, v2, next_nwid);

  ## }

  tranvertex_master__v1_neighs.writeAction(f"jmp __if_v1_neighs_17_post") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_16_false: movrl X22 144(X20) 0 8") 
  tranvertex_master__v1_neighs.writeAction(f"subi X18 X18 1") 
  tranvertex_master__v1_neighs.writeAction(f"bneiu X18 0 __if_v1_neighs_20_post") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_18_true: movir X25 -1") 
  tranvertex_master__v1_neighs.writeAction(f"sri X25 X25 1") 
  tranvertex_master__v1_neighs.writeAction(f"sendr_wcont X17 X25 X18 X18") 
  tranvertex_master__v1_neighs.writeAction(f"yield_terminate") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_20_post: yield") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_17_post: addi X23 X23 8") 
  tranvertex_master__v1_neighs.writeAction(f"jmp __if_v1_neighs_14_post") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_13_false: movrl X22 144(X20) 0 8") 
  tranvertex_master__v1_neighs.writeAction(f"subi X18 X18 1") 
  tranvertex_master__v1_neighs.writeAction(f"bneiu X18 0 __if_v1_neighs_23_post") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_21_true: movir X26 -1") 
  tranvertex_master__v1_neighs.writeAction(f"sri X26 X26 1") 
  tranvertex_master__v1_neighs.writeAction(f"sendr_wcont X17 X26 X18 X18") 
  tranvertex_master__v1_neighs.writeAction(f"yield_terminate") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_23_post: yield") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_14_post: bleu X19 X23 __if_v1_neighs_25_false") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_24_true: addi X10 X26 0") 
  tranvertex_master__v1_neighs.writeAction(f"ble X16 X26 __if_v1_neighs_28_false") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_27_true: addi X22 X22 1") 
  ## next_nwid = hash(v1, hash(v2, HASH_SEED))

  tranvertex_master__v1_neighs.writeAction(f"movir X25 0") 
  tranvertex_master__v1_neighs.writeAction(f"hash X26 X25") 
  tranvertex_master__v1_neighs.writeAction(f"hash X16 X25") 
  tranvertex_master__v1_neighs.writeAction(f"addi X24 X27 0")  # This is for casting. May be used later on
  tranvertex_master__v1_neighs.writeAction(f"and X25 X27 X25") 
  ## next_nwid = next_nwid % total_lanes

  tranvertex_master__v1_neighs.writeAction(f"movir X27 0") 
  tranvertex_master__v1_neighs.writeAction(f"evlb X27 intersection_launcher__send_to_worker_thread4") 
  tranvertex_master__v1_neighs.writeAction(f"evi X27 X27 255 4") 
  tranvertex_master__v1_neighs.writeAction(f"ev X27 X27 X25 X25 8") 
  tranvertex_master__v1_neighs.writeAction(f"movrl X26 8(X21) 0 8") 
  tranvertex_master__v1_neighs.writeAction(f"movrl X26 16(X21) 0 8") 
  tranvertex_master__v1_neighs.writeAction(f"movir X25 -1") 
  tranvertex_master__v1_neighs.writeAction(f"sri X25 X25 1") 
  tranvertex_master__v1_neighs.writeAction(f"send_wcont X27 X25 X21 4") 
  ## if(NETID == 47){

  ##     print("send (%lu %lu) to lane %lu", v1, v2, next_nwid);

  ## }

  tranvertex_master__v1_neighs.writeAction(f"jmp __if_v1_neighs_29_post") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_28_false: movrl X22 144(X20) 0 8") 
  tranvertex_master__v1_neighs.writeAction(f"subi X18 X18 1") 
  tranvertex_master__v1_neighs.writeAction(f"bneiu X18 0 __if_v1_neighs_32_post") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_30_true: movir X27 -1") 
  tranvertex_master__v1_neighs.writeAction(f"sri X27 X27 1") 
  tranvertex_master__v1_neighs.writeAction(f"sendr_wcont X17 X27 X18 X18") 
  tranvertex_master__v1_neighs.writeAction(f"yield_terminate") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_32_post: yield") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_29_post: addi X23 X23 8") 
  tranvertex_master__v1_neighs.writeAction(f"jmp __if_v1_neighs_26_post") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_25_false: movrl X22 144(X20) 0 8") 
  tranvertex_master__v1_neighs.writeAction(f"subi X18 X18 1") 
  tranvertex_master__v1_neighs.writeAction(f"bneiu X18 0 __if_v1_neighs_35_post") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_33_true: movir X26 -1") 
  tranvertex_master__v1_neighs.writeAction(f"sri X26 X26 1") 
  tranvertex_master__v1_neighs.writeAction(f"sendr_wcont X17 X26 X18 X18") 
  tranvertex_master__v1_neighs.writeAction(f"yield_terminate") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_35_post: yield") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_26_post: bleu X19 X23 __if_v1_neighs_37_false") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_36_true: addi X11 X26 0") 
  tranvertex_master__v1_neighs.writeAction(f"ble X16 X26 __if_v1_neighs_40_false") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_39_true: addi X22 X22 1") 
  ## next_nwid = hash(v1, hash(v2, HASH_SEED))

  tranvertex_master__v1_neighs.writeAction(f"movir X27 0") 
  tranvertex_master__v1_neighs.writeAction(f"hash X26 X27") 
  tranvertex_master__v1_neighs.writeAction(f"hash X16 X27") 
  tranvertex_master__v1_neighs.writeAction(f"addi X24 X25 0")  # This is for casting. May be used later on
  tranvertex_master__v1_neighs.writeAction(f"and X27 X25 X27") 
  ## next_nwid = next_nwid % total_lanes

  tranvertex_master__v1_neighs.writeAction(f"movir X25 0") 
  tranvertex_master__v1_neighs.writeAction(f"evlb X25 intersection_launcher__send_to_worker_thread4") 
  tranvertex_master__v1_neighs.writeAction(f"evi X25 X25 255 4") 
  tranvertex_master__v1_neighs.writeAction(f"ev X25 X25 X27 X27 8") 
  tranvertex_master__v1_neighs.writeAction(f"movrl X26 8(X21) 0 8") 
  tranvertex_master__v1_neighs.writeAction(f"movrl X26 16(X21) 0 8") 
  tranvertex_master__v1_neighs.writeAction(f"movir X27 -1") 
  tranvertex_master__v1_neighs.writeAction(f"sri X27 X27 1") 
  tranvertex_master__v1_neighs.writeAction(f"send_wcont X25 X27 X21 4") 
  ## if(NETID == 47){

  ##     print("send (%lu %lu) to lane %lu", v1, v2, next_nwid);

  ## }

  tranvertex_master__v1_neighs.writeAction(f"jmp __if_v1_neighs_41_post") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_40_false: movrl X22 144(X20) 0 8") 
  tranvertex_master__v1_neighs.writeAction(f"subi X18 X18 1") 
  tranvertex_master__v1_neighs.writeAction(f"bneiu X18 0 __if_v1_neighs_44_post") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_42_true: movir X25 -1") 
  tranvertex_master__v1_neighs.writeAction(f"sri X25 X25 1") 
  tranvertex_master__v1_neighs.writeAction(f"sendr_wcont X17 X25 X18 X18") 
  tranvertex_master__v1_neighs.writeAction(f"yield_terminate") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_44_post: yield") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_41_post: addi X23 X23 8") 
  tranvertex_master__v1_neighs.writeAction(f"jmp __if_v1_neighs_38_post") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_37_false: movrl X22 144(X20) 0 8") 
  tranvertex_master__v1_neighs.writeAction(f"subi X18 X18 1") 
  tranvertex_master__v1_neighs.writeAction(f"bneiu X18 0 __if_v1_neighs_47_post") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_45_true: movir X26 -1") 
  tranvertex_master__v1_neighs.writeAction(f"sri X26 X26 1") 
  tranvertex_master__v1_neighs.writeAction(f"sendr_wcont X17 X26 X18 X18") 
  tranvertex_master__v1_neighs.writeAction(f"yield_terminate") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_47_post: yield") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_38_post: bleu X19 X23 __if_v1_neighs_49_false") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_48_true: addi X12 X26 0") 
  tranvertex_master__v1_neighs.writeAction(f"ble X16 X26 __if_v1_neighs_52_false") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_51_true: addi X22 X22 1") 
  ## next_nwid = hash(v1, hash(v2, HASH_SEED))

  tranvertex_master__v1_neighs.writeAction(f"movir X25 0") 
  tranvertex_master__v1_neighs.writeAction(f"hash X26 X25") 
  tranvertex_master__v1_neighs.writeAction(f"hash X16 X25") 
  tranvertex_master__v1_neighs.writeAction(f"addi X24 X27 0")  # This is for casting. May be used later on
  tranvertex_master__v1_neighs.writeAction(f"and X25 X27 X25") 
  ## next_nwid = next_nwid % total_lanes

  tranvertex_master__v1_neighs.writeAction(f"movir X27 0") 
  tranvertex_master__v1_neighs.writeAction(f"evlb X27 intersection_launcher__send_to_worker_thread4") 
  tranvertex_master__v1_neighs.writeAction(f"evi X27 X27 255 4") 
  tranvertex_master__v1_neighs.writeAction(f"ev X27 X27 X25 X25 8") 
  tranvertex_master__v1_neighs.writeAction(f"movrl X26 8(X21) 0 8") 
  tranvertex_master__v1_neighs.writeAction(f"movrl X26 16(X21) 0 8") 
  tranvertex_master__v1_neighs.writeAction(f"movir X25 -1") 
  tranvertex_master__v1_neighs.writeAction(f"sri X25 X25 1") 
  tranvertex_master__v1_neighs.writeAction(f"send_wcont X27 X25 X21 4") 
  ## if(NETID == 47){

  ##     print("send (%lu %lu) to lane %lu", v1, v2, next_nwid);

  ## }

  tranvertex_master__v1_neighs.writeAction(f"jmp __if_v1_neighs_53_post") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_52_false: movrl X22 144(X20) 0 8") 
  tranvertex_master__v1_neighs.writeAction(f"subi X18 X18 1") 
  tranvertex_master__v1_neighs.writeAction(f"bneiu X18 0 __if_v1_neighs_56_post") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_54_true: movir X27 -1") 
  tranvertex_master__v1_neighs.writeAction(f"sri X27 X27 1") 
  tranvertex_master__v1_neighs.writeAction(f"sendr_wcont X17 X27 X18 X18") 
  tranvertex_master__v1_neighs.writeAction(f"yield_terminate") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_56_post: yield") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_53_post: addi X23 X23 8") 
  tranvertex_master__v1_neighs.writeAction(f"jmp __if_v1_neighs_50_post") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_49_false: movrl X22 144(X20) 0 8") 
  tranvertex_master__v1_neighs.writeAction(f"subi X18 X18 1") 
  tranvertex_master__v1_neighs.writeAction(f"bneiu X18 0 __if_v1_neighs_59_post") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_57_true: movir X26 -1") 
  tranvertex_master__v1_neighs.writeAction(f"sri X26 X26 1") 
  tranvertex_master__v1_neighs.writeAction(f"sendr_wcont X17 X26 X18 X18") 
  tranvertex_master__v1_neighs.writeAction(f"yield_terminate") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_59_post: yield") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_50_post: bleu X19 X23 __if_v1_neighs_61_false") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_60_true: addi X13 X26 0") 
  tranvertex_master__v1_neighs.writeAction(f"ble X16 X26 __if_v1_neighs_64_false") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_63_true: addi X22 X22 1") 
  ## next_nwid = hash(v1, hash(v2, HASH_SEED))

  tranvertex_master__v1_neighs.writeAction(f"movir X27 0") 
  tranvertex_master__v1_neighs.writeAction(f"hash X26 X27") 
  tranvertex_master__v1_neighs.writeAction(f"hash X16 X27") 
  tranvertex_master__v1_neighs.writeAction(f"addi X24 X25 0")  # This is for casting. May be used later on
  tranvertex_master__v1_neighs.writeAction(f"and X27 X25 X27") 
  ## next_nwid = next_nwid % total_lanes

  tranvertex_master__v1_neighs.writeAction(f"movir X25 0") 
  tranvertex_master__v1_neighs.writeAction(f"evlb X25 intersection_launcher__send_to_worker_thread4") 
  tranvertex_master__v1_neighs.writeAction(f"evi X25 X25 255 4") 
  tranvertex_master__v1_neighs.writeAction(f"ev X25 X25 X27 X27 8") 
  tranvertex_master__v1_neighs.writeAction(f"movrl X26 8(X21) 0 8") 
  tranvertex_master__v1_neighs.writeAction(f"movrl X26 16(X21) 0 8") 
  tranvertex_master__v1_neighs.writeAction(f"movir X27 -1") 
  tranvertex_master__v1_neighs.writeAction(f"sri X27 X27 1") 
  tranvertex_master__v1_neighs.writeAction(f"send_wcont X25 X27 X21 4") 
  ## if(NETID == 47){

  ##     print("send (%lu %lu) to lane %lu", v1, v2, next_nwid);

  ## }

  tranvertex_master__v1_neighs.writeAction(f"jmp __if_v1_neighs_65_post") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_64_false: movrl X22 144(X20) 0 8") 
  tranvertex_master__v1_neighs.writeAction(f"subi X18 X18 1") 
  tranvertex_master__v1_neighs.writeAction(f"bneiu X18 0 __if_v1_neighs_68_post") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_66_true: movir X25 -1") 
  tranvertex_master__v1_neighs.writeAction(f"sri X25 X25 1") 
  tranvertex_master__v1_neighs.writeAction(f"sendr_wcont X17 X25 X18 X18") 
  tranvertex_master__v1_neighs.writeAction(f"yield_terminate") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_68_post: yield") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_65_post: addi X23 X23 8") 
  tranvertex_master__v1_neighs.writeAction(f"jmp __if_v1_neighs_62_post") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_61_false: movrl X22 144(X20) 0 8") 
  tranvertex_master__v1_neighs.writeAction(f"subi X18 X18 1") 
  tranvertex_master__v1_neighs.writeAction(f"bneiu X18 0 __if_v1_neighs_71_post") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_69_true: movir X26 -1") 
  tranvertex_master__v1_neighs.writeAction(f"sri X26 X26 1") 
  tranvertex_master__v1_neighs.writeAction(f"sendr_wcont X17 X26 X18 X18") 
  tranvertex_master__v1_neighs.writeAction(f"yield_terminate") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_71_post: yield") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_62_post: bleu X19 X23 __if_v1_neighs_73_false") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_72_true: addi X14 X26 0") 
  tranvertex_master__v1_neighs.writeAction(f"ble X16 X26 __if_v1_neighs_76_false") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_75_true: addi X22 X22 1") 
  ## next_nwid = hash(v1, hash(v2, HASH_SEED))

  tranvertex_master__v1_neighs.writeAction(f"movir X25 0") 
  tranvertex_master__v1_neighs.writeAction(f"hash X26 X25") 
  tranvertex_master__v1_neighs.writeAction(f"hash X16 X25") 
  tranvertex_master__v1_neighs.writeAction(f"addi X24 X27 0")  # This is for casting. May be used later on
  tranvertex_master__v1_neighs.writeAction(f"and X25 X27 X25") 
  ## next_nwid = next_nwid % total_lanes

  tranvertex_master__v1_neighs.writeAction(f"movir X27 0") 
  tranvertex_master__v1_neighs.writeAction(f"evlb X27 intersection_launcher__send_to_worker_thread4") 
  tranvertex_master__v1_neighs.writeAction(f"evi X27 X27 255 4") 
  tranvertex_master__v1_neighs.writeAction(f"ev X27 X27 X25 X25 8") 
  tranvertex_master__v1_neighs.writeAction(f"movrl X26 8(X21) 0 8") 
  tranvertex_master__v1_neighs.writeAction(f"movrl X26 16(X21) 0 8") 
  tranvertex_master__v1_neighs.writeAction(f"movir X25 -1") 
  tranvertex_master__v1_neighs.writeAction(f"sri X25 X25 1") 
  tranvertex_master__v1_neighs.writeAction(f"send_wcont X27 X25 X21 4") 
  ## if(NETID == 47){

  ##     print("send (%lu %lu) to lane %lu", v1, v2, next_nwid);

  ## }

  tranvertex_master__v1_neighs.writeAction(f"jmp __if_v1_neighs_77_post") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_76_false: movrl X22 144(X20) 0 8") 
  tranvertex_master__v1_neighs.writeAction(f"subi X18 X18 1") 
  tranvertex_master__v1_neighs.writeAction(f"bneiu X18 0 __if_v1_neighs_80_post") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_78_true: movir X27 -1") 
  tranvertex_master__v1_neighs.writeAction(f"sri X27 X27 1") 
  tranvertex_master__v1_neighs.writeAction(f"sendr_wcont X17 X27 X18 X18") 
  tranvertex_master__v1_neighs.writeAction(f"yield_terminate") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_80_post: yield") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_77_post: addi X23 X23 8") 
  tranvertex_master__v1_neighs.writeAction(f"jmp __if_v1_neighs_74_post") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_73_false: movrl X22 144(X20) 0 8") 
  tranvertex_master__v1_neighs.writeAction(f"subi X18 X18 1") 
  tranvertex_master__v1_neighs.writeAction(f"bneiu X18 0 __if_v1_neighs_83_post") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_81_true: movir X26 -1") 
  tranvertex_master__v1_neighs.writeAction(f"sri X26 X26 1") 
  tranvertex_master__v1_neighs.writeAction(f"sendr_wcont X17 X26 X18 X18") 
  tranvertex_master__v1_neighs.writeAction(f"yield_terminate") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_83_post: yield") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_74_post: bleu X19 X23 __if_v1_neighs_85_false") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_84_true: addi X15 X26 0") 
  tranvertex_master__v1_neighs.writeAction(f"ble X16 X26 __if_v1_neighs_88_false") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_87_true: addi X22 X22 1") 
  ## next_nwid = hash(v1, hash(v2, HASH_SEED))

  tranvertex_master__v1_neighs.writeAction(f"movir X27 0") 
  tranvertex_master__v1_neighs.writeAction(f"hash X26 X27") 
  tranvertex_master__v1_neighs.writeAction(f"hash X16 X27") 
  tranvertex_master__v1_neighs.writeAction(f"addi X24 X25 0")  # This is for casting. May be used later on
  tranvertex_master__v1_neighs.writeAction(f"and X27 X25 X27") 
  ## next_nwid = next_nwid % total_lanes

  tranvertex_master__v1_neighs.writeAction(f"movir X25 0") 
  tranvertex_master__v1_neighs.writeAction(f"evlb X25 intersection_launcher__send_to_worker_thread4") 
  tranvertex_master__v1_neighs.writeAction(f"evi X25 X25 255 4") 
  tranvertex_master__v1_neighs.writeAction(f"ev X25 X25 X27 X27 8") 
  tranvertex_master__v1_neighs.writeAction(f"movrl X26 8(X21) 0 8") 
  tranvertex_master__v1_neighs.writeAction(f"movrl X26 16(X21) 0 8") 
  tranvertex_master__v1_neighs.writeAction(f"movir X27 -1") 
  tranvertex_master__v1_neighs.writeAction(f"sri X27 X27 1") 
  tranvertex_master__v1_neighs.writeAction(f"send_wcont X25 X27 X21 4") 
  ## if(NETID == 47){

  ##     print("send (%lu %lu) to lane %lu", v1, v2, next_nwid);

  ## }

  tranvertex_master__v1_neighs.writeAction(f"jmp __if_v1_neighs_89_post") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_88_false: movrl X22 144(X20) 0 8") 
  tranvertex_master__v1_neighs.writeAction(f"subi X18 X18 1") 
  tranvertex_master__v1_neighs.writeAction(f"bneiu X18 0 __if_v1_neighs_92_post") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_90_true: movir X25 -1") 
  tranvertex_master__v1_neighs.writeAction(f"sri X25 X25 1") 
  tranvertex_master__v1_neighs.writeAction(f"sendr_wcont X17 X25 X18 X18") 
  tranvertex_master__v1_neighs.writeAction(f"yield_terminate") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_92_post: yield") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_89_post: addi X23 X23 8") 
  tranvertex_master__v1_neighs.writeAction(f"jmp __if_v1_neighs_86_post") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_85_false: movrl X22 144(X20) 0 8") 
  tranvertex_master__v1_neighs.writeAction(f"subi X18 X18 1") 
  tranvertex_master__v1_neighs.writeAction(f"bneiu X18 0 __if_v1_neighs_95_post") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_93_true: movir X26 -1") 
  tranvertex_master__v1_neighs.writeAction(f"sri X26 X26 1") 
  tranvertex_master__v1_neighs.writeAction(f"sendr_wcont X17 X26 X18 X18") 
  tranvertex_master__v1_neighs.writeAction(f"yield_terminate") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_95_post: yield") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_86_post: movrl X22 144(X20) 0 8") 
  tranvertex_master__v1_neighs.writeAction(f"subi X18 X18 1") 
  tranvertex_master__v1_neighs.writeAction(f"bneiu X18 0 __if_v1_neighs_98_post") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_96_true: movir X22 -1") 
  tranvertex_master__v1_neighs.writeAction(f"sri X22 X22 1") 
  tranvertex_master__v1_neighs.writeAction(f"sendr_wcont X17 X22 X18 X18") 
  tranvertex_master__v1_neighs.writeAction(f"yield_terminate") 
  tranvertex_master__v1_neighs.writeAction(f"__if_v1_neighs_98_post: yield") 
  