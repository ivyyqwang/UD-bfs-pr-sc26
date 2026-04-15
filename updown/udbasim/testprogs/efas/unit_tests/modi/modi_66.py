from EFA_v2 import *
def modi_66():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3969579475314742453, -32506]
    tran0.writeAction("movir X16 14102")
    tran0.writeAction("slorii X16 X16 12 3192")
    tran0.writeAction("slorii X16 X16 12 69")
    tran0.writeAction("slorii X16 X16 12 3345")
    tran0.writeAction("slorii X16 X16 12 1205")
    tran0.writeAction("modi X16 X17 -32506")
    tran0.writeAction("yieldt")
    return efa
