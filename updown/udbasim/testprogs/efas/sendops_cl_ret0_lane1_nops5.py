
from EFA_v2 import *
def sendops_cl_ret0_lane1_nops5():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "start_event": 0,
        "send_event": 1,
        "cont_event": 2,
        "dram_return": 3,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['start_event'])

    tran0.writeAction("addi X8 X16 0")
    tran0.writeAction("addi X9 X17 0")
    tran0.writeAction("addi X10 X18 0")
    tran0.writeAction("addi X11 X19 0")
    tran0.writeAction("addi X12 X20 0")
    tran0.writeAction("addi X13 X21 0")
    tran0.writeAction("addi X14 X22 0")
    tran0.writeAction("addi X15 X23 0")
    
    tran0.writeAction("add X7 X16 X24") # local SP pointer, to read data from
    # update to the send event
    tran0.writeAction("evi X2 X31 1 1")    # update event_label
    tran0.writeAction("evi X31 X31 255 4") # update tid, new thread
    # construct Xc based on outside mode1
    # mode1==1, auto send_wret, Xc is the cont_label
    tran0.writeAction("evlb X25 2")

    # may or maynot write to SP
    
    
    # send events after write to SP
    tran0.writeAction("evi X31 X31 0 8")
    tran0.writeAction("sendops X31 X25 X8 5 1")

    
    
    # may or maynot terminate
    tran0.writeAction("yieldt")

    
    # only send* will use tran1
    tran1 = state.writeTransition("eventCarry", state, state, event_map['send_event'])
    # for sendr, obs are Xd, Xoffset, X1
    tran1.writeAction("addi X8 X16 8") # first 8 bytes are for flag
    tran1.writeAction("movir X24 0") # reset Xptr
    tran1.writeAction("add X7 X16 X24") # starting from base + Xoffset
    # write data in the SP, depending on how may operands received
    tran1.writeAction("movrl X8 0(X24) 1 8")
    tran1.writeAction("movrl X9 0(X24) 1 8")
    tran1.writeAction("movrl X10 0(X24) 1 8")
    tran1.writeAction("movrl X11 0(X24) 1 8")
    tran1.writeAction("movrl X12 0(X24) 1 8")
      
    # tran1 now can decide send_reply, send several values back
    

    
    # terminate and write termination flag to SP, Xbase[0] = flag
    tran1.writeAction("movir X30 1") # set flag to 1
    tran1.writeAction("addi X7 X24 0") # starting from base
    tran1.writeAction("movrl X30 0(X24) 0 8") # write flag the beginning of the SP
    tran1.writeAction("yieldt") # for sure e1 will term
    
    
    tran2= state.writeTransition("eventCarry", state, state, event_map['cont_event'])
    tran2.writeAction("addi X8 X16 8") # 
    tran2.writeAction("movir X24 0") # reset Xptr
    tran2.writeAction("add X7 X16 X24") # starting from base + Xoffset
    # get some values back, store them in SP
    
    # for sure is yieldt
    tran2.writeAction("yield")
 
    
    # only sendm* will use tran3
    tran3 = state.writeTransition("eventCarry", state, state, event_map['dram_return'])
    tran3.writeAction("movir X24 8") # reset Xptr, now always starts from the base + 8
     # always write to SP after the flag
    
    # terminate and write termination flag to SP, Xbase[0] = flag
    tran3.writeAction("movir X30 1") # set flag to 1
    tran3.writeAction("addi X7 X24 0") # starting from base
    tran3.writeAction("movrl X30 0(X24) 0 8") # write flag the beginning of the SP
    tran3.writeAction("yieldt") # for sure e1 will term
     # only run once, don't bother yield
    return efa
    