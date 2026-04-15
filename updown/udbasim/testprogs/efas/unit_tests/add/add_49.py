from EFA_v2 import *
def add_49():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5945706531048998037, -7755184798813687896]
    tran0.writeAction("movir X16 21123")
    tran0.writeAction("slorii X16 X16 12 1609")
    tran0.writeAction("slorii X16 X16 12 1689")
    tran0.writeAction("slorii X16 X16 12 3668")
    tran0.writeAction("slorii X16 X16 12 1173")
    tran0.writeAction("movir X17 37984")
    tran0.writeAction("slorii X17 X17 12 200")
    tran0.writeAction("slorii X17 X17 12 931")
    tran0.writeAction("slorii X17 X17 12 822")
    tran0.writeAction("slorii X17 X17 12 4008")
    tran0.writeAction("add X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
