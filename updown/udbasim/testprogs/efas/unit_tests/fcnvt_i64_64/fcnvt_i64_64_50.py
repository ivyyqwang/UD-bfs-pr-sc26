from EFA_v2 import *
def fcnvt_i64_64_50():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2191878277690946947]
    tran0.writeAction("movir X16 7787")
    tran0.writeAction("slorii X16 X16 12 474")
    tran0.writeAction("slorii X16 X16 12 3636")
    tran0.writeAction("slorii X16 X16 12 2719")
    tran0.writeAction("slorii X16 X16 12 1411")
    tran0.writeAction("fcnvt.i64.64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
