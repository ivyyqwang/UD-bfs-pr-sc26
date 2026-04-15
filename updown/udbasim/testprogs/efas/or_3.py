from EFA_v2 import *
def or_3():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 -23416")
    tran0.writeAction("slorii X16 X16 12 3374")
    tran0.writeAction("slorii X16 X16 12 2769")
    tran0.writeAction("slorii X16 X16 12 3709")
    tran0.writeAction("slorii X16 X16 12 2980")
    tran0.writeAction("movir X17 -6538")
    tran0.writeAction("slorii X17 X17 12 2244")
    tran0.writeAction("slorii X17 X17 12 373")
    tran0.writeAction("slorii X17 X17 12 4059")
    tran0.writeAction("slorii X17 X17 12 2913")
    tran0.writeAction("movir X18 -2579")
    tran0.writeAction("slorii X18 X18 12 784")
    tran0.writeAction("slorii X18 X18 12 1540")
    tran0.writeAction("slorii X18 X18 12 3850")
    tran0.writeAction("slorii X18 X18 12 3247")
    tran0.writeAction("or X16 X17 X18")
    tran0.writeAction(f"print '%d,%d,%d' X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
