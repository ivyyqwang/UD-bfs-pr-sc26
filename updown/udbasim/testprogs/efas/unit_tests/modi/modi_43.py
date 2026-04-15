from EFA_v2 import *
def modi_43():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4349397711897764380, -27269]
    tran0.writeAction("movir X16 15452")
    tran0.writeAction("slorii X16 X16 12 674")
    tran0.writeAction("slorii X16 X16 12 3268")
    tran0.writeAction("slorii X16 X16 12 2306")
    tran0.writeAction("slorii X16 X16 12 540")
    tran0.writeAction("modi X16 X17 -27269")
    tran0.writeAction("yieldt")
    return efa
