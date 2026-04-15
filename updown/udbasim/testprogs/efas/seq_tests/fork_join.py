from EFA_v2 import *

def fork_join():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_parent": 0,
        "forked_child": 1,
        "child_join": 2,
    }
    
    # launch_parent
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_parent'])
    INIT_OFFSET = "X16"
    NUM_LANES = "X17"
    NUM_THREADS_PER_LANE = "X18"
    
    WID = "X19"
    I = "X20"
    J = "X21"
    EVW = "X22"
    CW = "X23"
    RESULT = "X24"
    TOTAL_THREADS = "X25"
    NTHR = "X26"
    # OB_0 = offset, OB_1 = num_lanes, OB_2 = num_threads_per_lane
    printu(tran0, f"'Start, parent thread forking: lid=%ld' LID")
    tran0.writeAction(f"addi X8 {INIT_OFFSET} 0")
    tran0.writeAction(f"addi X9 {NUM_LANES} 0")
    tran0.writeAction(f"addi X10 {NUM_THREADS_PER_LANE} 0")
    tran0.writeAction(f"addi X11 {TOTAL_THREADS} 0")
    tran0.writeAction(f"movir {NTHR} 0")
    tran0.writeAction(f"movir {RESULT} 0")
    tran0.writeAction(f"movir {WID} 0")
    tran0.writeAction(f"evi X2 {CW} 2 1") # send_reply CW
    # loop over num lanes; then loop over num threads per lane
    tran0.writeAction(f"movir {I} 0")
    tran0.writeAction(f"lane_loop: ble {NUM_LANES} {I} lane_done")
    tran0.writeAction(f"movir {J} 0")
    tran0.writeAction(f"thread_loop: ble {NUM_THREADS_PER_LANE} {J} thread_done")
    # construct the event word and the send the event
    
    tran0.writeAction(f"evi X2 {EVW} {event_map['forked_child']} 1") # parent fork
    tran0.writeAction(f"evi {EVW} {EVW} 255 4") # new thread
    tran0.writeAction(f"ev {EVW} {EVW} {I} {I} 8") # lane id
    
    # tran0.writeAction(f"sendr {EVW} {CW} {WID} {J} 0")
    tran0.writeAction(f"sendr_wret {EVW} {event_map['child_join']} {WID} {J} {INIT_OFFSET}")
    tran0.writeAction(f"addi {WID} {WID} 1")
    tran0.writeAction(f"addi {J} {J} 1")
    tran0.writeAction(f"jmp thread_loop")
    tran0.writeAction(f"thread_done: addi {I} {I} 1")
    tran0.writeAction(f"jmp lane_loop")
    tran0.writeAction(f"lane_done: yield")
    
    tran1 = state.writeTransition("eventCarry", state, state, event_map['forked_child'])
    # OB_0 WID, OB_1 = INIT_OFFSET
    SPPTR = "X16"
    OFFSET = "X17"
    V = "X18"
    WID = "X19"
    TID = "X20"
    V0 = "X21"
    tran1.writeAction(f"addi X8 {WID} 0")
    tran1.writeAction(f"addi X9 {TID} 0")
    printu(tran1, f"'Start, child thread:lid=%ld wid=%ld tid=%ld' LID {WID} {TID}")
    # get the ptr for the SP
    tran1.writeAction(f"movir {SPPTR} 8") # init_offset = 8
    tran1.writeAction(f"sli {TID} {OFFSET} 3") # offset = tid << 3
    tran1.writeAction(f"add X7 {OFFSET} {SPPTR}") # SPTR = init_offset + offset
    tran1.writeAction(f"movlr 8({SPPTR}) {V} 0 8") # read the value from SPTR, first is used for flag
    # arithmetics, v = (v + 127 - 64) * 3 / 3 + v + v + v - v
    tran1.writeAction(f"addi {V} {V} 127")
    tran1.writeAction(f"subi {V} {V} 64")
    tran1.writeAction(f"muli {V} {V} 3")
    tran1.writeAction(f"divi {V} {V} 3")
    tran1.writeAction(f"addi {V} {V0} 0")
    tran1.writeAction(f"add {V} {V} {V}")
    tran1.writeAction(f"add {V} {V} {V}")
    tran1.writeAction(f"add {V} {V} {V}")
    tran1.writeAction(f"sub {V} {V0} {V}")
    tran1.writeAction(f"sendr_reply {WID} {V} {TID}")
    tran1.writeAction(f"yieldt")
    
    tran2 = state.writeTransition("eventCarry", state, state, event_map['child_join'])
    # OB_0 = WID, OB_1 = V, OB_2 = TID
    SPPTR = "X16"
    RESULT = "X24"
    TOTAL_THREADS = "X25" # from t0
    
    NTHR = "X26"
    WID = "X19"
    V = "X20"
    TID = "X21"
    
  
    
    tran2.writeAction(f"addi X8 {WID} 0")
    tran2.writeAction(f"addi X9 {V} 0")
    tran2.writeAction(f"addi X10 {TID} 0")
   
    tran2.writeAction(f"add {RESULT} {V} {RESULT}")
    tran2.writeAction(f"addi {NTHR} {NTHR} 1")
    tran2.writeAction(f"beq {NTHR} {TOTAL_THREADS} done")
    tran2.writeAction(f"yield")
    # write results to SP 0
    tran2.writeAction(f"done: movir {SPPTR} 0")
    # tran2.writeAction(f"print 'results: %ld' {RESULT}")
    tran2.writeAction(f"add X7 {SPPTR} {SPPTR}")
    tran2.writeAction(f"movrl {RESULT} 0({SPPTR}) 0 8")
    printu(tran2, f"'Done, result = %ld' {RESULT}")
    tran2.writeAction(f"yieldt")
    return efa
    
    
