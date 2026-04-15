from EFA_v2 import *
def fcnvt_64_i64_33():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [126258888512040049]
    tran0.writeAction("movir X16 448")
    tran0.writeAction("slorii X16 X16 12 2300")
    tran0.writeAction("slorii X16 X16 12 2631")
    tran0.writeAction("slorii X16 X16 12 2030")
    tran0.writeAction("slorii X16 X16 12 3185")
    tran0.writeAction("fcnvt.64.i64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
