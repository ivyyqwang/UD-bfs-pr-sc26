from EFA_v2 import *
def fmadd_32_61():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3441603158, 1484960069, 2841747303]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 205")
    tran0.writeAction("slorii X16 X16 12 555")
    tran0.writeAction("slorii X16 X16 12 598")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 88")
    tran0.writeAction("slorii X17 X17 12 2091")
    tran0.writeAction("slorii X17 X17 12 325")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 0")
    tran0.writeAction("slorii X18 X18 12 169")
    tran0.writeAction("slorii X18 X18 12 1561")
    tran0.writeAction("slorii X18 X18 12 3943")
    tran0.writeAction("fmadd.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
