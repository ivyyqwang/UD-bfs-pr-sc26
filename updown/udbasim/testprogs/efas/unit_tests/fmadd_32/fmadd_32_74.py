from EFA_v2 import *
def fmadd_32_74():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2726235761, 3552225680, 4126230142]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 162")
    tran0.writeAction("slorii X16 X16 12 2032")
    tran0.writeAction("slorii X16 X16 12 3697")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 211")
    tran0.writeAction("slorii X17 X17 12 2986")
    tran0.writeAction("slorii X17 X17 12 2448")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 0")
    tran0.writeAction("slorii X18 X18 12 245")
    tran0.writeAction("slorii X18 X18 12 3860")
    tran0.writeAction("slorii X18 X18 12 1662")
    tran0.writeAction("fmadd.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
