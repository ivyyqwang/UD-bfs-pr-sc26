from EFA_v2 import *
def fmadd_32_0():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [547336437, 737014787, 3982453694]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 32")
    tran0.writeAction("slorii X16 X16 12 2555")
    tran0.writeAction("slorii X16 X16 12 245")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 43")
    tran0.writeAction("slorii X17 X17 12 3807")
    tran0.writeAction("slorii X17 X17 12 1027")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 0")
    tran0.writeAction("slorii X18 X18 12 237")
    tran0.writeAction("slorii X18 X18 12 1526")
    tran0.writeAction("slorii X18 X18 12 3006")
    tran0.writeAction("fmadd.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
