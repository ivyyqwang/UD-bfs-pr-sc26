from linker.EFAProgram import efaProgram

## UDWeave version: 7808cc0 (2026-04-24)

## Global constants

@efaProgram
def EFA_prefixSum(efa):
  efa.code_level = 'machine'
  state0 = efa.State("udweave_init") #Only one state code 
  efa.add_initId(state0.state_id)
  ## Static declarations
  ## Scoped Variable "counter" uses Register X16, scope (0)
  ## Scoped Variable "expectedReturnValues" uses Register X17, scope (0)
  ## Scoped Variable "numLanes" uses Register X18, scope (0)
  ## Scoped Variable "vertex" uses Register X19, scope (0)
  ## Scoped Variable "numVertices" uses Register X20, scope (0)
  ## Scoped Variable "maxDegree" uses Register X21, scope (0)
  ## Scoped Variable "counter" uses Register X16, scope (0)
  ## Scoped Variable "expectedReturnValues" uses Register X17, scope (0)
  ## Scoped Variable "sum" uses Register X18, scope (0)
  ## Scoped Variable "counter" uses Register X16, scope (0)
  ## Scoped Variable "sum" uses Register X17, scope (0)
  ## Scoped Variable "counter" uses Register X16, scope (0)
  ## Scoped Variable "sum" uses Register X17, scope (0)
  ## Scoped Variable "srcBase" uses Register X16, scope (0)
  ## Scoped Variable "numVertices" uses Register X17, scope (0)
  ## Scoped Variable "counter" uses Register X18, scope (0)
  ## Scoped Variable "partialSum" uses Register X19, scope (0)
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
  
  ###############################################
  ###### Writing code for thread PrefixSum ######
  ###############################################
  # Writing code for event PrefixSum::start
  tranPrefixSum__start = efa.writeEvent('PrefixSum::start')
  tranPrefixSum__start.writeAction(f"__entry: addi X8 X19 0") 
  tranPrefixSum__start.writeAction(f"addi X9 X20 0") 
  tranPrefixSum__start.writeAction(f"addi X10 X18 0") 
  tranPrefixSum__start.writeAction(f"print 'start: vertex: %p, numVertices: %lu, numLanes: %lu' X19 X20 X10") 
  tranPrefixSum__start.writeAction(f"movir X16 0") 
  tranPrefixSum__start.writeAction(f"movir X21 0") 
  tranPrefixSum__start.writeAction(f"evi X2 X22 PrefixSum::returnFromChild 1") 
  tranPrefixSum__start.writeAction(f"movir X23 0") 
  tranPrefixSum__start.writeAction(f"__for_start_0_condition: bleu X18 X23 __for_start_2_post") 
  tranPrefixSum__start.writeAction(f"__for_start_1_body: add X0 X23 X24") 
  tranPrefixSum__start.writeAction(f"movir X25 0") 
  tranPrefixSum__start.writeAction(f"evlb X25 PrefixSumAboveNodeLevel::start") 
  tranPrefixSum__start.writeAction(f"evi X25 X25 255 4") 
  tranPrefixSum__start.writeAction(f"ev X25 X25 X24 X24 8") 
  tranPrefixSum__start.writeAction(f"sendops_wcont X25 X22 X8 3") 
  tranPrefixSum__start.writeAction(f"addi X16 X16 1") 
  tranPrefixSum__start.writeAction(f"movir X25 131072") 
  tranPrefixSum__start.writeAction(f"add X23 X25 X23") 
  tranPrefixSum__start.writeAction(f"jmp __for_start_0_condition") 
  tranPrefixSum__start.writeAction(f"__for_start_2_post: addi X16 X17 0") 
  tranPrefixSum__start.writeAction(f"yield") 
  
  # Writing code for event PrefixSum::returnFromChild
  tranPrefixSum__returnFromChild = efa.writeEvent('PrefixSum::returnFromChild')
  tranPrefixSum__returnFromChild.writeAction(f"__entry: sub X8 X0 X23") 
  tranPrefixSum__returnFromChild.writeAction(f"sari X23 X23 17") 
  tranPrefixSum__returnFromChild.writeAction(f"addi X23 X23 1") 
  tranPrefixSum__returnFromChild.writeAction(f"addi X7 X22 128") 
  tranPrefixSum__returnFromChild.writeAction(f"movwrl X9 X22(X23,0,0)") 
  tranPrefixSum__returnFromChild.writeAction(f"subi X16 X16 1") 
  tranPrefixSum__returnFromChild.writeAction(f"bneiu X16 0 __if_returnFromChild_2_post") 
  tranPrefixSum__returnFromChild.writeAction(f"__if_returnFromChild_0_true: addi X0 X23 0") 
  tranPrefixSum__returnFromChild.writeAction(f"addi X7 X25 8") 
  tranPrefixSum__returnFromChild.writeAction(f"movrl X19 0(X25) 0 8") 
  tranPrefixSum__returnFromChild.writeAction(f"movrl X20 8(X25) 0 8") 
  tranPrefixSum__returnFromChild.writeAction(f"movrl X18 16(X25) 0 8") 
  tranPrefixSum__returnFromChild.writeAction(f"movir X24 0") 
  tranPrefixSum__returnFromChild.writeAction(f"movrl X24 24(X25) 0 8") 
  ## prefix sum

  tranPrefixSum__returnFromChild.writeAction(f"evi X2 X24 PrefixSum::finishedAfterDown 1") 
  tranPrefixSum__returnFromChild.writeAction(f"movir X26 0") 
  tranPrefixSum__returnFromChild.writeAction(f"__for_returnFromChild_3_condition: bleu X17 X26 __if_returnFromChild_2_post") 
  tranPrefixSum__returnFromChild.writeAction(f"__for_returnFromChild_4_body: movlr 24(X25) X27 0 8") 
  tranPrefixSum__returnFromChild.writeAction(f"movwlr X22(X26,0,0) X28") 
  tranPrefixSum__returnFromChild.writeAction(f"add X27 X28 X27") 
  tranPrefixSum__returnFromChild.writeAction(f"movrl X27 24(X25) 0 8") 
  tranPrefixSum__returnFromChild.writeAction(f"movir X27 0") 
  tranPrefixSum__returnFromChild.writeAction(f"evlb X27 PrefixSumDownAboveNodeLevel::start") 
  tranPrefixSum__returnFromChild.writeAction(f"evi X27 X27 255 4") 
  tranPrefixSum__returnFromChild.writeAction(f"ev X27 X27 X23 X23 8") 
  tranPrefixSum__returnFromChild.writeAction(f"send_wcont X27 X24 X25 4") 
  tranPrefixSum__returnFromChild.writeAction(f"movir X27 131072") 
  tranPrefixSum__returnFromChild.writeAction(f"add X23 X27 X23") 
  tranPrefixSum__returnFromChild.writeAction(f"addi X26 X26 1") 
  tranPrefixSum__returnFromChild.writeAction(f"jmp __for_returnFromChild_3_condition") 
  tranPrefixSum__returnFromChild.writeAction(f"__if_returnFromChild_2_post: yield") 
  
  # Writing code for event PrefixSum::finishedAfterDown
  tranPrefixSum__finishedAfterDown = efa.writeEvent('PrefixSum::finishedAfterDown')
  tranPrefixSum__finishedAfterDown.writeAction(f"__entry: bleu X8 X21 __if_finishedAfterDown_2_post") 
  tranPrefixSum__finishedAfterDown.writeAction(f"__if_finishedAfterDown_0_true: addi X8 X21 0") 
  tranPrefixSum__finishedAfterDown.writeAction(f"__if_finishedAfterDown_2_post: subi X17 X17 1") 
  tranPrefixSum__finishedAfterDown.writeAction(f"bneiu X17 0 __if_finishedAfterDown_5_post") 
  tranPrefixSum__finishedAfterDown.writeAction(f"__if_finishedAfterDown_3_true: print 'done'") 
  ## we are done

  tranPrefixSum__finishedAfterDown.writeAction(f"addi X7 X22 0") 
  tranPrefixSum__finishedAfterDown.writeAction(f"movrl X21 8(X22) 0 8") 
  tranPrefixSum__finishedAfterDown.writeAction(f"movir X23 1") 
  tranPrefixSum__finishedAfterDown.writeAction(f"movrl X23 0(X22) 0 8") 
  tranPrefixSum__finishedAfterDown.writeAction(f"yield_terminate") 
  tranPrefixSum__finishedAfterDown.writeAction(f"__if_finishedAfterDown_5_post: yield") 
  
  ## distribute to the nodes
  
  #############################################################
  ###### Writing code for thread PrefixSumAboveNodeLevel ######
  #############################################################
  # Writing code for event PrefixSumAboveNodeLevel::start
  tranPrefixSumAboveNodeLevel__start = efa.writeEvent('PrefixSumAboveNodeLevel::start')
  tranPrefixSumAboveNodeLevel__start.writeAction(f"__entry: movir X16 0") 
  tranPrefixSumAboveNodeLevel__start.writeAction(f"movir X18 0") 
  tranPrefixSumAboveNodeLevel__start.writeAction(f"evi X2 X19 PrefixSumAboveNodeLevel::returnFromChild 1") 
  tranPrefixSumAboveNodeLevel__start.writeAction(f"movir X20 131072") 
  tranPrefixSumAboveNodeLevel__start.writeAction(f"bleu X20 X10 __if_start_2_post") 
  tranPrefixSumAboveNodeLevel__start.writeAction(f"__if_start_0_true: addi X10 X20 0") 
  tranPrefixSumAboveNodeLevel__start.writeAction(f"__if_start_2_post: movir X21 0") 
  tranPrefixSumAboveNodeLevel__start.writeAction(f"__for_start_3_condition: bleu X20 X21 __for_start_5_post") 
  tranPrefixSumAboveNodeLevel__start.writeAction(f"__for_start_4_body: add X0 X21 X22") 
  tranPrefixSumAboveNodeLevel__start.writeAction(f"movir X23 0") 
  tranPrefixSumAboveNodeLevel__start.writeAction(f"evlb X23 PrefixSumNodeLevel::start") 
  tranPrefixSumAboveNodeLevel__start.writeAction(f"evi X23 X23 255 4") 
  tranPrefixSumAboveNodeLevel__start.writeAction(f"ev X23 X23 X22 X22 8") 
  tranPrefixSumAboveNodeLevel__start.writeAction(f"sendops_wcont X23 X19 X8 3") 
  tranPrefixSumAboveNodeLevel__start.writeAction(f"addi X16 X16 1") 
  tranPrefixSumAboveNodeLevel__start.writeAction(f"addi X21 X21 2048") 
  tranPrefixSumAboveNodeLevel__start.writeAction(f"jmp __for_start_3_condition") 
  tranPrefixSumAboveNodeLevel__start.writeAction(f"__for_start_5_post: addi X16 X17 0") 
  tranPrefixSumAboveNodeLevel__start.writeAction(f"yield") 
  
  # Writing code for event PrefixSumAboveNodeLevel::returnFromChild
  tranPrefixSumAboveNodeLevel__returnFromChild = efa.writeEvent('PrefixSumAboveNodeLevel::returnFromChild')
  tranPrefixSumAboveNodeLevel__returnFromChild.writeAction(f"__entry: sub X8 X0 X20") 
  tranPrefixSumAboveNodeLevel__returnFromChild.writeAction(f"sari X20 X20 11") 
  tranPrefixSumAboveNodeLevel__returnFromChild.writeAction(f"addi X20 X20 1") 
  tranPrefixSumAboveNodeLevel__returnFromChild.writeAction(f"addi X7 X19 2184") 
  tranPrefixSumAboveNodeLevel__returnFromChild.writeAction(f"movwrl X9 X19(X20,0,0)") 
  tranPrefixSumAboveNodeLevel__returnFromChild.writeAction(f"add X18 X9 X18") 
  tranPrefixSumAboveNodeLevel__returnFromChild.writeAction(f"subi X16 X16 1") 
  tranPrefixSumAboveNodeLevel__returnFromChild.writeAction(f"bneiu X16 0 __if_returnFromChild_2_post") 
  tranPrefixSumAboveNodeLevel__returnFromChild.writeAction(f"__if_returnFromChild_0_true: movir X20 -1") 
  tranPrefixSumAboveNodeLevel__returnFromChild.writeAction(f"sri X20 X20 1") 
  tranPrefixSumAboveNodeLevel__returnFromChild.writeAction(f"sendr_wcont X1 X20 X0 X18") 
  tranPrefixSumAboveNodeLevel__returnFromChild.writeAction(f"yield_terminate") 
  tranPrefixSumAboveNodeLevel__returnFromChild.writeAction(f"__if_returnFromChild_2_post: yield") 
  
  ## distribute among UDs
  
  ########################################################
  ###### Writing code for thread PrefixSumNodeLevel ######
  ########################################################
  # Writing code for event PrefixSumNodeLevel::start
  tranPrefixSumNodeLevel__start = efa.writeEvent('PrefixSumNodeLevel::start')
  tranPrefixSumNodeLevel__start.writeAction(f"__entry: movir X16 32") 
  tranPrefixSumNodeLevel__start.writeAction(f"movir X17 0") 
  tranPrefixSumNodeLevel__start.writeAction(f"evi X2 X18 PrefixSumNodeLevel::returnFromChild 1") 
  tranPrefixSumNodeLevel__start.writeAction(f"movir X19 2048") 
  tranPrefixSumNodeLevel__start.writeAction(f"movir X20 0") 
  tranPrefixSumNodeLevel__start.writeAction(f"__for_start_0_condition: bleu X19 X20 __for_start_2_post") 
  tranPrefixSumNodeLevel__start.writeAction(f"__for_start_1_body: add X0 X20 X21") 
  tranPrefixSumNodeLevel__start.writeAction(f"movir X22 0") 
  tranPrefixSumNodeLevel__start.writeAction(f"evlb X22 PrefixSumUDLevel::start") 
  tranPrefixSumNodeLevel__start.writeAction(f"evi X22 X22 255 4") 
  tranPrefixSumNodeLevel__start.writeAction(f"ev X22 X22 X21 X21 8") 
  tranPrefixSumNodeLevel__start.writeAction(f"sendops_wcont X22 X18 X8 3") 
  tranPrefixSumNodeLevel__start.writeAction(f"addi X20 X20 64") 
  tranPrefixSumNodeLevel__start.writeAction(f"jmp __for_start_0_condition") 
  tranPrefixSumNodeLevel__start.writeAction(f"__for_start_2_post: yield") 
  
  # Writing code for event PrefixSumNodeLevel::returnFromChild
  tranPrefixSumNodeLevel__returnFromChild = efa.writeEvent('PrefixSumNodeLevel::returnFromChild')
  tranPrefixSumNodeLevel__returnFromChild.writeAction(f"__entry: sub X8 X0 X19") 
  tranPrefixSumNodeLevel__returnFromChild.writeAction(f"sari X19 X19 6") 
  tranPrefixSumNodeLevel__returnFromChild.writeAction(f"addi X19 X19 1") 
  tranPrefixSumNodeLevel__returnFromChild.writeAction(f"addi X7 X18 2704") 
  tranPrefixSumNodeLevel__returnFromChild.writeAction(f"movwrl X9 X18(X19,0,0)") 
  tranPrefixSumNodeLevel__returnFromChild.writeAction(f"add X17 X9 X17") 
  tranPrefixSumNodeLevel__returnFromChild.writeAction(f"subi X16 X16 1") 
  tranPrefixSumNodeLevel__returnFromChild.writeAction(f"bneiu X16 0 __if_returnFromChild_2_post") 
  tranPrefixSumNodeLevel__returnFromChild.writeAction(f"__if_returnFromChild_0_true: movir X19 -1") 
  tranPrefixSumNodeLevel__returnFromChild.writeAction(f"sri X19 X19 1") 
  tranPrefixSumNodeLevel__returnFromChild.writeAction(f"sendr_wcont X1 X19 X0 X17") 
  tranPrefixSumNodeLevel__returnFromChild.writeAction(f"yield_terminate") 
  tranPrefixSumNodeLevel__returnFromChild.writeAction(f"__if_returnFromChild_2_post: yield") 
  
  ## distribute among the lanes
  
  ######################################################
  ###### Writing code for thread PrefixSumUDLevel ######
  ######################################################
  # Writing code for event PrefixSumUDLevel::start
  tranPrefixSumUDLevel__start = efa.writeEvent('PrefixSumUDLevel::start')
  tranPrefixSumUDLevel__start.writeAction(f"__entry: movir X17 0") 
  tranPrefixSumUDLevel__start.writeAction(f"movir X16 64") 
  tranPrefixSumUDLevel__start.writeAction(f"evi X2 X18 PrefixSumUDLevel::returnFromChild 1") 
  tranPrefixSumUDLevel__start.writeAction(f"movir X19 64") 
  tranPrefixSumUDLevel__start.writeAction(f"movir X20 0") 
  tranPrefixSumUDLevel__start.writeAction(f"__for_start_0_condition: bleu X19 X20 __for_start_2_post") 
  tranPrefixSumUDLevel__start.writeAction(f"__for_start_1_body: add X0 X20 X21") 
  tranPrefixSumUDLevel__start.writeAction(f"movir X22 0") 
  tranPrefixSumUDLevel__start.writeAction(f"evlb X22 PrefixSumWorkerUp::start") 
  tranPrefixSumUDLevel__start.writeAction(f"evi X22 X22 255 4") 
  tranPrefixSumUDLevel__start.writeAction(f"ev X22 X22 X21 X21 8") 
  tranPrefixSumUDLevel__start.writeAction(f"sendops_wcont X22 X18 X8 3") 
  tranPrefixSumUDLevel__start.writeAction(f"addi X20 X20 1") 
  tranPrefixSumUDLevel__start.writeAction(f"jmp __for_start_0_condition") 
  tranPrefixSumUDLevel__start.writeAction(f"__for_start_2_post: yield") 
  
  # Writing code for event PrefixSumUDLevel::returnFromChild
  tranPrefixSumUDLevel__returnFromChild = efa.writeEvent('PrefixSumUDLevel::returnFromChild')
  tranPrefixSumUDLevel__returnFromChild.writeAction(f"__entry: sub X8 X0 X20") 
  tranPrefixSumUDLevel__returnFromChild.writeAction(f"addi X20 X20 1") 
  tranPrefixSumUDLevel__returnFromChild.writeAction(f"addi X7 X19 2968") 
  tranPrefixSumUDLevel__returnFromChild.writeAction(f"movwrl X9 X19(X20,0,0)") 
  tranPrefixSumUDLevel__returnFromChild.writeAction(f"add X17 X9 X17") 
  tranPrefixSumUDLevel__returnFromChild.writeAction(f"subi X16 X16 1") 
  tranPrefixSumUDLevel__returnFromChild.writeAction(f"bneiu X16 0 __if_returnFromChild_2_post") 
  tranPrefixSumUDLevel__returnFromChild.writeAction(f"__if_returnFromChild_0_true: movir X20 -1") 
  tranPrefixSumUDLevel__returnFromChild.writeAction(f"sri X20 X20 1") 
  tranPrefixSumUDLevel__returnFromChild.writeAction(f"sendr_wcont X1 X20 X0 X17") 
  tranPrefixSumUDLevel__returnFromChild.writeAction(f"yield_terminate") 
  tranPrefixSumUDLevel__returnFromChild.writeAction(f"__if_returnFromChild_2_post: yield") 
  
  
  #######################################################
  ###### Writing code for thread PrefixSumWorkerUp ######
  #######################################################
  # Writing code for event PrefixSumWorkerUp::start
  tranPrefixSumWorkerUp__start = efa.writeEvent('PrefixSumWorkerUp::start')
  ## determine the numVertices

  tranPrefixSumWorkerUp__start.writeAction(f"__entry: div X9 X10 X20") 
  tranPrefixSumWorkerUp__start.writeAction(f"mod X9 X10 X21") 
  tranPrefixSumWorkerUp__start.writeAction(f"bleu X21 X0 __if_start_1_false") 
  tranPrefixSumWorkerUp__start.writeAction(f"__if_start_0_true: addi X20 X17 1") 
  tranPrefixSumWorkerUp__start.writeAction(f"addi X0 X22 0") 
  tranPrefixSumWorkerUp__start.writeAction(f"jmp __if_start_2_post") 
  tranPrefixSumWorkerUp__start.writeAction(f"__if_start_1_false: addi X20 X17 0") 
  tranPrefixSumWorkerUp__start.writeAction(f"addi X21 X22 0") 
  tranPrefixSumWorkerUp__start.writeAction(f"__if_start_2_post: bneiu X17 0 __if_start_5_post") 
  tranPrefixSumWorkerUp__start.writeAction(f"__if_start_3_true: print 'Nothing to do, returning'") 
  tranPrefixSumWorkerUp__start.writeAction(f"movir X21 0") 
  tranPrefixSumWorkerUp__start.writeAction(f"movir X23 -1") 
  tranPrefixSumWorkerUp__start.writeAction(f"sri X23 X23 1") 
  tranPrefixSumWorkerUp__start.writeAction(f"sendr_wcont X1 X23 X0 X21") 
  tranPrefixSumWorkerUp__start.writeAction(f"yield_terminate") 
  ## set the base addresses

  tranPrefixSumWorkerUp__start.writeAction(f"__if_start_5_post: mul X0 X20 X20") 
  tranPrefixSumWorkerUp__start.writeAction(f"add X20 X22 X22") 
  tranPrefixSumWorkerUp__start.writeAction(f"sli X22 X22 3") 
  tranPrefixSumWorkerUp__start.writeAction(f"sli X22 X22 3") 
  ## size of vertex_t

  tranPrefixSumWorkerUp__start.writeAction(f"add X8 X22 X16") 
  tranPrefixSumWorkerUp__start.writeAction(f"addi X16 X16 8") 
  ## point to where the degree is

  tranPrefixSumWorkerUp__start.writeAction(f"movir X18 0") 
  tranPrefixSumWorkerUp__start.writeAction(f"movir X19 0") 
  tranPrefixSumWorkerUp__start.writeAction(f"movir X22 0") 
  tranPrefixSumWorkerUp__start.writeAction(f"__for_start_6_condition: clti X22 X20 32") 
  tranPrefixSumWorkerUp__start.writeAction(f"cgti X17 X21 0") 
  tranPrefixSumWorkerUp__start.writeAction(f"and X20 X21 X20") 
  tranPrefixSumWorkerUp__start.writeAction(f"beqiu X20 0 __for_start_8_post") 
  ## print("Reading: %p", srcBase);

  tranPrefixSumWorkerUp__start.writeAction(f"__for_start_7_body: send_dmlm_ld_wret X16 PrefixSumWorkerUp::returnFromRead 1 X20") 
  tranPrefixSumWorkerUp__start.writeAction(f"addi X16 X16 64") 
  tranPrefixSumWorkerUp__start.writeAction(f"subi X17 X17 1") 
  tranPrefixSumWorkerUp__start.writeAction(f"addi X18 X18 1") 
  tranPrefixSumWorkerUp__start.writeAction(f"addi X22 X22 1") 
  tranPrefixSumWorkerUp__start.writeAction(f"jmp __for_start_6_condition") 
  tranPrefixSumWorkerUp__start.writeAction(f"__for_start_8_post: yield") 
  
  ## event returnFromRead(uint64_t degree, uint64_t edgeBef, uint64_t vertID, uint64_t* readAddress) {
  # Writing code for event PrefixSumWorkerUp::returnFromRead
  tranPrefixSumWorkerUp__returnFromRead = efa.writeEvent('PrefixSumWorkerUp::returnFromRead')
  tranPrefixSumWorkerUp__returnFromRead.writeAction(f"__entry: add X19 X8 X19") 
  ## #ifdef DEBUG_PREFIXSUM

  ##     print("Vertex returned: ID: %lu, edgeBef: :%lu, degree: %lu, currentPartSum: %lu", vertID, edgeBef, degree, partialSum);

  ## #endif

  tranPrefixSumWorkerUp__returnFromRead.writeAction(f"beqiu X17 0 __if_returnFromRead_1_false") 
  tranPrefixSumWorkerUp__returnFromRead.writeAction(f"__if_returnFromRead_0_true: send_dmlm_ld X16 X2 1") 
  tranPrefixSumWorkerUp__returnFromRead.writeAction(f"addi X16 X16 64") 
  tranPrefixSumWorkerUp__returnFromRead.writeAction(f"subi X17 X17 1") 
  tranPrefixSumWorkerUp__returnFromRead.writeAction(f"jmp __if_returnFromRead_2_post") 
  tranPrefixSumWorkerUp__returnFromRead.writeAction(f"__if_returnFromRead_1_false: subi X18 X18 1") 
  tranPrefixSumWorkerUp__returnFromRead.writeAction(f"bneiu X18 0 __if_returnFromRead_2_post") 
  ## inform the broadcast library that we are done

  tranPrefixSumWorkerUp__returnFromRead.writeAction(f"__if_returnFromRead_3_true: movir X22 -1") 
  tranPrefixSumWorkerUp__returnFromRead.writeAction(f"sri X22 X22 1") 
  tranPrefixSumWorkerUp__returnFromRead.writeAction(f"sendr_wcont X1 X22 X0 X19") 
  tranPrefixSumWorkerUp__returnFromRead.writeAction(f"yield_terminate") 
  tranPrefixSumWorkerUp__returnFromRead.writeAction(f"__if_returnFromRead_2_post: yield") 
  