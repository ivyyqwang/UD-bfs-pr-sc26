from EFA_v2 import *
def fcnvt_64_i64_79():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [12781811176050565510]
    tran0.writeAction("movir X16 45410")
    tran0.writeAction("slorii X16 X16 12 472")
    tran0.writeAction("slorii X16 X16 12 2862")
    tran0.writeAction("slorii X16 X16 12 2506")
    tran0.writeAction("slorii X16 X16 12 390")
    tran0.writeAction("fcnvt.64.i64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
