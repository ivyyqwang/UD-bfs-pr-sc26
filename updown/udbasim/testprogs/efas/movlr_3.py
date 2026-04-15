from EFA_v2 import *
def movlr_3():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 3312")
    tran0.writeAction("slorii X16 X16 12 1361")
    tran0.writeAction("slorii X16 X16 12 3122")
    tran0.writeAction("slorii X16 X16 12 2329")
    tran0.writeAction("slorii X16 X16 12 3905")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 10")
    tran0.writeAction("slorii X17 X17 12 2828")
    tran0.writeAction("addi X17 X18 0")
    tran0.writeAction("add X7 X17 X17")
    tran0.writeAction("movrl X16 -118(X17) 0 8")
    tran0.writeAction("movlr -118(X17) X19 0 3")
    tran0.writeAction("sub X17 X7 X17")
    tran0.writeAction("yieldt")
    return efa
