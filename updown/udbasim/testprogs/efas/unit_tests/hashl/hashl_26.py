from EFA_v2 import *
def hashl_26():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6758615818900833981, -7623846414367563849, -7977331687534559043]
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movir X17 24011")
    tran0.writeAction("slorii X17 X17 12 1748")
    tran0.writeAction("slorii X17 X17 12 1874")
    tran0.writeAction("slorii X17 X17 12 3768")
    tran0.writeAction("slorii X17 X17 12 1725")
    tran0.writeAction("movrl X17 0(X16) 1 8")
    tran0.writeAction("movir X17 38450")
    tran0.writeAction("slorii X17 X17 12 2689")
    tran0.writeAction("slorii X17 X17 12 1081")
    tran0.writeAction("slorii X17 X17 12 1989")
    tran0.writeAction("slorii X17 X17 12 4023")
    tran0.writeAction("movrl X17 0(X16) 1 8")
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movir X17 37194")
    tran0.writeAction("slorii X17 X17 12 3377")
    tran0.writeAction("slorii X17 X17 12 2189")
    tran0.writeAction("slorii X17 X17 12 144")
    tran0.writeAction("slorii X17 X17 12 189")
    tran0.writeAction("hashl X16 X17 2")
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movrl X17 0(X16) 0 8")
    tran0.writeAction("yieldt")
    return efa
