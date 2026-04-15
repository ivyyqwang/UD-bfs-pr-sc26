from EFA_v2 import *
def cswp_3():
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
    tran0.writeAction("slorii X16 X16 12 3154")
    tran0.writeAction("movir X20 61394")
    tran0.writeAction("slorii X20 X20 12 1421")
    tran0.writeAction("slorii X20 X20 12 1686")
    tran0.writeAction("slorii X20 X20 12 700")
    tran0.writeAction("slorii X20 X20 12 171")
    tran0.writeAction("add X16 X7 X16")
    tran0.writeAction("movrl X20 0(X16) 0 8")
    tran0.writeAction("movir X18 61394")
    tran0.writeAction("slorii X18 X18 12 1421")
    tran0.writeAction("slorii X18 X18 12 1686")
    tran0.writeAction("slorii X18 X18 12 700")
    tran0.writeAction("slorii X18 X18 12 171")
    tran0.writeAction("movir X19 14185")
    tran0.writeAction("slorii X19 X19 12 984")
    tran0.writeAction("slorii X19 X19 12 3328")
    tran0.writeAction("slorii X19 X19 12 3048")
    tran0.writeAction("slorii X19 X19 12 1707")
    tran0.writeAction("cswp X16 X17 X18 X19")
    tran0.writeAction("sub X16 X7 X16")
    tran0.writeAction("yieldt")
    return efa
