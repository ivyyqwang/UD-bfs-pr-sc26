from EFA_v2 import *
def fadd_64_91():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7152292309897698890, 16161108941349126372]
    tran0.writeAction("movir X16 25410")
    tran0.writeAction("slorii X16 X16 12 191")
    tran0.writeAction("slorii X16 X16 12 1565")
    tran0.writeAction("slorii X16 X16 12 861")
    tran0.writeAction("slorii X16 X16 12 3658")
    tran0.writeAction("movir X17 57415")
    tran0.writeAction("slorii X17 X17 12 3247")
    tran0.writeAction("slorii X17 X17 12 1273")
    tran0.writeAction("slorii X17 X17 12 2064")
    tran0.writeAction("slorii X17 X17 12 228")
    tran0.writeAction("fadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
