from EFA_v2 import *
def addi_61():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1100451278153192419, 13080]
    tran0.writeAction("movir X16 61626")
    tran0.writeAction("slorii X16 X16 12 1686")
    tran0.writeAction("slorii X16 X16 12 1177")
    tran0.writeAction("slorii X16 X16 12 222")
    tran0.writeAction("slorii X16 X16 12 3101")
    tran0.writeAction("addi X16 X17 13080")
    tran0.writeAction("yieldt")
    return efa
