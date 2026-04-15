from EFA_v2 import *
def muli_1():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5372354268728263050, 7732]
    tran0.writeAction("movir X16 19086")
    tran0.writeAction("slorii X16 X16 12 1787")
    tran0.writeAction("slorii X16 X16 12 3667")
    tran0.writeAction("slorii X16 X16 12 416")
    tran0.writeAction("slorii X16 X16 12 394")
    tran0.writeAction("muli X16 X17 7732")
    tran0.writeAction("yieldt")
    return efa
