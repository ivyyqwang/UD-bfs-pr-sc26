from EFA_v2 import *
def fcnvt_64_32_34():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [16933947264547307054]
    tran0.writeAction("movir X16 60161")
    tran0.writeAction("slorii X16 X16 12 1909")
    tran0.writeAction("slorii X16 X16 12 308")
    tran0.writeAction("slorii X16 X16 12 2211")
    tran0.writeAction("slorii X16 X16 12 3630")
    tran0.writeAction("fcnvt.64.32 X16 X16")
    tran0.writeAction("yieldt")
    return efa
