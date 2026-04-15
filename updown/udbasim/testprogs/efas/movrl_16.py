from EFA_v2 import *
def movrl_16():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 33403")
    tran0.writeAction("slorii X16 X16 12 2543")
    tran0.writeAction("slorii X16 X16 12 566")
    tran0.writeAction("slorii X16 X16 12 1851")
    tran0.writeAction("slorii X16 X16 12 3250")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 5")
    tran0.writeAction("slorii X17 X17 12 4055")
    tran0.writeAction("addi X17 X18 0")
    tran0.writeAction("add X7 X17 X17")
    tran0.writeAction("movrl X16 153(X17) 1 5")
    tran0.writeAction("sub X17 X7 X17")
    tran0.writeAction("yieldt")
    return efa
