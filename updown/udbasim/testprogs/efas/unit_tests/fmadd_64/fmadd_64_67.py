from EFA_v2 import *
def fmadd_64_67():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [10223777460313931557, 12142683306536155869, 4858802837668834510]
    tran0.writeAction("movir X16 36322")
    tran0.writeAction("slorii X16 X16 12 630")
    tran0.writeAction("slorii X16 X16 12 3752")
    tran0.writeAction("slorii X16 X16 12 2691")
    tran0.writeAction("slorii X16 X16 12 3877")
    tran0.writeAction("movir X17 43139")
    tran0.writeAction("slorii X17 X17 12 1954")
    tran0.writeAction("slorii X17 X17 12 498")
    tran0.writeAction("slorii X17 X17 12 627")
    tran0.writeAction("slorii X17 X17 12 2781")
    tran0.writeAction("movir X18 17261")
    tran0.writeAction("slorii X18 X18 12 3831")
    tran0.writeAction("slorii X18 X18 12 20")
    tran0.writeAction("slorii X18 X18 12 3730")
    tran0.writeAction("slorii X18 X18 12 3278")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