def multilevel_fork_join():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "fork": 0,
        "join": 1,
        "task": 2,
    }
    
    tran0 = state.writeTransition("eventCarry", state, state, event_map['fork'])
    # OB_0 = LOG2_NUM_FORKS, OB_1 = LEVEL, OB_2 = NUM_DEVICES, OB_3 = RANDOM_NUM
    LOG2_NUM_FORKS = "X16"
    LEVEL = "X17"
    NUM_DEVICES = "X18"
    RANDOM_NUM = "X19"
    MAX_LEVEL = "X27"
    
    NUM_FORKS = "X20"
    I = "X21"
    TNWID = "X22"
    TEMP = "X23"
    SPPTR = "X24"
    RESULT = "X25"
    NUM_JOIN = "X26"
    
    
    # do the fork of first level, check if the level is 0
    tran0.writeAction(f"addi X8 {LOG2_NUM_FORKS} 0")
    tran0.writeAction(f"addi X9 {LEVEL} 0")
    tran0.writeAction(f"addi X10 {NUM_DEVICES} 0")
    tran0.writeAction(f"addi X11 {RANDOM_NUM} 0")
    tran0.writeAction(f"addi X12 {MAX_LEVEL} 0")
    
    tran0.writeAction(f"movir {RESULT} 0")
    tran0.writeAction(f"movir {NUM_JOIN} 0")
    printu(tran0, f"'==========================LEVEL %ld=========================' {LEVEL}")
    printu(tran0, f"'Start, parent thread forking: lid=%ld, LOG2_NUM_FORKS=%ld, LEVEL=%ld, NUM_DEVICES=%ld, RANDOM_NUM=%ld' LID {LOG2_NUM_FORKS} {LEVEL} {NUM_DEVICES} {RANDOM_NUM}")
    tran0.writeAction(f"beq {LEVEL} 0 do_task")
    # write values to the spm for further send instruction
    tran0.writeAction(f"movir {SPPTR} 8") # reset the spm ptr
    tran0.writeAction(f"add X7 {SPPTR} {SPPTR}") # SPTR = base(X7)
    tran0.writeAction(f"movrl {LOG2_NUM_FORKS} 0({SPPTR}) 0 8") # write log2_num_forks, starting by offset=8
    tran0.writeAction(f"subi {LEVEL} {TEMP} 1") # temp = level - 1
    tran0.writeAction(f"movrl {TEMP} 8({SPPTR}) 0 8") # write level, starting by offset=16
    tran0.writeAction(f"movrl {NUM_DEVICES} 16({SPPTR}) 0 8") # write num_devices, starting by offset=24
    tran0.writeAction(f"movrl {RANDOM_NUM} 24({SPPTR}) 0 8") # write random_num, starting by offset=32 
    tran0.writeAction(f"movrl {MAX_LEVEL} 32({SPPTR}) 0 8") # write max_level, starting by offset=40
    
    # fork; num_forks this level = 1 << log2_num_forks; tnwid = LID + 1 << log2_num_forks * (level - 1)
    tran0.writeAction(f"movir {NUM_FORKS} 1")
    tran0.writeAction(f"sl {NUM_FORKS} {LOG2_NUM_FORKS} {NUM_FORKS}")
    printu(tran0, f"'NUM_FORKS = %ld, LOG2=%ld' {NUM_FORKS} {LOG2_NUM_FORKS}")
    # loop over num_forks and send the event
    tran0.writeAction(f"movir {I} 0")
    tran0.writeAction(f"fork_loop: ble {NUM_FORKS} {I} fork_done")
    # first get the tnwid = LID + 1 << log2_num_forks << (level - 1)
    tran0.writeAction(f"movir {TNWID} 1")
    tran0.writeAction(f"subi {LEVEL} {TEMP} 1") # temp = level - 1
    tran0.writeAction(f"mul {LOG2_NUM_FORKS} {TEMP} {TEMP}") # temp = log2_num_forks * (level - 1)
    tran0.writeAction(f"sl {I} {TEMP} {TNWID}") # tnwid = 1 << temp
    tran0.writeAction(f"add {TNWID} LID {TNWID}") # tnwid = tnwid + LID
    tran0.writeAction(f"mod {TNWID} {NUM_DEVICES} {TNWID}") # tnwid = tnwid % num_devices
    # contruct the event word and send the event, write the data to the spm
    tran0.writeAction(f"evi X2 {TEMP} {event_map['fork']} 1") # label = fork
    tran0.writeAction(f"evi {TEMP} {TEMP} 255 4") # new thread
    tran0.writeAction(f"ev {TEMP} {TEMP} {TNWID} {TNWID} 8") # lane id
    printu(tran0, f"'Forking: lid=%ld, TNWID=%ld, LOG2_NUM_FORKS=%ld, I=%ld, NUM_FORKS=%ld' LID {TNWID} {LOG2_NUM_FORKS} {I} {NUM_FORKS}")
    tran0.writeAction(f"send_wret {TEMP} {event_map['join']} {SPPTR} 5") # send the event with return
    tran0.writeAction(f"addi {I} {I} 1")
    tran0.writeAction(f"jmp fork_loop")
    tran0.writeAction(f"fork_done: yield")
    
    tran0.writeAction(f"do_task: movir {SPPTR} 8") # reset the spm ptr = 8
    tran0.writeAction(f"add X7 {SPPTR} {SPPTR}") # SPTR = base(X7) + 8
    # do some arithmetics on the random number, then save to the spm, send_reply back reading that number
    tran0.writeAction(f"movrl {RANDOM_NUM} 0({SPPTR}) 0 8") # write random_num, starting by offset=8
    tran0.writeAction(f"evi X2 {TEMP} {event_map['task']} 1") # label = task
    tran0.writeAction(f"evi {TEMP} {TEMP} 255 4") # new thread
    tran0.writeAction(f"movir {NUM_FORKS} 1") # only expect one reply
    tran0.writeAction(f"send_wret {TEMP} {event_map['join']} {SPPTR} 1") # send this random number to task event
    tran0.writeAction(f"yield")
    
    tran1 = state.writeTransition("eventCarry", state, state, event_map['join'])
    # OB_0 = RESULT or RANDOM_NUM
    LEVEL = "X17"
    NUM_FORKS = "X20"
    RESULT = "X25"
    NUM_JOIN = "X26"
    MAX_LEVEL = "X27"
    tran1.writeAction(f"add X8 {RESULT} {RESULT}")
    tran1.writeAction(f"addi {NUM_JOIN} {NUM_JOIN} 1")
    printu(tran1, f"'Joining: Level=%ld, lid=%ld, RESULT=%ld, NUM_JOIN=%ld' {LEVEL} LID {RESULT} {NUM_JOIN}")
    tran1.writeAction(f"beq {NUM_JOIN} {NUM_FORKS} done")
    tran1.writeAction(f"yield")
    tran1.writeAction(f"done: movir {SPPTR} 8")
    tran1.writeAction(f"add X7 {SPPTR} {SPPTR}")
    tran1.writeAction(f"movrl {RESULT} 0({SPPTR}) 0 8")
    printu(tran1, f"'LEVEL=%ld, NUM_JOIN=%ld, NUM_FORKS=%ld' {LEVEL} {NUM_JOIN} {NUM_FORKS}")
    tran1.writeAction(f"beq {LEVEL} {MAX_LEVEL} terminate")
    printu(tran1, f"'Done, result = %ld' {RESULT}")
    tran1.writeAction(f"send_reply {SPPTR} 1")
    tran1.writeAction(f"yieldt")
    tran1.writeAction(f"terminate: print 'Root Done, result = %ld' {RESULT}")
    tran1.writeAction(f"movir {SPPTR} 0")
    tran1.writeAction(f"add X7 {SPPTR} {SPPTR}")
    tran1.writeAction(f"movir {TEMP} 1")
    tran1.writeAction(f"movrl {RESULT} 0({SPPTR}) 0 8")
    tran1.writeAction(f"yieldt")
    
    
    
    tran2 = state.writeTransition("eventCarry", state, state, event_map['task'])
    # OB_0 = RADOM_NUM
    V = "X28"
    V0 = "X29"
    tran2.writeAction(f"movir {SPPTR} 8") # reset the spm ptr = 8
    tran2.writeAction(f"add X7 {SPPTR} {SPPTR}")
    tran2.writeAction(f"addi X8 {V} 0")
    printu(tran2, f"'Task: lid=%ld, V=%ld' LID {V}")
    tran2.writeAction(f"addi {V} {V} 127")
    tran2.writeAction(f"subi {V} {V} 64")
    tran2.writeAction(f"muli {V} {V} 3")
    tran2.writeAction(f"divi {V} {V} 3")
    tran2.writeAction(f"addi {V} {V0} 0")
    tran2.writeAction(f"add {V} {V} {V}")
    tran2.writeAction(f"add {V} {V} {V}")
    tran2.writeAction(f"add {V} {V} {V}")
    tran2.writeAction(f"sub {V} {V0} {V}")
    tran2.writeAction(f"movrl {V} 0({SPPTR}) 0 8") # write random_num, starting by offset=8
    printu(tran2, f"'Task Done, result = %ld' {V}")
    tran2.writeAction(f"send_reply {SPPTR} 1")
    tran2.writeAction(f"yieldt")
    
    return efa

def printu(tran, msg):
    return None
    return tran.writeAction(f"print {msg}")