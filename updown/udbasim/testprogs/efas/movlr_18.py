from EFA_v2 import *
def movlr_18():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 53342")
    tran0.writeAction("slorii X16 X16 12 944")
    tran0.writeAction("slorii X16 X16 12 3880")
    tran0.writeAction("slorii X16 X16 12 2857")
    tran0.writeAction("slorii X16 X16 12 3440")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 8")
    tran0.writeAction("slorii X17 X17 12 5")
    tran0.writeAction("addi X17 X18 0")
    tran0.writeAction("add X7 X17 X17")
    tran0.writeAction("movrl X16 -274(X17) 0 8")
    tran0.writeAction("movlr -274(X17) X19 1 6")
    tran0.writeAction("sub X17 X7 X17")
    tran0.writeAction("yieldt")
    return efa
