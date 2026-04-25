from linker.EFAProgram import efaProgram

## UDWeave version: 7808cc0 (2026-04-24)

## Global constants

@efaProgram
def EFA_broadcast(efa):
  efa.code_level = 'machine'
  state0 = efa.State("udweave_init") #Only one state code 
  efa.add_initId(state0.state_id)
  ## Static declarations
  ## Scoped Variable "counter" uses Register X16, scope (0)
  ## Scoped Variable "sum" uses Register X17, scope (0)
  ## Scoped Variable "counter" uses Register X16, scope (0)
  ## Scoped Variable "sum" uses Register X17, scope (0)
  ## Scoped Variable "counter" uses Register X16, scope (0)
  ## Scoped Variable "sum" uses Register X17, scope (0)
  ## Scoped Variable "counter" uses Register X16, scope (0)
  ## Scoped Variable "sum" uses Register X17, scope (0)
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
  ## #define DEBUG_BROADCAST
  
  ###############################################
  ###### Writing code for thread Broadcast ######
  ###############################################
  # Writing code for event Broadcast::start
  tranBroadcast__start = efa.writeEvent('Broadcast::start')
  tranBroadcast__start.writeAction(f"__entry: addi X7 X18 1664") 
  tranBroadcast__start.writeAction(f"addi X18 X19 8") 
  tranBroadcast__start.writeAction(f"bcpyoli X9 X19 7") 
  tranBroadcast__start.writeAction(f"movir X17 0") 
  tranBroadcast__start.writeAction(f"evi X2 X19 Broadcast::returnFromChild 1") 
  tranBroadcast__start.writeAction(f"movir X20 65536") 
  tranBroadcast__start.writeAction(f"bgtu X20 X8 __if_start_2_post") 
  ## determine the number of lanes that the next level of tree nodes have to handle each

  tranBroadcast__start.writeAction(f"__if_start_0_true: sari X8 X20 5") 
  tranBroadcast__start.writeAction(f"movrl X20 0(X18) 0 8") 
  tranBroadcast__start.writeAction(f"movir X16 0") 
  tranBroadcast__start.writeAction(f"movir X21 0") 
  tranBroadcast__start.writeAction(f"__for_start_3_condition: bleu X8 X21 __for_start_5_post") 
  tranBroadcast__start.writeAction(f"__for_start_4_body: add X0 X21 X22") 
  tranBroadcast__start.writeAction(f"movir X23 0") 
  tranBroadcast__start.writeAction(f"evlb X23 BroadcastAboveNodeLevel::start") 
  tranBroadcast__start.writeAction(f"evi X23 X23 255 4") 
  tranBroadcast__start.writeAction(f"ev X23 X23 X22 X22 8") 
  tranBroadcast__start.writeAction(f"send_wcont X23 X19 X18 8") 
  tranBroadcast__start.writeAction(f"addi X16 X16 1") 
  tranBroadcast__start.writeAction(f"add X21 X20 X21") 
  tranBroadcast__start.writeAction(f"jmp __for_start_3_condition") 
  tranBroadcast__start.writeAction(f"__for_start_5_post: yield") 
  tranBroadcast__start.writeAction(f"__if_start_2_post: movir X16 1") 
  tranBroadcast__start.writeAction(f"movir X20 0") 
  tranBroadcast__start.writeAction(f"evlb X20 BroadcastAboveNodeLevel::start") 
  tranBroadcast__start.writeAction(f"evi X20 X20 255 4") 
  tranBroadcast__start.writeAction(f"ev X20 X20 X0 X0 8") 
  tranBroadcast__start.writeAction(f"movrl X8 0(X18) 0 8") 
  tranBroadcast__start.writeAction(f"send_wcont X20 X19 X18 8") 
  tranBroadcast__start.writeAction(f"yield") 
  
  # Writing code for event Broadcast::returnFromChild
  tranBroadcast__returnFromChild = efa.writeEvent('Broadcast::returnFromChild')
  tranBroadcast__returnFromChild.writeAction(f"__entry: subi X16 X16 1") 
  tranBroadcast__returnFromChild.writeAction(f"add X17 X8 X17") 
  tranBroadcast__returnFromChild.writeAction(f"bneiu X16 0 __if_returnFromChild_2_post") 
  tranBroadcast__returnFromChild.writeAction(f"__if_returnFromChild_0_true: addi X7 X18 1664") 
  tranBroadcast__returnFromChild.writeAction(f"movrl X17 0(X18) 0 8") 
  tranBroadcast__returnFromChild.writeAction(f"addi X7 X18 0") 
  tranBroadcast__returnFromChild.writeAction(f"movir X19 1") 
  tranBroadcast__returnFromChild.writeAction(f"movrl X19 0(X18) 0 8") 
  tranBroadcast__returnFromChild.writeAction(f"yield_terminate") 
  tranBroadcast__returnFromChild.writeAction(f"__if_returnFromChild_2_post: yield") 
  
  ## distribute to the nodes
  
  #############################################################
  ###### Writing code for thread BroadcastAboveNodeLevel ######
  #############################################################
  # Writing code for event BroadcastAboveNodeLevel::start
  tranBroadcastAboveNodeLevel__start = efa.writeEvent('BroadcastAboveNodeLevel::start')
  tranBroadcastAboveNodeLevel__start.writeAction(f"__entry: addi X7 X18 1664") 
  tranBroadcastAboveNodeLevel__start.writeAction(f"addi X18 X19 8") 
  tranBroadcastAboveNodeLevel__start.writeAction(f"bcpyoli X9 X19 7") 
  tranBroadcastAboveNodeLevel__start.writeAction(f"movir X19 2048") 
  tranBroadcastAboveNodeLevel__start.writeAction(f"movrl X19 0(X18) 0 8") 
  tranBroadcastAboveNodeLevel__start.writeAction(f"movir X16 0") 
  tranBroadcastAboveNodeLevel__start.writeAction(f"movir X17 0") 
  tranBroadcastAboveNodeLevel__start.writeAction(f"evi X2 X19 BroadcastAboveNodeLevel::returnFromChild 1") 
  tranBroadcastAboveNodeLevel__start.writeAction(f"movir X20 65536") 
  tranBroadcastAboveNodeLevel__start.writeAction(f"bleu X20 X8 __if_start_2_post") 
  tranBroadcastAboveNodeLevel__start.writeAction(f"__if_start_0_true: addi X8 X20 0") 
  tranBroadcastAboveNodeLevel__start.writeAction(f"__if_start_2_post: movir X21 0") 
  tranBroadcastAboveNodeLevel__start.writeAction(f"__for_start_3_condition: bleu X20 X21 __for_start_5_post") 
  tranBroadcastAboveNodeLevel__start.writeAction(f"__for_start_4_body: add X0 X21 X22") 
  tranBroadcastAboveNodeLevel__start.writeAction(f"movir X23 0") 
  tranBroadcastAboveNodeLevel__start.writeAction(f"evlb X23 BroadcastNodeLevel::start") 
  tranBroadcastAboveNodeLevel__start.writeAction(f"evi X23 X23 255 4") 
  tranBroadcastAboveNodeLevel__start.writeAction(f"ev X23 X23 X22 X22 8") 
  tranBroadcastAboveNodeLevel__start.writeAction(f"send_wcont X23 X19 X18 8") 
  tranBroadcastAboveNodeLevel__start.writeAction(f"addi X16 X16 1") 
  tranBroadcastAboveNodeLevel__start.writeAction(f"addi X21 X21 2048") 
  tranBroadcastAboveNodeLevel__start.writeAction(f"jmp __for_start_3_condition") 
  tranBroadcastAboveNodeLevel__start.writeAction(f"__for_start_5_post: yield") 
  
  # Writing code for event BroadcastAboveNodeLevel::returnFromChild
  tranBroadcastAboveNodeLevel__returnFromChild = efa.writeEvent('BroadcastAboveNodeLevel::returnFromChild')
  tranBroadcastAboveNodeLevel__returnFromChild.writeAction(f"__entry: subi X16 X16 1") 
  tranBroadcastAboveNodeLevel__returnFromChild.writeAction(f"add X17 X8 X17") 
  tranBroadcastAboveNodeLevel__returnFromChild.writeAction(f"bneiu X16 0 __if_returnFromChild_2_post") 
  tranBroadcastAboveNodeLevel__returnFromChild.writeAction(f"__if_returnFromChild_0_true: movir X18 -1") 
  tranBroadcastAboveNodeLevel__returnFromChild.writeAction(f"sri X18 X18 1") 
  tranBroadcastAboveNodeLevel__returnFromChild.writeAction(f"sendr_wcont X1 X18 X17 X17") 
  tranBroadcastAboveNodeLevel__returnFromChild.writeAction(f"yield_terminate") 
  tranBroadcastAboveNodeLevel__returnFromChild.writeAction(f"__if_returnFromChild_2_post: yield") 
  
  ## distribute among UDs
  
  ########################################################
  ###### Writing code for thread BroadcastNodeLevel ######
  ########################################################
  # Writing code for event BroadcastNodeLevel::start
  tranBroadcastNodeLevel__start = efa.writeEvent('BroadcastNodeLevel::start')
  tranBroadcastNodeLevel__start.writeAction(f"__entry: addi X7 X18 1664") 
  tranBroadcastNodeLevel__start.writeAction(f"addi X18 X19 8") 
  tranBroadcastNodeLevel__start.writeAction(f"bcpyoli X9 X19 7") 
  tranBroadcastNodeLevel__start.writeAction(f"movir X19 64") 
  tranBroadcastNodeLevel__start.writeAction(f"movrl X19 0(X18) 0 8") 
  tranBroadcastNodeLevel__start.writeAction(f"movir X16 0") 
  tranBroadcastNodeLevel__start.writeAction(f"movir X17 0") 
  tranBroadcastNodeLevel__start.writeAction(f"evi X2 X19 BroadcastNodeLevel::returnFromChild 1") 
  tranBroadcastNodeLevel__start.writeAction(f"movir X20 0") 
  tranBroadcastNodeLevel__start.writeAction(f"__for_start_0_condition: bleu X8 X20 __for_start_2_post") 
  tranBroadcastNodeLevel__start.writeAction(f"__for_start_1_body: add X0 X20 X21") 
  tranBroadcastNodeLevel__start.writeAction(f"movir X22 0") 
  tranBroadcastNodeLevel__start.writeAction(f"evlb X22 BroadcastUDLevel::start") 
  tranBroadcastNodeLevel__start.writeAction(f"evi X22 X22 255 4") 
  tranBroadcastNodeLevel__start.writeAction(f"ev X22 X22 X21 X21 8") 
  tranBroadcastNodeLevel__start.writeAction(f"send_wcont X22 X19 X18 8") 
  tranBroadcastNodeLevel__start.writeAction(f"addi X16 X16 1") 
  tranBroadcastNodeLevel__start.writeAction(f"addi X20 X20 64") 
  tranBroadcastNodeLevel__start.writeAction(f"jmp __for_start_0_condition") 
  tranBroadcastNodeLevel__start.writeAction(f"__for_start_2_post: yield") 
  
  # Writing code for event BroadcastNodeLevel::returnFromChild
  tranBroadcastNodeLevel__returnFromChild = efa.writeEvent('BroadcastNodeLevel::returnFromChild')
  tranBroadcastNodeLevel__returnFromChild.writeAction(f"__entry: subi X16 X16 1") 
  tranBroadcastNodeLevel__returnFromChild.writeAction(f"add X17 X8 X17") 
  tranBroadcastNodeLevel__returnFromChild.writeAction(f"bneiu X16 0 __if_returnFromChild_2_post") 
  tranBroadcastNodeLevel__returnFromChild.writeAction(f"__if_returnFromChild_0_true: movir X18 -1") 
  tranBroadcastNodeLevel__returnFromChild.writeAction(f"sri X18 X18 1") 
  tranBroadcastNodeLevel__returnFromChild.writeAction(f"sendr_wcont X1 X18 X17 X17") 
  tranBroadcastNodeLevel__returnFromChild.writeAction(f"yield_terminate") 
  tranBroadcastNodeLevel__returnFromChild.writeAction(f"__if_returnFromChild_2_post: yield") 
  
  ## distribute among the lanes
  
  ######################################################
  ###### Writing code for thread BroadcastUDLevel ######
  ######################################################
  # Writing code for event BroadcastUDLevel::start
  tranBroadcastUDLevel__start = efa.writeEvent('BroadcastUDLevel::start')
  tranBroadcastUDLevel__start.writeAction(f"__entry: movir X17 0") 
  tranBroadcastUDLevel__start.writeAction(f"addi X8 X16 0") 
  tranBroadcastUDLevel__start.writeAction(f"evi X2 X18 BroadcastUDLevel::returnFromChild 1") 
  tranBroadcastUDLevel__start.writeAction(f"movir X19 0") 
  tranBroadcastUDLevel__start.writeAction(f"__for_start_0_condition: bleu X8 X19 __for_start_2_post") 
  tranBroadcastUDLevel__start.writeAction(f"__for_start_1_body: add X19 X0 X20") 
  tranBroadcastUDLevel__start.writeAction(f"ev X9 X20 X20 X20 8") 
  tranBroadcastUDLevel__start.writeAction(f"sendops_wcont X20 X18 X10 8") 
  tranBroadcastUDLevel__start.writeAction(f"addi X19 X19 1") 
  tranBroadcastUDLevel__start.writeAction(f"jmp __for_start_0_condition") 
  tranBroadcastUDLevel__start.writeAction(f"__for_start_2_post: yield") 
  
  # Writing code for event BroadcastUDLevel::returnFromChild
  tranBroadcastUDLevel__returnFromChild = efa.writeEvent('BroadcastUDLevel::returnFromChild')
  tranBroadcastUDLevel__returnFromChild.writeAction(f"__entry: subi X16 X16 1") 
  tranBroadcastUDLevel__returnFromChild.writeAction(f"add X17 X8 X17") 
  tranBroadcastUDLevel__returnFromChild.writeAction(f"bneiu X16 0 __if_returnFromChild_2_post") 
  tranBroadcastUDLevel__returnFromChild.writeAction(f"__if_returnFromChild_0_true: movir X19 -1") 
  tranBroadcastUDLevel__returnFromChild.writeAction(f"sri X19 X19 1") 
  tranBroadcastUDLevel__returnFromChild.writeAction(f"sendr_wcont X1 X19 X17 X17") 
  tranBroadcastUDLevel__returnFromChild.writeAction(f"yield_terminate") 
  tranBroadcastUDLevel__returnFromChild.writeAction(f"__if_returnFromChild_2_post: yield") 
  