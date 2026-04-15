from EFA_v2 import *
def modi_77():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-4115763892508834312, -2760]
    tran0.writeAction("movir X16 50913")
    tran0.writeAction("slorii X16 X16 12 3560")
    tran0.writeAction("slorii X16 X16 12 3015")
    tran0.writeAction("slorii X16 X16 12 2588")
    tran0.writeAction("slorii X16 X16 12 1528")
    tran0.writeAction("modi X16 X17 -2760")
    tran0.writeAction("yieldt")
    return efa
