from EFA_v2 import *
def sub_97():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-3446176830156126662, 3948829215886288484]
    tran0.writeAction("movir X16 53292")
    tran0.writeAction("slorii X16 X16 12 2950")
    tran0.writeAction("slorii X16 X16 12 3709")
    tran0.writeAction("slorii X16 X16 12 1484")
    tran0.writeAction("slorii X16 X16 12 1594")
    tran0.writeAction("movir X17 14029")
    tran0.writeAction("slorii X17 X17 12 244")
    tran0.writeAction("slorii X17 X17 12 3")
    tran0.writeAction("slorii X17 X17 12 2402")
    tran0.writeAction("slorii X17 X17 12 1636")
    tran0.writeAction("sub X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
