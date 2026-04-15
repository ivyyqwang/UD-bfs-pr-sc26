from EFA_v2 import *
def add_31():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-7376135708661250381, -276387449011521123]
    tran0.writeAction("movir X16 39330")
    tran0.writeAction("slorii X16 X16 12 2874")
    tran0.writeAction("slorii X16 X16 12 1862")
    tran0.writeAction("slorii X16 X16 12 704")
    tran0.writeAction("slorii X16 X16 12 1715")
    tran0.writeAction("movir X17 64554")
    tran0.writeAction("slorii X17 X17 12 305")
    tran0.writeAction("slorii X17 X17 12 1113")
    tran0.writeAction("slorii X17 X17 12 1195")
    tran0.writeAction("slorii X17 X17 12 2461")
    tran0.writeAction("add X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
