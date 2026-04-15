from EFA_v2 import *
def sub_13():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-2148175757145106564, -2981163183805589010]
    tran0.writeAction("movir X16 57904")
    tran0.writeAction("slorii X16 X16 12 600")
    tran0.writeAction("slorii X16 X16 12 1992")
    tran0.writeAction("slorii X16 X16 12 1065")
    tran0.writeAction("slorii X16 X16 12 1916")
    tran0.writeAction("movir X17 54944")
    tran0.writeAction("slorii X17 X17 12 3198")
    tran0.writeAction("slorii X17 X17 12 275")
    tran0.writeAction("slorii X17 X17 12 3257")
    tran0.writeAction("slorii X17 X17 12 2542")
    tran0.writeAction("sub X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
