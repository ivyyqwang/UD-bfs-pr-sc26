from EFA_v2 import *
def muli_95():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-6857857320497494891, -16677]
    tran0.writeAction("movir X16 41171")
    tran0.writeAction("slorii X16 X16 12 4081")
    tran0.writeAction("slorii X16 X16 12 2555")
    tran0.writeAction("slorii X16 X16 12 1780")
    tran0.writeAction("slorii X16 X16 12 1173")
    tran0.writeAction("muli X16 X17 -16677")
    tran0.writeAction("yieldt")
    return efa
