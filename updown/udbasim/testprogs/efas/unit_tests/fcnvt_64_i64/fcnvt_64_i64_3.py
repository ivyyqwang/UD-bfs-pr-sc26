from EFA_v2 import *
def fcnvt_64_i64_3():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6594525596001730076]
    tran0.writeAction("movir X16 23428")
    tran0.writeAction("slorii X16 X16 12 1889")
    tran0.writeAction("slorii X16 X16 12 1819")
    tran0.writeAction("slorii X16 X16 12 3703")
    tran0.writeAction("slorii X16 X16 12 3612")
    tran0.writeAction("fcnvt.64.i64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
