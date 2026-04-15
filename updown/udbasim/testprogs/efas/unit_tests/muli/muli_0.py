from EFA_v2 import *
def muli_0():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-7521888478027137510, -13304]
    tran0.writeAction("movir X16 38812")
    tran0.writeAction("slorii X16 X16 12 3620")
    tran0.writeAction("slorii X16 X16 12 2091")
    tran0.writeAction("slorii X16 X16 12 363")
    tran0.writeAction("slorii X16 X16 12 3610")
    tran0.writeAction("muli X16 X17 -13304")
    tran0.writeAction("yieldt")
    return efa
