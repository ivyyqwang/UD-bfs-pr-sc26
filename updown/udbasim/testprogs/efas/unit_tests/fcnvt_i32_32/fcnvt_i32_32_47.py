from EFA_v2 import *
def fcnvt_i32_32_47():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-2084970868]
    tran0.writeAction("movir X16 65535")
    tran0.writeAction("slorii X16 X16 12 4095")
    tran0.writeAction("slorii X16 X16 12 3971")
    tran0.writeAction("slorii X16 X16 12 2973")
    tran0.writeAction("slorii X16 X16 12 3724")
    tran0.writeAction("fcnvt.i32.32 X16 X16")
    tran0.writeAction("yieldt")
    return efa
