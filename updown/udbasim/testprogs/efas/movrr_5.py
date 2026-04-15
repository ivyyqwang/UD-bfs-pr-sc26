from EFA_v2 import *
def movrr_5():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X17 38403")
    tran0.writeAction("slorii X17 X17 12 2381")
    tran0.writeAction("slorii X17 X17 12 3901")
    tran0.writeAction("slorii X17 X17 12 1601")
    tran0.writeAction("slorii X17 X17 12 406")
    tran0.writeAction("movrr X17 X16")
    tran0.writeAction("movrr X7 X31")
    tran0.writeAction("movrl X16 0(X31) 0 8")
    tran0.writeAction("yieldt")
    return efa
