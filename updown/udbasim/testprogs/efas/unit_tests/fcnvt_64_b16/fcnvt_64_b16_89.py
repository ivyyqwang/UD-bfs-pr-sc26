from EFA_v2 import *
def fcnvt_64_b16_89():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2999759256370054246]
    tran0.writeAction("movir X16 10657")
    tran0.writeAction("slorii X16 X16 12 1170")
    tran0.writeAction("slorii X16 X16 12 1655")
    tran0.writeAction("slorii X16 X16 12 2568")
    tran0.writeAction("slorii X16 X16 12 1126")
    tran0.writeAction("fcnvt.64.b16 X16 X16")
    tran0.writeAction("yieldt")
    return efa
