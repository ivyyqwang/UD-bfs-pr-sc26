from EFA_v2 import *
def movrr_16():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X18 44161")
    tran0.writeAction("slorii X18 X18 12 123")
    tran0.writeAction("slorii X18 X18 12 2194")
    tran0.writeAction("slorii X18 X18 12 2421")
    tran0.writeAction("slorii X18 X18 12 1289")
    tran0.writeAction("movrr X18 X16")
    tran0.writeAction("movrr X7 X31")
    tran0.writeAction("movrl X16 0(X31) 0 8")
    tran0.writeAction("yieldt")
    return efa
