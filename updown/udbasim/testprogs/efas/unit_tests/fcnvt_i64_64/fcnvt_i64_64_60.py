from EFA_v2 import *
def fcnvt_i64_64_60():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-3552293611044969741]
    tran0.writeAction("movir X16 52915")
    tran0.writeAction("slorii X16 X16 12 2940")
    tran0.writeAction("slorii X16 X16 12 2071")
    tran0.writeAction("slorii X16 X16 12 3174")
    tran0.writeAction("slorii X16 X16 12 755")
    tran0.writeAction("fcnvt.i64.64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
