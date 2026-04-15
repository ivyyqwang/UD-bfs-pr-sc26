from EFA_v2 import *
def fadd_64_80():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [354401939955804934, 8435666417112135362]
    tran0.writeAction("movir X16 1259")
    tran0.writeAction("slorii X16 X16 12 362")
    tran0.writeAction("slorii X16 X16 12 4042")
    tran0.writeAction("slorii X16 X16 12 3174")
    tran0.writeAction("slorii X16 X16 12 2822")
    tran0.writeAction("movir X17 29969")
    tran0.writeAction("slorii X17 X17 12 2078")
    tran0.writeAction("slorii X17 X17 12 2443")
    tran0.writeAction("slorii X17 X17 12 2707")
    tran0.writeAction("slorii X17 X17 12 1730")
    tran0.writeAction("fadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
