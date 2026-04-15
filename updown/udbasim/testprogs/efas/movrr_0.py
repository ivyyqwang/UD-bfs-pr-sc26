from EFA_v2 import *
def movrr_0():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X30 5289")
    tran0.writeAction("slorii X30 X30 12 2696")
    tran0.writeAction("slorii X30 X30 12 1560")
    tran0.writeAction("slorii X30 X30 12 2510")
    tran0.writeAction("slorii X30 X30 12 2173")
    tran0.writeAction("movrr X30 X23")
    tran0.writeAction("movrr X7 X31")
    tran0.writeAction("movrl X23 0(X31) 0 8")
    tran0.writeAction("yieldt")
    return efa
