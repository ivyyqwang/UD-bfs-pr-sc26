from EFA_v2 import *
def fcnvt_i64_64_85():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8021273197784643111]
    tran0.writeAction("movir X16 28497")
    tran0.writeAction("slorii X16 X16 12 1175")
    tran0.writeAction("slorii X16 X16 12 2448")
    tran0.writeAction("slorii X16 X16 12 1291")
    tran0.writeAction("slorii X16 X16 12 1575")
    tran0.writeAction("fcnvt.i64.64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
