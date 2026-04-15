from EFA_v2 import *
def fcnvt_32_i32_60():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3633279057]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 216")
    tran0.writeAction("slorii X16 X16 12 2295")
    tran0.writeAction("slorii X16 X16 12 81")
    tran0.writeAction("fcnvt.32.i32 X16 X16")
    tran0.writeAction("yieldt")
    return efa
