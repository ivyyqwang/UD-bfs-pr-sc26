from linker.EFAProgram import efaProgram

## UDWeave version: 0fe75f3 (2026-04-17)

## Global constants

@efaProgram
def EFA_vertex_master(efa):
  efa.code_level = 'machine'
  state0 = efa.State("udweave_init") #Only one state code 
  efa.add_initId(state0.state_id)
  ## Static declarations
  ## Scoped Variable "g_v" uses Register X16, scope (0)
  ## Scoped Variable "vid" uses Register X17, scope (0)
  ## Scoped Variable "parent" uses Register X18, scope (0)
  ## Scoped Variable "itera" uses Register X19, scope (0)
  ## Scoped Variable "cont" uses Register X20, scope (0)
  ## Scoped Variable "num_lanes_total" uses Register X21, scope (0)
  ## Scoped Variable "count" uses Register X22, scope (0)
  ## Scoped Variable "hash_id" uses Register X23, scope (0)
  ## Scoped Variable "return_value" uses Register X24, scope (0)
  ## Scoped Variable "deg" uses Register X25, scope (0)
  ## Scoped Variable "neigh_ptr" uses Register X26, scope (0)
  ## This is all metadata information
  ## #define DEBUG
  ## This is all metadata information
  ## Total threads used in BFS
  ## #define NUM_THREADS 245
  ## #define NUM_LANES_PER_MASTER 2048
  ## Each threads in the same lane shared the following scratchpad
  ## send buffer 1 - 17 (16 words)
  ## #define DEBUG
  ## #define LANEID 2023
  
  ###################################################
  ###### Writing code for thread vertex_master ######
  ###################################################
  # Writing code for event vertex_master::launch
  tranvertex_master__launch = efa.writeEvent('vertex_master::launch')
  tranvertex_master__launch.writeAction(f"__entry: addi X7 X27 16384") 
  tranvertex_master__launch.writeAction(f"addi X1 X20 0") 
  tranvertex_master__launch.writeAction(f"bnei X13 1 __if_launch_1_false") 
  tranvertex_master__launch.writeAction(f"__if_launch_0_true: movir X24 2") 
  tranvertex_master__launch.writeAction(f"jmp __if_launch_2_post") 
  tranvertex_master__launch.writeAction(f"__if_launch_1_false: movir X24 0") 
  tranvertex_master__launch.writeAction(f"__if_launch_2_post: movir X23 0") 
  tranvertex_master__launch.writeAction(f"hash X9 X23") 
  tranvertex_master__launch.writeAction(f"div X23 X11 X23") 
  tranvertex_master__launch.writeAction(f"andi X23 X23 2047") 
  tranvertex_master__launch.writeAction(f"sli X23 X23 1") 
  tranvertex_master__launch.writeAction(f"movwlr X27(X23,0,0) X17") 
  tranvertex_master__launch.writeAction(f"addi X23 X28 1") 
  tranvertex_master__launch.writeAction(f"movwlr X27(X28,0,0) X19") 
  tranvertex_master__launch.writeAction(f"movir X28 -1") 
  tranvertex_master__launch.writeAction(f"ceq X17 X9 X29") 
  tranvertex_master__launch.writeAction(f"ceq X19 X28 X30") 
  tranvertex_master__launch.writeAction(f"xori X30 X30 1") 
  tranvertex_master__launch.writeAction(f"and X29 X30 X29") 
  tranvertex_master__launch.writeAction(f"beqi X29 0 __if_launch_5_post") 
  ## cache hit

  tranvertex_master__launch.writeAction(f"__if_launch_3_true: subi X28 X29 1") 
  tranvertex_master__launch.writeAction(f"beq X19 X29 __if_launch_5_post") 
  tranvertex_master__launch.writeAction(f"__if_launch_6_true: movir X29 -1") 
  tranvertex_master__launch.writeAction(f"sri X29 X29 1") 
  tranvertex_master__launch.writeAction(f"sendr_wcont X20 X29 X24 X17") 
  tranvertex_master__launch.writeAction(f"yield_terminate") 
  tranvertex_master__launch.writeAction(f"__if_launch_5_post: sli X9 X28 6") 
  tranvertex_master__launch.writeAction(f"add X8 X28 X28") 
  tranvertex_master__launch.writeAction(f"send_dmlm_ld_wret X28 vertex_master::v_return 8 X29") 
  tranvertex_master__launch.writeAction(f"addi X9 X17 0") 
  tranvertex_master__launch.writeAction(f"addi X12 X19 0") 
  tranvertex_master__launch.writeAction(f"movwrl X17 X27(X23,0,0)") 
  tranvertex_master__launch.writeAction(f"addi X23 X28 1") 
  tranvertex_master__launch.writeAction(f"movwrl X19 X27(X28,0,0)") 
  tranvertex_master__launch.writeAction(f"addi X8 X16 0") 
  tranvertex_master__launch.writeAction(f"addi X10 X18 0") 
  tranvertex_master__launch.writeAction(f"subi X11 X21 1") 
  tranvertex_master__launch.writeAction(f"yield") 
  
  # Writing code for event vertex_master::v_return
  tranvertex_master__v_return = efa.writeEvent('vertex_master::v_return')
  tranvertex_master__v_return.writeAction(f"__entry: addi X7 X27 16384") 
  ## if(vid != _vid){

  ##     print("error, vertex %lu %lu different", vid, _vid);

  ## }

  tranvertex_master__v_return.writeAction(f"beqi X15 -1 __if_v_return_2_post") 
  tranvertex_master__v_return.writeAction(f"__if_v_return_0_true: ble X15 X19 __if_v_return_5_post") 
  tranvertex_master__v_return.writeAction(f"__if_v_return_3_true: print 'Error vid = %lu (%lu), previous itera %lu > current itera %lu' X9 X11 X15 X19") 
  tranvertex_master__v_return.writeAction(f"__if_v_return_5_post: movwrl X17 X27(X23,0,0)") 
  tranvertex_master__v_return.writeAction(f"addi X23 X28 1") 
  tranvertex_master__v_return.writeAction(f"movwrl X15 X27(X28,0,0)") 
  tranvertex_master__v_return.writeAction(f"movir X28 -1") 
  tranvertex_master__v_return.writeAction(f"sri X28 X28 1") 
  tranvertex_master__v_return.writeAction(f"sendr_wcont X20 X28 X24 X17") 
  tranvertex_master__v_return.writeAction(f"yield_terminate") 
  tranvertex_master__v_return.writeAction(f"__if_v_return_2_post: movir X22 0") 
  tranvertex_master__v_return.writeAction(f"bnei X24 2 __if_v_return_8_post") 
  tranvertex_master__v_return.writeAction(f"__if_v_return_6_true: sli X17 X27 6") 
  tranvertex_master__v_return.writeAction(f"add X16 X27 X27") 
  tranvertex_master__v_return.writeAction(f"addi X27 X27 48") 
  tranvertex_master__v_return.writeAction(f"sendr2_dmlm_wret X27 vertex_master::v_neighs_return X18 X19 X28") 
  tranvertex_master__v_return.writeAction(f"addi X22 X22 1") 
  ## lmbuff[hash_id] = vid;

  ## lmbuff[hash_id+1] = itera;

  tranvertex_master__v_return.writeAction(f"addi X11 X17 0") 
  tranvertex_master__v_return.writeAction(f"addi X10 X27 0") 
  tranvertex_master__v_return.writeAction(f"sli X8 X28 3") 
  tranvertex_master__v_return.writeAction(f"add X10 X28 X28") 
  tranvertex_master__v_return.writeAction(f"__while_v_return_9_condition: bleu X28 X27 __while_v_return_11_post") 
  tranvertex_master__v_return.writeAction(f"__while_v_return_10_body: send_dmlm_ld_wret X27 vertex_master::v_neighs 8 X29") 
  tranvertex_master__v_return.writeAction(f"addi X27 X27 64") 
  tranvertex_master__v_return.writeAction(f"addi X22 X22 8") 
  tranvertex_master__v_return.writeAction(f"jmp __while_v_return_9_condition") 
  tranvertex_master__v_return.writeAction(f"__while_v_return_11_post: yield") 
  tranvertex_master__v_return.writeAction(f"__if_v_return_8_post: beq X11 X9 __if_v_return_14_post") 
  ## split vertex

  tranvertex_master__v_return.writeAction(f"__if_v_return_12_true: addi X8 X25 0") 
  tranvertex_master__v_return.writeAction(f"addi X10 X26 0") 
  tranvertex_master__v_return.writeAction(f"sli X11 X28 6") 
  tranvertex_master__v_return.writeAction(f"add X16 X28 X28") 
  tranvertex_master__v_return.writeAction(f"send_dmlm_ld_wret X28 vertex_master::v_orig_return 8 X27") 
  tranvertex_master__v_return.writeAction(f"yield") 
  tranvertex_master__v_return.writeAction(f"__if_v_return_14_post: bnei X13 0 __if_v_return_17_post") 
  tranvertex_master__v_return.writeAction(f"__if_v_return_15_true: sli X17 X28 6") 
  tranvertex_master__v_return.writeAction(f"add X16 X28 X28") 
  tranvertex_master__v_return.writeAction(f"addi X28 X28 48") 
  tranvertex_master__v_return.writeAction(f"sendr2_dmlm_wret X28 vertex_master::v_neighs_return X18 X19 X27") 
  tranvertex_master__v_return.writeAction(f"addi X22 X22 1") 
  tranvertex_master__v_return.writeAction(f"movir X24 1") 
  ## lmbuff[hash_id] = vid;

  ## lmbuff[hash_id+1] = itera;

  tranvertex_master__v_return.writeAction(f"addi X10 X28 0") 
  tranvertex_master__v_return.writeAction(f"sli X8 X27 3") 
  tranvertex_master__v_return.writeAction(f"add X10 X27 X27") 
  tranvertex_master__v_return.writeAction(f"__while_v_return_18_condition: bleu X27 X28 __while_v_return_20_post") 
  tranvertex_master__v_return.writeAction(f"__while_v_return_19_body: send_dmlm_ld_wret X28 vertex_master::v_neighs 8 X29") 
  tranvertex_master__v_return.writeAction(f"addi X28 X28 64") 
  tranvertex_master__v_return.writeAction(f"addi X22 X22 8") 
  tranvertex_master__v_return.writeAction(f"jmp __while_v_return_18_condition") 
  tranvertex_master__v_return.writeAction(f"__while_v_return_20_post: yield") 
  tranvertex_master__v_return.writeAction(f"__if_v_return_17_post: addi X12 X28 0") 
  tranvertex_master__v_return.writeAction(f"addi X13 X27 0") 
  tranvertex_master__v_return.writeAction(f"__while_v_return_21_condition: ble X27 X28 __while_v_return_23_post") 
  tranvertex_master__v_return.writeAction(f"__while_v_return_22_body: beq X17 X28 __if_v_return_26_post") 
  tranvertex_master__v_return.writeAction(f"__if_v_return_24_true: movir X23 0") 
  tranvertex_master__v_return.writeAction(f"hash X28 X23") 
  ## hash_id = hash_id / CACHE_ENTRIES_NUM;

  tranvertex_master__v_return.writeAction(f"and X23 X21 X23") 
  tranvertex_master__v_return.writeAction(f"movir X29 0") 
  tranvertex_master__v_return.writeAction(f"evlb X29 map_master__add_split_vertex") 
  tranvertex_master__v_return.writeAction(f"evi X29 X29 255 4") 
  tranvertex_master__v_return.writeAction(f"ev X29 X29 X23 X23 8") 
  tranvertex_master__v_return.writeAction(f"sendr_wret X29 vertex_master::v_neighs_return X28 X18 X30") 
  tranvertex_master__v_return.writeAction(f"addi X22 X22 1") 
  ## print("count = %lu", count);

  tranvertex_master__v_return.writeAction(f"__if_v_return_26_post: addi X28 X28 1") 
  tranvertex_master__v_return.writeAction(f"jmp __while_v_return_21_condition") 
  tranvertex_master__v_return.writeAction(f"__while_v_return_23_post: sli X17 X28 6") 
  tranvertex_master__v_return.writeAction(f"add X16 X28 X28") 
  tranvertex_master__v_return.writeAction(f"addi X28 X28 48") 
  tranvertex_master__v_return.writeAction(f"sendr2_dmlm_wret X28 vertex_master::v_neighs_return X18 X19 X29") 
  tranvertex_master__v_return.writeAction(f"addi X22 X22 1") 
  ## lmbuff[hash_id] = vid;

  ## lmbuff[hash_id+1] = itera;

  tranvertex_master__v_return.writeAction(f"addi X11 X17 0") 
  tranvertex_master__v_return.writeAction(f"addi X10 X28 0") 
  tranvertex_master__v_return.writeAction(f"sli X8 X29 3") 
  tranvertex_master__v_return.writeAction(f"add X10 X29 X27") 
  tranvertex_master__v_return.writeAction(f"__while_v_return_27_condition: bleu X27 X28 __while_v_return_29_post") 
  tranvertex_master__v_return.writeAction(f"__while_v_return_28_body: send_dmlm_ld_wret X28 vertex_master::v_neighs 8 X29") 
  tranvertex_master__v_return.writeAction(f"addi X28 X28 64") 
  tranvertex_master__v_return.writeAction(f"addi X22 X22 8") 
  tranvertex_master__v_return.writeAction(f"jmp __while_v_return_27_condition") 
  tranvertex_master__v_return.writeAction(f"__while_v_return_29_post: yield") 
  
  ## check if this is zero degree or split == -1 vertex
  # Writing code for event vertex_master::v_orig_return
  tranvertex_master__v_orig_return = efa.writeEvent('vertex_master::v_orig_return')
  tranvertex_master__v_orig_return.writeAction(f"__entry: beqi X15 -1 __if_v_orig_return_2_post") 
  tranvertex_master__v_orig_return.writeAction(f"__if_v_orig_return_0_true: addi X7 X27 16384") 
  tranvertex_master__v_orig_return.writeAction(f"movwrl X17 X27(X23,0,0)") 
  tranvertex_master__v_orig_return.writeAction(f"addi X23 X28 1") 
  tranvertex_master__v_orig_return.writeAction(f"movwrl X15 X27(X28,0,0)") 
  tranvertex_master__v_orig_return.writeAction(f"sli X17 X27 6") 
  tranvertex_master__v_orig_return.writeAction(f"add X16 X27 X27") 
  tranvertex_master__v_orig_return.writeAction(f"addi X27 X27 48") 
  tranvertex_master__v_orig_return.writeAction(f"sendr2_dmlm_wret X27 vertex_master::v_neighs_return X18 X15 X28") 
  tranvertex_master__v_orig_return.writeAction(f"addi X22 X22 1") 
  tranvertex_master__v_orig_return.writeAction(f"movir X24 1") 
  tranvertex_master__v_orig_return.writeAction(f"addi X11 X17 0") 
  tranvertex_master__v_orig_return.writeAction(f"addi X26 X27 0") 
  tranvertex_master__v_orig_return.writeAction(f"sli X25 X28 3") 
  tranvertex_master__v_orig_return.writeAction(f"add X27 X28 X28") 
  tranvertex_master__v_orig_return.writeAction(f"__while_v_orig_return_3_condition: bleu X28 X27 __while_v_orig_return_5_post") 
  tranvertex_master__v_orig_return.writeAction(f"__while_v_orig_return_4_body: send_dmlm_ld_wret X27 vertex_master::v_neighs 8 X29") 
  tranvertex_master__v_orig_return.writeAction(f"addi X27 X27 64") 
  tranvertex_master__v_orig_return.writeAction(f"addi X22 X22 8") 
  tranvertex_master__v_orig_return.writeAction(f"jmp __while_v_orig_return_3_condition") 
  tranvertex_master__v_orig_return.writeAction(f"__while_v_orig_return_5_post: yield") 
  ## lmbuff[hash_id] = vid;

  ## lmbuff[hash_id+1] = -1;

  tranvertex_master__v_orig_return.writeAction(f"__if_v_orig_return_2_post: sli X11 X28 6") 
  tranvertex_master__v_orig_return.writeAction(f"add X16 X28 X28") 
  tranvertex_master__v_orig_return.writeAction(f"addi X28 X28 48") 
  tranvertex_master__v_orig_return.writeAction(f"sendr2_dmlm_wret X28 vertex_master::v_neighs_return X18 X19 X27") 
  tranvertex_master__v_orig_return.writeAction(f"addi X22 X22 1") 
  tranvertex_master__v_orig_return.writeAction(f"addi X12 X27 0") 
  tranvertex_master__v_orig_return.writeAction(f"addi X13 X29 0") 
  tranvertex_master__v_orig_return.writeAction(f"__while_v_orig_return_6_condition: ble X29 X27 __while_v_orig_return_8_post") 
  tranvertex_master__v_orig_return.writeAction(f"__while_v_orig_return_7_body: beq X17 X27 __if_v_orig_return_11_post") 
  tranvertex_master__v_orig_return.writeAction(f"__if_v_orig_return_9_true: movir X23 0") 
  tranvertex_master__v_orig_return.writeAction(f"hash X27 X23") 
  ## hash_id = hash_id / CACHE_ENTRIES_NUM;

  tranvertex_master__v_orig_return.writeAction(f"and X23 X21 X23") 
  tranvertex_master__v_orig_return.writeAction(f"movir X30 0") 
  tranvertex_master__v_orig_return.writeAction(f"evlb X30 map_master__add_split_vertex") 
  tranvertex_master__v_orig_return.writeAction(f"evi X30 X30 255 4") 
  tranvertex_master__v_orig_return.writeAction(f"ev X30 X30 X23 X23 8") 
  tranvertex_master__v_orig_return.writeAction(f"sendr_wret X30 vertex_master::v_neighs_return X27 X18 X31") 
  tranvertex_master__v_orig_return.writeAction(f"addi X22 X22 1") 
  ## print("split_vid = %lu", split_vid);

  tranvertex_master__v_orig_return.writeAction(f"__if_v_orig_return_11_post: addi X27 X27 1") 
  tranvertex_master__v_orig_return.writeAction(f"jmp __while_v_orig_return_6_condition") 
  tranvertex_master__v_orig_return.writeAction(f"__while_v_orig_return_8_post: sli X17 X27 6") 
  tranvertex_master__v_orig_return.writeAction(f"add X16 X27 X28") 
  tranvertex_master__v_orig_return.writeAction(f"addi X28 X28 48") 
  tranvertex_master__v_orig_return.writeAction(f"sendr2_dmlm_wret X28 vertex_master::v_neighs_return X18 X19 X27") 
  tranvertex_master__v_orig_return.writeAction(f"addi X22 X22 1") 
  ## lmbuff[hash_id] = vid;

  ## lmbuff[hash_id+1] = itera;

  tranvertex_master__v_orig_return.writeAction(f"addi X11 X17 0") 
  tranvertex_master__v_orig_return.writeAction(f"addi X26 X28 0") 
  tranvertex_master__v_orig_return.writeAction(f"sli X25 X27 3") 
  tranvertex_master__v_orig_return.writeAction(f"add X28 X27 X29") 
  tranvertex_master__v_orig_return.writeAction(f"__while_v_orig_return_12_condition: bleu X29 X28 __while_v_orig_return_14_post") 
  tranvertex_master__v_orig_return.writeAction(f"__while_v_orig_return_13_body: send_dmlm_ld_wret X28 vertex_master::v_neighs 8 X27") 
  tranvertex_master__v_orig_return.writeAction(f"addi X28 X28 64") 
  tranvertex_master__v_orig_return.writeAction(f"addi X22 X22 8") 
  tranvertex_master__v_orig_return.writeAction(f"jmp __while_v_orig_return_12_condition") 
  tranvertex_master__v_orig_return.writeAction(f"__while_v_orig_return_14_post: yield") 
  
  # Writing code for event vertex_master::v_neighs
  tranvertex_master__v_neighs = efa.writeEvent('vertex_master::v_neighs')
  tranvertex_master__v_neighs.writeAction(f"__entry: addi X8 X28 0") 
  tranvertex_master__v_neighs.writeAction(f"movir X29 -1") 
  tranvertex_master__v_neighs.writeAction(f"bne X28 X29 __if_v_neighs_2_post") 
  tranvertex_master__v_neighs.writeAction(f"__if_v_neighs_0_true: subi X22 X22 8") 
  tranvertex_master__v_neighs.writeAction(f"bnei X22 0 __if_v_neighs_4_false") 
  tranvertex_master__v_neighs.writeAction(f"__if_v_neighs_3_true: movir X27 -1") 
  tranvertex_master__v_neighs.writeAction(f"sri X27 X27 1") 
  tranvertex_master__v_neighs.writeAction(f"sendr_wcont X20 X27 X24 X17") 
  tranvertex_master__v_neighs.writeAction(f"yield_terminate") 
  tranvertex_master__v_neighs.writeAction(f"jmp __if_v_neighs_2_post") 
  tranvertex_master__v_neighs.writeAction(f"__if_v_neighs_4_false: yield") 
  tranvertex_master__v_neighs.writeAction(f"__if_v_neighs_2_post: movir X23 0") 
  tranvertex_master__v_neighs.writeAction(f"hash X28 X23") 
  ## hash_id = hash_id / CACHE_ENTRIES_NUM;

  tranvertex_master__v_neighs.writeAction(f"and X23 X21 X23") 
  tranvertex_master__v_neighs.writeAction(f"movir X27 0") 
  tranvertex_master__v_neighs.writeAction(f"evlb X27 map_master__add_vertex") 
  tranvertex_master__v_neighs.writeAction(f"evi X27 X27 255 4") 
  tranvertex_master__v_neighs.writeAction(f"ev X27 X27 X23 X23 8") 
  tranvertex_master__v_neighs.writeAction(f"sendr_wret X27 vertex_master::v_neighs_return X28 X17 X30") 
  tranvertex_master__v_neighs.writeAction(f"addi X9 X28 0") 
  tranvertex_master__v_neighs.writeAction(f"bne X28 X29 __if_v_neighs_8_post") 
  tranvertex_master__v_neighs.writeAction(f"__if_v_neighs_6_true: subi X22 X22 7") 
  tranvertex_master__v_neighs.writeAction(f"bnei X22 0 __if_v_neighs_10_false") 
  tranvertex_master__v_neighs.writeAction(f"__if_v_neighs_9_true: movir X30 -1") 
  tranvertex_master__v_neighs.writeAction(f"sri X30 X30 1") 
  tranvertex_master__v_neighs.writeAction(f"sendr_wcont X20 X30 X24 X17") 
  tranvertex_master__v_neighs.writeAction(f"yield_terminate") 
  tranvertex_master__v_neighs.writeAction(f"jmp __if_v_neighs_8_post") 
  tranvertex_master__v_neighs.writeAction(f"__if_v_neighs_10_false: yield") 
  tranvertex_master__v_neighs.writeAction(f"__if_v_neighs_8_post: movir X23 0") 
  tranvertex_master__v_neighs.writeAction(f"hash X28 X23") 
  ## hash_id = hash_id / CACHE_ENTRIES_NUM;

  tranvertex_master__v_neighs.writeAction(f"and X23 X21 X23") 
  tranvertex_master__v_neighs.writeAction(f"movir X27 0") 
  tranvertex_master__v_neighs.writeAction(f"evlb X27 map_master__add_vertex") 
  tranvertex_master__v_neighs.writeAction(f"evi X27 X27 255 4") 
  tranvertex_master__v_neighs.writeAction(f"ev X27 X27 X23 X23 8") 
  tranvertex_master__v_neighs.writeAction(f"sendr_wret X27 vertex_master::v_neighs_return X28 X17 X30") 
  tranvertex_master__v_neighs.writeAction(f"addi X10 X28 0") 
  tranvertex_master__v_neighs.writeAction(f"bne X28 X29 __if_v_neighs_14_post") 
  tranvertex_master__v_neighs.writeAction(f"__if_v_neighs_12_true: subi X22 X22 6") 
  tranvertex_master__v_neighs.writeAction(f"bnei X22 0 __if_v_neighs_16_false") 
  tranvertex_master__v_neighs.writeAction(f"__if_v_neighs_15_true: movir X30 -1") 
  tranvertex_master__v_neighs.writeAction(f"sri X30 X30 1") 
  tranvertex_master__v_neighs.writeAction(f"sendr_wcont X20 X30 X24 X17") 
  tranvertex_master__v_neighs.writeAction(f"yield_terminate") 
  tranvertex_master__v_neighs.writeAction(f"jmp __if_v_neighs_14_post") 
  tranvertex_master__v_neighs.writeAction(f"__if_v_neighs_16_false: yield") 
  tranvertex_master__v_neighs.writeAction(f"__if_v_neighs_14_post: movir X23 0") 
  tranvertex_master__v_neighs.writeAction(f"hash X28 X23") 
  ## hash_id = hash_id / CACHE_ENTRIES_NUM;

  tranvertex_master__v_neighs.writeAction(f"and X23 X21 X23") 
  tranvertex_master__v_neighs.writeAction(f"movir X27 0") 
  tranvertex_master__v_neighs.writeAction(f"evlb X27 map_master__add_vertex") 
  tranvertex_master__v_neighs.writeAction(f"evi X27 X27 255 4") 
  tranvertex_master__v_neighs.writeAction(f"ev X27 X27 X23 X23 8") 
  tranvertex_master__v_neighs.writeAction(f"sendr_wret X27 vertex_master::v_neighs_return X28 X17 X30") 
  tranvertex_master__v_neighs.writeAction(f"addi X11 X28 0") 
  tranvertex_master__v_neighs.writeAction(f"bne X28 X29 __if_v_neighs_20_post") 
  tranvertex_master__v_neighs.writeAction(f"__if_v_neighs_18_true: subi X22 X22 5") 
  tranvertex_master__v_neighs.writeAction(f"bnei X22 0 __if_v_neighs_22_false") 
  tranvertex_master__v_neighs.writeAction(f"__if_v_neighs_21_true: movir X30 -1") 
  tranvertex_master__v_neighs.writeAction(f"sri X30 X30 1") 
  tranvertex_master__v_neighs.writeAction(f"sendr_wcont X20 X30 X24 X17") 
  tranvertex_master__v_neighs.writeAction(f"yield_terminate") 
  tranvertex_master__v_neighs.writeAction(f"jmp __if_v_neighs_20_post") 
  tranvertex_master__v_neighs.writeAction(f"__if_v_neighs_22_false: yield") 
  tranvertex_master__v_neighs.writeAction(f"__if_v_neighs_20_post: movir X23 0") 
  tranvertex_master__v_neighs.writeAction(f"hash X28 X23") 
  ## hash_id = hash_id / CACHE_ENTRIES_NUM;

  tranvertex_master__v_neighs.writeAction(f"and X23 X21 X23") 
  tranvertex_master__v_neighs.writeAction(f"movir X27 0") 
  tranvertex_master__v_neighs.writeAction(f"evlb X27 map_master__add_vertex") 
  tranvertex_master__v_neighs.writeAction(f"evi X27 X27 255 4") 
  tranvertex_master__v_neighs.writeAction(f"ev X27 X27 X23 X23 8") 
  tranvertex_master__v_neighs.writeAction(f"sendr_wret X27 vertex_master::v_neighs_return X28 X17 X30") 
  tranvertex_master__v_neighs.writeAction(f"addi X12 X28 0") 
  tranvertex_master__v_neighs.writeAction(f"bne X28 X29 __if_v_neighs_26_post") 
  tranvertex_master__v_neighs.writeAction(f"__if_v_neighs_24_true: subi X22 X22 4") 
  tranvertex_master__v_neighs.writeAction(f"bnei X22 0 __if_v_neighs_28_false") 
  tranvertex_master__v_neighs.writeAction(f"__if_v_neighs_27_true: movir X30 -1") 
  tranvertex_master__v_neighs.writeAction(f"sri X30 X30 1") 
  tranvertex_master__v_neighs.writeAction(f"sendr_wcont X20 X30 X24 X17") 
  tranvertex_master__v_neighs.writeAction(f"yield_terminate") 
  tranvertex_master__v_neighs.writeAction(f"jmp __if_v_neighs_26_post") 
  tranvertex_master__v_neighs.writeAction(f"__if_v_neighs_28_false: yield") 
  tranvertex_master__v_neighs.writeAction(f"__if_v_neighs_26_post: movir X23 0") 
  tranvertex_master__v_neighs.writeAction(f"hash X28 X23") 
  ## hash_id = hash_id / CACHE_ENTRIES_NUM;

  tranvertex_master__v_neighs.writeAction(f"and X23 X21 X23") 
  tranvertex_master__v_neighs.writeAction(f"movir X27 0") 
  tranvertex_master__v_neighs.writeAction(f"evlb X27 map_master__add_vertex") 
  tranvertex_master__v_neighs.writeAction(f"evi X27 X27 255 4") 
  tranvertex_master__v_neighs.writeAction(f"ev X27 X27 X23 X23 8") 
  tranvertex_master__v_neighs.writeAction(f"sendr_wret X27 vertex_master::v_neighs_return X28 X17 X30") 
  tranvertex_master__v_neighs.writeAction(f"addi X13 X28 0") 
  tranvertex_master__v_neighs.writeAction(f"bne X28 X29 __if_v_neighs_32_post") 
  tranvertex_master__v_neighs.writeAction(f"__if_v_neighs_30_true: subi X22 X22 3") 
  tranvertex_master__v_neighs.writeAction(f"bnei X22 0 __if_v_neighs_34_false") 
  tranvertex_master__v_neighs.writeAction(f"__if_v_neighs_33_true: movir X30 -1") 
  tranvertex_master__v_neighs.writeAction(f"sri X30 X30 1") 
  tranvertex_master__v_neighs.writeAction(f"sendr_wcont X20 X30 X24 X17") 
  tranvertex_master__v_neighs.writeAction(f"yield_terminate") 
  tranvertex_master__v_neighs.writeAction(f"jmp __if_v_neighs_32_post") 
  tranvertex_master__v_neighs.writeAction(f"__if_v_neighs_34_false: yield") 
  tranvertex_master__v_neighs.writeAction(f"__if_v_neighs_32_post: movir X23 0") 
  tranvertex_master__v_neighs.writeAction(f"hash X28 X23") 
  ## hash_id = hash_id / CACHE_ENTRIES_NUM;

  tranvertex_master__v_neighs.writeAction(f"and X23 X21 X23") 
  tranvertex_master__v_neighs.writeAction(f"movir X27 0") 
  tranvertex_master__v_neighs.writeAction(f"evlb X27 map_master__add_vertex") 
  tranvertex_master__v_neighs.writeAction(f"evi X27 X27 255 4") 
  tranvertex_master__v_neighs.writeAction(f"ev X27 X27 X23 X23 8") 
  tranvertex_master__v_neighs.writeAction(f"sendr_wret X27 vertex_master::v_neighs_return X28 X17 X30") 
  tranvertex_master__v_neighs.writeAction(f"addi X14 X28 0") 
  tranvertex_master__v_neighs.writeAction(f"bne X28 X29 __if_v_neighs_38_post") 
  tranvertex_master__v_neighs.writeAction(f"__if_v_neighs_36_true: subi X22 X22 2") 
  tranvertex_master__v_neighs.writeAction(f"bnei X22 0 __if_v_neighs_40_false") 
  tranvertex_master__v_neighs.writeAction(f"__if_v_neighs_39_true: movir X30 -1") 
  tranvertex_master__v_neighs.writeAction(f"sri X30 X30 1") 
  tranvertex_master__v_neighs.writeAction(f"sendr_wcont X20 X30 X24 X17") 
  tranvertex_master__v_neighs.writeAction(f"yield_terminate") 
  tranvertex_master__v_neighs.writeAction(f"jmp __if_v_neighs_38_post") 
  tranvertex_master__v_neighs.writeAction(f"__if_v_neighs_40_false: yield") 
  tranvertex_master__v_neighs.writeAction(f"__if_v_neighs_38_post: movir X23 0") 
  tranvertex_master__v_neighs.writeAction(f"hash X28 X23") 
  ## hash_id = hash_id / CACHE_ENTRIES_NUM;

  tranvertex_master__v_neighs.writeAction(f"and X23 X21 X23") 
  tranvertex_master__v_neighs.writeAction(f"movir X27 0") 
  tranvertex_master__v_neighs.writeAction(f"evlb X27 map_master__add_vertex") 
  tranvertex_master__v_neighs.writeAction(f"evi X27 X27 255 4") 
  tranvertex_master__v_neighs.writeAction(f"ev X27 X27 X23 X23 8") 
  tranvertex_master__v_neighs.writeAction(f"sendr_wret X27 vertex_master::v_neighs_return X28 X17 X30") 
  tranvertex_master__v_neighs.writeAction(f"addi X15 X28 0") 
  tranvertex_master__v_neighs.writeAction(f"bne X28 X29 __if_v_neighs_44_post") 
  tranvertex_master__v_neighs.writeAction(f"__if_v_neighs_42_true: subi X22 X22 1") 
  tranvertex_master__v_neighs.writeAction(f"bnei X22 0 __if_v_neighs_46_false") 
  tranvertex_master__v_neighs.writeAction(f"__if_v_neighs_45_true: movir X29 -1") 
  tranvertex_master__v_neighs.writeAction(f"sri X29 X29 1") 
  tranvertex_master__v_neighs.writeAction(f"sendr_wcont X20 X29 X24 X17") 
  tranvertex_master__v_neighs.writeAction(f"yield_terminate") 
  tranvertex_master__v_neighs.writeAction(f"jmp __if_v_neighs_44_post") 
  tranvertex_master__v_neighs.writeAction(f"__if_v_neighs_46_false: yield") 
  tranvertex_master__v_neighs.writeAction(f"__if_v_neighs_44_post: movir X23 0") 
  tranvertex_master__v_neighs.writeAction(f"hash X28 X23") 
  ## hash_id = hash_id / CACHE_ENTRIES_NUM;

  tranvertex_master__v_neighs.writeAction(f"and X23 X21 X23") 
  tranvertex_master__v_neighs.writeAction(f"movir X27 0") 
  tranvertex_master__v_neighs.writeAction(f"evlb X27 map_master__add_vertex") 
  tranvertex_master__v_neighs.writeAction(f"evi X27 X27 255 4") 
  tranvertex_master__v_neighs.writeAction(f"ev X27 X27 X23 X23 8") 
  tranvertex_master__v_neighs.writeAction(f"sendr_wret X27 vertex_master::v_neighs_return X28 X17 X29") 
  tranvertex_master__v_neighs.writeAction(f"yield") 
  
  # Writing code for event vertex_master::v_neighs_return
  tranvertex_master__v_neighs_return = efa.writeEvent('vertex_master::v_neighs_return')
  tranvertex_master__v_neighs_return.writeAction(f"__entry: subi X22 X22 1") 
  tranvertex_master__v_neighs_return.writeAction(f"bnei X22 0 __if_v_neighs_return_2_post") 
  tranvertex_master__v_neighs_return.writeAction(f"__if_v_neighs_return_0_true: movir X28 -1") 
  tranvertex_master__v_neighs_return.writeAction(f"sri X28 X28 1") 
  tranvertex_master__v_neighs_return.writeAction(f"sendr_wcont X20 X28 X24 X17") 
  tranvertex_master__v_neighs_return.writeAction(f"yield_terminate") 
  tranvertex_master__v_neighs_return.writeAction(f"__if_v_neighs_return_2_post: yield") 
  