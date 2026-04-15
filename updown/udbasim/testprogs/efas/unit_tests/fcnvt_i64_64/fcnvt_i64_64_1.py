from EFA_v2 import *
def fcnvt_i64_64_1():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2603096526409027721]
    tran0.writeAction("movir X16 9248")
    tran0.writeAction("slorii X16 X16 12 231")
    tran0.writeAction("slorii X16 X16 12 4028")
    tran0.writeAction("slorii X16 X16 12 2717")
    tran0.writeAction("slorii X16 X16 12 137")
    tran0.writeAction("fcnvt.i64.64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
