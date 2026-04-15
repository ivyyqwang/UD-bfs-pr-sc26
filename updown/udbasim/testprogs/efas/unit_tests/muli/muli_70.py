from EFA_v2 import *
def muli_70():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3116331724975759525, -2001]
    tran0.writeAction("movir X16 11071")
    tran0.writeAction("slorii X16 X16 12 1779")
    tran0.writeAction("slorii X16 X16 12 349")
    tran0.writeAction("slorii X16 X16 12 1886")
    tran0.writeAction("slorii X16 X16 12 165")
    tran0.writeAction("muli X16 X17 -2001")
    tran0.writeAction("yieldt")
    return efa
