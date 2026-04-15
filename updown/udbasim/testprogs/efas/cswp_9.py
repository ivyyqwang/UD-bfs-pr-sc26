from EFA_v2 import *
def cswp_9():
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
    tran0.writeAction("slorii X16 X16 12 5")
    tran0.writeAction("slorii X16 X16 12 1229")
    tran0.writeAction("movir X20 17988")
    tran0.writeAction("slorii X20 X20 12 2910")
    tran0.writeAction("slorii X20 X20 12 3172")
    tran0.writeAction("slorii X20 X20 12 3461")
    tran0.writeAction("slorii X20 X20 12 2381")
    tran0.writeAction("add X16 X7 X16")
    tran0.writeAction("movrl X20 0(X16) 0 8")
    tran0.writeAction("movir X18 40191")
    tran0.writeAction("slorii X18 X18 12 584")
    tran0.writeAction("slorii X18 X18 12 776")
    tran0.writeAction("slorii X18 X18 12 506")
    tran0.writeAction("slorii X18 X18 12 770")
    tran0.writeAction("movir X19 34331")
    tran0.writeAction("slorii X19 X19 12 1453")
    tran0.writeAction("slorii X19 X19 12 3756")
    tran0.writeAction("slorii X19 X19 12 3137")
    tran0.writeAction("slorii X19 X19 12 536")
    tran0.writeAction("cswp X16 X17 X18 X19")
    tran0.writeAction("sub X16 X7 X16")
    tran0.writeAction("yieldt")
    return efa
