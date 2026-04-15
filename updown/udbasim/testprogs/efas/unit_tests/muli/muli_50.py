from EFA_v2 import *
def muli_50():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [142670455072086016, -1824]
    tran0.writeAction("movir X16 506")
    tran0.writeAction("slorii X16 X16 12 3552")
    tran0.writeAction("slorii X16 X16 12 1506")
    tran0.writeAction("slorii X16 X16 12 2109")
    tran0.writeAction("slorii X16 X16 12 2048")
    tran0.writeAction("muli X16 X17 -1824")
    tran0.writeAction("yieldt")
    return efa
