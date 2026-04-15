from EFA_v2 import *
def fcnvt_64_i64_90():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [12814782445451971791]
    tran0.writeAction("movir X16 45527")
    tran0.writeAction("slorii X16 X16 12 1035")
    tran0.writeAction("slorii X16 X16 12 3343")
    tran0.writeAction("slorii X16 X16 12 312")
    tran0.writeAction("slorii X16 X16 12 3279")
    tran0.writeAction("fcnvt.64.i64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
