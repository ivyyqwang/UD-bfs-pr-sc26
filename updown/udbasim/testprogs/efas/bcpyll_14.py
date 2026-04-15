from EFA_v2 import *
def bcpyll_14():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 6")
    tran0.writeAction("slorii X16 X16 12 2744")
    tran0.writeAction("addi X16 X21 0")
    tran0.writeAction("add X16 X7 X16")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 6")
    tran0.writeAction("slorii X17 X17 12 278")
    tran0.writeAction("addi X17 X22 0")
    tran0.writeAction("add X17 X7 X17")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 0")
    tran0.writeAction("slorii X18 X18 12 0")
    tran0.writeAction("slorii X18 X18 12 0")
    tran0.writeAction("slorii X18 X18 12 0")
    tran0.writeAction("addi X18 X23 0")
    tran0.writeAction("addi X16 X19 0")
    tran0.writeAction("bcpyll X16 X17 X18")
    tran0.writeAction("sub X16 X7 X16")
    tran0.writeAction("sub X17 X7 X17")
    tran0.writeAction("yieldt")
    return efa
