from EFA_v2 import *
def fcnvt_i32_32_57():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1829999318]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 109")
    tran0.writeAction("slorii X16 X16 12 313")
    tran0.writeAction("slorii X16 X16 12 726")
    tran0.writeAction("fcnvt.i32.32 X16 X16")
    tran0.writeAction("yieldt")
    return efa
