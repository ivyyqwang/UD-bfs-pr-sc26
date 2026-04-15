from EFA_v2 import *
def fcnvt_64_i64_95():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [17253644510281211609]
    tran0.writeAction("movir X16 61297")
    tran0.writeAction("slorii X16 X16 12 1060")
    tran0.writeAction("slorii X16 X16 12 1204")
    tran0.writeAction("slorii X16 X16 12 737")
    tran0.writeAction("slorii X16 X16 12 3801")
    tran0.writeAction("fcnvt.64.i64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
