from EFA_v2 import *
def fcnvt_64_i64_57():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [15207431851209930736]
    tran0.writeAction("movir X16 54027")
    tran0.writeAction("slorii X16 X16 12 2667")
    tran0.writeAction("slorii X16 X16 12 573")
    tran0.writeAction("slorii X16 X16 12 1347")
    tran0.writeAction("slorii X16 X16 12 2032")
    tran0.writeAction("fcnvt.64.i64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
