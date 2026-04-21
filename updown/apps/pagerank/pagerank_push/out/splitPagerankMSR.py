from linker.EFAProgram import efaProgram

## Global constants

@efaProgram
def EFA_splitPagerankMSR(efa):
  efa.code_level = 'machine'
  state0 = efa.State("udweave_init") #Only one state code 
  efa.add_initId(state0.state_id)
  ## Static declarations
  ## Scoped Variable "vid" uses Register X16, scope (0)
  ## Scoped Variable "degree" uses Register X17, scope (0)
  ## Scoped Variable "nlist_ptr" uses Register X18, scope (0)
  ## Scoped Variable "out_value" uses Register X19, scope (0)
  ## Scoped Variable "nlist_bound" uses Register X20, scope (0)
  ## Scoped Variable "sibling_addr" uses Register X21, scope (0)
  ## Scoped Variable "sibling_ptr" uses Register X22, scope (0)
  ## Scoped Variable "orig_degree" uses Register X23, scope (0)
  ## Scoped Variable "num_processed" uses Register X24, scope (0)
  ## Scoped Variable "emit_evw" uses Register X25, scope (0)
  ## Param "deg_op" uses Register X8, scope (0->4)
  ## Param "vid_op" uses Register X9, scope (0->4)
  ## Param "neighbors_op" uses Register X10, scope (0->4)
  ## Param "orig_vid_op" uses Register X11, scope (0->4)
  ## Param "split_start_op" uses Register X12, scope (0->4)
  ## Param "split_bound_op" uses Register X13, scope (0->4)
  ## Param "val_op" uses Register X14, scope (0->4)
  ## Param "gv_bin" uses Register X15, scope (0->4)
  ## Param "vertex_addr" uses Register X3, scope (0->4)
  ## Scoped Variable "evw" uses Register X26, scope (0->4->6)
  ## Scoped Variable "max_parallelism" uses Register X26, scope (0->4->10)
  ## Scoped Variable "deg" uses Register X26, scope (0->4->15)
  ## Scoped Variable "evw" uses Register X27, scope (0->4->15)
  ## Param "deg_sibling" uses Register X8, scope (0->18)
  ## Param "vid_sibling" uses Register X9, scope (0->18)
  ## Param "neighbors_sibling" uses Register X10, scope (0->18)
  ## Param "orig_vid" uses Register X11, scope (0->18)
  ## Param "split_start_sibling" uses Register X12, scope (0->18)
  ## Param "split_bound_sibling" uses Register X13, scope (0->18)
  ## Param "val_sibling" uses Register X14, scope (0->18)
  ## Param "gv_bin" uses Register X15, scope (0->18)
  ## Param "vertex_addr" uses Register X3, scope (0->18)
  ## Scoped Variable "num_siblings" uses Register X26, scope (0->18)
  ## Scoped Variable "deg" uses Register X27, scope (0->18->24)
  ## Scoped Variable "evw" uses Register X28, scope (0->18->24)
  ## Param "vid_op" uses Register X8, scope (0->26)
  ## Param "out_value_op" uses Register X9, scope (0->26)
  ## Scoped Variable "evw" uses Register X26, scope (0->26)
  ## Param "e0" uses Register X8, scope (0->30)
  ## Param "e1" uses Register X9, scope (0->30)
  ## Param "e2" uses Register X10, scope (0->30)
  ## Param "e3" uses Register X11, scope (0->30)
  ## Param "e4" uses Register X12, scope (0->30)
  ## Param "e5" uses Register X13, scope (0->30)
  ## Param "e6" uses Register X14, scope (0->30)
  ## Param "e7" uses Register X15, scope (0->30)
  ## Param "curr_nlist_addr" uses Register X3, scope (0->30)
  ## Scoped Variable "tmp_nlist_ptr" uses Register X26, scope (0->30)
  ## Scoped Variable "evw" uses Register X27, scope (0->30->33)
  ## Scoped Variable "evw" uses Register X27, scope (0->30->39)
  ## Scoped Variable "evw" uses Register X27, scope (0->30->45)
  ## Scoped Variable "evw" uses Register X27, scope (0->30->51)
  ## Scoped Variable "evw" uses Register X27, scope (0->30->57)
  ## Scoped Variable "evw" uses Register X27, scope (0->30->63)
  ## Scoped Variable "evw" uses Register X27, scope (0->30->69)
  ## Scoped Variable "evw" uses Register X27, scope (0->30->75)
  ## Scoped Variable "tmp_lm_ptr" uses Register X16, scope (0)
  ## Param "partition_array" uses Register X8, scope (0->79)
  ## Param "NUM_PARTITION_PER_LANE" uses Register X9, scope (0->79)
  ## Param "num_lanes" uses Register X10, scope (0->79)
  ## Param "vertices" uses Register X11, scope (0->79)
  ## Param "num_vertices" uses Register X12, scope (0->79)
  ## Param "values" uses Register X13, scope (0->79)
  ## Param "num_values" uses Register X14, scope (0->79)
  ## Scoped Variable "send_buffer" uses Register X17, scope (0->79)
  ## Scoped Variable "evw" uses Register X18, scope (0->79)
  ## #define GRAPH_PTR_OFFSET (768)
  
  #####################################################
  ###### Writing code for thread splitPageRankMS ######
  #####################################################
  # Writing code for event splitPageRankMS::kv_map
  transplitPageRankMS__kv_map = efa.writeEvent('splitPageRankMS::kv_map')
  ## The vertex has degree 0, skip it
  transplitPageRankMS__kv_map.writeAction(f"entry: bnei X8 0 __if_kv_map_2_post") 
  transplitPageRankMS__kv_map.writeAction(f"__if_kv_map_0_true: evi X2 X26 splitPageRankMS::kv_map_return 1") 
  transplitPageRankMS__kv_map.writeAction(f"sendr_wcont X26 X2 X9 X9") 
  transplitPageRankMS__kv_map.writeAction(f"yield") 
  transplitPageRankMS__kv_map.writeAction(f"__if_kv_map_2_post: addi X9 X16 0") 
  transplitPageRankMS__kv_map.writeAction(f"addi X8 X17 0") 
  transplitPageRankMS__kv_map.writeAction(f"addi X12 X22 0") 
  ## Set the nlist pointer to the start of the neighbor list
  ## The nlist pointer is the address of the neighbor list in DRAM
  ## The nlist_bound is the end of the neighbor list
  transplitPageRankMS__kv_map.writeAction(f"sli X8 X26 3") 
  transplitPageRankMS__kv_map.writeAction(f"add X10 X26 X20") 
  transplitPageRankMS__kv_map.writeAction(f"addi X10 X18 0") 
  transplitPageRankMS__kv_map.writeAction(f"beq X9 X11 __if_kv_map_10_false") 
  ## if (deg_op == 0) {
  ## If the vertex is split, we need to pull the values from the sibling vertices
  transplitPageRankMS__kv_map.writeAction(f"__if_kv_map_9_true: evi X2 X25 splitPageRankMS::sibling_rd_return 1") 
  transplitPageRankMS__kv_map.writeAction(f"movir X26 256") 
  transplitPageRankMS__kv_map.writeAction(f"addi X15 X21 0") 
  transplitPageRankMS__kv_map.writeAction(f"sli X22 X27 6") 
  transplitPageRankMS__kv_map.writeAction(f"add X21 X27 X21") 
  ## Issue DRAM read requests to fetch sibling vertices
  transplitPageRankMS__kv_map.writeAction(f"movir X24 0") 
  transplitPageRankMS__kv_map.writeAction(f"__while_kv_map_15_condition: clt X22 X13 X27") 
  transplitPageRankMS__kv_map.writeAction(f"clt X24 X26 X28") 
  transplitPageRankMS__kv_map.writeAction(f"and X27 X28 X29") 
  transplitPageRankMS__kv_map.writeAction(f"beqi X29 0 __while_kv_map_17_post") 
  transplitPageRankMS__kv_map.writeAction(f"__while_kv_map_16_body: send_dmlm_ld X21 X25 8") 
  transplitPageRankMS__kv_map.writeAction(f"addi X22 X22 1") 
  transplitPageRankMS__kv_map.writeAction(f"addi X21 X21 64") 
  transplitPageRankMS__kv_map.writeAction(f"addi X24 X24 1") 
  transplitPageRankMS__kv_map.writeAction(f"jmp __while_kv_map_15_condition") 
  transplitPageRankMS__kv_map.writeAction(f"__while_kv_map_17_post: movir X24 0") 
  transplitPageRankMS__kv_map.writeAction(f"movir X19 0") 
  ## Initialize out_value to 0.0 for the split case
  transplitPageRankMS__kv_map.writeAction(f"movir X23 0") 
  transplitPageRankMS__kv_map.writeAction(f"yield") 
  transplitPageRankMS__kv_map.writeAction(f"jmp __if_kv_map_11_post") 
  ## If the vertex is not split, we can process it directly
  transplitPageRankMS__kv_map.writeAction(f"__if_kv_map_10_false: fcnvt.i64.64 X8 X26")  # This is for casting. May be used later on
  transplitPageRankMS__kv_map.writeAction(f"fdiv.64 X14 X26 X19") 
  transplitPageRankMS__kv_map.writeAction(f"evi X2 X27 splitPageRankMS::push_update 1") 
  transplitPageRankMS__kv_map.writeAction(f"sendr_wcont X27 X2 X16 X19") 
  transplitPageRankMS__kv_map.writeAction(f"yield") 
  transplitPageRankMS__kv_map.writeAction(f"__if_kv_map_11_post: yield") 
  
  # Writing code for event splitPageRankMS::sibling_rd_return
  transplitPageRankMS__sibling_rd_return = efa.writeEvent('splitPageRankMS::sibling_rd_return')
  transplitPageRankMS__sibling_rd_return.writeAction(f"entry: ble X13 X22 __if_sibling_rd_return_2_post") 
  transplitPageRankMS__sibling_rd_return.writeAction(f"__if_sibling_rd_return_0_true: send_dmlm_ld X21 X2 8") 
  transplitPageRankMS__sibling_rd_return.writeAction(f"addi X22 X22 1") 
  transplitPageRankMS__sibling_rd_return.writeAction(f"addi X21 X21 64") 
  transplitPageRankMS__sibling_rd_return.writeAction(f"__if_sibling_rd_return_2_post: fadd.64 X19 X14 X19") 
  transplitPageRankMS__sibling_rd_return.writeAction(f"fcnvt.i64.64 X8 X26")  # This is for casting. May be used later on
  transplitPageRankMS__sibling_rd_return.writeAction(f"fadd.64 X23 X26 X23") 
  transplitPageRankMS__sibling_rd_return.writeAction(f"addi X24 X24 1") 
  transplitPageRankMS__sibling_rd_return.writeAction(f"sub X13 X12 X26") 
  transplitPageRankMS__sibling_rd_return.writeAction(f"bne X24 X26 __if_sibling_rd_return_11_post") 
  transplitPageRankMS__sibling_rd_return.writeAction(f"__if_sibling_rd_return_9_true: addi X23 X27 0") 
  transplitPageRankMS__sibling_rd_return.writeAction(f"fdiv.64 X19 X27 X19") 
  transplitPageRankMS__sibling_rd_return.writeAction(f"evi X2 X28 splitPageRankMS::push_update 1") 
  transplitPageRankMS__sibling_rd_return.writeAction(f"sendr_wcont X28 X2 X16 X19") 
  transplitPageRankMS__sibling_rd_return.writeAction(f"__if_sibling_rd_return_11_post: yield") 
  
  # Writing code for event splitPageRankMS::push_update
  transplitPageRankMS__push_update = efa.writeEvent('splitPageRankMS::push_update')
  transplitPageRankMS__push_update.writeAction(f"entry: movir X24 0") 
  transplitPageRankMS__push_update.writeAction(f"movir X25 0") 
  transplitPageRankMS__push_update.writeAction(f"evlb X25 splitPageRankMS::kv_map_emit") 
  transplitPageRankMS__push_update.writeAction(f"evi X25 X25 255 4") 
  transplitPageRankMS__push_update.writeAction(f"ev X25 X25 X0 X0 8") 
  transplitPageRankMS__push_update.writeAction(f"evi X2 X26 splitPageRankMS::rd_nlist_return 1") 
  transplitPageRankMS__push_update.writeAction(f"__while_push_update_3_condition: ble X20 X18 __while_push_update_5_post") 
  transplitPageRankMS__push_update.writeAction(f"__while_push_update_4_body: send_dmlm_ld X18 X26 8") 
  transplitPageRankMS__push_update.writeAction(f"addi X18 X18 64") 
  transplitPageRankMS__push_update.writeAction(f"jmp __while_push_update_3_condition") 
  transplitPageRankMS__push_update.writeAction(f"__while_push_update_5_post: yield") 
  
  # Writing code for event splitPageRankMS::rd_nlist_return
  transplitPageRankMS__rd_nlist_return = efa.writeEvent('splitPageRankMS::rd_nlist_return')
  ## if(e0 == 57){
  ##     print("[DEBUG][NWID %d][push_update] Vertex %ld start to push value updated to %lu", NETID, vid, out_value);
  ## }
  ## if(e1 == 57){
  ##     print("[DEBUG][NWID %d][push_update] Vertex %ld start to push value updated to %lu", NETID, vid, out_value);
  ## }
  ## if(e2 == 57){
  ##     print("[DEBUG][NWID %d][push_update] Vertex %ld start to push value updated to %lu", NETID, vid, out_value);
  ## }
  ## if(e3 == 57){
  ##     print("[DEBUG][NWID %d][push_update] Vertex %ld start to push value updated to %lu", NETID, vid, out_value);
  ## }
  ## if(e4 == 57){
  ##     print("[DEBUG][NWID %d][push_update] Vertex %ld start to push value updated to %lu", NETID, vid, out_value);
  ## }
  ## if(e5 == 57){
  ##     print("[DEBUG][NWID %d][push_update] Vertex %ld start to push value updated to %lu", NETID, vid, out_value);
  ## }
  ## if(e6 == 57){
  ##     print("[DEBUG][NWID %d][push_update] Vertex %ld start to push value updated to %lu", NETID, vid, out_value);
  ## }
  ## if(e7 == 57){
  ##     print("[DEBUG][NWID %d][push_update] Vertex %ld start to push value updated to %lu", NETID, vid, out_value);
  ## }
  transplitPageRankMS__rd_nlist_return.writeAction(f"entry: addi X3 X26 0") 
  transplitPageRankMS__rd_nlist_return.writeAction(f"movir X27 -1") 
  transplitPageRankMS__rd_nlist_return.writeAction(f"sri X27 X27 1") 
  transplitPageRankMS__rd_nlist_return.writeAction(f"sendr_wcont X25 X27 X8 X19") 
  transplitPageRankMS__rd_nlist_return.writeAction(f"addi X24 X24 1") 
  transplitPageRankMS__rd_nlist_return.writeAction(f"bne X24 X17 __if_rd_nlist_return_5_post") 
  transplitPageRankMS__rd_nlist_return.writeAction(f"__if_rd_nlist_return_3_true: evi X2 X27 splitPageRankMS::kv_map_return 1") 
  transplitPageRankMS__rd_nlist_return.writeAction(f"sendr_wcont X27 X2 X16 X16") 
  transplitPageRankMS__rd_nlist_return.writeAction(f"yield") 
  transplitPageRankMS__rd_nlist_return.writeAction(f"__if_rd_nlist_return_5_post: addi X26 X26 8") 
  transplitPageRankMS__rd_nlist_return.writeAction(f"bgt X20 X26 __if_rd_nlist_return_11_post") 
  transplitPageRankMS__rd_nlist_return.writeAction(f"__if_rd_nlist_return_9_true: yield") 
  transplitPageRankMS__rd_nlist_return.writeAction(f"__if_rd_nlist_return_11_post: movir X27 -1") 
  transplitPageRankMS__rd_nlist_return.writeAction(f"sri X27 X27 1") 
  transplitPageRankMS__rd_nlist_return.writeAction(f"sendr_wcont X25 X27 X9 X19") 
  transplitPageRankMS__rd_nlist_return.writeAction(f"addi X24 X24 1") 
  transplitPageRankMS__rd_nlist_return.writeAction(f"bne X24 X17 __if_rd_nlist_return_17_post") 
  transplitPageRankMS__rd_nlist_return.writeAction(f"__if_rd_nlist_return_15_true: evi X2 X27 splitPageRankMS::kv_map_return 1") 
  transplitPageRankMS__rd_nlist_return.writeAction(f"sendr_wcont X27 X2 X16 X16") 
  transplitPageRankMS__rd_nlist_return.writeAction(f"yield") 
  transplitPageRankMS__rd_nlist_return.writeAction(f"__if_rd_nlist_return_17_post: addi X26 X26 8") 
  transplitPageRankMS__rd_nlist_return.writeAction(f"bgt X20 X26 __if_rd_nlist_return_23_post") 
  transplitPageRankMS__rd_nlist_return.writeAction(f"__if_rd_nlist_return_21_true: yield") 
  transplitPageRankMS__rd_nlist_return.writeAction(f"__if_rd_nlist_return_23_post: movir X27 -1") 
  transplitPageRankMS__rd_nlist_return.writeAction(f"sri X27 X27 1") 
  transplitPageRankMS__rd_nlist_return.writeAction(f"sendr_wcont X25 X27 X10 X19") 
  transplitPageRankMS__rd_nlist_return.writeAction(f"addi X24 X24 1") 
  transplitPageRankMS__rd_nlist_return.writeAction(f"bne X24 X17 __if_rd_nlist_return_29_post") 
  transplitPageRankMS__rd_nlist_return.writeAction(f"__if_rd_nlist_return_27_true: evi X2 X27 splitPageRankMS::kv_map_return 1") 
  transplitPageRankMS__rd_nlist_return.writeAction(f"sendr_wcont X27 X2 X16 X16") 
  transplitPageRankMS__rd_nlist_return.writeAction(f"yield") 
  transplitPageRankMS__rd_nlist_return.writeAction(f"__if_rd_nlist_return_29_post: addi X26 X26 8") 
  transplitPageRankMS__rd_nlist_return.writeAction(f"bgt X20 X26 __if_rd_nlist_return_35_post") 
  transplitPageRankMS__rd_nlist_return.writeAction(f"__if_rd_nlist_return_33_true: yield") 
  transplitPageRankMS__rd_nlist_return.writeAction(f"__if_rd_nlist_return_35_post: movir X27 -1") 
  transplitPageRankMS__rd_nlist_return.writeAction(f"sri X27 X27 1") 
  transplitPageRankMS__rd_nlist_return.writeAction(f"sendr_wcont X25 X27 X11 X19") 
  transplitPageRankMS__rd_nlist_return.writeAction(f"addi X24 X24 1") 
  transplitPageRankMS__rd_nlist_return.writeAction(f"bne X24 X17 __if_rd_nlist_return_41_post") 
  transplitPageRankMS__rd_nlist_return.writeAction(f"__if_rd_nlist_return_39_true: evi X2 X27 splitPageRankMS::kv_map_return 1") 
  transplitPageRankMS__rd_nlist_return.writeAction(f"sendr_wcont X27 X2 X16 X16") 
  transplitPageRankMS__rd_nlist_return.writeAction(f"yield") 
  transplitPageRankMS__rd_nlist_return.writeAction(f"__if_rd_nlist_return_41_post: addi X26 X26 8") 
  transplitPageRankMS__rd_nlist_return.writeAction(f"bgt X20 X26 __if_rd_nlist_return_47_post") 
  transplitPageRankMS__rd_nlist_return.writeAction(f"__if_rd_nlist_return_45_true: yield") 
  transplitPageRankMS__rd_nlist_return.writeAction(f"__if_rd_nlist_return_47_post: movir X27 -1") 
  transplitPageRankMS__rd_nlist_return.writeAction(f"sri X27 X27 1") 
  transplitPageRankMS__rd_nlist_return.writeAction(f"sendr_wcont X25 X27 X12 X19") 
  transplitPageRankMS__rd_nlist_return.writeAction(f"addi X24 X24 1") 
  transplitPageRankMS__rd_nlist_return.writeAction(f"bne X24 X17 __if_rd_nlist_return_53_post") 
  transplitPageRankMS__rd_nlist_return.writeAction(f"__if_rd_nlist_return_51_true: evi X2 X27 splitPageRankMS::kv_map_return 1") 
  transplitPageRankMS__rd_nlist_return.writeAction(f"sendr_wcont X27 X2 X16 X16") 
  transplitPageRankMS__rd_nlist_return.writeAction(f"yield") 
  transplitPageRankMS__rd_nlist_return.writeAction(f"__if_rd_nlist_return_53_post: addi X26 X26 8") 
  transplitPageRankMS__rd_nlist_return.writeAction(f"bgt X20 X26 __if_rd_nlist_return_59_post") 
  transplitPageRankMS__rd_nlist_return.writeAction(f"__if_rd_nlist_return_57_true: yield") 
  transplitPageRankMS__rd_nlist_return.writeAction(f"__if_rd_nlist_return_59_post: movir X27 -1") 
  transplitPageRankMS__rd_nlist_return.writeAction(f"sri X27 X27 1") 
  transplitPageRankMS__rd_nlist_return.writeAction(f"sendr_wcont X25 X27 X13 X19") 
  transplitPageRankMS__rd_nlist_return.writeAction(f"addi X24 X24 1") 
  transplitPageRankMS__rd_nlist_return.writeAction(f"bne X24 X17 __if_rd_nlist_return_65_post") 
  transplitPageRankMS__rd_nlist_return.writeAction(f"__if_rd_nlist_return_63_true: evi X2 X27 splitPageRankMS::kv_map_return 1") 
  transplitPageRankMS__rd_nlist_return.writeAction(f"sendr_wcont X27 X2 X16 X16") 
  transplitPageRankMS__rd_nlist_return.writeAction(f"yield") 
  transplitPageRankMS__rd_nlist_return.writeAction(f"__if_rd_nlist_return_65_post: addi X26 X26 8") 
  transplitPageRankMS__rd_nlist_return.writeAction(f"bgt X20 X26 __if_rd_nlist_return_71_post") 
  transplitPageRankMS__rd_nlist_return.writeAction(f"__if_rd_nlist_return_69_true: yield") 
  transplitPageRankMS__rd_nlist_return.writeAction(f"__if_rd_nlist_return_71_post: movir X27 -1") 
  transplitPageRankMS__rd_nlist_return.writeAction(f"sri X27 X27 1") 
  transplitPageRankMS__rd_nlist_return.writeAction(f"sendr_wcont X25 X27 X14 X19") 
  transplitPageRankMS__rd_nlist_return.writeAction(f"addi X24 X24 1") 
  transplitPageRankMS__rd_nlist_return.writeAction(f"bne X24 X17 __if_rd_nlist_return_77_post") 
  transplitPageRankMS__rd_nlist_return.writeAction(f"__if_rd_nlist_return_75_true: evi X2 X27 splitPageRankMS::kv_map_return 1") 
  transplitPageRankMS__rd_nlist_return.writeAction(f"sendr_wcont X27 X2 X16 X16") 
  transplitPageRankMS__rd_nlist_return.writeAction(f"yield") 
  transplitPageRankMS__rd_nlist_return.writeAction(f"__if_rd_nlist_return_77_post: addi X26 X26 8") 
  transplitPageRankMS__rd_nlist_return.writeAction(f"bgt X20 X26 __if_rd_nlist_return_83_post") 
  transplitPageRankMS__rd_nlist_return.writeAction(f"__if_rd_nlist_return_81_true: yield") 
  transplitPageRankMS__rd_nlist_return.writeAction(f"__if_rd_nlist_return_83_post: movir X27 -1") 
  transplitPageRankMS__rd_nlist_return.writeAction(f"sri X27 X27 1") 
  transplitPageRankMS__rd_nlist_return.writeAction(f"sendr_wcont X25 X27 X15 X19") 
  transplitPageRankMS__rd_nlist_return.writeAction(f"addi X24 X24 1") 
  transplitPageRankMS__rd_nlist_return.writeAction(f"bne X24 X17 __if_rd_nlist_return_89_post") 
  transplitPageRankMS__rd_nlist_return.writeAction(f"__if_rd_nlist_return_87_true: evi X2 X27 splitPageRankMS::kv_map_return 1") 
  transplitPageRankMS__rd_nlist_return.writeAction(f"sendr_wcont X27 X2 X16 X16") 
  transplitPageRankMS__rd_nlist_return.writeAction(f"yield") 
  transplitPageRankMS__rd_nlist_return.writeAction(f"__if_rd_nlist_return_89_post: yield") 
  
  
  ################################################
  ###### Writing code for thread InitUpDown ######
  ################################################
  # Writing code for event InitUpDown::init
  tranInitUpDown__init = efa.writeEvent('InitUpDown::init')
  tranInitUpDown__init.writeAction(f"entry: print 'Top parameters: partition_array=0x%lX, num_lanes=%ld, vertices=0x%lX, values=0x%lX' X8 X10 X11 X13") 
  tranInitUpDown__init.writeAction(f"addi X7 X17 8") 
  tranInitUpDown__init.writeAction(f"movrl X8 0(X17) 0 8") 
  tranInitUpDown__init.writeAction(f"movrl X9 8(X17) 0 8") 
  tranInitUpDown__init.writeAction(f"movrl X10 16(X17) 0 8") 
  tranInitUpDown__init.writeAction(f"addi X7 X16 768") 
  tranInitUpDown__init.writeAction(f"movrl X11 0(X16) 0 8") 
  tranInitUpDown__init.writeAction(f"movrl X12 8(X16) 0 8") 
  tranInitUpDown__init.writeAction(f"movrl X16 24(X17) 0 8") 
  tranInitUpDown__init.writeAction(f"addi X7 X16 832") 
  tranInitUpDown__init.writeAction(f"movrl X13 0(X16) 0 8") 
  tranInitUpDown__init.writeAction(f"movrl X14 8(X16) 0 8") 
  tranInitUpDown__init.writeAction(f"movrl X16 32(X17) 0 8") 
  tranInitUpDown__init.writeAction(f"movir X18 0") 
  tranInitUpDown__init.writeAction(f"evlb X18 splitPageRankMS::map_shuffle_reduce") 
  tranInitUpDown__init.writeAction(f"evi X18 X18 255 4") 
  tranInitUpDown__init.writeAction(f"ev X18 X18 X0 X0 8") 
  tranInitUpDown__init.writeAction(f"send_wret X18 InitUpDown::terminate X17 5 X19") 
  tranInitUpDown__init.writeAction(f"addi X7 X16 0") 
  tranInitUpDown__init.writeAction(f"movir X20 0") 
  tranInitUpDown__init.writeAction(f"movrl X20 0(X16) 0 8") 
  tranInitUpDown__init.writeAction(f"yield") 
  
  # Writing code for event InitUpDown::terminate
  tranInitUpDown__terminate = efa.writeEvent('InitUpDown::terminate')
  tranInitUpDown__terminate.writeAction(f"entry: print 'PageRank Map Shuffle Reduce returned. Finish updown execution and return to top.'") 
  tranInitUpDown__terminate.writeAction(f"movir X18 1") 
  tranInitUpDown__terminate.writeAction(f"movrl X18 0(X16) 0 8") 
  tranInitUpDown__terminate.writeAction(f"yield_terminate") 
  
