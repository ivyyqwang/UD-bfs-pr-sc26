from linker.EFAProgram import efaProgram

## UDWeave version: 7808cc0 (2026-04-24)

## Global constants

@efaProgram
def EFA_markVertices(efa):
  efa.code_level = 'machine'
  state0 = efa.State("udweave_init") #Only one state code 
  efa.add_initId(state0.state_id)
  ## Static declarations
  ## Scoped Variable "srcBase" uses Register X16, scope (0)
  ## Scoped Variable "numVertices" uses Register X17, scope (0)
  ## Scoped Variable "k" uses Register X18, scope (0)
  ## Scoped Variable "reqInFlight" uses Register X19, scope (0)
  ## Scoped Variable "numEmpty" uses Register X20, scope (0)
  ## =============================================================================
  ## kcore.udwh — Header/macros for the K-Core UpDown accelerator kernel
  ## =============================================================================
  ##
  ## This header defines constants, memory layout, and utility macros used by
  ## kcore.udw. It establishes:
  ##   1. Scratchpad memory layout (how the lane's 64KB local memory is partitioned)
  ##   2. Vertex struct size and work-balancing parameters
  ##   3. Lane encoding helpers (FAKE_SPREAD/COMBINE_LANES)
  ##   4. Child-data management macros (for tracking sub-tasks in the split tree)
  ##   5. Batched DRAM read macros (array_loadN) for reading neighbor vertex data
  ##   6. Assert macros for debugging
  ##
  ## MEMORY LAYOUT (per-lane scratchpad):
  ## ┌──────────────────────────────────┐  offset 0
  ## │  TOP_FLAG_OFFSET (1 word)        │  ← EXIT writes 1 here to signal TOP
  ## │  ... (reserved/unused) ...       │
  ## ├──────────────────────────────────┤  offset HEAP_OFFSET (1600)
  ## │  ... (64 bytes gap) ...          │
  ## ├──────────────────────────────────┤  offset HEAP_OFFSET+64 = 1664
  ## │  args_scratch_space (128 bytes)  │  ← temp buffer for building event args
  ## ├──────────────────────────────────┤  offset HEAP_OFFSET+64+128 = 1792
  ## │  ... (128 bytes gap) ...         │
  ## ├──────────────────────────────────┤  offset HEAP_OFFSET+64+128+128 = 1920
  ## │  child_data_location             │  ← per-thread child tracking data
  ## │  (indexed by TID * DATA_PER_THREAD)
  ## └──────────────────────────────────┘
  ##
  ## TOP also reads back results from the scratchpad after each iteration:
  ##   - HEAP_OFFSET+64   (offset 1664): max_delta (double) — max score change
  ##   - HEAP_OFFSET+80   (offset 1680): next_thread_id — event word for run_iter
  ##
  ## VERTEX STRUCT IN DRAM (vertex_size = 64 bytes = 8 words of 8 bytes):
  ##   offset  0: dests       — pointer to neighbor list in DRAM
  ##   offset  8: degree      — edge count (set to 0 when vertex is deleted)
  ##   offset 16: edges_before— cumulative edges before this vertex (for splitting)
  ##   offset 24: vertex_id   — this vertex's ID
  ##   offset 32: scratch1    — current iteration score (as double)
  ##   offset 40: scratch2    — previous iteration score / orig_score (as double)
  ##   offset 48: scratch3    — iteration number
  ##   offset 56: scratch4    — unused
  ##
  ## =============================================================================
  ## ---------------------------------------------------------------------------
  ## Scratchpad layout constants
  ## ---------------------------------------------------------------------------
  ## Offset in scratchpad where EXIT writes a 1 to signal the TOP (host) core
  ## that the UpDown program has finished the current iteration.
  ## Start of the heap region in scratchpad. Below this is reserved for
  ## system use (thread state, etc.). The usable scratch area begins here.
  ## ---------------------------------------------------------------------------
  ## Data structure sizes and work-balancing parameters
  ## ---------------------------------------------------------------------------
  ## Bytes of scratchpad reserved per thread for child tracking data.
  ## Used by the 8-way splitter (split_vertexsKCORE_MULTI) which has up to
  ## 8 children, each needing 3 words (24 bytes) → 8*3 = 24 words, but
  ## rounded up to 30 words * 8 bytes = 240 bytes per thread.
  ## 8 children each with three words of data each taking 8 bytes
  ## can also be 6 children each with 4 words of data each taking 8 bytes
  ## can also be 6 childen with 5 words each
  ## Size of one vertex_t struct in bytes: 8 fields * 8 bytes each = 64 bytes.
  ## Used for pointer arithmetic when iterating through the vertex array in DRAM.
  ## Weight factor for vertices (vs edges) when computing proportional lane
  ## allocation. Total work for a region = VERTEX_WORK_FACTOR * N + M, where
  ## N = number of vertices, M = number of edges. This accounts for per-vertex
  ## overhead (reading the struct, writing results) beyond just edge processing.
  ## For the first FORCE_FIRST_NODE levels of recursion in the split tree,
  ## force the lane target to stay within the first 2048 logical lanes
  ## (via modulo). This helps ensure initial splits spread across nodes
  ## before going deeper.
  ## Maximum number of outstanding (in-flight) DRAM read requests when reading
  ## a vertex's neighbor list. Limits memory pressure by not issuing all reads
  ## at once for high-degree vertices. Each read fetches 8 neighbor IDs (64 bytes).
  ## ---------------------------------------------------------------------------
  ## Scratchpad pointer macros
  ## ---------------------------------------------------------------------------
  ## Pointer to a temporary argument buffer in scratchpad, used to build
  ## event argument arrays before calling send_event(). Located at
  ## LMBASE + HEAP_OFFSET + 64 = LMBASE + 1664. Has room for ~16 words (128 bytes).
  ## This is also where TOP reads back results:
  ##   args[0] at offset 1664 = max_delta
  ##   args[2] at offset 1680 = next_thread_id (TID for run_iter)
  ## Pointer to the per-thread child data region in scratchpad.
  ## Located at LMBASE + 1920. Each thread uses TID * DATA_PER_THREAD bytes.
  ## Stores child event words, edge counts, scores, etc. for the 8-way and
  ## binary splitters and the multi-vertex-per-lane processor.
  ## ---------------------------------------------------------------------------
  ## Lane encoding macros
  ## ---------------------------------------------------------------------------
  ## The UpDown network ID encodes which lane to target. These macros convert
  ## between a "logical lane count" and the actual network ID encoding.
  ## FAKE_SPREAD_LANES: converts a lane count to the network-ID-scaled value
  ##   (left-shift by 5, i.e., multiply by 32)
  ## FAKE_COMBINE_LANES: converts a network-ID-scaled value back to a lane index
  ##   (right-shift by 5, i.e., divide by 32)
  ## These are used when computing target lane IDs for evw_new().
  ## Threshold for choosing between the 8-way splitter and the binary splitter.
  ## If num_lanes > SWITCH_TO_SPLIT_2 (expressed in FAKE_SPREAD form), use the
  ## 8-way splitter (split_vertexsKCORE_MULTI); otherwise use the binary
  ## splitter (split_vertexs2KCORE_MULTI).
  ## ---------------------------------------------------------------------------
  ## Assert macros for debugging
  ## ---------------------------------------------------------------------------
  ## When ENABLE_ASSERTS == 1, these macros check conditions and crash via
  ## divide-by-zero (divi X16 X16 0) if violated, printing a diagnostic message.
  ## When disabled, they compile to empty if(1){} blocks (zero overhead due to
  ## UDWeave's if(1) optimization).
  ## ---------------------------------------------------------------------------
  ## EXIT macro — signals completion to the TOP (host) core
  ## ---------------------------------------------------------------------------
  ## Writes 1 to scratchpad[TOP_FLAG_OFFSET]. The TOP core polls this address
  ## via rt->test_wait_addr(nwid, TOP_FLAG_OFFSET, 1) and proceeds when it
  ## reads 1. Used by KCORE_MULTI_main::done and ::run_iter to signal that
  ## one iteration of the UpDown computation is complete.
  ## ---------------------------------------------------------------------------
  ## Child data access macros (for the splitter threads)
  ## ---------------------------------------------------------------------------
  ## The splitter threads (split_vertexsKCORE_MULTI, split_vertexs2KCORE_MULTI)
  ## track their children's event words in a scratchpad array. Each child
  ## occupies 3 words (24 bytes): [event_word, reserved, reserved].
  ## These macros provide array-like access indexed by child number (0-7).
  ##
  ## local_child_data_ptr(ptr): Sets ptr to the child data base address for
  ##   the current thread (child_data_location + TID * DATA_PER_THREAD).
  ##   Uses if(1) to create a scope for the temporary computation.
  ## ref_child_event(ptr, num): Direct array access to child #num's event word.
  ##   ptr must already point to the child data base for this thread.
  ##   Stride is 3 words per child (event_word at offset 0).
  ## set_child_event(child, num): Store an event word for child #num.
  ##   Computes the child data pointer internally (allocates a temp register).
  ## get_child_event(child, num): Load the event word for child #num into `child`.
  ##   Computes the child data pointer internally.
  ## ---------------------------------------------------------------------------
  ## Batched DRAM read macros (array_loadN)
  ## ---------------------------------------------------------------------------
  ## These macros issue multiple DRAM read requests for neighbor vertex structs.
  ## Used after reading a batch of neighbor IDs (data0..data7) from the neighbor
  ## list: for each neighbor ID, we need to read that neighbor's vertex struct
  ## from the graph array to check its degree (alive or deleted?).
  ##
  ## array_load(array, offset, scale, size, cont):
  ##   Issues a single send_dram_read for the vertex at array[offset].
  ##   - array: base of the graph vertex array in DRAM
  ##   - offset: the neighbor's vertex ID
  ##   - scale: vertex_size (64 bytes) — stride between vertices
  ##   - size: number of words to read (7 = first 7 fields of vertex_t, 56 bytes)
  ##   - cont: continuation event word — the event that receives the read data
  ##
  ## array_loadN: Issues N parallel DRAM reads using the token-pasting operator
  ##   (##) to construct variable names data0, data1, ... dataN-1 from the
  ##   base_var_offset prefix. For example, array_load8(graph, data, ...) expands
  ##   to 8 calls reading graph[data0], graph[data1], ..., graph[data7].
  ##   Each read returns the vertex struct data to the continuation event.
  ## #define DEBUG_MARKVERTICES
  
  ##################################################
  ###### Writing code for thread MarkVertices ######
  ##################################################
  # Writing code for event MarkVertices::start
  tranMarkVertices__start = efa.writeEvent('MarkVertices::start')
  ## distribute the work among all lanes available

  tranMarkVertices__start.writeAction(f"__entry: movir X16 0") 
  tranMarkVertices__start.writeAction(f"evlb X16 Broadcast::start") 
  tranMarkVertices__start.writeAction(f"evi X16 X16 255 4") 
  tranMarkVertices__start.writeAction(f"ev X16 X16 X0 X0 8") 
  tranMarkVertices__start.writeAction(f"evi X2 X17 MarkVertices::done 1") 
  tranMarkVertices__start.writeAction(f"movir X18 0") 
  tranMarkVertices__start.writeAction(f"evlb X18 BroadcastWorker::start") 
  tranMarkVertices__start.writeAction(f"evi X18 X18 255 4") 
  tranMarkVertices__start.writeAction(f"ev X18 X18 X0 X0 8") 
  tranMarkVertices__start.writeAction(f"addi X7 X19 1664") 
  tranMarkVertices__start.writeAction(f"movrl X11 0(X19) 0 8") 
  tranMarkVertices__start.writeAction(f"movrl X18 8(X19) 0 8") 
  tranMarkVertices__start.writeAction(f"addi X19 X18 16") 
  tranMarkVertices__start.writeAction(f"bcpyoli X8 X18 4") 
  ## length and destination address in the LM is configured in the Broadcast receiver

  tranMarkVertices__start.writeAction(f"send_wcont X16 X17 X19 8") 
  tranMarkVertices__start.writeAction(f"yield") 
  
  # Writing code for event MarkVertices::done
  tranMarkVertices__done = efa.writeEvent('MarkVertices::done')
  tranMarkVertices__done.writeAction(f"__entry: addi X7 X16 1664") 
  tranMarkVertices__done.writeAction(f"movrl X8 0(X16) 0 8") 
  tranMarkVertices__done.writeAction(f"addi X7 X16 0") 
  tranMarkVertices__done.writeAction(f"movir X17 1") 
  tranMarkVertices__done.writeAction(f"movrl X17 0(X16) 0 8") 
  tranMarkVertices__done.writeAction(f"yield_terminate") 
  
  
  #####################################################
  ###### Writing code for thread BroadcastWorker ######
  #####################################################
  # Writing code for event BroadcastWorker::start
  tranBroadcastWorker__start = efa.writeEvent('BroadcastWorker::start')
  ## determine the numVertices that this lane has to handle

  tranBroadcastWorker__start.writeAction(f"__entry: div X10 X11 X21") 
  tranBroadcastWorker__start.writeAction(f"mod X10 X11 X22") 
  tranBroadcastWorker__start.writeAction(f"bleu X22 X0 __if_start_1_false") 
  tranBroadcastWorker__start.writeAction(f"__if_start_0_true: addi X21 X17 1") 
  tranBroadcastWorker__start.writeAction(f"addi X0 X23 0") 
  tranBroadcastWorker__start.writeAction(f"jmp __if_start_2_post") 
  tranBroadcastWorker__start.writeAction(f"__if_start_1_false: addi X21 X17 0") 
  tranBroadcastWorker__start.writeAction(f"addi X22 X23 0") 
  tranBroadcastWorker__start.writeAction(f"__if_start_2_post: bneiu X17 0 __if_start_5_post") 
  tranBroadcastWorker__start.writeAction(f"__if_start_3_true: movir X22 0") 
  tranBroadcastWorker__start.writeAction(f"movir X24 -1") 
  tranBroadcastWorker__start.writeAction(f"sri X24 X24 1") 
  tranBroadcastWorker__start.writeAction(f"sendr_wcont X1 X24 X22 X22") 
  tranBroadcastWorker__start.writeAction(f"yield_terminate") 
  ## set the base addresses

  tranBroadcastWorker__start.writeAction(f"__if_start_5_post: mul X0 X21 X21") 
  tranBroadcastWorker__start.writeAction(f"add X21 X23 X23") 
  tranBroadcastWorker__start.writeAction(f"sli X23 X23 3") 
  tranBroadcastWorker__start.writeAction(f"sli X23 X23 3") 
  ## size of vertex_t

  tranBroadcastWorker__start.writeAction(f"add X8 X23 X23") 
  tranBroadcastWorker__start.writeAction(f"addi X23 X16 8") 
  tranBroadcastWorker__start.writeAction(f"movir X19 0") 
  tranBroadcastWorker__start.writeAction(f"movir X20 0") 
  tranBroadcastWorker__start.writeAction(f"addi X9 X18 0") 
  tranBroadcastWorker__start.writeAction(f"movir X23 0") 
  tranBroadcastWorker__start.writeAction(f"__for_start_6_condition: clti X23 X21 10") 
  tranBroadcastWorker__start.writeAction(f"cgti X17 X22 0") 
  tranBroadcastWorker__start.writeAction(f"and X21 X22 X21") 
  tranBroadcastWorker__start.writeAction(f"beqiu X21 0 __for_start_8_post") 
  tranBroadcastWorker__start.writeAction(f"__for_start_7_body: send_dmlm_ld_wret X16 BroadcastWorker::returnFromRead 4 X21") 
  tranBroadcastWorker__start.writeAction(f"addi X16 X16 64") 
  tranBroadcastWorker__start.writeAction(f"subi X17 X17 1") 
  tranBroadcastWorker__start.writeAction(f"addi X19 X19 1") 
  tranBroadcastWorker__start.writeAction(f"addi X23 X23 1") 
  tranBroadcastWorker__start.writeAction(f"jmp __for_start_6_condition") 
  tranBroadcastWorker__start.writeAction(f"__for_start_8_post: yield") 
  
  # Writing code for event BroadcastWorker::returnFromRead
  tranBroadcastWorker__returnFromRead = efa.writeEvent('BroadcastWorker::returnFromRead')
  tranBroadcastWorker__returnFromRead.writeAction(f"__entry: ceqi X8 X23 0") 
  tranBroadcastWorker__returnFromRead.writeAction(f"ceqi X11 X21 0") 
  tranBroadcastWorker__returnFromRead.writeAction(f"and X23 X21 X23") 
  tranBroadcastWorker__returnFromRead.writeAction(f"beqiu X23 0 __if_returnFromRead_1_false") 
  tranBroadcastWorker__returnFromRead.writeAction(f"__if_returnFromRead_0_true: addi X20 X20 1") 
  tranBroadcastWorker__returnFromRead.writeAction(f"jmp __if_returnFromRead_2_post") 
  tranBroadcastWorker__returnFromRead.writeAction(f"__if_returnFromRead_1_false: clt X8 X18 X23") 
  tranBroadcastWorker__returnFromRead.writeAction(f"clt X11 X18 X21") 
  tranBroadcastWorker__returnFromRead.writeAction(f"or X23 X21 X23") 
  tranBroadcastWorker__returnFromRead.writeAction(f"beqiu X23 0 __if_returnFromRead_4_false") 
  tranBroadcastWorker__returnFromRead.writeAction(f"__if_returnFromRead_3_true: addi X7 X23 1664") 
  tranBroadcastWorker__returnFromRead.writeAction(f"movir X21 0") 
  tranBroadcastWorker__returnFromRead.writeAction(f"movrl X21 0(X23) 0 8") 
  tranBroadcastWorker__returnFromRead.writeAction(f"movrl X9 8(X23) 0 8") 
  tranBroadcastWorker__returnFromRead.writeAction(f"movrl X10 16(X23) 0 8") 
  tranBroadcastWorker__returnFromRead.writeAction(f"movir X21 0") 
  tranBroadcastWorker__returnFromRead.writeAction(f"movrl X21 24(X23) 0 8") 
  tranBroadcastWorker__returnFromRead.writeAction(f"send_dmlm_wret X12 BroadcastWorker::returnFromWrite X23 4 X21") 
  tranBroadcastWorker__returnFromRead.writeAction(f"addi X19 X19 1") 
  tranBroadcastWorker__returnFromRead.writeAction(f"addi X20 X20 1") 
  tranBroadcastWorker__returnFromRead.writeAction(f"jmp __if_returnFromRead_2_post") 
  ## ERROR, if scratch1 > degree

  tranBroadcastWorker__returnFromRead.writeAction(f"__if_returnFromRead_4_false: sub X8 X11 X23") 
  tranBroadcastWorker__returnFromRead.writeAction(f"bgei X23 0 __if_returnFromRead_2_post") 
  tranBroadcastWorker__returnFromRead.writeAction(f"__if_returnFromRead_6_true: print 'test had a value of %d, required non negative' X23") 
  tranBroadcastWorker__returnFromRead.writeAction(f"divi X16 X16 0") 
  tranBroadcastWorker__returnFromRead.writeAction(f"__if_returnFromRead_2_post: beqiu X17 0 __if_returnFromRead_10_false") 
  tranBroadcastWorker__returnFromRead.writeAction(f"__if_returnFromRead_9_true: send_dmlm_ld X16 X2 4") 
  tranBroadcastWorker__returnFromRead.writeAction(f"addi X16 X16 64") 
  tranBroadcastWorker__returnFromRead.writeAction(f"subi X17 X17 1") 
  tranBroadcastWorker__returnFromRead.writeAction(f"jmp __if_returnFromRead_11_post") 
  tranBroadcastWorker__returnFromRead.writeAction(f"__if_returnFromRead_10_false: subi X19 X19 1") 
  tranBroadcastWorker__returnFromRead.writeAction(f"bneiu X19 0 __if_returnFromRead_11_post") 
  ## inform the broadcast library that we are done

  tranBroadcastWorker__returnFromRead.writeAction(f"__if_returnFromRead_12_true: movir X23 -1") 
  tranBroadcastWorker__returnFromRead.writeAction(f"sri X23 X23 1") 
  tranBroadcastWorker__returnFromRead.writeAction(f"sendr_wcont X1 X23 X20 X20") 
  tranBroadcastWorker__returnFromRead.writeAction(f"yield_terminate") 
  tranBroadcastWorker__returnFromRead.writeAction(f"__if_returnFromRead_11_post: yield") 
  
  # Writing code for event BroadcastWorker::returnFromWrite
  tranBroadcastWorker__returnFromWrite = efa.writeEvent('BroadcastWorker::returnFromWrite')
  tranBroadcastWorker__returnFromWrite.writeAction(f"__entry: subi X19 X19 1") 
  tranBroadcastWorker__returnFromWrite.writeAction(f"bneiu X19 0 __if_returnFromWrite_2_post") 
  ## inform the broadcast library that we are done

  tranBroadcastWorker__returnFromWrite.writeAction(f"__if_returnFromWrite_0_true: movir X23 -1") 
  tranBroadcastWorker__returnFromWrite.writeAction(f"sri X23 X23 1") 
  tranBroadcastWorker__returnFromWrite.writeAction(f"sendr_wcont X1 X23 X20 X20") 
  tranBroadcastWorker__returnFromWrite.writeAction(f"yield_terminate") 
  tranBroadcastWorker__returnFromWrite.writeAction(f"__if_returnFromWrite_2_post: yield") 
  