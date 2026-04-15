from EFA_v2 import *
def subi_101():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [9223372036854775807, -16872]
    tran0.writeAction("movir X16 32767")
    tran0.writeAction("slorii X16 X16 12 4095")
    tran0.writeAction("slorii X16 X16 12 4095")
    tran0.writeAction("slorii X16 X16 12 4095")
    tran0.writeAction("slorii X16 X16 12 4095")
    tran0.writeAction("subi X16 X17 -16872")
    tran0.writeAction("addi X7 X18 0")
    tran0.writeAction("movrl X4 0(X18) 0 8")
    tran0.writeAction("yieldt")
    return efa
