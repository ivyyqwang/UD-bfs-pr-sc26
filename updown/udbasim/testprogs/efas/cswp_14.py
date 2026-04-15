from EFA_v2 import *
def cswp_14():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 2")
    tran0.writeAction("slorii X16 X16 12 3913")
    tran0.writeAction("movir X20 9071")
    tran0.writeAction("slorii X20 X20 12 987")
    tran0.writeAction("slorii X20 X20 12 2619")
    tran0.writeAction("slorii X20 X20 12 1938")
    tran0.writeAction("slorii X20 X20 12 3369")
    tran0.writeAction("add X16 X7 X16")
    tran0.writeAction("movrl X20 0(X16) 0 8")
    tran0.writeAction("movir X18 9071")
    tran0.writeAction("slorii X18 X18 12 987")
    tran0.writeAction("slorii X18 X18 12 2619")
    tran0.writeAction("slorii X18 X18 12 1938")
    tran0.writeAction("slorii X18 X18 12 3369")
    tran0.writeAction("movir X19 14739")
    tran0.writeAction("slorii X19 X19 12 595")
    tran0.writeAction("slorii X19 X19 12 2926")
    tran0.writeAction("slorii X19 X19 12 1655")
    tran0.writeAction("slorii X19 X19 12 560")
    tran0.writeAction("cswp X16 X17 X18 X19")
    tran0.writeAction("sub X16 X7 X16")
    tran0.writeAction("yieldt")
    return efa
