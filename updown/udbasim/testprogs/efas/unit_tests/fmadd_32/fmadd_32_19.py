from EFA_v2 import *
def fmadd_32_19():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [134045914, 2590829053, 1529673819]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 7")
    tran0.writeAction("slorii X16 X16 12 4054")
    tran0.writeAction("slorii X16 X16 12 218")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 154")
    tran0.writeAction("slorii X17 X17 12 1742")
    tran0.writeAction("slorii X17 X17 12 2557")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 0")
    tran0.writeAction("slorii X18 X18 12 91")
    tran0.writeAction("slorii X18 X18 12 719")
    tran0.writeAction("slorii X18 X18 12 2139")
    tran0.writeAction("fmadd.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
