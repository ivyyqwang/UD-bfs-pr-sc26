from EFA_v2 import *
def fcnvt_64_i64_45():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [17913134886783260519]
    tran0.writeAction("movir X16 63640")
    tran0.writeAction("slorii X16 X16 12 980")
    tran0.writeAction("slorii X16 X16 12 1420")
    tran0.writeAction("slorii X16 X16 12 1529")
    tran0.writeAction("slorii X16 X16 12 1895")
    tran0.writeAction("fcnvt.64.i64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
