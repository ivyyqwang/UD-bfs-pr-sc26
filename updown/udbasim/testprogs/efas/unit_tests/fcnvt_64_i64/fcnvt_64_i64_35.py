from EFA_v2 import *
def fcnvt_64_i64_35():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6800982237524684824]
    tran0.writeAction("movir X16 24161")
    tran0.writeAction("slorii X16 X16 12 3860")
    tran0.writeAction("slorii X16 X16 12 4055")
    tran0.writeAction("slorii X16 X16 12 1639")
    tran0.writeAction("slorii X16 X16 12 24")
    tran0.writeAction("fcnvt.64.i64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
