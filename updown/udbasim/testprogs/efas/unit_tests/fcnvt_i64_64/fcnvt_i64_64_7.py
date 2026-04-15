from EFA_v2 import *
def fcnvt_i64_64_7():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1007691038091957252]
    tran0.writeAction("movir X16 61955")
    tran0.writeAction("slorii X16 X16 12 3941")
    tran0.writeAction("slorii X16 X16 12 1791")
    tran0.writeAction("slorii X16 X16 12 754")
    tran0.writeAction("slorii X16 X16 12 3068")
    tran0.writeAction("fcnvt.i64.64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
