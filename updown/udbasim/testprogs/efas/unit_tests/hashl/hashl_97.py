from EFA_v2 import *
def hashl_97():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3803551374222281967, 2215019371209738488, -2885313737054118987]
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movir X17 13512")
    tran0.writeAction("slorii X17 X17 12 3805")
    tran0.writeAction("slorii X17 X17 12 673")
    tran0.writeAction("slorii X17 X17 12 1916")
    tran0.writeAction("slorii X17 X17 12 3311")
    tran0.writeAction("movrl X17 0(X16) 1 8")
    tran0.writeAction("movir X17 7869")
    tran0.writeAction("slorii X17 X17 12 1350")
    tran0.writeAction("slorii X17 X17 12 487")
    tran0.writeAction("slorii X17 X17 12 2316")
    tran0.writeAction("slorii X17 X17 12 2296")
    tran0.writeAction("movrl X17 0(X16) 1 8")
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movir X17 55285")
    tran0.writeAction("slorii X17 X17 12 1255")
    tran0.writeAction("slorii X17 X17 12 373")
    tran0.writeAction("slorii X17 X17 12 1369")
    tran0.writeAction("slorii X17 X17 12 2997")
    tran0.writeAction("hashl X16 X17 2")
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movrl X17 0(X16) 0 8")
    tran0.writeAction("yieldt")
    return efa
