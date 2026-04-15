from EFA_v2 import *
def fcnvt_i32_32_90():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-606705010]
    tran0.writeAction("movir X16 65535")
    tran0.writeAction("slorii X16 X16 12 4095")
    tran0.writeAction("slorii X16 X16 12 4059")
    tran0.writeAction("slorii X16 X16 12 3430")
    tran0.writeAction("slorii X16 X16 12 2702")
    tran0.writeAction("fcnvt.i32.32 X16 X16")
    tran0.writeAction("yieldt")
    return efa
