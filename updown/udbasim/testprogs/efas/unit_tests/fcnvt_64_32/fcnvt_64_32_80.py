from EFA_v2 import *
def fcnvt_64_32_80():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1026232410419443742]
    tran0.writeAction("movir X16 3645")
    tran0.writeAction("slorii X16 X16 12 3727")
    tran0.writeAction("slorii X16 X16 12 168")
    tran0.writeAction("slorii X16 X16 12 179")
    tran0.writeAction("slorii X16 X16 12 2078")
    tran0.writeAction("fcnvt.64.32 X16 X16")
    tran0.writeAction("yieldt")
    return efa
