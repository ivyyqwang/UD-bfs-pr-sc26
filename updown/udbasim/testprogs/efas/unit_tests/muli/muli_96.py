from EFA_v2 import *
def muli_96():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3077427345169936103, -11838]
    tran0.writeAction("movir X16 10933")
    tran0.writeAction("slorii X16 X16 12 893")
    tran0.writeAction("slorii X16 X16 12 3474")
    tran0.writeAction("slorii X16 X16 12 3798")
    tran0.writeAction("slorii X16 X16 12 3815")
    tran0.writeAction("muli X16 X17 -11838")
    tran0.writeAction("yieldt")
    return efa
