from EFA_v2 import *
def fcnvt_64_i64_15():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3150325497301141292]
    tran0.writeAction("movir X16 11192")
    tran0.writeAction("slorii X16 X16 12 837")
    tran0.writeAction("slorii X16 X16 12 2369")
    tran0.writeAction("slorii X16 X16 12 2008")
    tran0.writeAction("slorii X16 X16 12 1836")
    tran0.writeAction("fcnvt.64.i64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
