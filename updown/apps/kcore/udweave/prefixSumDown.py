from linker.EFAProgram import efaProgram

## UDWeave version: 7808cc0 (2026-04-24)

## Global constants

@efaProgram
def EFA_prefixSumDown(efa):
  efa.code_level = 'machine'
  state0 = efa.State("udweave_init") #Only one state code 
  efa.add_initId(state0.state_id)
  ## Static declarations
  ## Scoped Variable "counter" uses Register X16, scope (0)
  ## Scoped Variable "maxDegree" uses Register X17, scope (0)
  ## Scoped Variable "counter" uses Register X16, scope (0)
  ## Scoped Variable "maxDegree" uses Register X17, scope (0)
  ## Scoped Variable "counter" uses Register X16, scope (0)
  ## Scoped Variable "maxDegree" uses Register X17, scope (0)
  ## Scoped Variable "curAddressBlock" uses Register X16, scope (0)
  ## Scoped Variable "curVertexID" uses Register X17, scope (0)
  ## Scoped Variable "numVertices" uses Register X18, scope (0)
  ## Scoped Variable "counter" uses Register X19, scope (0)
  ## Scoped Variable "expectedReturnValues" uses Register X20, scope (0)
  ## Scoped Variable "prefixSum" uses Register X21, scope (0)
  ## Scoped Variable "maxDegree" uses Register X22, scope (0)
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
  ## #define DEBUG_PREFIXSUM
  ## size: (max (16384 / THRESHOLD_NODE_BC) + 1) * 8 Bytes each entries
  ## size: 1 entry per node + 1 (max THRESHOLD_NODE_BC * 8 Bytes)
  ## size: (32 + 1) (UDs) * 8
  ## size: (64 + 1) (Lanes/UD) * 8
  ## size: (MAX_OUTSTANDING_READ_REQUESTS + 1) * 8
  ## how many vertices to load in the lane in a batch
  ## distribute to the nodes
  
  #################################################################
  ###### Writing code for thread PrefixSumDownAboveNodeLevel ######
  #################################################################
  # Writing code for event PrefixSumDownAboveNodeLevel::start
  tranPrefixSumDownAboveNodeLevel__start = efa.writeEvent('PrefixSumDownAboveNodeLevel::start')
  tranPrefixSumDownAboveNodeLevel__start.writeAction(f"__entry: movir X16 0") 
  tranPrefixSumDownAboveNodeLevel__start.writeAction(f"movir X17 0") 
  tranPrefixSumDownAboveNodeLevel__start.writeAction(f"addi X11 X18 0") 
  tranPrefixSumDownAboveNodeLevel__start.writeAction(f"addi X7 X19 2184") 
  tranPrefixSumDownAboveNodeLevel__start.writeAction(f"addi X7 X20 8") 
  tranPrefixSumDownAboveNodeLevel__start.writeAction(f"bcpyoli X8 X20 3") 
  tranPrefixSumDownAboveNodeLevel__start.writeAction(f"evi X2 X21 PrefixSumDownAboveNodeLevel::returnFromChild 1") 
  tranPrefixSumDownAboveNodeLevel__start.writeAction(f"movir X22 131072") 
  tranPrefixSumDownAboveNodeLevel__start.writeAction(f"bleu X22 X10 __if_start_2_post") 
  tranPrefixSumDownAboveNodeLevel__start.writeAction(f"__if_start_0_true: addi X10 X22 0") 
  tranPrefixSumDownAboveNodeLevel__start.writeAction(f"__if_start_2_post: movir X23 0") 
  tranPrefixSumDownAboveNodeLevel__start.writeAction(f"__for_start_3_condition: bleu X22 X23 __for_start_5_post") 
  tranPrefixSumDownAboveNodeLevel__start.writeAction(f"__for_start_4_body: movwlr X19(X16,0,0) X24") 
  tranPrefixSumDownAboveNodeLevel__start.writeAction(f"add X18 X24 X18") 
  tranPrefixSumDownAboveNodeLevel__start.writeAction(f"movrl X18 24(X20) 0 8") 
  tranPrefixSumDownAboveNodeLevel__start.writeAction(f"add X0 X23 X24") 
  tranPrefixSumDownAboveNodeLevel__start.writeAction(f"movir X25 0") 
  tranPrefixSumDownAboveNodeLevel__start.writeAction(f"evlb X25 PrefixSumDownNodeLevel::start") 
  tranPrefixSumDownAboveNodeLevel__start.writeAction(f"evi X25 X25 255 4") 
  tranPrefixSumDownAboveNodeLevel__start.writeAction(f"ev X25 X25 X24 X24 8") 
  tranPrefixSumDownAboveNodeLevel__start.writeAction(f"send_wcont X25 X21 X20 4") 
  tranPrefixSumDownAboveNodeLevel__start.writeAction(f"addi X16 X16 1") 
  tranPrefixSumDownAboveNodeLevel__start.writeAction(f"addi X23 X23 2048") 
  tranPrefixSumDownAboveNodeLevel__start.writeAction(f"jmp __for_start_3_condition") 
  tranPrefixSumDownAboveNodeLevel__start.writeAction(f"__for_start_5_post: yield") 
  
  # Writing code for event PrefixSumDownAboveNodeLevel::returnFromChild
  tranPrefixSumDownAboveNodeLevel__returnFromChild = efa.writeEvent('PrefixSumDownAboveNodeLevel::returnFromChild')
  tranPrefixSumDownAboveNodeLevel__returnFromChild.writeAction(f"__entry: bleu X8 X17 __if_returnFromChild_2_post") 
  tranPrefixSumDownAboveNodeLevel__returnFromChild.writeAction(f"__if_returnFromChild_0_true: addi X8 X17 0") 
  tranPrefixSumDownAboveNodeLevel__returnFromChild.writeAction(f"__if_returnFromChild_2_post: subi X16 X16 1") 
  tranPrefixSumDownAboveNodeLevel__returnFromChild.writeAction(f"bneiu X16 0 __if_returnFromChild_5_post") 
  tranPrefixSumDownAboveNodeLevel__returnFromChild.writeAction(f"__if_returnFromChild_3_true: movir X20 -1") 
  tranPrefixSumDownAboveNodeLevel__returnFromChild.writeAction(f"sri X20 X20 1") 
  tranPrefixSumDownAboveNodeLevel__returnFromChild.writeAction(f"sendr_wcont X1 X20 X17 X17") 
  tranPrefixSumDownAboveNodeLevel__returnFromChild.writeAction(f"yield_terminate") 
  tranPrefixSumDownAboveNodeLevel__returnFromChild.writeAction(f"__if_returnFromChild_5_post: yield") 
  
  ## distribute among UDs
  
  ############################################################
  ###### Writing code for thread PrefixSumDownNodeLevel ######
  ############################################################
  # Writing code for event PrefixSumDownNodeLevel::start
  tranPrefixSumDownNodeLevel__start = efa.writeEvent('PrefixSumDownNodeLevel::start')
  tranPrefixSumDownNodeLevel__start.writeAction(f"__entry: movir X16 0") 
  tranPrefixSumDownNodeLevel__start.writeAction(f"movir X17 0") 
  tranPrefixSumDownNodeLevel__start.writeAction(f"addi X11 X18 0") 
  tranPrefixSumDownNodeLevel__start.writeAction(f"addi X7 X19 2704") 
  tranPrefixSumDownNodeLevel__start.writeAction(f"addi X7 X20 8") 
  tranPrefixSumDownNodeLevel__start.writeAction(f"bcpyoli X8 X20 3") 
  tranPrefixSumDownNodeLevel__start.writeAction(f"evi X2 X21 PrefixSumDownNodeLevel::returnFromChild 1") 
  tranPrefixSumDownNodeLevel__start.writeAction(f"movir X22 2048") 
  tranPrefixSumDownNodeLevel__start.writeAction(f"movir X23 0") 
  tranPrefixSumDownNodeLevel__start.writeAction(f"__for_start_0_condition: bleu X22 X23 __for_start_2_post") 
  tranPrefixSumDownNodeLevel__start.writeAction(f"__for_start_1_body: movwlr X19(X16,0,0) X24") 
  tranPrefixSumDownNodeLevel__start.writeAction(f"add X18 X24 X18") 
  tranPrefixSumDownNodeLevel__start.writeAction(f"movrl X18 24(X20) 0 8") 
  tranPrefixSumDownNodeLevel__start.writeAction(f"add X0 X23 X24") 
  tranPrefixSumDownNodeLevel__start.writeAction(f"movir X25 0") 
  tranPrefixSumDownNodeLevel__start.writeAction(f"evlb X25 PrefixSumDownUDLevel::start") 
  tranPrefixSumDownNodeLevel__start.writeAction(f"evi X25 X25 255 4") 
  tranPrefixSumDownNodeLevel__start.writeAction(f"ev X25 X25 X24 X24 8") 
  tranPrefixSumDownNodeLevel__start.writeAction(f"send_wcont X25 X21 X20 4") 
  tranPrefixSumDownNodeLevel__start.writeAction(f"addi X16 X16 1") 
  tranPrefixSumDownNodeLevel__start.writeAction(f"addi X23 X23 64") 
  tranPrefixSumDownNodeLevel__start.writeAction(f"jmp __for_start_0_condition") 
  tranPrefixSumDownNodeLevel__start.writeAction(f"__for_start_2_post: yield") 
  
  # Writing code for event PrefixSumDownNodeLevel::returnFromChild
  tranPrefixSumDownNodeLevel__returnFromChild = efa.writeEvent('PrefixSumDownNodeLevel::returnFromChild')
  tranPrefixSumDownNodeLevel__returnFromChild.writeAction(f"__entry: bleu X8 X17 __if_returnFromChild_2_post") 
  tranPrefixSumDownNodeLevel__returnFromChild.writeAction(f"__if_returnFromChild_0_true: addi X8 X17 0") 
  tranPrefixSumDownNodeLevel__returnFromChild.writeAction(f"__if_returnFromChild_2_post: subi X16 X16 1") 
  tranPrefixSumDownNodeLevel__returnFromChild.writeAction(f"bneiu X16 0 __if_returnFromChild_5_post") 
  tranPrefixSumDownNodeLevel__returnFromChild.writeAction(f"__if_returnFromChild_3_true: movir X19 -1") 
  tranPrefixSumDownNodeLevel__returnFromChild.writeAction(f"sri X19 X19 1") 
  tranPrefixSumDownNodeLevel__returnFromChild.writeAction(f"sendr_wcont X1 X19 X17 X17") 
  tranPrefixSumDownNodeLevel__returnFromChild.writeAction(f"yield_terminate") 
  tranPrefixSumDownNodeLevel__returnFromChild.writeAction(f"__if_returnFromChild_5_post: yield") 
  
  ## distribute among the lanes
  
  ##########################################################
  ###### Writing code for thread PrefixSumDownUDLevel ######
  ##########################################################
  # Writing code for event PrefixSumDownUDLevel::start
  tranPrefixSumDownUDLevel__start = efa.writeEvent('PrefixSumDownUDLevel::start')
  tranPrefixSumDownUDLevel__start.writeAction(f"__entry: movir X16 64") 
  tranPrefixSumDownUDLevel__start.writeAction(f"movir X17 0") 
  tranPrefixSumDownUDLevel__start.writeAction(f"addi X11 X18 0") 
  tranPrefixSumDownUDLevel__start.writeAction(f"addi X7 X19 2968") 
  tranPrefixSumDownUDLevel__start.writeAction(f"addi X7 X20 8") 
  tranPrefixSumDownUDLevel__start.writeAction(f"bcpyoli X8 X20 3") 
  tranPrefixSumDownUDLevel__start.writeAction(f"evi X2 X21 PrefixSumDownUDLevel::returnFromChild 1") 
  tranPrefixSumDownUDLevel__start.writeAction(f"movir X22 64") 
  tranPrefixSumDownUDLevel__start.writeAction(f"movir X23 0") 
  tranPrefixSumDownUDLevel__start.writeAction(f"__for_start_0_condition: bleu X22 X23 __for_start_2_post") 
  tranPrefixSumDownUDLevel__start.writeAction(f"__for_start_1_body: movwlr X19(X23,0,0) X24") 
  tranPrefixSumDownUDLevel__start.writeAction(f"add X18 X24 X18") 
  tranPrefixSumDownUDLevel__start.writeAction(f"movrl X18 24(X20) 0 8") 
  tranPrefixSumDownUDLevel__start.writeAction(f"add X0 X23 X24") 
  tranPrefixSumDownUDLevel__start.writeAction(f"movir X25 0") 
  tranPrefixSumDownUDLevel__start.writeAction(f"evlb X25 PrefixSumDownWorker::start") 
  tranPrefixSumDownUDLevel__start.writeAction(f"evi X25 X25 255 4") 
  tranPrefixSumDownUDLevel__start.writeAction(f"ev X25 X25 X24 X24 8") 
  tranPrefixSumDownUDLevel__start.writeAction(f"send_wcont X25 X21 X20 4") 
  tranPrefixSumDownUDLevel__start.writeAction(f"addi X23 X23 1") 
  tranPrefixSumDownUDLevel__start.writeAction(f"jmp __for_start_0_condition") 
  tranPrefixSumDownUDLevel__start.writeAction(f"__for_start_2_post: yield") 
  
  # Writing code for event PrefixSumDownUDLevel::returnFromChild
  tranPrefixSumDownUDLevel__returnFromChild = efa.writeEvent('PrefixSumDownUDLevel::returnFromChild')
  tranPrefixSumDownUDLevel__returnFromChild.writeAction(f"__entry: bleu X8 X17 __if_returnFromChild_2_post") 
  tranPrefixSumDownUDLevel__returnFromChild.writeAction(f"__if_returnFromChild_0_true: addi X8 X17 0") 
  tranPrefixSumDownUDLevel__returnFromChild.writeAction(f"__if_returnFromChild_2_post: subi X16 X16 1") 
  tranPrefixSumDownUDLevel__returnFromChild.writeAction(f"bneiu X16 0 __if_returnFromChild_5_post") 
  tranPrefixSumDownUDLevel__returnFromChild.writeAction(f"__if_returnFromChild_3_true: movir X19 -1") 
  tranPrefixSumDownUDLevel__returnFromChild.writeAction(f"sri X19 X19 1") 
  tranPrefixSumDownUDLevel__returnFromChild.writeAction(f"sendr_wcont X1 X19 X17 X17") 
  tranPrefixSumDownUDLevel__returnFromChild.writeAction(f"yield_terminate") 
  tranPrefixSumDownUDLevel__returnFromChild.writeAction(f"__if_returnFromChild_5_post: yield") 
  
  
  #########################################################
  ###### Writing code for thread PrefixSumDownWorker ######
  #########################################################
  # Writing code for event PrefixSumDownWorker::start
  tranPrefixSumDownWorker__start = efa.writeEvent('PrefixSumDownWorker::start')
  ## determine the numVertices

  tranPrefixSumDownWorker__start.writeAction(f"__entry: div X9 X10 X23") 
  tranPrefixSumDownWorker__start.writeAction(f"mod X9 X10 X24") 
  tranPrefixSumDownWorker__start.writeAction(f"bleu X24 X0 __if_start_1_false") 
  tranPrefixSumDownWorker__start.writeAction(f"__if_start_0_true: addi X23 X18 1") 
  tranPrefixSumDownWorker__start.writeAction(f"addi X0 X25 0") 
  tranPrefixSumDownWorker__start.writeAction(f"jmp __if_start_2_post") 
  tranPrefixSumDownWorker__start.writeAction(f"__if_start_1_false: addi X23 X18 0") 
  tranPrefixSumDownWorker__start.writeAction(f"addi X24 X25 0") 
  tranPrefixSumDownWorker__start.writeAction(f"__if_start_2_post: bneiu X18 0 __if_start_5_post") 
  tranPrefixSumDownWorker__start.writeAction(f"__if_start_3_true: movir X24 0") 
  tranPrefixSumDownWorker__start.writeAction(f"movir X26 -1") 
  tranPrefixSumDownWorker__start.writeAction(f"sri X26 X26 1") 
  tranPrefixSumDownWorker__start.writeAction(f"sendr_wcont X1 X26 X24 X24") 
  tranPrefixSumDownWorker__start.writeAction(f"yield_terminate") 
  tranPrefixSumDownWorker__start.writeAction(f"__if_start_5_post: addi X11 X21 0") 
  ## set the base addresses

  tranPrefixSumDownWorker__start.writeAction(f"mul X0 X23 X23") 
  tranPrefixSumDownWorker__start.writeAction(f"add X23 X25 X17") 
  tranPrefixSumDownWorker__start.writeAction(f"sli X17 X25 6") 
  tranPrefixSumDownWorker__start.writeAction(f"add X8 X25 X16") 
  tranPrefixSumDownWorker__start.writeAction(f"addi X16 X25 8") 
  ## point to where the degree is

  tranPrefixSumDownWorker__start.writeAction(f"movir X19 0") 
  tranPrefixSumDownWorker__start.writeAction(f"movir X22 0") 
  tranPrefixSumDownWorker__start.writeAction(f"evi X2 X23 PrefixSumDownWorker::returnFromRead 1") 
  tranPrefixSumDownWorker__start.writeAction(f"movir X24 0") 
  tranPrefixSumDownWorker__start.writeAction(f"__for_start_6_condition: clti X24 X26 32") 
  tranPrefixSumDownWorker__start.writeAction(f"cgti X18 X27 0") 
  tranPrefixSumDownWorker__start.writeAction(f"and X26 X27 X26") 
  tranPrefixSumDownWorker__start.writeAction(f"beqiu X26 0 __for_start_8_post") 
  tranPrefixSumDownWorker__start.writeAction(f"__for_start_7_body: send_dmlm_ld X25 X23 1") 
  tranPrefixSumDownWorker__start.writeAction(f"addi X25 X25 64") 
  tranPrefixSumDownWorker__start.writeAction(f"subi X18 X18 1") 
  tranPrefixSumDownWorker__start.writeAction(f"addi X19 X19 1") 
  tranPrefixSumDownWorker__start.writeAction(f"addi X24 X24 1") 
  tranPrefixSumDownWorker__start.writeAction(f"jmp __for_start_6_condition") 
  tranPrefixSumDownWorker__start.writeAction(f"__for_start_8_post: addi X19 X20 0") 
  tranPrefixSumDownWorker__start.writeAction(f"yield") 
  
  # Writing code for event PrefixSumDownWorker::returnFromRead
  tranPrefixSumDownWorker__returnFromRead = efa.writeEvent('PrefixSumDownWorker::returnFromRead')
  ## determine, which vertex has been read

  tranPrefixSumDownWorker__returnFromRead.writeAction(f"__entry: sub X9 X16 X24") 
  tranPrefixSumDownWorker__returnFromRead.writeAction(f"sari X24 X23 6") 
  tranPrefixSumDownWorker__returnFromRead.writeAction(f"addi X23 X24 1") 
  ## shift by 1, since the first element of the prefix sum should be 0

  tranPrefixSumDownWorker__returnFromRead.writeAction(f"addi X7 X23 3488") 
  tranPrefixSumDownWorker__returnFromRead.writeAction(f"movwrl X8 X23(X24,0,0)") 
  tranPrefixSumDownWorker__returnFromRead.writeAction(f"subi X19 X19 1") 
  tranPrefixSumDownWorker__returnFromRead.writeAction(f"bleu X8 X22 __if_returnFromRead_2_post") 
  tranPrefixSumDownWorker__returnFromRead.writeAction(f"__if_returnFromRead_0_true: addi X8 X22 0") 
  tranPrefixSumDownWorker__returnFromRead.writeAction(f"__if_returnFromRead_2_post: bneiu X19 0 __if_returnFromRead_5_post") 
  tranPrefixSumDownWorker__returnFromRead.writeAction(f"__if_returnFromRead_3_true: addi X7 X24 8") 
  tranPrefixSumDownWorker__returnFromRead.writeAction(f"movir X25 1") 
  tranPrefixSumDownWorker__returnFromRead.writeAction(f"movrl X25 16(X24) 0 8") 
  ## vert->scratch1 = starting_value -> k=1

  tranPrefixSumDownWorker__returnFromRead.writeAction(f"movir X25 0") 
  tranPrefixSumDownWorker__returnFromRead.writeAction(f"movrl X25 24(X24) 0 8") 
  ## vert->scratch2 = 0;

  tranPrefixSumDownWorker__returnFromRead.writeAction(f"movir X25 0") 
  tranPrefixSumDownWorker__returnFromRead.writeAction(f"movrl X25 32(X24) 0 8") 
  ## vert->scratch3 = 0;

  tranPrefixSumDownWorker__returnFromRead.writeAction(f"movir X25 0") 
  tranPrefixSumDownWorker__returnFromRead.writeAction(f"movrl X25 40(X24) 0 8") 
  ## vert->scratch4 = 0;

  tranPrefixSumDownWorker__returnFromRead.writeAction(f"evi X2 X25 PrefixSumDownWorker::returnFromWrite 1") 
  ## compute the prefixSum

  tranPrefixSumDownWorker__returnFromRead.writeAction(f"movir X26 0") 
  tranPrefixSumDownWorker__returnFromRead.writeAction(f"__for_returnFromRead_6_condition: bleu X20 X26 __for_returnFromRead_8_post") 
  tranPrefixSumDownWorker__returnFromRead.writeAction(f"__for_returnFromRead_7_body: movwlr X23(X26,0,0) X27") 
  tranPrefixSumDownWorker__returnFromRead.writeAction(f"add X21 X27 X21") 
  tranPrefixSumDownWorker__returnFromRead.writeAction(f"movrl X21 0(X24) 0 8") 
  tranPrefixSumDownWorker__returnFromRead.writeAction(f"add X17 X26 X27") 
  tranPrefixSumDownWorker__returnFromRead.writeAction(f"movrl X27 8(X24) 0 8") 
  ## rewrite the vertexID (should be the same)

  ## write the data

  ## FOR DEBUGGING. You can store the data into the scratch fields and then compare it with the existing data

  ## send_dram_write(curAddressBlock + 32 /* point to edges_before */, spPtrSend, 2, cont);

  tranPrefixSumDownWorker__returnFromRead.writeAction(f"addi X16 X27 16") 
  tranPrefixSumDownWorker__returnFromRead.writeAction(f"send_dmlm X27 X25 X24 6") 
  tranPrefixSumDownWorker__returnFromRead.writeAction(f"addi X16 X16 64") 
  tranPrefixSumDownWorker__returnFromRead.writeAction(f"addi X26 X26 1") 
  tranPrefixSumDownWorker__returnFromRead.writeAction(f"jmp __for_returnFromRead_6_condition") 
  tranPrefixSumDownWorker__returnFromRead.writeAction(f"__for_returnFromRead_8_post: addi X20 X19 0") 
  tranPrefixSumDownWorker__returnFromRead.writeAction(f"movwlr X23(X20,0,0) X24") 
  tranPrefixSumDownWorker__returnFromRead.writeAction(f"add X21 X24 X21") 
  ## move up the block

  tranPrefixSumDownWorker__returnFromRead.writeAction(f"add X17 X20 X17") 
  tranPrefixSumDownWorker__returnFromRead.writeAction(f"__if_returnFromRead_5_post: yield") 
  
  # Writing code for event PrefixSumDownWorker::returnFromWrite
  tranPrefixSumDownWorker__returnFromWrite = efa.writeEvent('PrefixSumDownWorker::returnFromWrite')
  tranPrefixSumDownWorker__returnFromWrite.writeAction(f"__entry: subi X19 X19 1") 
  tranPrefixSumDownWorker__returnFromWrite.writeAction(f"bneiu X19 0 __if_returnFromWrite_2_post") 
  ## send the next batch

  tranPrefixSumDownWorker__returnFromWrite.writeAction(f"__if_returnFromWrite_0_true: bleiu X18 0 __if_returnFromWrite_5_post") 
  tranPrefixSumDownWorker__returnFromWrite.writeAction(f"__if_returnFromWrite_3_true: addi X16 X23 8") 
  ## point to where the degree is

  tranPrefixSumDownWorker__returnFromWrite.writeAction(f"evi X2 X24 PrefixSumDownWorker::returnFromRead 1") 
  tranPrefixSumDownWorker__returnFromWrite.writeAction(f"movir X26 0") 
  tranPrefixSumDownWorker__returnFromWrite.writeAction(f"__for_returnFromWrite_6_condition: clti X26 X25 32") 
  tranPrefixSumDownWorker__returnFromWrite.writeAction(f"cgti X18 X27 0") 
  tranPrefixSumDownWorker__returnFromWrite.writeAction(f"and X25 X27 X25") 
  tranPrefixSumDownWorker__returnFromWrite.writeAction(f"beqiu X25 0 __for_returnFromWrite_8_post") 
  tranPrefixSumDownWorker__returnFromWrite.writeAction(f"__for_returnFromWrite_7_body: send_dmlm_ld X23 X24 1") 
  tranPrefixSumDownWorker__returnFromWrite.writeAction(f"addi X23 X23 64") 
  tranPrefixSumDownWorker__returnFromWrite.writeAction(f"subi X18 X18 1") 
  tranPrefixSumDownWorker__returnFromWrite.writeAction(f"addi X19 X19 1") 
  tranPrefixSumDownWorker__returnFromWrite.writeAction(f"addi X26 X26 1") 
  tranPrefixSumDownWorker__returnFromWrite.writeAction(f"jmp __for_returnFromWrite_6_condition") 
  tranPrefixSumDownWorker__returnFromWrite.writeAction(f"__for_returnFromWrite_8_post: addi X19 X20 0") 
  tranPrefixSumDownWorker__returnFromWrite.writeAction(f"yield") 
  ## we are done

  tranPrefixSumDownWorker__returnFromWrite.writeAction(f"__if_returnFromWrite_5_post: movir X23 -1") 
  tranPrefixSumDownWorker__returnFromWrite.writeAction(f"sri X23 X23 1") 
  tranPrefixSumDownWorker__returnFromWrite.writeAction(f"sendr_wcont X1 X23 X22 X22") 
  tranPrefixSumDownWorker__returnFromWrite.writeAction(f"yield_terminate") 
  tranPrefixSumDownWorker__returnFromWrite.writeAction(f"__if_returnFromWrite_2_post: yield") 
  