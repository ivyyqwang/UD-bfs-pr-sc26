from EFA_v2 import *
def fcnvt_64_32_46():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [11983280427193303447]
    tran0.writeAction("movir X16 42573")
    tran0.writeAction("slorii X16 X16 12 672")
    tran0.writeAction("slorii X16 X16 12 3826")
    tran0.writeAction("slorii X16 X16 12 3064")
    tran0.writeAction("slorii X16 X16 12 407")
    tran0.writeAction("fcnvt.64.32 X16 X16")
    tran0.writeAction("yieldt")
    return efa
