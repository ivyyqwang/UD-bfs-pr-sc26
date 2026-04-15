from EFA_v2 import *
def fcnvt_64_32_29():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8406885336480675600]
    tran0.writeAction("movir X16 29867")
    tran0.writeAction("slorii X16 X16 12 1050")
    tran0.writeAction("slorii X16 X16 12 3076")
    tran0.writeAction("slorii X16 X16 12 1519")
    tran0.writeAction("slorii X16 X16 12 1808")
    tran0.writeAction("fcnvt.64.32 X16 X16")
    tran0.writeAction("yieldt")
    return efa
