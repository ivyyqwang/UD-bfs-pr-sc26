from EFA_v2 import *
def movrl_5():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 25105")
    tran0.writeAction("slorii X16 X16 12 628")
    tran0.writeAction("slorii X16 X16 12 815")
    tran0.writeAction("slorii X16 X16 12 578")
    tran0.writeAction("slorii X16 X16 12 1674")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 6")
    tran0.writeAction("slorii X17 X17 12 3715")
    tran0.writeAction("addi X17 X18 0")
    tran0.writeAction("add X7 X17 X17")
    tran0.writeAction("movrl X16 -784(X17) 0 6")
    tran0.writeAction("sub X17 X7 X17")
    tran0.writeAction("yieldt")
    return efa
