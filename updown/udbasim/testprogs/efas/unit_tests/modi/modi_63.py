from EFA_v2 import *
def modi_63():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-234951508537825556, -24595]
    tran0.writeAction("movir X16 64701")
    tran0.writeAction("slorii X16 X16 12 1165")
    tran0.writeAction("slorii X16 X16 12 2314")
    tran0.writeAction("slorii X16 X16 12 658")
    tran0.writeAction("slorii X16 X16 12 1772")
    tran0.writeAction("modi X16 X17 -24595")
    tran0.writeAction("yieldt")
    return efa
