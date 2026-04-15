from EFA_v2 import *
def refill_9():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 35421")
    tran0.writeAction("slorii X16 X16 12 1977")
    tran0.writeAction("slorii X16 X16 12 2305")
    tran0.writeAction("slorii X16 X16 12 3649")
    tran0.writeAction("slorii X16 X16 12 2200")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("add X7 X17 X17")
    tran0.writeAction("movrl X16 0(X17) 0 8")
    tran0.writeAction("movir X18 1")
    tran0.writeAction("sli X18 X18 23")
    tran0.writeAction("or X18 X2 X2")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("add X16 X17 X5")
    tran0.writeAction("movir X18 1")
    tran0.writeAction("sli X18 X18 32")
    tran0.writeAction("add X18 X17 X4")
    tran0.writeAction("refill 48748")
    tran0.writeAction("yieldt")
    return efa
