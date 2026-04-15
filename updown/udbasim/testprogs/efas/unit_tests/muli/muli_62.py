from EFA_v2 import *
def muli_62():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5077488911285750751, -19333]
    tran0.writeAction("movir X16 18038")
    tran0.writeAction("slorii X16 X16 12 3540")
    tran0.writeAction("slorii X16 X16 12 860")
    tran0.writeAction("slorii X16 X16 12 704")
    tran0.writeAction("slorii X16 X16 12 3039")
    tran0.writeAction("muli X16 X17 -19333")
    tran0.writeAction("yieldt")
    return efa
