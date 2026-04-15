from EFA_v2 import *
def movil2_2():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 9")
    tran0.writeAction("slorii X16 X16 12 767")
    tran0.writeAction("add X7 X16 X16")
    tran0.writeAction("addi X16 X17 0")
    tran0.writeAction("movil2 X16 35298")
    tran0.writeAction("addi X16 X18 0")
    tran0.writeAction("movil2 X18 0")
    tran0.writeAction("movil2 X18 0")
    tran0.writeAction("movil2 X18 0")
    tran0.writeAction("sub X16 X7 X16")
    tran0.writeAction("sub X17 X7 X17")
    tran0.writeAction("sub X18 X7 X18")
    tran0.writeAction("yieldt")
    return efa
