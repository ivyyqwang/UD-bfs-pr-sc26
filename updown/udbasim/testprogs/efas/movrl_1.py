from EFA_v2 import *
def movrl_1():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 33397")
    tran0.writeAction("slorii X16 X16 12 3883")
    tran0.writeAction("slorii X16 X16 12 3204")
    tran0.writeAction("slorii X16 X16 12 1111")
    tran0.writeAction("slorii X16 X16 12 2297")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 14")
    tran0.writeAction("slorii X17 X17 12 1235")
    tran0.writeAction("addi X17 X18 0")
    tran0.writeAction("add X7 X17 X17")
    tran0.writeAction("movrl X16 812(X17) 0 7")
    tran0.writeAction("sub X17 X7 X17")
    tran0.writeAction("yieldt")
    return efa
