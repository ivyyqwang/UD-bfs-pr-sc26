from EFA_v2 import *
def fcnvt_64_b16_77():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5603912569701179717]
    tran0.writeAction("movir X16 19909")
    tran0.writeAction("slorii X16 X16 12 396")
    tran0.writeAction("slorii X16 X16 12 2709")
    tran0.writeAction("slorii X16 X16 12 1578")
    tran0.writeAction("slorii X16 X16 12 325")
    tran0.writeAction("fcnvt.64.b16 X16 X16")
    tran0.writeAction("yieldt")
    return efa
