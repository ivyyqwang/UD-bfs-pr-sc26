from EFA_v2 import *
def movlr_17():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 10045")
    tran0.writeAction("slorii X16 X16 12 418")
    tran0.writeAction("slorii X16 X16 12 548")
    tran0.writeAction("slorii X16 X16 12 3732")
    tran0.writeAction("slorii X16 X16 12 3928")
    tran0.writeAction("movir X17 65535")
    tran0.writeAction("slorii X17 X17 12 4095")
    tran0.writeAction("slorii X17 X17 12 4095")
    tran0.writeAction("slorii X17 X17 12 4095")
    tran0.writeAction("slorii X17 X17 12 3919")
    tran0.writeAction("addi X17 X18 0")
    tran0.writeAction("add X7 X17 X17")
    tran0.writeAction("movrl X16 472(X17) 0 8")
    tran0.writeAction("movlr 472(X17) X19 0 3")
    tran0.writeAction("sub X17 X7 X17")
    tran0.writeAction("yieldt")
    return efa
