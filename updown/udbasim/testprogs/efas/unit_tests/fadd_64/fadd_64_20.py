from EFA_v2 import *
def fadd_64_20():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [17569084137680560065, 11158394983818737161]
    tran0.writeAction("movir X16 62417")
    tran0.writeAction("slorii X16 X16 12 3791")
    tran0.writeAction("slorii X16 X16 12 47")
    tran0.writeAction("slorii X16 X16 12 1637")
    tran0.writeAction("slorii X16 X16 12 4033")
    tran0.writeAction("movir X17 39642")
    tran0.writeAction("slorii X17 X17 12 2385")
    tran0.writeAction("slorii X17 X17 12 3642")
    tran0.writeAction("slorii X17 X17 12 67")
    tran0.writeAction("slorii X17 X17 12 1545")
    tran0.writeAction("fadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
