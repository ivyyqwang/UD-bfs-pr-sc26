from EFA_v2 import *
def modi_7():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1373476602770655173, -20131]
    tran0.writeAction("movir X16 60656")
    tran0.writeAction("slorii X16 X16 12 1764")
    tran0.writeAction("slorii X16 X16 12 3720")
    tran0.writeAction("slorii X16 X16 12 2231")
    tran0.writeAction("slorii X16 X16 12 2107")
    tran0.writeAction("modi X16 X17 -20131")
    tran0.writeAction("yieldt")
    return efa
