from EFA_v2 import *
def muli_36():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8374531267002150599, 3562]
    tran0.writeAction("movir X16 29752")
    tran0.writeAction("slorii X16 X16 12 1277")
    tran0.writeAction("slorii X16 X16 12 306")
    tran0.writeAction("slorii X16 X16 12 266")
    tran0.writeAction("slorii X16 X16 12 3783")
    tran0.writeAction("muli X16 X17 3562")
    tran0.writeAction("yieldt")
    return efa
