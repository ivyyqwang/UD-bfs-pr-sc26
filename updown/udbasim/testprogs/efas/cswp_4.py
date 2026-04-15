from EFA_v2 import *
def cswp_4():
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
    tran0.writeAction("slorii X16 X16 12 13")
    tran0.writeAction("slorii X16 X16 12 242")
    tran0.writeAction("movir X20 24780")
    tran0.writeAction("slorii X20 X20 12 2619")
    tran0.writeAction("slorii X20 X20 12 632")
    tran0.writeAction("slorii X20 X20 12 3247")
    tran0.writeAction("slorii X20 X20 12 2968")
    tran0.writeAction("add X16 X7 X16")
    tran0.writeAction("movrl X20 0(X16) 0 8")
    tran0.writeAction("movir X18 2578")
    tran0.writeAction("slorii X18 X18 12 3050")
    tran0.writeAction("slorii X18 X18 12 2110")
    tran0.writeAction("slorii X18 X18 12 3811")
    tran0.writeAction("slorii X18 X18 12 449")
    tran0.writeAction("movir X19 18993")
    tran0.writeAction("slorii X19 X19 12 1822")
    tran0.writeAction("slorii X19 X19 12 2268")
    tran0.writeAction("slorii X19 X19 12 326")
    tran0.writeAction("slorii X19 X19 12 1817")
    tran0.writeAction("cswp X16 X17 X18 X19")
    tran0.writeAction("sub X16 X7 X16")
    tran0.writeAction("yieldt")
    return efa
