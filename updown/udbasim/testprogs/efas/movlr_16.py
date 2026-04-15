from EFA_v2 import *
def movlr_16():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 41410")
    tran0.writeAction("slorii X16 X16 12 1348")
    tran0.writeAction("slorii X16 X16 12 659")
    tran0.writeAction("slorii X16 X16 12 1521")
    tran0.writeAction("slorii X16 X16 12 15")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 3")
    tran0.writeAction("slorii X17 X17 12 3688")
    tran0.writeAction("addi X17 X18 0")
    tran0.writeAction("add X7 X17 X17")
    tran0.writeAction("movrl X16 1257(X17) 0 8")
    tran0.writeAction("movlr 1257(X17) X19 1 8")
    tran0.writeAction("sub X17 X7 X17")
    tran0.writeAction("yieldt")
    return efa
