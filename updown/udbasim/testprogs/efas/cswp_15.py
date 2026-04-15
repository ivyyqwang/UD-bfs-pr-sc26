from EFA_v2 import *
def cswp_15():
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
    tran0.writeAction("slorii X16 X16 12 4")
    tran0.writeAction("slorii X16 X16 12 1642")
    tran0.writeAction("movir X20 43233")
    tran0.writeAction("slorii X20 X20 12 16")
    tran0.writeAction("slorii X20 X20 12 1358")
    tran0.writeAction("slorii X20 X20 12 3441")
    tran0.writeAction("slorii X20 X20 12 996")
    tran0.writeAction("add X16 X7 X16")
    tran0.writeAction("movrl X20 0(X16) 0 8")
    tran0.writeAction("movir X18 43233")
    tran0.writeAction("slorii X18 X18 12 16")
    tran0.writeAction("slorii X18 X18 12 1358")
    tran0.writeAction("slorii X18 X18 12 3441")
    tran0.writeAction("slorii X18 X18 12 996")
    tran0.writeAction("movir X19 12520")
    tran0.writeAction("slorii X19 X19 12 1078")
    tran0.writeAction("slorii X19 X19 12 801")
    tran0.writeAction("slorii X19 X19 12 2878")
    tran0.writeAction("slorii X19 X19 12 972")
    tran0.writeAction("cswp X16 X17 X18 X19")
    tran0.writeAction("sub X16 X7 X16")
    tran0.writeAction("yieldt")
    return efa
