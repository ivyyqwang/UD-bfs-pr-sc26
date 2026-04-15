from EFA_v2 import *
def fcnvt_i64_64_58():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-7466272922464659799]
    tran0.writeAction("movir X16 39010")
    tran0.writeAction("slorii X16 X16 12 1925")
    tran0.writeAction("slorii X16 X16 12 1476")
    tran0.writeAction("slorii X16 X16 12 1541")
    tran0.writeAction("slorii X16 X16 12 1705")
    tran0.writeAction("fcnvt.i64.64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
