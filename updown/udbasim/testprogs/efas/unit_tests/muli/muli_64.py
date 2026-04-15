from EFA_v2 import *
def muli_64():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-3832370889662088437, -27747]
    tran0.writeAction("movir X16 51920")
    tran0.writeAction("slorii X16 X16 12 2799")
    tran0.writeAction("slorii X16 X16 12 2826")
    tran0.writeAction("slorii X16 X16 12 587")
    tran0.writeAction("slorii X16 X16 12 2827")
    tran0.writeAction("muli X16 X17 -27747")
    tran0.writeAction("yieldt")
    return efa
