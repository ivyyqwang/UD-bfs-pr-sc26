from EFA_v2 import *
def movlr_15():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 33061")
    tran0.writeAction("slorii X16 X16 12 3481")
    tran0.writeAction("slorii X16 X16 12 273")
    tran0.writeAction("slorii X16 X16 12 3993")
    tran0.writeAction("slorii X16 X16 12 2471")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 13")
    tran0.writeAction("slorii X17 X17 12 3231")
    tran0.writeAction("addi X17 X18 0")
    tran0.writeAction("add X7 X17 X17")
    tran0.writeAction("movrl X16 695(X17) 0 8")
    tran0.writeAction("movlr 695(X17) X19 0 8")
    tran0.writeAction("sub X17 X7 X17")
    tran0.writeAction("yieldt")
    return efa
