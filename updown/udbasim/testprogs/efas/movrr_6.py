from EFA_v2 import *
def movrr_6():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X27 31611")
    tran0.writeAction("slorii X27 X27 12 1397")
    tran0.writeAction("slorii X27 X27 12 2043")
    tran0.writeAction("slorii X27 X27 12 1667")
    tran0.writeAction("slorii X27 X27 12 2738")
    tran0.writeAction("movrr X27 X21")
    tran0.writeAction("movrr X7 X31")
    tran0.writeAction("movrl X21 0(X31) 0 8")
    tran0.writeAction("yieldt")
    return efa
