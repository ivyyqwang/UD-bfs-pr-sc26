from EFA_v2 import *
def movlr_1():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 38664")
    tran0.writeAction("slorii X16 X16 12 313")
    tran0.writeAction("slorii X16 X16 12 1866")
    tran0.writeAction("slorii X16 X16 12 1984")
    tran0.writeAction("slorii X16 X16 12 1718")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 11")
    tran0.writeAction("slorii X17 X17 12 1433")
    tran0.writeAction("addi X17 X18 0")
    tran0.writeAction("add X7 X17 X17")
    tran0.writeAction("movrl X16 1666(X17) 0 8")
    tran0.writeAction("movlr 1666(X17) X19 1 2")
    tran0.writeAction("sub X17 X7 X17")
    tran0.writeAction("yieldt")
    return efa
