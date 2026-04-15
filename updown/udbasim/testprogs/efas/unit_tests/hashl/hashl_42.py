from EFA_v2 import *
def hashl_42():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-9086053294379345195, 1129514794925883825]
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movir X17 33255")
    tran0.writeAction("slorii X17 X17 12 3498")
    tran0.writeAction("slorii X17 X17 12 2866")
    tran0.writeAction("slorii X17 X17 12 1029")
    tran0.writeAction("slorii X17 X17 12 2773")
    tran0.writeAction("movrl X17 0(X16) 1 8")
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movir X17 4012")
    tran0.writeAction("slorii X17 X17 12 3451")
    tran0.writeAction("slorii X17 X17 12 2232")
    tran0.writeAction("slorii X17 X17 12 432")
    tran0.writeAction("slorii X17 X17 12 433")
    tran0.writeAction("hashl X16 X17 1")
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movrl X17 0(X16) 0 8")
    tran0.writeAction("yieldt")
    return efa
