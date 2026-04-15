from EFA_v2 import *
def cswp_17():
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
    tran0.writeAction("slorii X16 X16 12 4027")
    tran0.writeAction("movir X20 9815")
    tran0.writeAction("slorii X20 X20 12 4051")
    tran0.writeAction("slorii X20 X20 12 3318")
    tran0.writeAction("slorii X20 X20 12 214")
    tran0.writeAction("slorii X20 X20 12 1740")
    tran0.writeAction("add X16 X7 X16")
    tran0.writeAction("movrl X20 0(X16) 0 8")
    tran0.writeAction("movir X18 9815")
    tran0.writeAction("slorii X18 X18 12 4051")
    tran0.writeAction("slorii X18 X18 12 3318")
    tran0.writeAction("slorii X18 X18 12 214")
    tran0.writeAction("slorii X18 X18 12 1740")
    tran0.writeAction("movir X19 10844")
    tran0.writeAction("slorii X19 X19 12 975")
    tran0.writeAction("slorii X19 X19 12 4001")
    tran0.writeAction("slorii X19 X19 12 352")
    tran0.writeAction("slorii X19 X19 12 2265")
    tran0.writeAction("cswp X16 X17 X18 X19")
    tran0.writeAction("sub X16 X7 X16")
    tran0.writeAction("yieldt")
    return efa
