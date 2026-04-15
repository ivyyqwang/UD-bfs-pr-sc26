from EFA_v2 import *
def movlr_19():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 35980")
    tran0.writeAction("slorii X16 X16 12 2835")
    tran0.writeAction("slorii X16 X16 12 834")
    tran0.writeAction("slorii X16 X16 12 384")
    tran0.writeAction("slorii X16 X16 12 2152")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 7")
    tran0.writeAction("slorii X17 X17 12 3819")
    tran0.writeAction("addi X17 X18 0")
    tran0.writeAction("add X7 X17 X17")
    tran0.writeAction("movrl X16 1792(X17) 0 8")
    tran0.writeAction("movlr 1792(X17) X19 1 5")
    tran0.writeAction("sub X17 X7 X17")
    tran0.writeAction("yieldt")
    return efa
