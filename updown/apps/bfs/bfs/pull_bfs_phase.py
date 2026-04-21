from linker.EFAProgram import efaProgram

## UDWeave version: 6f85520 (2025-11-06)

## Global constants

@efaProgram
def EFA_BfsPullPhase(efa):
  efa.code_level = 'machine'
  state0 = efa.State("udweave_init") #Only one state code 
  efa.add_initId(state0.state_id)
  ## Static declarations
  ## Scoped Variable "graph" uses Register X16, scope (0)
  ## Scoped Variable "nlist_ptr" uses Register X17, scope (0)
  ## Scoped Variable "sibling_vid" uses Register X18, scope (0)
  ## Scoped Variable "num_siblings" uses Register X19, scope (0)
  ## Scoped Variable "vid" uses Register X20, scope (0)
  ## Scoped Variable "orig_vid" uses Register X21, scope (0)
  ## Scoped Variable "parent" uses Register X22, scope (0)
  ## Scoped Variable "nlist_bound" uses Register X23, scope (0)
  ## Scoped Variable "num_pending" uses Register X24, scope (0)
  ## Scoped Variable "iteration" uses Register X25, scope (0)
  
  ##############################################
  ###### Writing code for thread BFS_pull ######
  ##############################################
  ## long* orig_graph;
  ## Vertex structure 
  ## Operands:
  ##     X8  degree;
  ##     X9  orig_vid;
  ##     X10 vid;
  ##     X11 *neighbors;
  ##     X12 distance;
  ##     X13 parent;
  ##     X14 split_range;
  ##     X15 padding;
  # Writing code for event BFS_pull::kv_map
  tranBFS_pull__kv_map = efa.writeEvent('BFS_pull::kv_map')
  tranBFS_pull__kv_map.writeAction(f"__entry: addi X7 X26 256") 
  tranBFS_pull__kv_map.writeAction(f"movlr 0(X26) X25 0 8") 
  ## The vertex is visited, skip it

  tranBFS_pull__kv_map.writeAction(f"clti X12 X27 0") 
  tranBFS_pull__kv_map.writeAction(f"xori X27 X27 1") 
  tranBFS_pull__kv_map.writeAction(f"cgt X12 X25 X28") 
  tranBFS_pull__kv_map.writeAction(f"xori X28 X28 1") 
  tranBFS_pull__kv_map.writeAction(f"and X27 X28 X27") 
  tranBFS_pull__kv_map.writeAction(f"beqi X27 0 __if_kv_map_5_post") 
  tranBFS_pull__kv_map.writeAction(f"__if_kv_map_3_true: evi X2 X27 BFS_pull::kv_map_return 1") 
  tranBFS_pull__kv_map.writeAction(f"sendr_wcont X27 X2 X10 X10") 
  tranBFS_pull__kv_map.writeAction(f"yield") 
  ## The vertex has degree 0, skip it

  tranBFS_pull__kv_map.writeAction(f"__if_kv_map_5_post: bnei X8 0 __if_kv_map_11_post") 
  tranBFS_pull__kv_map.writeAction(f"__if_kv_map_9_true: evi X2 X27 BFS_pull::kv_map_return 1") 
  tranBFS_pull__kv_map.writeAction(f"sendr_wcont X27 X2 X10 X10") 
  tranBFS_pull__kv_map.writeAction(f"yield") 
  tranBFS_pull__kv_map.writeAction(f"__if_kv_map_11_post: sli X8 X27 3") 
  tranBFS_pull__kv_map.writeAction(f"add X11 X27 X23") 
  tranBFS_pull__kv_map.writeAction(f"addi X11 X17 0") 
  tranBFS_pull__kv_map.writeAction(f"addi X10 X20 0") 
  tranBFS_pull__kv_map.writeAction(f"addi X9 X21 0") 
  tranBFS_pull__kv_map.writeAction(f"sari X14 X18 32") 
  tranBFS_pull__kv_map.writeAction(f"movir X27 -1") 
  tranBFS_pull__kv_map.writeAction(f"sri X27 X27 32") 
  tranBFS_pull__kv_map.writeAction(f"and X14 X27 X27") 
  tranBFS_pull__kv_map.writeAction(f"sub X27 X18 X19") 
  tranBFS_pull__kv_map.writeAction(f"movir X24 0") 
  tranBFS_pull__kv_map.writeAction(f"addi X7 X26 0") 
  tranBFS_pull__kv_map.writeAction(f"movlr 0(X26) X16 0 8") 
  tranBFS_pull__kv_map.writeAction(f"evi X2 X27 BFS_pull::rd_nlist_return 1") 
  tranBFS_pull__kv_map.writeAction(f"movir X28 16") 
  tranBFS_pull__kv_map.writeAction(f"__while_kv_map_15_condition: ble X8 X24 __while_kv_map_17_post") 
  tranBFS_pull__kv_map.writeAction(f"__while_kv_map_16_body: send_dmlm_ld X17 X27 8") 
  tranBFS_pull__kv_map.writeAction(f"addi X24 X24 8") 
  tranBFS_pull__kv_map.writeAction(f"addi X17 X17 64") 
  tranBFS_pull__kv_map.writeAction(f"bgt X28 X24 __if_kv_map_20_post") 
  tranBFS_pull__kv_map.writeAction(f"__if_kv_map_18_true: jmp __while_kv_map_17_post") 
  tranBFS_pull__kv_map.writeAction(f"__if_kv_map_20_post: jmp __while_kv_map_15_condition") 
  tranBFS_pull__kv_map.writeAction(f"__while_kv_map_17_post: addi X7 X26 112") 
  tranBFS_pull__kv_map.writeAction(f"movlr 0(X26) X28 0 8") 
  tranBFS_pull__kv_map.writeAction(f"add X28 X24 X28") 
  tranBFS_pull__kv_map.writeAction(f"movrl X28 0(X26) 0 8") 
  tranBFS_pull__kv_map.writeAction(f"movir X22 -1") 
  tranBFS_pull__kv_map.writeAction(f"yield") 
  
  # Writing code for event BFS_pull::rd_nlist_return
  tranBFS_pull__rd_nlist_return = efa.writeEvent('BFS_pull::rd_nlist_return')
  tranBFS_pull__rd_nlist_return.writeAction(f"__entry: blti X22 0 __if_rd_nlist_return_2_post") 
  tranBFS_pull__rd_nlist_return.writeAction(f"__if_rd_nlist_return_0_true: subi X24 X24 8") 
  tranBFS_pull__rd_nlist_return.writeAction(f"bnei X24 0 __if_rd_nlist_return_8_post") 
  ## Finish fetching the neighbors, read the original vertex

  tranBFS_pull__rd_nlist_return.writeAction(f"__if_rd_nlist_return_6_true: addi X7 X26 88") 
  tranBFS_pull__rd_nlist_return.writeAction(f"movlr 0(X26) X26 0 8") 
  tranBFS_pull__rd_nlist_return.writeAction(f"sli X21 X28 6") 
  tranBFS_pull__rd_nlist_return.writeAction(f"add X26 X28 X26") 
  tranBFS_pull__rd_nlist_return.writeAction(f"evi X2 X28 BFS_pull::read_orig_vertex 1") 
  tranBFS_pull__rd_nlist_return.writeAction(f"send_dmlm_ld X26 X28 8") 
  tranBFS_pull__rd_nlist_return.writeAction(f"__if_rd_nlist_return_8_post: yield") 
  tranBFS_pull__rd_nlist_return.writeAction(f"__if_rd_nlist_return_2_post: addi X7 X26 112") 
  tranBFS_pull__rd_nlist_return.writeAction(f"movlr 0(X26) X28 0 8") 
  tranBFS_pull__rd_nlist_return.writeAction(f"bleu X23 X17 __if_rd_nlist_return_14_post") 
  tranBFS_pull__rd_nlist_return.writeAction(f"__if_rd_nlist_return_12_true: send_dmlm_ld X17 X2 8") 
  tranBFS_pull__rd_nlist_return.writeAction(f"addi X24 X24 8") 
  tranBFS_pull__rd_nlist_return.writeAction(f"addi X17 X17 64") 
  tranBFS_pull__rd_nlist_return.writeAction(f"addi X28 X28 8") 
  tranBFS_pull__rd_nlist_return.writeAction(f"__if_rd_nlist_return_14_post: addi X3 X27 0") 
  tranBFS_pull__rd_nlist_return.writeAction(f"evi X2 X29 BFS_pull::read_vertex 1") 
  tranBFS_pull__rd_nlist_return.writeAction(f"bgtu X23 X27 __if_rd_nlist_return_17_post") 
  tranBFS_pull__rd_nlist_return.writeAction(f"__if_rd_nlist_return_15_true: subi X24 X24 8") 
  tranBFS_pull__rd_nlist_return.writeAction(f"subi X28 X28 8") 
  tranBFS_pull__rd_nlist_return.writeAction(f"jmp break_label") 
  tranBFS_pull__rd_nlist_return.writeAction(f"yield") 
  tranBFS_pull__rd_nlist_return.writeAction(f"__if_rd_nlist_return_17_post: sli X8 X30 6") 
  tranBFS_pull__rd_nlist_return.writeAction(f"add X16 X30 X30") 
  tranBFS_pull__rd_nlist_return.writeAction(f"send_dmlm_ld X30 X29 8") 
  tranBFS_pull__rd_nlist_return.writeAction(f"addi X27 X27 8") 
  tranBFS_pull__rd_nlist_return.writeAction(f"bgtu X23 X27 __if_rd_nlist_return_20_post") 
  tranBFS_pull__rd_nlist_return.writeAction(f"__if_rd_nlist_return_18_true: subi X24 X24 7") 
  tranBFS_pull__rd_nlist_return.writeAction(f"subi X28 X28 7") 
  tranBFS_pull__rd_nlist_return.writeAction(f"jmp break_label") 
  tranBFS_pull__rd_nlist_return.writeAction(f"yield") 
  tranBFS_pull__rd_nlist_return.writeAction(f"__if_rd_nlist_return_20_post: sli X9 X31 6") 
  tranBFS_pull__rd_nlist_return.writeAction(f"add X16 X31 X30") 
  tranBFS_pull__rd_nlist_return.writeAction(f"send_dmlm_ld X30 X29 8") 
  tranBFS_pull__rd_nlist_return.writeAction(f"addi X27 X27 8") 
  tranBFS_pull__rd_nlist_return.writeAction(f"bgtu X23 X27 __if_rd_nlist_return_23_post") 
  tranBFS_pull__rd_nlist_return.writeAction(f"__if_rd_nlist_return_21_true: subi X24 X24 6") 
  tranBFS_pull__rd_nlist_return.writeAction(f"subi X28 X28 6") 
  tranBFS_pull__rd_nlist_return.writeAction(f"jmp break_label") 
  tranBFS_pull__rd_nlist_return.writeAction(f"yield") 
  tranBFS_pull__rd_nlist_return.writeAction(f"__if_rd_nlist_return_23_post: sli X10 X31 6") 
  tranBFS_pull__rd_nlist_return.writeAction(f"add X16 X31 X30") 
  tranBFS_pull__rd_nlist_return.writeAction(f"send_dmlm_ld X30 X29 8") 
  tranBFS_pull__rd_nlist_return.writeAction(f"addi X27 X27 8") 
  tranBFS_pull__rd_nlist_return.writeAction(f"bgtu X23 X27 __if_rd_nlist_return_26_post") 
  tranBFS_pull__rd_nlist_return.writeAction(f"__if_rd_nlist_return_24_true: subi X24 X24 5") 
  tranBFS_pull__rd_nlist_return.writeAction(f"subi X28 X28 5") 
  tranBFS_pull__rd_nlist_return.writeAction(f"jmp break_label") 
  tranBFS_pull__rd_nlist_return.writeAction(f"yield") 
  tranBFS_pull__rd_nlist_return.writeAction(f"__if_rd_nlist_return_26_post: sli X11 X31 6") 
  tranBFS_pull__rd_nlist_return.writeAction(f"add X16 X31 X30") 
  tranBFS_pull__rd_nlist_return.writeAction(f"send_dmlm_ld X30 X29 8") 
  tranBFS_pull__rd_nlist_return.writeAction(f"addi X27 X27 8") 
  tranBFS_pull__rd_nlist_return.writeAction(f"bgtu X23 X27 __if_rd_nlist_return_29_post") 
  tranBFS_pull__rd_nlist_return.writeAction(f"__if_rd_nlist_return_27_true: subi X24 X24 4") 
  tranBFS_pull__rd_nlist_return.writeAction(f"subi X28 X28 4") 
  tranBFS_pull__rd_nlist_return.writeAction(f"jmp break_label") 
  tranBFS_pull__rd_nlist_return.writeAction(f"yield") 
  tranBFS_pull__rd_nlist_return.writeAction(f"__if_rd_nlist_return_29_post: sli X12 X31 6") 
  tranBFS_pull__rd_nlist_return.writeAction(f"add X16 X31 X30") 
  tranBFS_pull__rd_nlist_return.writeAction(f"send_dmlm_ld X30 X29 8") 
  tranBFS_pull__rd_nlist_return.writeAction(f"addi X27 X27 8") 
  tranBFS_pull__rd_nlist_return.writeAction(f"bgtu X23 X27 __if_rd_nlist_return_32_post") 
  tranBFS_pull__rd_nlist_return.writeAction(f"__if_rd_nlist_return_30_true: subi X24 X24 3") 
  tranBFS_pull__rd_nlist_return.writeAction(f"subi X28 X28 3") 
  tranBFS_pull__rd_nlist_return.writeAction(f"jmp break_label") 
  tranBFS_pull__rd_nlist_return.writeAction(f"yield") 
  tranBFS_pull__rd_nlist_return.writeAction(f"__if_rd_nlist_return_32_post: sli X13 X31 6") 
  tranBFS_pull__rd_nlist_return.writeAction(f"add X16 X31 X30") 
  tranBFS_pull__rd_nlist_return.writeAction(f"send_dmlm_ld X30 X29 8") 
  tranBFS_pull__rd_nlist_return.writeAction(f"addi X27 X27 8") 
  tranBFS_pull__rd_nlist_return.writeAction(f"bgtu X23 X27 __if_rd_nlist_return_35_post") 
  tranBFS_pull__rd_nlist_return.writeAction(f"__if_rd_nlist_return_33_true: subi X24 X24 2") 
  tranBFS_pull__rd_nlist_return.writeAction(f"subi X28 X28 2") 
  tranBFS_pull__rd_nlist_return.writeAction(f"jmp break_label") 
  tranBFS_pull__rd_nlist_return.writeAction(f"yield") 
  tranBFS_pull__rd_nlist_return.writeAction(f"__if_rd_nlist_return_35_post: sli X14 X31 6") 
  tranBFS_pull__rd_nlist_return.writeAction(f"add X16 X31 X30") 
  tranBFS_pull__rd_nlist_return.writeAction(f"send_dmlm_ld X30 X29 8") 
  tranBFS_pull__rd_nlist_return.writeAction(f"addi X27 X27 8") 
  tranBFS_pull__rd_nlist_return.writeAction(f"bgtu X23 X27 __if_rd_nlist_return_38_post") 
  tranBFS_pull__rd_nlist_return.writeAction(f"__if_rd_nlist_return_36_true: subi X24 X24 1") 
  tranBFS_pull__rd_nlist_return.writeAction(f"subi X28 X28 1") 
  tranBFS_pull__rd_nlist_return.writeAction(f"jmp break_label") 
  tranBFS_pull__rd_nlist_return.writeAction(f"yield") 
  tranBFS_pull__rd_nlist_return.writeAction(f"__if_rd_nlist_return_38_post: sli X15 X27 6") 
  tranBFS_pull__rd_nlist_return.writeAction(f"add X16 X27 X30") 
  tranBFS_pull__rd_nlist_return.writeAction(f"send_dmlm_ld X30 X29 8") 
  tranBFS_pull__rd_nlist_return.writeAction(f"break_label: movrl X28 0(X26) 0 8") 
  tranBFS_pull__rd_nlist_return.writeAction(f"yield") 
  
  # Writing code for event BFS_pull::read_vertex
  tranBFS_pull__read_vertex = efa.writeEvent('BFS_pull::read_vertex')
  tranBFS_pull__read_vertex.writeAction(f"__entry: subi X24 X24 1") 
  tranBFS_pull__read_vertex.writeAction(f"clti X22 X26 0") 
  tranBFS_pull__read_vertex.writeAction(f"subi X25 X28 1") 
  tranBFS_pull__read_vertex.writeAction(f"ceq X12 X28 X28") 
  tranBFS_pull__read_vertex.writeAction(f"and X26 X28 X26") 
  tranBFS_pull__read_vertex.writeAction(f"beqi X26 0 __if_read_vertex_5_post") 
  ## Insert into the frontier

  tranBFS_pull__read_vertex.writeAction(f"__if_read_vertex_3_true: addi X9 X22 0") 
  ## if (DEBUG_FLAG) {

  ##     print("[DEBUG][NWID %d][read_vertex] Find a visited neighbor vid=%ld (orig_vid=%ld) distance=%ld of vertex %ls, update the origianl vid=%ld", NETID, vid_op, orig_vid_op, dist_op, vid, orig_vid);

  ## }

  tranBFS_pull__read_vertex.writeAction(f"__if_read_vertex_5_post: bnei X24 0 __if_read_vertex_8_post") 
  tranBFS_pull__read_vertex.writeAction(f"__if_read_vertex_6_true: blti X22 0 __if_read_vertex_10_false") 
  ## Finish fetching the neighbors, read the original vertex

  tranBFS_pull__read_vertex.writeAction(f"__if_read_vertex_9_true: addi X7 X26 88") 
  tranBFS_pull__read_vertex.writeAction(f"movlr 0(X26) X26 0 8") 
  tranBFS_pull__read_vertex.writeAction(f"sli X21 X28 6") 
  tranBFS_pull__read_vertex.writeAction(f"add X26 X28 X26") 
  tranBFS_pull__read_vertex.writeAction(f"evi X2 X28 BFS_pull::read_orig_vertex 1") 
  tranBFS_pull__read_vertex.writeAction(f"send_dmlm_ld X26 X28 8") 
  tranBFS_pull__read_vertex.writeAction(f"yield") 
  tranBFS_pull__read_vertex.writeAction(f"jmp __if_read_vertex_8_post") 
  tranBFS_pull__read_vertex.writeAction(f"__if_read_vertex_10_false: evi X2 X26 BFS_pull::kv_map_return 1") 
  ## long* local tmp_lm_ptr = LMBASE + KVMSR_META_DATA_OFFSET;

  ## *tmp_lm_ptr = *tmp_lm_ptr - ;

  tranBFS_pull__read_vertex.writeAction(f"sendr_wcont X26 X2 X10 X10") 
  tranBFS_pull__read_vertex.writeAction(f"yield") 
  tranBFS_pull__read_vertex.writeAction(f"__if_read_vertex_8_post: yield") 
  
  # Writing code for event BFS_pull::read_orig_vertex
  tranBFS_pull__read_orig_vertex = efa.writeEvent('BFS_pull::read_orig_vertex')
  tranBFS_pull__read_orig_vertex.writeAction(f"__entry: bne X12 X25 __if_read_orig_vertex_2_post") 
  tranBFS_pull__read_orig_vertex.writeAction(f"__if_read_orig_vertex_0_true: evi X2 X26 BFS_pull::kv_map_return 1") 
  ## long* local tmp_lm_ptr = LMBASE + KVMSR_META_DATA_OFFSET;

  ## *tmp_lm_ptr = *tmp_lm_ptr + 0;

  tranBFS_pull__read_orig_vertex.writeAction(f"sendr_wcont X26 X2 X10 X10") 
  tranBFS_pull__read_orig_vertex.writeAction(f"yield") 
  tranBFS_pull__read_orig_vertex.writeAction(f"__if_read_orig_vertex_2_post: blti X25 5 __if_read_orig_vertex_13_false") 
  ## generate frontier for push phase

  tranBFS_pull__read_orig_vertex.writeAction(f"__if_read_orig_vertex_12_true: evi X2 X26 BFS_pull::alloc_frontier 1") 
  tranBFS_pull__read_orig_vertex.writeAction(f"addi X7 X28 104") 
  tranBFS_pull__read_orig_vertex.writeAction(f"movlr 0(X28) X28 0 8") 
  tranBFS_pull__read_orig_vertex.writeAction(f"evi X28 X28 BFS::allocate_frontier 1") 
  tranBFS_pull__read_orig_vertex.writeAction(f"sendr_wcont X28 X26 X19 X19") 
  tranBFS_pull__read_orig_vertex.writeAction(f"sli X19 X24 1") 
  ## tmp_lm_ptr = LMBASE + KVMSR_META_DATA_OFFSET;

  ## *tmp_lm_ptr = *tmp_lm_ptr + num_siblings;

  tranBFS_pull__read_orig_vertex.writeAction(f"jmp __if_read_orig_vertex_14_post") 
  ## long* local tmp_lm_ptr = LMBASE + KVMSR_META_DATA_OFFSET;

  ## *tmp_lm_ptr = *tmp_lm_ptr + num_siblings;

  tranBFS_pull__read_orig_vertex.writeAction(f"__if_read_orig_vertex_13_false: add X18 X19 X26") 
  tranBFS_pull__read_orig_vertex.writeAction(f"evi X2 X28 BFS_pull::update_siblings 1") 
  tranBFS_pull__read_orig_vertex.writeAction(f"sendr_wcont X28 X1 X26 X26") 
  tranBFS_pull__read_orig_vertex.writeAction(f"addi X19 X24 0") 
  tranBFS_pull__read_orig_vertex.writeAction(f"__if_read_orig_vertex_14_post: addi X3 X26 32") 
  tranBFS_pull__read_orig_vertex.writeAction(f"evi X2 X28 BFS_pull::write_dram_return 1") 
  tranBFS_pull__read_orig_vertex.writeAction(f"sendr2_dmlm X26 X28 X25 X22") 
  tranBFS_pull__read_orig_vertex.writeAction(f"addi X24 X24 1") 
  tranBFS_pull__read_orig_vertex.writeAction(f"yield") 
  
  # Writing code for event BFS_pull::update_siblings
  tranBFS_pull__update_siblings = efa.writeEvent('BFS_pull::update_siblings')
  tranBFS_pull__update_siblings.writeAction(f"__entry: sli X18 X26 6") 
  tranBFS_pull__update_siblings.writeAction(f"add X16 X26 X26") 
  tranBFS_pull__update_siblings.writeAction(f"addi X26 X26 32") 
  tranBFS_pull__update_siblings.writeAction(f"evi X2 X28 BFS_pull::write_dram_return 1") 
  tranBFS_pull__update_siblings.writeAction(f"addi X18 X29 32") 
  tranBFS_pull__update_siblings.writeAction(f"__while_update_siblings_3_condition: ble X8 X18 __while_update_siblings_5_post") 
  tranBFS_pull__update_siblings.writeAction(f"__while_update_siblings_4_body: ble X18 X29 __if_update_siblings_8_post") 
  tranBFS_pull__update_siblings.writeAction(f"__if_update_siblings_6_true: sendr_wcont X2 X1 X8 X8") 
  tranBFS_pull__update_siblings.writeAction(f"yield") 
  tranBFS_pull__update_siblings.writeAction(f"__if_update_siblings_8_post: sendr2_dmlm X26 X28 X25 X22") 
  tranBFS_pull__update_siblings.writeAction(f"addi X18 X18 1") 
  tranBFS_pull__update_siblings.writeAction(f"addi X26 X26 64") 
  tranBFS_pull__update_siblings.writeAction(f"jmp __while_update_siblings_3_condition") 
  tranBFS_pull__update_siblings.writeAction(f"__while_update_siblings_5_post: yield") 
  
  ## Allocate the frontier for the push phase
  # Writing code for event BFS_pull::alloc_frontier
  tranBFS_pull__alloc_frontier = efa.writeEvent('BFS_pull::alloc_frontier')
  tranBFS_pull__alloc_frontier.writeAction(f"__entry: add X18 X19 X29") 
  tranBFS_pull__alloc_frontier.writeAction(f"evi X2 X28 BFS_pull::update_siblings_frontier 1") 
  tranBFS_pull__alloc_frontier.writeAction(f"bnei X29 9 __if_alloc_frontier_5_false") 
  tranBFS_pull__alloc_frontier.writeAction(f"__if_alloc_frontier_4_true: send_wcont X28 X1 X8 9") 
  tranBFS_pull__alloc_frontier.writeAction(f"jmp __if_alloc_frontier_3_post") 
  tranBFS_pull__alloc_frontier.writeAction(f"__if_alloc_frontier_5_false: bnei X29 2 __if_alloc_frontier_7_false") 
  tranBFS_pull__alloc_frontier.writeAction(f"__if_alloc_frontier_6_true: send_wcont X28 X1 X8 2") 
  tranBFS_pull__alloc_frontier.writeAction(f"jmp __if_alloc_frontier_3_post") 
  tranBFS_pull__alloc_frontier.writeAction(f"__if_alloc_frontier_7_false: bnei X29 8 __if_alloc_frontier_9_false") 
  tranBFS_pull__alloc_frontier.writeAction(f"__if_alloc_frontier_8_true: send_wcont X28 X1 X8 8") 
  tranBFS_pull__alloc_frontier.writeAction(f"jmp __if_alloc_frontier_3_post") 
  tranBFS_pull__alloc_frontier.writeAction(f"__if_alloc_frontier_9_false: bnei X29 7 __if_alloc_frontier_11_false") 
  tranBFS_pull__alloc_frontier.writeAction(f"__if_alloc_frontier_10_true: send_wcont X28 X1 X8 7") 
  tranBFS_pull__alloc_frontier.writeAction(f"jmp __if_alloc_frontier_3_post") 
  tranBFS_pull__alloc_frontier.writeAction(f"__if_alloc_frontier_11_false: bnei X29 6 __if_alloc_frontier_13_false") 
  tranBFS_pull__alloc_frontier.writeAction(f"__if_alloc_frontier_12_true: send_wcont X28 X1 X8 6") 
  tranBFS_pull__alloc_frontier.writeAction(f"jmp __if_alloc_frontier_3_post") 
  tranBFS_pull__alloc_frontier.writeAction(f"__if_alloc_frontier_13_false: bnei X29 5 __if_alloc_frontier_15_false") 
  tranBFS_pull__alloc_frontier.writeAction(f"__if_alloc_frontier_14_true: send_wcont X28 X1 X8 5") 
  tranBFS_pull__alloc_frontier.writeAction(f"jmp __if_alloc_frontier_3_post") 
  tranBFS_pull__alloc_frontier.writeAction(f"__if_alloc_frontier_15_false: bnei X29 4 __if_alloc_frontier_17_false") 
  tranBFS_pull__alloc_frontier.writeAction(f"__if_alloc_frontier_16_true: send_wcont X28 X1 X8 4") 
  tranBFS_pull__alloc_frontier.writeAction(f"jmp __if_alloc_frontier_3_post") 
  tranBFS_pull__alloc_frontier.writeAction(f"__if_alloc_frontier_17_false: send_wcont X28 X1 X8 3") 
  tranBFS_pull__alloc_frontier.writeAction(f"__if_alloc_frontier_3_post: yield") 
  
  # Writing code for event BFS_pull::update_siblings_frontier
  tranBFS_pull__update_siblings_frontier = efa.writeEvent('BFS_pull::update_siblings_frontier')
  tranBFS_pull__update_siblings_frontier.writeAction(f"__entry: sli X18 X28 6") 
  tranBFS_pull__update_siblings_frontier.writeAction(f"add X16 X28 X28") 
  tranBFS_pull__update_siblings_frontier.writeAction(f"addi X28 X28 32") 
  tranBFS_pull__update_siblings_frontier.writeAction(f"addi X8 X29 0") 
  tranBFS_pull__update_siblings_frontier.writeAction(f"evi X2 X26 BFS_pull::write_dram_return 1") 
  tranBFS_pull__update_siblings_frontier.writeAction(f"addi X18 X30 32") 
  tranBFS_pull__update_siblings_frontier.writeAction(f"__while_update_siblings_frontier_3_condition: ble X9 X18 __while_update_siblings_frontier_5_post") 
  tranBFS_pull__update_siblings_frontier.writeAction(f"__while_update_siblings_frontier_4_body: ble X18 X30 __if_update_siblings_frontier_8_post") 
  tranBFS_pull__update_siblings_frontier.writeAction(f"__if_update_siblings_frontier_6_true: bnei X9 9 __if_update_siblings_frontier_14_false") 
  tranBFS_pull__update_siblings_frontier.writeAction(f"__if_update_siblings_frontier_13_true: send_wcont X2 X1 X29 9") 
  tranBFS_pull__update_siblings_frontier.writeAction(f"jmp __if_update_siblings_frontier_12_post") 
  tranBFS_pull__update_siblings_frontier.writeAction(f"__if_update_siblings_frontier_14_false: bnei X9 2 __if_update_siblings_frontier_16_false") 
  tranBFS_pull__update_siblings_frontier.writeAction(f"__if_update_siblings_frontier_15_true: send_wcont X2 X1 X29 2") 
  tranBFS_pull__update_siblings_frontier.writeAction(f"jmp __if_update_siblings_frontier_12_post") 
  tranBFS_pull__update_siblings_frontier.writeAction(f"__if_update_siblings_frontier_16_false: bnei X9 8 __if_update_siblings_frontier_18_false") 
  tranBFS_pull__update_siblings_frontier.writeAction(f"__if_update_siblings_frontier_17_true: send_wcont X2 X1 X29 8") 
  tranBFS_pull__update_siblings_frontier.writeAction(f"jmp __if_update_siblings_frontier_12_post") 
  tranBFS_pull__update_siblings_frontier.writeAction(f"__if_update_siblings_frontier_18_false: bnei X9 7 __if_update_siblings_frontier_20_false") 
  tranBFS_pull__update_siblings_frontier.writeAction(f"__if_update_siblings_frontier_19_true: send_wcont X2 X1 X29 7") 
  tranBFS_pull__update_siblings_frontier.writeAction(f"jmp __if_update_siblings_frontier_12_post") 
  tranBFS_pull__update_siblings_frontier.writeAction(f"__if_update_siblings_frontier_20_false: bnei X9 6 __if_update_siblings_frontier_22_false") 
  tranBFS_pull__update_siblings_frontier.writeAction(f"__if_update_siblings_frontier_21_true: send_wcont X2 X1 X29 6") 
  tranBFS_pull__update_siblings_frontier.writeAction(f"jmp __if_update_siblings_frontier_12_post") 
  tranBFS_pull__update_siblings_frontier.writeAction(f"__if_update_siblings_frontier_22_false: bnei X9 5 __if_update_siblings_frontier_24_false") 
  tranBFS_pull__update_siblings_frontier.writeAction(f"__if_update_siblings_frontier_23_true: send_wcont X2 X1 X29 5") 
  tranBFS_pull__update_siblings_frontier.writeAction(f"jmp __if_update_siblings_frontier_12_post") 
  tranBFS_pull__update_siblings_frontier.writeAction(f"__if_update_siblings_frontier_24_false: bnei X9 4 __if_update_siblings_frontier_26_false") 
  tranBFS_pull__update_siblings_frontier.writeAction(f"__if_update_siblings_frontier_25_true: send_wcont X2 X1 X29 4") 
  tranBFS_pull__update_siblings_frontier.writeAction(f"jmp __if_update_siblings_frontier_12_post") 
  tranBFS_pull__update_siblings_frontier.writeAction(f"__if_update_siblings_frontier_26_false: send_wcont X2 X1 X29 3") 
  tranBFS_pull__update_siblings_frontier.writeAction(f"__if_update_siblings_frontier_12_post: yield") 
  tranBFS_pull__update_siblings_frontier.writeAction(f"__if_update_siblings_frontier_8_post: sendr2_dmlm X28 X26 X25 X22") 
  tranBFS_pull__update_siblings_frontier.writeAction(f"sendr_dmlm X29 X26 X18") 
  tranBFS_pull__update_siblings_frontier.writeAction(f"addi X18 X18 1") 
  tranBFS_pull__update_siblings_frontier.writeAction(f"addi X28 X28 64") 
  tranBFS_pull__update_siblings_frontier.writeAction(f"addi X29 X29 8") 
  tranBFS_pull__update_siblings_frontier.writeAction(f"jmp __while_update_siblings_frontier_3_condition") 
  tranBFS_pull__update_siblings_frontier.writeAction(f"__while_update_siblings_frontier_5_post: yield") 
  
  # Writing code for event BFS_pull::write_dram_return
  tranBFS_pull__write_dram_return = efa.writeEvent('BFS_pull::write_dram_return')
  tranBFS_pull__write_dram_return.writeAction(f"__entry: subi X24 X24 1") 
  tranBFS_pull__write_dram_return.writeAction(f"bnei X24 0 __if_write_dram_return_5_post") 
  tranBFS_pull__write_dram_return.writeAction(f"__if_write_dram_return_3_true: evi X2 X29 BFS_pull::kv_map_return 1") 
  tranBFS_pull__write_dram_return.writeAction(f"sendr_wcont X29 X2 X21 X19") 
  tranBFS_pull__write_dram_return.writeAction(f"__if_write_dram_return_5_post: yield") 
  