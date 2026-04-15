from linker.EFAProgram import efaProgram

## UDWeave version: 02d7c60 (2026-01-27)

## Global constants

@efaProgram
def EFA_v1v2intersection(efa):
  efa.code_level = 'machine'
  state0 = efa.State("udweave_init") #Only one state code 
  efa.add_initId(state0.state_id)
  ## Static declarations
  ## Scoped Variable "abreturn_count" uses Register X16, scope (0)
  ## Scoped Variable "offs_a" uses Register X17, scope (0)
  ## Scoped Variable "offs_b" uses Register X18, scope (0)
  ## Scoped Variable "lmbuff" uses Register X19, scope (0)
  ## Scoped Variable "alist" uses Register X20, scope (0)
  ## Scoped Variable "blist" uses Register X21, scope (0)
  ## Scoped Variable "tc" uses Register X22, scope (0)
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
  ## thread offsets (total space = 41*8 = 336 bytes)
  ## #define NO_ADVANCED_STOP
  
  ######################################################
  ###### Writing code for thread v1v2intersection ######
  ######################################################
  # Writing code for event v1v2intersection::launch
  tranv1v2intersection__launch = efa.writeEvent('v1v2intersection::launch')
  ## fetch v1 and v2

  ## print("Intersection v1:%lu v2:%lu threshold:%lu", v1, v2, threshold);

  tranv1v2intersection__launch.writeAction(f"__entry: movir X23 224") 
  tranv1v2intersection__launch.writeAction(f"sri X2 X24 24") 
  tranv1v2intersection__launch.writeAction(f"andi X24 X24 255") 
  tranv1v2intersection__launch.writeAction(f"muli X24 X24 240") 
  tranv1v2intersection__launch.writeAction(f"addi X24 X24 0")  # This is for casting. May be used later on
  tranv1v2intersection__launch.writeAction(f"add X24 X23 X24") 
  tranv1v2intersection__launch.writeAction(f"add X7 X24 X19") 
  ## lmbuff[TC] = 0;

  tranv1v2intersection__launch.writeAction(f"movir X22 0") 
  tranv1v2intersection__launch.writeAction(f"movrl X1 8(X19) 0 8") 
  tranv1v2intersection__launch.writeAction(f"movrl X10 192(X19) 0 8") 
  tranv1v2intersection__launch.writeAction(f"movrl X11 200(X19) 0 8") 
  tranv1v2intersection__launch.writeAction(f"movrl X12 208(X19) 0 8") 
  tranv1v2intersection__launch.writeAction(f"movir X24 0") 
  tranv1v2intersection__launch.writeAction(f"movrl X24 16(X19) 0 8") 
  tranv1v2intersection__launch.writeAction(f"movir X24 0") 
  tranv1v2intersection__launch.writeAction(f"movrl X24 24(X19) 0 8") 
  tranv1v2intersection__launch.writeAction(f"movrl X13 216(X19) 0 8") 
  tranv1v2intersection__launch.writeAction(f"movir X16 0") 
  tranv1v2intersection__launch.writeAction(f"movir X17 0") 
  tranv1v2intersection__launch.writeAction(f"movir X18 0") 
  tranv1v2intersection__launch.writeAction(f"sli X10 X24 6") 
  tranv1v2intersection__launch.writeAction(f"add X9 X24 X24") 
  tranv1v2intersection__launch.writeAction(f"send_dmlm_ld_wret X24 v1v2intersection::vert_return 5 X23") 
  tranv1v2intersection__launch.writeAction(f"sli X11 X23 6") 
  tranv1v2intersection__launch.writeAction(f"add X9 X23 X24") 
  tranv1v2intersection__launch.writeAction(f"send_dmlm_ld_wret X24 v1v2intersection::vert_return 5 X23") 
  tranv1v2intersection__launch.writeAction(f"addi X19 X20 64") 
  tranv1v2intersection__launch.writeAction(f"addi X19 X21 128") 
  tranv1v2intersection__launch.writeAction(f"yield") 
  
  # Writing code for event v1v2intersection::vert_return
  tranv1v2intersection__vert_return = efa.writeEvent('v1v2intersection::vert_return')
  ##0 - deg, 2 - neighlistptr

  ## save nlist

  ## if degree is 0, yield_t

  tranv1v2intersection__vert_return.writeAction(f"__entry: bnei X8 0 __if_vert_return_2_post") 
  tranv1v2intersection__vert_return.writeAction(f"__if_vert_return_0_true: bnei X16 0 __if_vert_return_4_false") 
  tranv1v2intersection__vert_return.writeAction(f"__if_vert_return_3_true: movir X17 1") 
  tranv1v2intersection__vert_return.writeAction(f"jmp __if_vert_return_2_post") 
  tranv1v2intersection__vert_return.writeAction(f"__if_vert_return_4_false: movir X24 0") 
  tranv1v2intersection__vert_return.writeAction(f"movlr 8(X19) X23 0 8") 
  tranv1v2intersection__vert_return.writeAction(f"movlr 216(X19) X25 0 8") 
  tranv1v2intersection__vert_return.writeAction(f"movir X26 -1") 
  tranv1v2intersection__vert_return.writeAction(f"sri X26 X26 1") 
  tranv1v2intersection__vert_return.writeAction(f"sendr_wcont X23 X26 X25 X24") 
  tranv1v2intersection__vert_return.writeAction(f"yield_terminate") 
  tranv1v2intersection__vert_return.writeAction(f"__if_vert_return_2_post: ceqi X16 X24 1") 
  tranv1v2intersection__vert_return.writeAction(f"ceqi X17 X23 1") 
  tranv1v2intersection__vert_return.writeAction(f"and X24 X23 X24") 
  tranv1v2intersection__vert_return.writeAction(f"beqi X24 0 __if_vert_return_8_post") 
  tranv1v2intersection__vert_return.writeAction(f"__if_vert_return_6_true: movir X24 0") 
  tranv1v2intersection__vert_return.writeAction(f"movlr 8(X19) X23 0 8") 
  tranv1v2intersection__vert_return.writeAction(f"movlr 216(X19) X25 0 8") 
  tranv1v2intersection__vert_return.writeAction(f"movir X26 -1") 
  tranv1v2intersection__vert_return.writeAction(f"sri X26 X26 1") 
  tranv1v2intersection__vert_return.writeAction(f"sendr_wcont X23 X26 X25 X24") 
  tranv1v2intersection__vert_return.writeAction(f"yield_terminate") 
  tranv1v2intersection__vert_return.writeAction(f"__if_vert_return_8_post: addi X16 X16 1") 
  tranv1v2intersection__vert_return.writeAction(f"bnei X16 2 __if_vert_return_10_false") 
  tranv1v2intersection__vert_return.writeAction(f"__if_vert_return_9_true: ble X11 X22 __if_vert_return_14_post") 
  tranv1v2intersection__vert_return.writeAction(f"__if_vert_return_12_true: movir X24 0") 
  tranv1v2intersection__vert_return.writeAction(f"movlr 8(X19) X23 0 8") 
  tranv1v2intersection__vert_return.writeAction(f"movlr 216(X19) X25 0 8") 
  tranv1v2intersection__vert_return.writeAction(f"movir X26 -1") 
  tranv1v2intersection__vert_return.writeAction(f"sri X26 X26 1") 
  tranv1v2intersection__vert_return.writeAction(f"sendr_wcont X23 X26 X25 X24") 
  tranv1v2intersection__vert_return.writeAction(f"yield_terminate") 
  tranv1v2intersection__vert_return.writeAction(f"__if_vert_return_14_post: bne X11 X22 __if_vert_return_17_post") 
  tranv1v2intersection__vert_return.writeAction(f"__if_vert_return_15_true: movlr 208(X19) X24 0 8") 
  tranv1v2intersection__vert_return.writeAction(f"bleu X24 X11 __if_vert_return_19_false") 
  tranv1v2intersection__vert_return.writeAction(f"__if_vert_return_18_true: movir X24 1") 
  tranv1v2intersection__vert_return.writeAction(f"jmp __if_vert_return_20_post") 
  tranv1v2intersection__vert_return.writeAction(f"__if_vert_return_19_false: movir X24 0") 
  tranv1v2intersection__vert_return.writeAction(f"__if_vert_return_20_post: movlr 8(X19) X23 0 8") 
  tranv1v2intersection__vert_return.writeAction(f"movlr 216(X19) X25 0 8") 
  tranv1v2intersection__vert_return.writeAction(f"movir X26 -1") 
  tranv1v2intersection__vert_return.writeAction(f"sri X26 X26 1") 
  tranv1v2intersection__vert_return.writeAction(f"sendr_wcont X23 X26 X25 X24") 
  tranv1v2intersection__vert_return.writeAction(f"yield_terminate") 
  tranv1v2intersection__vert_return.writeAction(f"__if_vert_return_17_post: ble X18 X12 __if_vert_return_23_post") 
  tranv1v2intersection__vert_return.writeAction(f"__if_vert_return_21_true: movir X24 0") 
  tranv1v2intersection__vert_return.writeAction(f"movlr 8(X19) X23 0 8") 
  tranv1v2intersection__vert_return.writeAction(f"movlr 216(X19) X25 0 8") 
  tranv1v2intersection__vert_return.writeAction(f"movir X26 -1") 
  tranv1v2intersection__vert_return.writeAction(f"sri X26 X26 1") 
  tranv1v2intersection__vert_return.writeAction(f"sendr_wcont X23 X26 X25 X24") 
  tranv1v2intersection__vert_return.writeAction(f"yield_terminate") 
  tranv1v2intersection__vert_return.writeAction(f"__if_vert_return_23_post: bne X12 X18 __if_vert_return_26_post") 
  tranv1v2intersection__vert_return.writeAction(f"__if_vert_return_24_true: movlr 208(X19) X24 0 8") 
  tranv1v2intersection__vert_return.writeAction(f"bleu X24 X12 __if_vert_return_28_false") 
  tranv1v2intersection__vert_return.writeAction(f"__if_vert_return_27_true: movir X24 1") 
  tranv1v2intersection__vert_return.writeAction(f"jmp __if_vert_return_29_post") 
  tranv1v2intersection__vert_return.writeAction(f"__if_vert_return_28_false: movir X24 0") 
  tranv1v2intersection__vert_return.writeAction(f"__if_vert_return_29_post: movlr 8(X19) X23 0 8") 
  tranv1v2intersection__vert_return.writeAction(f"movlr 216(X19) X25 0 8") 
  tranv1v2intersection__vert_return.writeAction(f"movir X26 -1") 
  tranv1v2intersection__vert_return.writeAction(f"sri X26 X26 1") 
  tranv1v2intersection__vert_return.writeAction(f"sendr_wcont X23 X26 X25 X24") 
  tranv1v2intersection__vert_return.writeAction(f"yield_terminate") 
  tranv1v2intersection__vert_return.writeAction(f"__if_vert_return_26_post: movrl X10 40(X19) 0 8") 
  tranv1v2intersection__vert_return.writeAction(f"movrl X8 56(X19) 0 8") 
  tranv1v2intersection__vert_return.writeAction(f"addi X19 X24 32") 
  tranv1v2intersection__vert_return.writeAction(f"evi X2 X23 v1v2intersection::intersect_lists 1") 
  tranv1v2intersection__vert_return.writeAction(f"send_wcont X23 X23 X24 4") 
  tranv1v2intersection__vert_return.writeAction(f"movir X18 0") 
  tranv1v2intersection__vert_return.writeAction(f"movir X22 0") 
  tranv1v2intersection__vert_return.writeAction(f"jmp __if_vert_return_11_post") 
  tranv1v2intersection__vert_return.writeAction(f"__if_vert_return_10_false: addi X11 X18 0") 
  tranv1v2intersection__vert_return.writeAction(f"addi X12 X22 0") 
  tranv1v2intersection__vert_return.writeAction(f"movrl X10 32(X19) 0 8") 
  tranv1v2intersection__vert_return.writeAction(f"movrl X8 48(X19) 0 8") 
  tranv1v2intersection__vert_return.writeAction(f"yield") 
  ## // save neighbor ptr

  ## lmbuff[PTRA + abreturn_count] = op2;

  ## // save degree

  ## lmbuff[SIZEA + abreturn_count] = op0;

  ## abreturn_count = abreturn_count + 1;

  ## if(abreturn_count == 2){

  ##     // launch intersection

  ##     long* local int_addr = lmbuff + (PTRA << 3); 

  ##     long evword = evw_update_event(CEVNT, intersect_lists);

  ##     send_event(evword, int_addr, 4, evword);

  ## }else{

  ##     yield; 

  ## }

  tranv1v2intersection__vert_return.writeAction(f"__if_vert_return_11_post: yield") 
  
  ## size_a, size_b, ptr_a, ptr_b, lm_offset
  ## return -1 if not enough size was available  -- master should relaunch
  ## size per intersection - 8 words, ptr_a, ptr_b
  # Writing code for event v1v2intersection::intersect_lists
  tranv1v2intersection__intersect_lists = efa.writeEvent('v1v2intersection::intersect_lists')
  tranv1v2intersection__intersect_lists.writeAction(f"__entry: send_dmlm_ld_wret X8 v1v2intersection::lista_ret_1 8 X24") 
  tranv1v2intersection__intersect_lists.writeAction(f"send_dmlm_ld_wret X9 v1v2intersection::listb_ret_1 8 X24") 
  tranv1v2intersection__intersect_lists.writeAction(f"movir X16 2") 
  tranv1v2intersection__intersect_lists.writeAction(f"yield") 
  
  # Writing code for event v1v2intersection::lista_ret_1
  tranv1v2intersection__lista_ret_1 = efa.writeEvent('v1v2intersection::lista_ret_1')
  ## Update the return count

  tranv1v2intersection__lista_ret_1.writeAction(f"__entry: movir X24 8") 
  tranv1v2intersection__lista_ret_1.writeAction(f"subi X16 X16 1") 
  ## Get the num ops

  ## long* local a_addr = lmbuff + (CURRA * 8); 

  tranv1v2intersection__lista_ret_1.writeAction(f"bcpyol X8 X20 X24") 
  tranv1v2intersection__lista_ret_1.writeAction(f"bnei X16 0 __if_lista_ret_1_2_post") 
  tranv1v2intersection__lista_ret_1.writeAction(f"__if_lista_ret_1_0_true: evi X2 X24 v1v2intersection::intersect_ab 1") 
  tranv1v2intersection__lista_ret_1.writeAction(f"sendr_wcont X24 X24 X16 X16") 
  tranv1v2intersection__lista_ret_1.writeAction(f"__if_lista_ret_1_2_post: yield") 
  
  # Writing code for event v1v2intersection::listb_ret_1
  tranv1v2intersection__listb_ret_1 = efa.writeEvent('v1v2intersection::listb_ret_1')
  ## Update the return count

  tranv1v2intersection__listb_ret_1.writeAction(f"__entry: movir X24 8") 
  tranv1v2intersection__listb_ret_1.writeAction(f"subi X16 X16 1") 
  ## Get the num ops

  ## long* local b_addr = lmbuff + (CURRB * 8);

  tranv1v2intersection__listb_ret_1.writeAction(f"bcpyol X8 X21 X24") 
  tranv1v2intersection__listb_ret_1.writeAction(f"bnei X16 0 __if_listb_ret_1_2_post") 
  tranv1v2intersection__listb_ret_1.writeAction(f"__if_listb_ret_1_0_true: evi X2 X24 v1v2intersection::intersect_ab 1") 
  tranv1v2intersection__listb_ret_1.writeAction(f"sendr_wcont X24 X24 X16 X16") 
  tranv1v2intersection__listb_ret_1.writeAction(f"__if_listb_ret_1_2_post: yield") 
  
  # Writing code for event v1v2intersection::intersect_ab
  tranv1v2intersection__intersect_ab = efa.writeEvent('v1v2intersection::intersect_ab')
  ## long* local alist = lmbuff + (CURRA * 8); 

  ## long* local blist = lmbuff + (CURRB * 8); 

  tranv1v2intersection__intersect_ab.writeAction(f"__entry: movlr 48(X19) X24 0 8") 
  tranv1v2intersection__intersect_ab.writeAction(f"movlr 56(X19) X23 0 8") 
  tranv1v2intersection__intersect_ab.writeAction(f"movlr 16(X19) X25 0 8") 
  tranv1v2intersection__intersect_ab.writeAction(f"movlr 24(X19) X26 0 8") 
  tranv1v2intersection__intersect_ab.writeAction(f"sub X24 X25 X27") 
  ## if rem (loc_tc) < 8 then that's all that's remaining

  tranv1v2intersection__intersect_ab.writeAction(f"blei X27 8 __if_intersect_ab_1_false") 
  tranv1v2intersection__intersect_ab.writeAction(f"__if_intersect_ab_0_true: movir X24 8") 
  tranv1v2intersection__intersect_ab.writeAction(f"jmp __if_intersect_ab_2_post") 
  tranv1v2intersection__intersect_ab.writeAction(f"__if_intersect_ab_1_false: addi X27 X24 0") 
  tranv1v2intersection__intersect_ab.writeAction(f"__if_intersect_ab_2_post: sub X23 X26 X27") 
  tranv1v2intersection__intersect_ab.writeAction(f"blei X27 8 __if_intersect_ab_4_false") 
  tranv1v2intersection__intersect_ab.writeAction(f"__if_intersect_ab_3_true: movir X23 8") 
  tranv1v2intersection__intersect_ab.writeAction(f"jmp __if_intersect_ab_5_post") 
  tranv1v2intersection__intersect_ab.writeAction(f"__if_intersect_ab_4_false: addi X27 X23 0") 
  tranv1v2intersection__intersect_ab.writeAction(f"__if_intersect_ab_5_post: movir X27 0") 
  ## tmp reg iter_a = threshold, iter_b = end (0)

  tranv1v2intersection__intersect_ab.writeAction(f"movlr 208(X19) X25 0 8") 
  tranv1v2intersection__intersect_ab.writeAction(f"movir X26 0") 
  ## else walk through the two lists simultaeously

  tranv1v2intersection__intersect_ab.writeAction(f"__while_intersect_ab_6_condition: clt X17 X24 X28") 
  tranv1v2intersection__intersect_ab.writeAction(f"clt X18 X23 X29") 
  tranv1v2intersection__intersect_ab.writeAction(f"and X28 X29 X28") 
  tranv1v2intersection__intersect_ab.writeAction(f"beqi X28 0 __while_intersect_ab_8_post") 
  tranv1v2intersection__intersect_ab.writeAction(f"__while_intersect_ab_7_body: movwlr X20(X17,0,0) X28") 
  tranv1v2intersection__intersect_ab.writeAction(f"movwlr X21(X18,0,0) X29") 
  tranv1v2intersection__intersect_ab.writeAction(f"bgt X25 X28 __if_intersect_ab_10_false") 
  tranv1v2intersection__intersect_ab.writeAction(f"__if_intersect_ab_9_true: movir X26 1") 
  tranv1v2intersection__intersect_ab.writeAction(f"addi X24 X17 0") 
  tranv1v2intersection__intersect_ab.writeAction(f"jmp __if_intersect_ab_11_post") 
  tranv1v2intersection__intersect_ab.writeAction(f"__if_intersect_ab_10_false: bgt X25 X29 __if_intersect_ab_13_false") 
  tranv1v2intersection__intersect_ab.writeAction(f"__if_intersect_ab_12_true: movir X26 1") 
  tranv1v2intersection__intersect_ab.writeAction(f"addi X24 X17 0") 
  tranv1v2intersection__intersect_ab.writeAction(f"jmp __if_intersect_ab_11_post") 
  tranv1v2intersection__intersect_ab.writeAction(f"__if_intersect_ab_13_false: ble X29 X28 __if_intersect_ab_16_false") 
  tranv1v2intersection__intersect_ab.writeAction(f"__if_intersect_ab_15_true: addi X17 X17 1") 
  tranv1v2intersection__intersect_ab.writeAction(f"jmp __if_intersect_ab_11_post") 
  tranv1v2intersection__intersect_ab.writeAction(f"__if_intersect_ab_16_false: ble X28 X29 __if_intersect_ab_19_false") 
  tranv1v2intersection__intersect_ab.writeAction(f"__if_intersect_ab_18_true: addi X18 X18 1") 
  tranv1v2intersection__intersect_ab.writeAction(f"jmp __if_intersect_ab_11_post") 
  tranv1v2intersection__intersect_ab.writeAction(f"__if_intersect_ab_19_false: addi X27 X27 1") 
  tranv1v2intersection__intersect_ab.writeAction(f"addi X17 X17 1") 
  tranv1v2intersection__intersect_ab.writeAction(f"addi X18 X18 1") 
  tranv1v2intersection__intersect_ab.writeAction(f"__if_intersect_ab_11_post: jmp __while_intersect_ab_6_condition") 
  ## update the loc tc

  tranv1v2intersection__intersect_ab.writeAction(f"__while_intersect_ab_8_post: add X22 X27 X22") 
  ## if intersect result > v0 (symmetric break), end

  tranv1v2intersection__intersect_ab.writeAction(f"bnei X26 1 __if_intersect_ab_23_post") 
  tranv1v2intersection__intersect_ab.writeAction(f"__if_intersect_ab_21_true: movlr 8(X19) X27 0 8") 
  ## lmbuff = LMBASE;

  ## lmbuff[TOP_FLAG_OFFSET] = 1;

  tranv1v2intersection__intersect_ab.writeAction(f"movlr 216(X19) X29 0 8") 
  tranv1v2intersection__intersect_ab.writeAction(f"movir X28 -1") 
  tranv1v2intersection__intersect_ab.writeAction(f"sri X28 X28 1") 
  tranv1v2intersection__intersect_ab.writeAction(f"sendr_wcont X27 X28 X29 X22") 
  tranv1v2intersection__intersect_ab.writeAction(f"yield_terminate") 
  ## one or both the lists exited --> whichever did fetch that

  ## update iter by how much ever was processed 

  ## check for bounds and fetch

  ## retain offs of the other one 

  tranv1v2intersection__intersect_ab.writeAction(f"__if_intersect_ab_23_post: bne X17 X24 __if_intersect_ab_26_post") 
  tranv1v2intersection__intersect_ab.writeAction(f"__if_intersect_ab_24_true: movlr 48(X19) X27 0 8") 
  tranv1v2intersection__intersect_ab.writeAction(f"movlr 16(X19) X25 0 8") 
  tranv1v2intersection__intersect_ab.writeAction(f"add X25 X24 X25") 
  tranv1v2intersection__intersect_ab.writeAction(f"bgt X27 X25 __if_intersect_ab_26_post") 
  tranv1v2intersection__intersect_ab.writeAction(f"__if_intersect_ab_27_true: movlr 8(X19) X29 0 8") 
  tranv1v2intersection__intersect_ab.writeAction(f"movlr 216(X19) X27 0 8") 
  tranv1v2intersection__intersect_ab.writeAction(f"movir X28 -1") 
  tranv1v2intersection__intersect_ab.writeAction(f"sri X28 X28 1") 
  tranv1v2intersection__intersect_ab.writeAction(f"sendr_wcont X29 X28 X27 X22") 
  ## lmbuff = LMBASE;

  ## iter_a = 1;

  ## lmbuff[TOP_FLAG_OFFSET] = iter_a;

  tranv1v2intersection__intersect_ab.writeAction(f"yield_terminate") 
  tranv1v2intersection__intersect_ab.writeAction(f"__if_intersect_ab_26_post: bne X18 X23 __if_intersect_ab_32_post") 
  tranv1v2intersection__intersect_ab.writeAction(f"__if_intersect_ab_30_true: movlr 24(X19) X26 0 8") 
  tranv1v2intersection__intersect_ab.writeAction(f"movlr 56(X19) X27 0 8") 
  tranv1v2intersection__intersect_ab.writeAction(f"add X26 X23 X26") 
  tranv1v2intersection__intersect_ab.writeAction(f"bgt X27 X26 __if_intersect_ab_32_post") 
  tranv1v2intersection__intersect_ab.writeAction(f"__if_intersect_ab_33_true: movlr 8(X19) X29 0 8") 
  tranv1v2intersection__intersect_ab.writeAction(f"movlr 216(X19) X27 0 8") 
  tranv1v2intersection__intersect_ab.writeAction(f"movir X28 -1") 
  tranv1v2intersection__intersect_ab.writeAction(f"sri X28 X28 1") 
  tranv1v2intersection__intersect_ab.writeAction(f"sendr_wcont X29 X28 X27 X22") 
  ## lmbuff = LMBASE;

  ## iter_a = 1;

  ## lmbuff[TOP_FLAG_OFFSET] = iter_a;

  tranv1v2intersection__intersect_ab.writeAction(f"yield_terminate") 
  tranv1v2intersection__intersect_ab.writeAction(f"__if_intersect_ab_32_post: bne X17 X24 __if_intersect_ab_38_post") 
  tranv1v2intersection__intersect_ab.writeAction(f"__if_intersect_ab_36_true: movlr 32(X19) X24 0 8") 
  tranv1v2intersection__intersect_ab.writeAction(f"sli X25 X27 3") 
  tranv1v2intersection__intersect_ab.writeAction(f"add X24 X27 X24") 
  tranv1v2intersection__intersect_ab.writeAction(f"send_dmlm_ld_wret X24 v1v2intersection::lista_ret_1 8 X27") 
  tranv1v2intersection__intersect_ab.writeAction(f"movrl X25 16(X19) 0 8") 
  tranv1v2intersection__intersect_ab.writeAction(f"movir X17 0") 
  tranv1v2intersection__intersect_ab.writeAction(f"addi X16 X16 1") 
  tranv1v2intersection__intersect_ab.writeAction(f"__if_intersect_ab_38_post: bne X18 X23 __if_intersect_ab_41_post") 
  tranv1v2intersection__intersect_ab.writeAction(f"__if_intersect_ab_39_true: movlr 40(X19) X23 0 8") 
  tranv1v2intersection__intersect_ab.writeAction(f"sli X26 X25 3") 
  tranv1v2intersection__intersect_ab.writeAction(f"add X23 X25 X23") 
  tranv1v2intersection__intersect_ab.writeAction(f"send_dmlm_ld_wret X23 v1v2intersection::listb_ret_1 8 X25") 
  tranv1v2intersection__intersect_ab.writeAction(f"movrl X26 24(X19) 0 8") 
  tranv1v2intersection__intersect_ab.writeAction(f"movir X18 0") 
  tranv1v2intersection__intersect_ab.writeAction(f"addi X16 X16 1") 
  tranv1v2intersection__intersect_ab.writeAction(f"__if_intersect_ab_41_post: yield") 
  