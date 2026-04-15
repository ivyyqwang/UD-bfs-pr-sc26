from EFA_v2 import *
def movrl_8():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 17636")
    tran0.writeAction("slorii X16 X16 12 2426")
    tran0.writeAction("slorii X16 X16 12 3965")
    tran0.writeAction("slorii X16 X16 12 304")
    tran0.writeAction("slorii X16 X16 12 2618")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 8")
    tran0.writeAction("slorii X17 X17 12 2808")
    tran0.writeAction("addi X17 X18 0")
    tran0.writeAction("add X7 X17 X17")
    tran0.writeAction("movrl X16 -105(X17) 0 1")
    tran0.writeAction("sub X17 X7 X17")
    tran0.writeAction("yieldt")
    return efa
