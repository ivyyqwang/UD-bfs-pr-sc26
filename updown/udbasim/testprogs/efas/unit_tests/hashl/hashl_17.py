from EFA_v2 import *
def hashl_17():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1324231071634606921, 7034275612273188730, 4307213061662228291]
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movir X17 4704")
    tran0.writeAction("slorii X17 X17 12 2514")
    tran0.writeAction("slorii X17 X17 12 1217")
    tran0.writeAction("slorii X17 X17 12 1292")
    tran0.writeAction("slorii X17 X17 12 2889")
    tran0.writeAction("movrl X17 0(X16) 1 8")
    tran0.writeAction("movir X17 24990")
    tran0.writeAction("slorii X17 X17 12 3142")
    tran0.writeAction("slorii X17 X17 12 1649")
    tran0.writeAction("slorii X17 X17 12 3017")
    tran0.writeAction("slorii X17 X17 12 3962")
    tran0.writeAction("movrl X17 0(X16) 1 8")
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movir X17 15302")
    tran0.writeAction("slorii X17 X17 12 1207")
    tran0.writeAction("slorii X17 X17 12 1408")
    tran0.writeAction("slorii X17 X17 12 1227")
    tran0.writeAction("slorii X17 X17 12 3907")
    tran0.writeAction("hashl X16 X17 2")
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movrl X17 0(X16) 0 8")
    tran0.writeAction("yieldt")
    return efa
