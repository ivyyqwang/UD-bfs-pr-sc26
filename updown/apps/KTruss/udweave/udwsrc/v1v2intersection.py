from linker.EFAProgram import efaProgram

## UDWeave version: unknown

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
  ## Scoped Variable "add_event" uses Register X23, scope (0)
  ## #define DEBUG
  ## This is all metadata information
  ## Each threads in the same lane shared the following scratchpad
  ## #define TOP_TC_OUTPUT 1
  ## send buffer 4 - 13 (9 words)
  ## #define NUM_WRITE 16
  ## #define NUM_INT 18
  ## master, intersection launcher offsets
  ## Each thread's own private scratchpad size: [(THREAD_STATUS << 3) + TID * THREAD_LM_SIZE, (THREAD_STATUS << 3) + (TID+1) * THREAD_LM_SIZE]
  ## thread offsets (total space = 28*8 = 224 bytes)
  ## #define MIN_VID 4
  ## #define MAX_VID 6
  
  ######################################################
  ###### Writing code for thread v1v2intersection ######
  ######################################################
  ## unsigned long va_addr;
  ## unsigned long vb_addr;
  # Writing code for event v1v2intersection::launch
  tranv1v2intersection__launch = efa.writeEvent('v1v2intersection::launch')
  ## fetch v1 and v2

  ## print("[NWID %lu] Intersection offset_id:%lu, v1:%lu v2:%lu threshold:%lu", re_netid, offset_id, v1, v2, threshold);

  tranv1v2intersection__launch.writeAction(f"__entry: movir X24 2000") 
  tranv1v2intersection__launch.writeAction(f"muli X8 X25 232") 
  tranv1v2intersection__launch.writeAction(f"add X25 X24 X25") 
  tranv1v2intersection__launch.writeAction(f"add X7 X25 X19") 
  ## print("NWID %lu] lmbuff = %lu", NETID ,lmbuff);

  tranv1v2intersection__launch.writeAction(f"movir X22 0") 
  tranv1v2intersection__launch.writeAction(f"movrl X1 0(X19) 0 8") 
  tranv1v2intersection__launch.writeAction(f"movrl X12 200(X19) 0 8") 
  tranv1v2intersection__launch.writeAction(f"movir X26 0") 
  tranv1v2intersection__launch.writeAction(f"movrl X26 8(X19) 0 8") 
  tranv1v2intersection__launch.writeAction(f"movir X26 0") 
  tranv1v2intersection__launch.writeAction(f"movrl X26 16(X19) 0 8") 
  tranv1v2intersection__launch.writeAction(f"movrl X13 208(X19) 0 8") 
  tranv1v2intersection__launch.writeAction(f"movir X16 0") 
  tranv1v2intersection__launch.writeAction(f"movir X17 0") 
  tranv1v2intersection__launch.writeAction(f"movir X18 0") 
  tranv1v2intersection__launch.writeAction(f"movrl X14 216(X19) 0 8") 
  tranv1v2intersection__launch.writeAction(f"movrl X8 224(X19) 0 8") 
  tranv1v2intersection__launch.writeAction(f"sli X10 X26 6") 
  tranv1v2intersection__launch.writeAction(f"add X9 X26 X26") 
  tranv1v2intersection__launch.writeAction(f"send_dmlm_ld_wret X26 v1v2intersection::vert_return 6 X27") 
  tranv1v2intersection__launch.writeAction(f"sli X11 X27 6") 
  tranv1v2intersection__launch.writeAction(f"add X9 X27 X26") 
  tranv1v2intersection__launch.writeAction(f"send_dmlm_ld_wret X26 v1v2intersection::vert_return 6 X27") 
  tranv1v2intersection__launch.writeAction(f"addi X19 X20 56") 
  tranv1v2intersection__launch.writeAction(f"addi X19 X21 128") 
  tranv1v2intersection__launch.writeAction(f"movir X26 65512") 
  tranv1v2intersection__launch.writeAction(f"add X7 X26 X26") 
  tranv1v2intersection__launch.writeAction(f"movlr 0(X26) X24 0 8") 
  tranv1v2intersection__launch.writeAction(f"evi X2 X25 intersection_launcher__add_one 1") 
  tranv1v2intersection__launch.writeAction(f"ev X25 X23 X24 X24 4") 
  tranv1v2intersection__launch.writeAction(f"yield") 
  
  # Writing code for event v1v2intersection::vert_return
  tranv1v2intersection__vert_return = efa.writeEvent('v1v2intersection::vert_return')
  ##0 - deg, 2 - neighlistptr

  ## save nlist

  ## if degree is 0, yield_t

  tranv1v2intersection__vert_return.writeAction(f"__entry: bnei X8 0 __if_vert_return_2_post") 
  tranv1v2intersection__vert_return.writeAction(f"__if_vert_return_0_true: bneiu X16 0 __if_vert_return_4_false") 
  tranv1v2intersection__vert_return.writeAction(f"__if_vert_return_3_true: movir X17 1") 
  tranv1v2intersection__vert_return.writeAction(f"jmp __if_vert_return_2_post") 
  tranv1v2intersection__vert_return.writeAction(f"__if_vert_return_4_false: movlr 0(X19) X24 0 8") 
  tranv1v2intersection__vert_return.writeAction(f"addi X7 X25 32") 
  tranv1v2intersection__vert_return.writeAction(f"movlr 208(X19) X26 0 8") 
  tranv1v2intersection__vert_return.writeAction(f"movrl X26 0(X25) 0 8") 
  tranv1v2intersection__vert_return.writeAction(f"movrl X8 8(X25) 0 8") 
  tranv1v2intersection__vert_return.writeAction(f"movlr 216(X19) X26 0 8") 
  tranv1v2intersection__vert_return.writeAction(f"movrl X26 16(X25) 0 8") 
  tranv1v2intersection__vert_return.writeAction(f"movlr 224(X19) X26 0 8") 
  tranv1v2intersection__vert_return.writeAction(f"movrl X26 24(X25) 0 8") 
  tranv1v2intersection__vert_return.writeAction(f"movrl X8 32(X25) 0 8") 
  tranv1v2intersection__vert_return.writeAction(f"movir X26 -1") 
  tranv1v2intersection__vert_return.writeAction(f"sri X26 X26 1") 
  tranv1v2intersection__vert_return.writeAction(f"send_wcont X24 X26 X25 5") 
  tranv1v2intersection__vert_return.writeAction(f"yield_terminate") 
  tranv1v2intersection__vert_return.writeAction(f"__if_vert_return_2_post: ceqi X16 X24 1") 
  tranv1v2intersection__vert_return.writeAction(f"ceqi X17 X25 1") 
  tranv1v2intersection__vert_return.writeAction(f"and X24 X25 X24") 
  tranv1v2intersection__vert_return.writeAction(f"beqi X24 0 __if_vert_return_8_post") 
  tranv1v2intersection__vert_return.writeAction(f"__if_vert_return_6_true: movlr 0(X19) X24 0 8") 
  tranv1v2intersection__vert_return.writeAction(f"addi X7 X25 32") 
  tranv1v2intersection__vert_return.writeAction(f"movlr 208(X19) X26 0 8") 
  tranv1v2intersection__vert_return.writeAction(f"movrl X26 0(X25) 0 8") 
  tranv1v2intersection__vert_return.writeAction(f"movir X26 0") 
  tranv1v2intersection__vert_return.writeAction(f"movrl X26 8(X25) 0 8") 
  tranv1v2intersection__vert_return.writeAction(f"movrl X26 32(X25) 0 8") 
  tranv1v2intersection__vert_return.writeAction(f"movlr 216(X19) X26 0 8") 
  tranv1v2intersection__vert_return.writeAction(f"movrl X26 16(X25) 0 8") 
  tranv1v2intersection__vert_return.writeAction(f"movlr 224(X19) X26 0 8") 
  tranv1v2intersection__vert_return.writeAction(f"movrl X26 24(X25) 0 8") 
  tranv1v2intersection__vert_return.writeAction(f"movir X26 -1") 
  tranv1v2intersection__vert_return.writeAction(f"sri X26 X26 1") 
  tranv1v2intersection__vert_return.writeAction(f"send_wcont X24 X26 X25 5") 
  tranv1v2intersection__vert_return.writeAction(f"yield_terminate") 
  tranv1v2intersection__vert_return.writeAction(f"__if_vert_return_8_post: addi X16 X16 1") 
  tranv1v2intersection__vert_return.writeAction(f"bneiu X16 2 __if_vert_return_10_false") 
  tranv1v2intersection__vert_return.writeAction(f"__if_vert_return_9_true: bleu X12 X22 __if_vert_return_14_post") 
  tranv1v2intersection__vert_return.writeAction(f"__if_vert_return_12_true: movir X24 0") 
  tranv1v2intersection__vert_return.writeAction(f"movlr 0(X19) X25 0 8") 
  tranv1v2intersection__vert_return.writeAction(f"movlr 208(X19) X26 0 8") 
  tranv1v2intersection__vert_return.writeAction(f"addi X7 X27 32") 
  tranv1v2intersection__vert_return.writeAction(f"movrl X26 0(X27) 0 8") 
  tranv1v2intersection__vert_return.writeAction(f"movrl X24 8(X27) 0 8") 
  tranv1v2intersection__vert_return.writeAction(f"movrl X24 32(X27) 0 8") 
  tranv1v2intersection__vert_return.writeAction(f"movlr 216(X19) X24 0 8") 
  tranv1v2intersection__vert_return.writeAction(f"movrl X24 16(X27) 0 8") 
  tranv1v2intersection__vert_return.writeAction(f"movlr 224(X19) X24 0 8") 
  tranv1v2intersection__vert_return.writeAction(f"movrl X24 24(X27) 0 8") 
  tranv1v2intersection__vert_return.writeAction(f"movir X24 -1") 
  tranv1v2intersection__vert_return.writeAction(f"sri X24 X24 1") 
  tranv1v2intersection__vert_return.writeAction(f"send_wcont X25 X24 X27 5") 
  tranv1v2intersection__vert_return.writeAction(f"yield_terminate") 
  tranv1v2intersection__vert_return.writeAction(f"__if_vert_return_14_post: bneu X12 X22 __if_vert_return_17_post") 
  tranv1v2intersection__vert_return.writeAction(f"__if_vert_return_15_true: movir X25 1") 
  tranv1v2intersection__vert_return.writeAction(f"movlr 0(X19) X27 0 8") 
  tranv1v2intersection__vert_return.writeAction(f"movlr 208(X19) X24 0 8") 
  tranv1v2intersection__vert_return.writeAction(f"addi X7 X26 32") 
  tranv1v2intersection__vert_return.writeAction(f"movrl X24 0(X26) 0 8") 
  tranv1v2intersection__vert_return.writeAction(f"movrl X25 8(X26) 0 8") 
  tranv1v2intersection__vert_return.writeAction(f"movlr 216(X19) X25 0 8") 
  tranv1v2intersection__vert_return.writeAction(f"movrl X25 16(X26) 0 8") 
  tranv1v2intersection__vert_return.writeAction(f"movlr 224(X19) X25 0 8") 
  tranv1v2intersection__vert_return.writeAction(f"movrl X25 24(X26) 0 8") 
  tranv1v2intersection__vert_return.writeAction(f"movir X25 2") 
  tranv1v2intersection__vert_return.writeAction(f"movrl X25 32(X26) 0 8") 
  tranv1v2intersection__vert_return.writeAction(f"movir X28 -1") 
  tranv1v2intersection__vert_return.writeAction(f"sri X28 X28 1") 
  tranv1v2intersection__vert_return.writeAction(f"send_wcont X27 X28 X26 5") 
  tranv1v2intersection__vert_return.writeAction(f"movir X27 -1") 
  tranv1v2intersection__vert_return.writeAction(f"sri X27 X27 1") 
  tranv1v2intersection__vert_return.writeAction(f"sendr_wcont X23 X27 X11 X11") 
  tranv1v2intersection__vert_return.writeAction(f"movlr 40(X19) X27 0 8") 
  tranv1v2intersection__vert_return.writeAction(f"subi X27 X25 1") 
  tranv1v2intersection__vert_return.writeAction(f"sli X25 X24 3") 
  tranv1v2intersection__vert_return.writeAction(f"movlr 120(X19) X25 0 8") 
  tranv1v2intersection__vert_return.writeAction(f"add X25 X24 X25") 
  tranv1v2intersection__vert_return.writeAction(f"movir X24 -1") 
  tranv1v2intersection__vert_return.writeAction(f"sri X24 X24 1") 
  tranv1v2intersection__vert_return.writeAction(f"sendr_wcont X23 X24 X25 X25") 
  ## lmbuff = LMBASE;

  ## temp = lmbuff[NUM_WRITE];

  ## temp = temp + 2;

  ## lmbuff[NUM_WRITE] = temp;

  tranv1v2intersection__vert_return.writeAction(f"yield_terminate") 
  tranv1v2intersection__vert_return.writeAction(f"__if_vert_return_17_post: ble X18 X13 __if_vert_return_20_post") 
  tranv1v2intersection__vert_return.writeAction(f"__if_vert_return_18_true: movir X25 0") 
  tranv1v2intersection__vert_return.writeAction(f"movlr 0(X19) X24 0 8") 
  tranv1v2intersection__vert_return.writeAction(f"movlr 208(X19) X27 0 8") 
  tranv1v2intersection__vert_return.writeAction(f"addi X7 X26 32") 
  tranv1v2intersection__vert_return.writeAction(f"movrl X27 0(X26) 0 8") 
  tranv1v2intersection__vert_return.writeAction(f"movrl X25 8(X26) 0 8") 
  tranv1v2intersection__vert_return.writeAction(f"movrl X25 32(X26) 0 8") 
  tranv1v2intersection__vert_return.writeAction(f"movlr 216(X19) X25 0 8") 
  tranv1v2intersection__vert_return.writeAction(f"movrl X25 16(X26) 0 8") 
  tranv1v2intersection__vert_return.writeAction(f"movlr 224(X19) X25 0 8") 
  tranv1v2intersection__vert_return.writeAction(f"movrl X25 24(X26) 0 8") 
  tranv1v2intersection__vert_return.writeAction(f"movir X25 -1") 
  tranv1v2intersection__vert_return.writeAction(f"sri X25 X25 1") 
  tranv1v2intersection__vert_return.writeAction(f"send_wcont X24 X25 X26 5") 
  tranv1v2intersection__vert_return.writeAction(f"yield_terminate") 
  tranv1v2intersection__vert_return.writeAction(f"__if_vert_return_20_post: bne X13 X18 __if_vert_return_23_post") 
  tranv1v2intersection__vert_return.writeAction(f"__if_vert_return_21_true: movir X24 1") 
  tranv1v2intersection__vert_return.writeAction(f"movlr 0(X19) X26 0 8") 
  tranv1v2intersection__vert_return.writeAction(f"movlr 208(X19) X25 0 8") 
  tranv1v2intersection__vert_return.writeAction(f"addi X7 X27 32") 
  tranv1v2intersection__vert_return.writeAction(f"movrl X25 0(X27) 0 8") 
  tranv1v2intersection__vert_return.writeAction(f"movrl X24 8(X27) 0 8") 
  tranv1v2intersection__vert_return.writeAction(f"movlr 216(X19) X24 0 8") 
  tranv1v2intersection__vert_return.writeAction(f"movrl X24 16(X27) 0 8") 
  tranv1v2intersection__vert_return.writeAction(f"movlr 224(X19) X24 0 8") 
  tranv1v2intersection__vert_return.writeAction(f"movrl X24 24(X27) 0 8") 
  tranv1v2intersection__vert_return.writeAction(f"movir X24 2") 
  tranv1v2intersection__vert_return.writeAction(f"movrl X24 32(X27) 0 8") 
  tranv1v2intersection__vert_return.writeAction(f"movir X28 -1") 
  tranv1v2intersection__vert_return.writeAction(f"sri X28 X28 1") 
  tranv1v2intersection__vert_return.writeAction(f"send_wcont X26 X28 X27 5") 
  tranv1v2intersection__vert_return.writeAction(f"movlr 120(X19) X24 0 8") 
  tranv1v2intersection__vert_return.writeAction(f"movir X26 -1") 
  tranv1v2intersection__vert_return.writeAction(f"sri X26 X26 1") 
  tranv1v2intersection__vert_return.writeAction(f"sendr_wcont X23 X26 X24 X24") 
  tranv1v2intersection__vert_return.writeAction(f"subi X8 X25 1") 
  tranv1v2intersection__vert_return.writeAction(f"sli X25 X25 3") 
  tranv1v2intersection__vert_return.writeAction(f"add X11 X25 X24") 
  tranv1v2intersection__vert_return.writeAction(f"movir X25 -1") 
  tranv1v2intersection__vert_return.writeAction(f"sri X25 X25 1") 
  tranv1v2intersection__vert_return.writeAction(f"sendr_wcont X23 X25 X24 X24") 
  ## lmbuff = LMBASE;

  ## temp = lmbuff[NUM_WRITE];

  ## temp = temp + 2;

  ## lmbuff[NUM_WRITE] = temp;

  tranv1v2intersection__vert_return.writeAction(f"yield_terminate") 
  ## save neighbor ptr

  tranv1v2intersection__vert_return.writeAction(f"__if_vert_return_23_post: movrl X10 32(X19) 0 8") 
  ## save degree

  tranv1v2intersection__vert_return.writeAction(f"movrl X8 48(X19) 0 8") 
  tranv1v2intersection__vert_return.writeAction(f"movrl X11 192(X19) 0 8") 
  ## launch intersection

  tranv1v2intersection__vert_return.writeAction(f"addi X19 X24 24") 
  tranv1v2intersection__vert_return.writeAction(f"evi X2 X25 v1v2intersection::intersect_lists 1") 
  tranv1v2intersection__vert_return.writeAction(f"send_wcont X25 X25 X24 4") 
  tranv1v2intersection__vert_return.writeAction(f"movir X18 0") 
  tranv1v2intersection__vert_return.writeAction(f"movir X22 0") 
  tranv1v2intersection__vert_return.writeAction(f"jmp __if_vert_return_11_post") 
  tranv1v2intersection__vert_return.writeAction(f"__if_vert_return_10_false: addi X12 X18 0") 
  tranv1v2intersection__vert_return.writeAction(f"addi X13 X22 0") 
  ## save neighbor ptr

  tranv1v2intersection__vert_return.writeAction(f"movrl X10 24(X19) 0 8") 
  ## save degree

  tranv1v2intersection__vert_return.writeAction(f"movrl X8 40(X19) 0 8") 
  tranv1v2intersection__vert_return.writeAction(f"movrl X11 120(X19) 0 8") 
  tranv1v2intersection__vert_return.writeAction(f"yield") 
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
  tranv1v2intersection__lista_ret_1.writeAction(f"bneiu X16 0 __if_lista_ret_1_2_post") 
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
  tranv1v2intersection__listb_ret_1.writeAction(f"bneiu X16 0 __if_listb_ret_1_2_post") 
  tranv1v2intersection__listb_ret_1.writeAction(f"__if_listb_ret_1_0_true: evi X2 X24 v1v2intersection::intersect_ab 1") 
  tranv1v2intersection__listb_ret_1.writeAction(f"sendr_wcont X24 X24 X16 X16") 
  tranv1v2intersection__listb_ret_1.writeAction(f"__if_listb_ret_1_2_post: yield") 
  
  # Writing code for event v1v2intersection::intersect_ab
  tranv1v2intersection__intersect_ab = efa.writeEvent('v1v2intersection::intersect_ab')
  ## long* local alist = lmbuff + (CURRA * 8); 

  ## long* local blist = lmbuff + (CURRB * 8); 

  tranv1v2intersection__intersect_ab.writeAction(f"__entry: movlr 40(X19) X24 0 8") 
  tranv1v2intersection__intersect_ab.writeAction(f"movlr 48(X19) X25 0 8") 
  tranv1v2intersection__intersect_ab.writeAction(f"movlr 8(X19) X26 0 8") 
  tranv1v2intersection__intersect_ab.writeAction(f"movlr 16(X19) X27 0 8") 
  tranv1v2intersection__intersect_ab.writeAction(f"sub X24 X26 X16") 
  ## if rem (abreturn_count) < 8 then that's all that's remaining

  tranv1v2intersection__intersect_ab.writeAction(f"bleiu X16 8 __if_intersect_ab_1_false") 
  tranv1v2intersection__intersect_ab.writeAction(f"__if_intersect_ab_0_true: movir X24 8") 
  tranv1v2intersection__intersect_ab.writeAction(f"jmp __if_intersect_ab_2_post") 
  tranv1v2intersection__intersect_ab.writeAction(f"__if_intersect_ab_1_false: addi X16 X24 0") 
  tranv1v2intersection__intersect_ab.writeAction(f"__if_intersect_ab_2_post: sub X25 X27 X16") 
  tranv1v2intersection__intersect_ab.writeAction(f"bleiu X16 8 __if_intersect_ab_4_false") 
  tranv1v2intersection__intersect_ab.writeAction(f"__if_intersect_ab_3_true: movir X25 8") 
  tranv1v2intersection__intersect_ab.writeAction(f"jmp __if_intersect_ab_5_post") 
  tranv1v2intersection__intersect_ab.writeAction(f"__if_intersect_ab_4_false: addi X16 X25 0") 
  ## #ifdef DEBUG        

  ## print("[DEBUG][NWID %lu] <intersect> loc_size_a:%lu loc_size_b:%lu", NETID, loc_size_a, loc_size_b);

  ## #endif

  ## abreturn_count reg iter_a = threshold, iter_b = end (0)

  tranv1v2intersection__intersect_ab.writeAction(f"__if_intersect_ab_5_post: movlr 200(X19) X26 0 8") 
  tranv1v2intersection__intersect_ab.writeAction(f"movir X27 0") 
  ## else walk through the two lists simultaeously

  tranv1v2intersection__intersect_ab.writeAction(f"__while_intersect_ab_6_condition: clt X17 X24 X28") 
  tranv1v2intersection__intersect_ab.writeAction(f"clt X18 X25 X29") 
  tranv1v2intersection__intersect_ab.writeAction(f"and X28 X29 X28") 
  tranv1v2intersection__intersect_ab.writeAction(f"beqi X28 0 __while_intersect_ab_8_post") 
  tranv1v2intersection__intersect_ab.writeAction(f"__while_intersect_ab_7_body: movwlr X20(X17,0,0) X28") 
  tranv1v2intersection__intersect_ab.writeAction(f"movwlr X21(X18,0,0) X29") 
  tranv1v2intersection__intersect_ab.writeAction(f"bgt X26 X28 __if_intersect_ab_10_false") 
  tranv1v2intersection__intersect_ab.writeAction(f"__if_intersect_ab_9_true: movir X27 1") 
  tranv1v2intersection__intersect_ab.writeAction(f"addi X24 X17 0") 
  tranv1v2intersection__intersect_ab.writeAction(f"jmp __if_intersect_ab_11_post") 
  tranv1v2intersection__intersect_ab.writeAction(f"__if_intersect_ab_10_false: bgt X26 X29 __if_intersect_ab_13_false") 
  tranv1v2intersection__intersect_ab.writeAction(f"__if_intersect_ab_12_true: movir X27 1") 
  tranv1v2intersection__intersect_ab.writeAction(f"addi X24 X17 0") 
  tranv1v2intersection__intersect_ab.writeAction(f"jmp __if_intersect_ab_11_post") 
  tranv1v2intersection__intersect_ab.writeAction(f"__if_intersect_ab_13_false: ble X29 X28 __if_intersect_ab_16_false") 
  tranv1v2intersection__intersect_ab.writeAction(f"__if_intersect_ab_15_true: addi X17 X17 1") 
  tranv1v2intersection__intersect_ab.writeAction(f"jmp __if_intersect_ab_11_post") 
  tranv1v2intersection__intersect_ab.writeAction(f"__if_intersect_ab_16_false: ble X28 X29 __if_intersect_ab_19_false") 
  tranv1v2intersection__intersect_ab.writeAction(f"__if_intersect_ab_18_true: addi X18 X18 1") 
  tranv1v2intersection__intersect_ab.writeAction(f"jmp __if_intersect_ab_11_post") 
  tranv1v2intersection__intersect_ab.writeAction(f"__if_intersect_ab_19_false: movlr 120(X19) X16 0 8") 
  tranv1v2intersection__intersect_ab.writeAction(f"sli X17 X30 3") 
  tranv1v2intersection__intersect_ab.writeAction(f"add X16 X30 X16") 
  tranv1v2intersection__intersect_ab.writeAction(f"movir X30 -1") 
  tranv1v2intersection__intersect_ab.writeAction(f"sri X30 X30 1") 
  tranv1v2intersection__intersect_ab.writeAction(f"sendr_wcont X23 X30 X16 X16") 
  tranv1v2intersection__intersect_ab.writeAction(f"movlr 192(X19) X16 0 8") 
  tranv1v2intersection__intersect_ab.writeAction(f"sli X18 X30 3") 
  tranv1v2intersection__intersect_ab.writeAction(f"add X16 X30 X16") 
  tranv1v2intersection__intersect_ab.writeAction(f"movir X30 -1") 
  tranv1v2intersection__intersect_ab.writeAction(f"sri X30 X30 1") 
  tranv1v2intersection__intersect_ab.writeAction(f"sendr_wcont X23 X30 X16 X16") 
  tranv1v2intersection__intersect_ab.writeAction(f"addi X22 X22 1") 
  tranv1v2intersection__intersect_ab.writeAction(f"addi X17 X17 1") 
  tranv1v2intersection__intersect_ab.writeAction(f"addi X18 X18 1") 
  tranv1v2intersection__intersect_ab.writeAction(f"__if_intersect_ab_11_post: jmp __while_intersect_ab_6_condition") 
  ## update the loc tc

  ## #ifdef DEBUG        

  ## print("[DEBUG][NWID %lu] <intersect> loc tc updated:%lu", NETID, tc);

  ## #endif

  ## if intersect result > v0 (symmetric break), end

  tranv1v2intersection__intersect_ab.writeAction(f"__while_intersect_ab_8_post: bnei X27 1 __if_intersect_ab_23_post") 
  tranv1v2intersection__intersect_ab.writeAction(f"__if_intersect_ab_21_true: movlr 0(X19) X28 0 8") 
  tranv1v2intersection__intersect_ab.writeAction(f"movlr 208(X19) X16 0 8") 
  tranv1v2intersection__intersect_ab.writeAction(f"addi X7 X29 32") 
  tranv1v2intersection__intersect_ab.writeAction(f"movrl X16 0(X29) 0 8") 
  tranv1v2intersection__intersect_ab.writeAction(f"movrl X22 8(X29) 0 8") 
  tranv1v2intersection__intersect_ab.writeAction(f"movlr 216(X19) X16 0 8") 
  tranv1v2intersection__intersect_ab.writeAction(f"movrl X16 16(X29) 0 8") 
  tranv1v2intersection__intersect_ab.writeAction(f"movlr 224(X19) X16 0 8") 
  tranv1v2intersection__intersect_ab.writeAction(f"movrl X16 24(X29) 0 8") 
  tranv1v2intersection__intersect_ab.writeAction(f"sli X22 X16 1") 
  tranv1v2intersection__intersect_ab.writeAction(f"movrl X16 32(X29) 0 8") 
  ## print("1 [DEBUG][NWID %lu] <intersect> iter_b == 1", NETID);

  tranv1v2intersection__intersect_ab.writeAction(f"movir X30 -1") 
  tranv1v2intersection__intersect_ab.writeAction(f"sri X30 X30 1") 
  tranv1v2intersection__intersect_ab.writeAction(f"send_wcont X28 X30 X29 5") 
  ## print("2 [DEBUG][NWID %lu] <intersect> iter_b == 1", NETID);

  ## lmbuff = LMBASE;

  ## abreturn_count = lmbuff[NUM_WRITE];

  ## abreturn_count = abreturn_count + (tc << 1);

  ## lmbuff[NUM_WRITE] = abreturn_count;

  tranv1v2intersection__intersect_ab.writeAction(f"yield_terminate") 
  ## one or both the lists exited --> whichever did fetch that

  ## update iter by how much ever was processed 

  ## check for bounds and fetch

  ## retain offs of the other one 

  ## print("offs_a:%lu loc_size_a:%lu offs_b:%lu loc_size_b:%lu", offs_a, loc_size_a, offs_b, loc_size_b);

  tranv1v2intersection__intersect_ab.writeAction(f"__if_intersect_ab_23_post: bne X17 X24 __if_intersect_ab_26_post") 
  ## listA end

  tranv1v2intersection__intersect_ab.writeAction(f"__if_intersect_ab_24_true: movlr 40(X19) X28 0 8") 
  tranv1v2intersection__intersect_ab.writeAction(f"movlr 8(X19) X26 0 8") 
  tranv1v2intersection__intersect_ab.writeAction(f"add X26 X24 X26") 
  ## print("iter_a = %lu, loc_size=%lu", iter_a, loc_size);

  tranv1v2intersection__intersect_ab.writeAction(f"bgt X28 X26 __if_intersect_ab_26_post") 
  tranv1v2intersection__intersect_ab.writeAction(f"__if_intersect_ab_27_true: movlr 0(X19) X26 0 8") 
  tranv1v2intersection__intersect_ab.writeAction(f"movlr 208(X19) X28 0 8") 
  tranv1v2intersection__intersect_ab.writeAction(f"movlr 216(X19) X16 0 8") 
  tranv1v2intersection__intersect_ab.writeAction(f"addi X7 X29 32") 
  tranv1v2intersection__intersect_ab.writeAction(f"movrl X28 0(X29) 0 8") 
  tranv1v2intersection__intersect_ab.writeAction(f"movrl X22 8(X29) 0 8") 
  tranv1v2intersection__intersect_ab.writeAction(f"movrl X16 16(X29) 0 8") 
  tranv1v2intersection__intersect_ab.writeAction(f"movlr 224(X19) X28 0 8") 
  tranv1v2intersection__intersect_ab.writeAction(f"movrl X28 24(X29) 0 8") 
  tranv1v2intersection__intersect_ab.writeAction(f"sli X22 X28 1") 
  tranv1v2intersection__intersect_ab.writeAction(f"movrl X28 32(X29) 0 8") 
  tranv1v2intersection__intersect_ab.writeAction(f"movir X30 -1") 
  tranv1v2intersection__intersect_ab.writeAction(f"sri X30 X30 1") 
  tranv1v2intersection__intersect_ab.writeAction(f"send_wcont X26 X30 X29 5") 
  ## #ifdef DEBUG        

  ## print("Terminate since lista is done");

  ## #endif

  ## lmbuff = LMBASE;

  ## abreturn_count = lmbuff[NUM_WRITE];

  ## abreturn_count = abreturn_count + (tc << 1);

  ## lmbuff[NUM_WRITE] = abreturn_count;

  tranv1v2intersection__intersect_ab.writeAction(f"yield_terminate") 
  tranv1v2intersection__intersect_ab.writeAction(f"__if_intersect_ab_26_post: bne X18 X25 __if_intersect_ab_32_post") 
  tranv1v2intersection__intersect_ab.writeAction(f"__if_intersect_ab_30_true: movlr 16(X19) X27 0 8") 
  tranv1v2intersection__intersect_ab.writeAction(f"movlr 48(X19) X28 0 8") 
  tranv1v2intersection__intersect_ab.writeAction(f"add X27 X25 X27") 
  ## print("iter_b = %lu, loc_size=%lu", iter_b, loc_size);

  tranv1v2intersection__intersect_ab.writeAction(f"bgt X28 X27 __if_intersect_ab_32_post") 
  tranv1v2intersection__intersect_ab.writeAction(f"__if_intersect_ab_33_true: movlr 0(X19) X27 0 8") 
  tranv1v2intersection__intersect_ab.writeAction(f"movlr 208(X19) X28 0 8") 
  tranv1v2intersection__intersect_ab.writeAction(f"movlr 216(X19) X16 0 8") 
  tranv1v2intersection__intersect_ab.writeAction(f"addi X7 X29 32") 
  tranv1v2intersection__intersect_ab.writeAction(f"movrl X28 0(X29) 0 8") 
  tranv1v2intersection__intersect_ab.writeAction(f"movrl X22 8(X29) 0 8") 
  tranv1v2intersection__intersect_ab.writeAction(f"movrl X16 16(X29) 0 8") 
  tranv1v2intersection__intersect_ab.writeAction(f"movlr 224(X19) X28 0 8") 
  tranv1v2intersection__intersect_ab.writeAction(f"movrl X28 24(X29) 0 8") 
  tranv1v2intersection__intersect_ab.writeAction(f"sli X22 X28 1") 
  tranv1v2intersection__intersect_ab.writeAction(f"movrl X28 32(X29) 0 8") 
  tranv1v2intersection__intersect_ab.writeAction(f"movir X30 -1") 
  tranv1v2intersection__intersect_ab.writeAction(f"sri X30 X30 1") 
  tranv1v2intersection__intersect_ab.writeAction(f"send_wcont X27 X30 X29 5") 
  ## #ifdef DEBUG        

  ## print("Terminate since listb is done");

  ## #endif

  ## lmbuff = LMBASE;

  ## abreturn_count = lmbuff[NUM_WRITE];

  ## abreturn_count = abreturn_count + (tc << 1);

  ## lmbuff[NUM_WRITE] = abreturn_count;

  tranv1v2intersection__intersect_ab.writeAction(f"yield_terminate") 
  tranv1v2intersection__intersect_ab.writeAction(f"__if_intersect_ab_32_post: movir X16 0") 
  tranv1v2intersection__intersect_ab.writeAction(f"bne X17 X24 __if_intersect_ab_38_post") 
  tranv1v2intersection__intersect_ab.writeAction(f"__if_intersect_ab_36_true: movlr 24(X19) X24 0 8") 
  tranv1v2intersection__intersect_ab.writeAction(f"sli X26 X28 3") 
  tranv1v2intersection__intersect_ab.writeAction(f"add X24 X28 X24") 
  tranv1v2intersection__intersect_ab.writeAction(f"send_dmlm_ld_wret X24 v1v2intersection::lista_ret_1 8 X28") 
  tranv1v2intersection__intersect_ab.writeAction(f"movrl X26 8(X19) 0 8") 
  tranv1v2intersection__intersect_ab.writeAction(f"addi X16 X16 1") 
  tranv1v2intersection__intersect_ab.writeAction(f"movlr 120(X19) X17 0 8") 
  tranv1v2intersection__intersect_ab.writeAction(f"addi X17 X17 64") 
  tranv1v2intersection__intersect_ab.writeAction(f"movrl X17 120(X19) 0 8") 
  tranv1v2intersection__intersect_ab.writeAction(f"movir X17 0") 
  ## print("lista_ret_1 0x%lx 0x%lx", lmbuff[PTRA], local_ptr);

  tranv1v2intersection__intersect_ab.writeAction(f"__if_intersect_ab_38_post: bne X18 X25 __if_intersect_ab_41_post") 
  tranv1v2intersection__intersect_ab.writeAction(f"__if_intersect_ab_39_true: movlr 32(X19) X25 0 8") 
  tranv1v2intersection__intersect_ab.writeAction(f"sli X27 X26 3") 
  tranv1v2intersection__intersect_ab.writeAction(f"add X25 X26 X25") 
  tranv1v2intersection__intersect_ab.writeAction(f"send_dmlm_ld_wret X25 v1v2intersection::listb_ret_1 8 X26") 
  tranv1v2intersection__intersect_ab.writeAction(f"movrl X27 16(X19) 0 8") 
  tranv1v2intersection__intersect_ab.writeAction(f"addi X16 X16 1") 
  tranv1v2intersection__intersect_ab.writeAction(f"movlr 192(X19) X18 0 8") 
  tranv1v2intersection__intersect_ab.writeAction(f"addi X18 X18 64") 
  tranv1v2intersection__intersect_ab.writeAction(f"movrl X18 192(X19) 0 8") 
  tranv1v2intersection__intersect_ab.writeAction(f"movir X18 0") 
  ## print("lista_ret_2 0x%lx 0x%lx", lmbuff[PTRB], local_ptr);

  tranv1v2intersection__intersect_ab.writeAction(f"__if_intersect_ab_41_post: yield") 
  