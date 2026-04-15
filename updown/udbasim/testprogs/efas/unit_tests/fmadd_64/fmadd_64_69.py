from EFA_v2 import *
def fmadd_64_69():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [14509176644788607829, 818566286253603026, 403842731570524285]
    tran0.writeAction("movir X16 51546")
    tran0.writeAction("slorii X16 X16 12 3892")
    tran0.writeAction("slorii X16 X16 12 2328")
    tran0.writeAction("slorii X16 X16 12 77")
    tran0.writeAction("slorii X16 X16 12 2901")
    tran0.writeAction("movir X17 2908")
    tran0.writeAction("slorii X17 X17 12 539")
    tran0.writeAction("slorii X17 X17 12 845")
    tran0.writeAction("slorii X17 X17 12 1051")
    tran0.writeAction("slorii X17 X17 12 2258")
    tran0.writeAction("movir X18 1434")
    tran0.writeAction("slorii X18 X18 12 3021")
    tran0.writeAction("slorii X18 X18 12 800")
    tran0.writeAction("slorii X18 X18 12 1575")
    tran0.writeAction("slorii X18 X18 12 125")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
