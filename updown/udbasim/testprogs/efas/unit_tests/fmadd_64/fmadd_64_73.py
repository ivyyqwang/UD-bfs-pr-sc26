from EFA_v2 import *
def fmadd_64_73():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1119407664184759397, 14365602895617740318, 3326039311284851636]
    tran0.writeAction("movir X16 3976")
    tran0.writeAction("slorii X16 X16 12 3829")
    tran0.writeAction("slorii X16 X16 12 1782")
    tran0.writeAction("slorii X16 X16 12 2385")
    tran0.writeAction("slorii X16 X16 12 1125")
    tran0.writeAction("movir X17 51036")
    tran0.writeAction("slorii X17 X17 12 3579")
    tran0.writeAction("slorii X17 X17 12 2217")
    tran0.writeAction("slorii X17 X17 12 2532")
    tran0.writeAction("slorii X17 X17 12 3614")
    tran0.writeAction("movir X18 11816")
    tran0.writeAction("slorii X18 X18 12 1906")
    tran0.writeAction("slorii X18 X18 12 426")
    tran0.writeAction("slorii X18 X18 12 485")
    tran0.writeAction("slorii X18 X18 12 948")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
