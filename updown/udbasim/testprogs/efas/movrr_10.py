from EFA_v2 import *
def movrr_10():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movrr X0 X24")
    tran0.writeAction("movrr X7 X31")
    tran0.writeAction("movrl X24 0(X31) 0 8")
    tran0.writeAction("yieldt")
    return efa
