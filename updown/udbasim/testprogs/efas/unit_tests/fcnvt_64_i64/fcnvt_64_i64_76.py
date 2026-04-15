from EFA_v2 import *
def fcnvt_64_i64_76():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6796101040055801841]
    tran0.writeAction("movir X16 24144")
    tran0.writeAction("slorii X16 X16 12 2462")
    tran0.writeAction("slorii X16 X16 12 894")
    tran0.writeAction("slorii X16 X16 12 773")
    tran0.writeAction("slorii X16 X16 12 2033")
    tran0.writeAction("fcnvt.64.i64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
