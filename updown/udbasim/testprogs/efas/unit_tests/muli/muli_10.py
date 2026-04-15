from EFA_v2 import *
def muli_10():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4066799727170678389, -15050]
    tran0.writeAction("movir X16 14448")
    tran0.writeAction("slorii X16 X16 12 716")
    tran0.writeAction("slorii X16 X16 12 3606")
    tran0.writeAction("slorii X16 X16 12 2718")
    tran0.writeAction("slorii X16 X16 12 3701")
    tran0.writeAction("muli X16 X17 -15050")
    tran0.writeAction("yieldt")
    return efa
