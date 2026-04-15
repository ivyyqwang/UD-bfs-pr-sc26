from EFA_v2 import *
def muli_49():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-3805961195223335671, -16081]
    tran0.writeAction("movir X16 52014")
    tran0.writeAction("slorii X16 X16 12 2087")
    tran0.writeAction("slorii X16 X16 12 1329")
    tran0.writeAction("slorii X16 X16 12 3243")
    tran0.writeAction("slorii X16 X16 12 3337")
    tran0.writeAction("muli X16 X17 -16081")
    tran0.writeAction("yieldt")
    return efa
