from EFA_v2 import *
def fcnvt_32_i32_30():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1146336233]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 68")
    tran0.writeAction("slorii X16 X16 12 1339")
    tran0.writeAction("slorii X16 X16 12 1001")
    tran0.writeAction("fcnvt.32.i32 X16 X16")
    tran0.writeAction("yieldt")
    return efa
