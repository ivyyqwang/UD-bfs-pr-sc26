from EFA_v2 import *
def movwlr_19():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 8642")
    tran0.writeAction("slorii X16 X16 12 749")
    tran0.writeAction("slorii X16 X16 12 3056")
    tran0.writeAction("slorii X16 X16 12 1174")
    tran0.writeAction("slorii X16 X16 12 233")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 4")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 0")
    tran0.writeAction("slorii X18 X18 12 0")
    tran0.writeAction("slorii X18 X18 12 1")
    tran0.writeAction("slorii X18 X18 12 3142")
    tran0.writeAction("addi X18 X19 0")
    tran0.writeAction("add X17 X7 X17")
    tran0.writeAction("movwrl X16 X17(X18,0,0)")
    tran0.writeAction("movwlr X17(X18,1,0) X20")
    tran0.writeAction("sub X17 X7 X17")
    tran0.writeAction("yieldt")
    return efa
