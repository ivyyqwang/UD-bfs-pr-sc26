from EFA_v2 import *
def divi_69():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-215139551245938084, -31749]
    tran0.writeAction("movir X16 64771")
    tran0.writeAction("slorii X16 X16 12 2747")
    tran0.writeAction("slorii X16 X16 12 1998")
    tran0.writeAction("slorii X16 X16 12 3477")
    tran0.writeAction("slorii X16 X16 12 604")
    tran0.writeAction("divi X16 X17 -31749")
    tran0.writeAction("yieldt")
    return efa
