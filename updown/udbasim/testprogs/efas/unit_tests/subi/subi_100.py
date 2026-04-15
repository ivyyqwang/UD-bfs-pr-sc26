from EFA_v2 import *
def subi_100():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-9223372036854775808, 31217]
    tran0.writeAction("movir X16 32768")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("subi X16 X17 31217")
    tran0.writeAction("addi X7 X18 0")
    tran0.writeAction("movrl X4 0(X18) 0 8")
    tran0.writeAction("yieldt")
    return efa
