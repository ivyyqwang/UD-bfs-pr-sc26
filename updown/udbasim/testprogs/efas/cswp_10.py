from EFA_v2 import *
def cswp_10():
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
    tran0.writeAction("slorii X16 X16 12 10")
    tran0.writeAction("slorii X16 X16 12 189")
    tran0.writeAction("movir X20 45315")
    tran0.writeAction("slorii X20 X20 12 1939")
    tran0.writeAction("slorii X20 X20 12 2983")
    tran0.writeAction("slorii X20 X20 12 3420")
    tran0.writeAction("slorii X20 X20 12 3510")
    tran0.writeAction("add X16 X7 X16")
    tran0.writeAction("movrl X20 0(X16) 0 8")
    tran0.writeAction("movir X18 9125")
    tran0.writeAction("slorii X18 X18 12 2831")
    tran0.writeAction("slorii X18 X18 12 2247")
    tran0.writeAction("slorii X18 X18 12 3775")
    tran0.writeAction("slorii X18 X18 12 721")
    tran0.writeAction("movir X19 58682")
    tran0.writeAction("slorii X19 X19 12 3384")
    tran0.writeAction("slorii X19 X19 12 3394")
    tran0.writeAction("slorii X19 X19 12 236")
    tran0.writeAction("slorii X19 X19 12 1527")
    tran0.writeAction("cswp X16 X17 X18 X19")
    tran0.writeAction("sub X16 X7 X16")
    tran0.writeAction("yieldt")
    return efa
