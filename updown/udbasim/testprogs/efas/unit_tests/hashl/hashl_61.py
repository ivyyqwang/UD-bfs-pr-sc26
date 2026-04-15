from EFA_v2 import *
def hashl_61():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4926142704195100372, -500628514871672110]
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movir X17 17501")
    tran0.writeAction("slorii X17 X17 12 715")
    tran0.writeAction("slorii X17 X17 12 140")
    tran0.writeAction("slorii X17 X17 12 1765")
    tran0.writeAction("slorii X17 X17 12 3796")
    tran0.writeAction("movrl X17 0(X16) 1 8")
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movir X17 63757")
    tran0.writeAction("slorii X17 X17 12 1680")
    tran0.writeAction("slorii X17 X17 12 1190")
    tran0.writeAction("slorii X17 X17 12 2632")
    tran0.writeAction("slorii X17 X17 12 722")
    tran0.writeAction("hashl X16 X17 1")
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movrl X17 0(X16) 0 8")
    tran0.writeAction("yieldt")
    return efa
