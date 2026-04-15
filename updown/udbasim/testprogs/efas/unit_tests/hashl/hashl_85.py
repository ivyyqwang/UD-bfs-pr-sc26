from EFA_v2 import *
def hashl_85():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-8891417474110984702, -5104590070805897355]
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movir X17 33947")
    tran0.writeAction("slorii X17 X17 12 1390")
    tran0.writeAction("slorii X17 X17 12 2689")
    tran0.writeAction("slorii X17 X17 12 3742")
    tran0.writeAction("slorii X17 X17 12 3586")
    tran0.writeAction("movrl X17 0(X16) 1 8")
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movir X17 47400")
    tran0.writeAction("slorii X17 X17 12 3494")
    tran0.writeAction("slorii X17 X17 12 57")
    tran0.writeAction("slorii X17 X17 12 2573")
    tran0.writeAction("slorii X17 X17 12 3957")
    tran0.writeAction("hashl X16 X17 1")
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movrl X17 0(X16) 0 8")
    tran0.writeAction("yieldt")
    return efa
