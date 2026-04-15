from EFA_v2 import *
def fcnvt_64_b16_53():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [18245831998905592475]
    tran0.writeAction("movir X16 64822")
    tran0.writeAction("slorii X16 X16 12 888")
    tran0.writeAction("slorii X16 X16 12 2126")
    tran0.writeAction("slorii X16 X16 12 914")
    tran0.writeAction("slorii X16 X16 12 2715")
    tran0.writeAction("fcnvt.64.b16 X16 X16")
    tran0.writeAction("yieldt")
    return efa
