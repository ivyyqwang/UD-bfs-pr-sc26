from EFA_v2 import *
def add_71():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2459303211824035078, -4575121476691317542]
    tran0.writeAction("movir X16 8737")
    tran0.writeAction("slorii X16 X16 12 819")
    tran0.writeAction("slorii X16 X16 12 3519")
    tran0.writeAction("slorii X16 X16 12 3067")
    tran0.writeAction("slorii X16 X16 12 1286")
    tran0.writeAction("movir X17 49281")
    tran0.writeAction("slorii X17 X17 12 3700")
    tran0.writeAction("slorii X17 X17 12 457")
    tran0.writeAction("slorii X17 X17 12 2266")
    tran0.writeAction("slorii X17 X17 12 3290")
    tran0.writeAction("add X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
