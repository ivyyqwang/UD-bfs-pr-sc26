from EFA_v2 import *
def fcnvt_64_i64_77():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7617682323749353693]
    tran0.writeAction("movir X16 27063")
    tran0.writeAction("slorii X16 X16 12 1819")
    tran0.writeAction("slorii X16 X16 12 1686")
    tran0.writeAction("slorii X16 X16 12 3491")
    tran0.writeAction("slorii X16 X16 12 2269")
    tran0.writeAction("fcnvt.64.i64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
