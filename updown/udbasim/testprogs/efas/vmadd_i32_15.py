from EFA_v2 import *
def vmadd_i32_15():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1236934667, 1231180508, 196688324, 524030853, 1386986534, 1512330810, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 1174")
    tran0.writeAction("slorii X19 X19 12 594")
    tran0.writeAction("slorii X19 X19 8 220")
    tran0.writeAction("slorii X19 X19 12 2916")
    tran0.writeAction("slorii X19 X19 12 1503")
    tran0.writeAction("slorii X19 X19 8 245")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 499")
    tran0.writeAction("slorii X17 X17 12 3091")
    tran0.writeAction("slorii X17 X17 8 133")
    tran0.writeAction("slorii X17 X17 12 187")
    tran0.writeAction("slorii X17 X17 12 2361")
    tran0.writeAction("slorii X17 X17 8 196")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1442")
    tran0.writeAction("slorii X18 X18 12 1110")
    tran0.writeAction("slorii X18 X18 8 58")
    tran0.writeAction("slorii X18 X18 12 1322")
    tran0.writeAction("slorii X18 X18 12 3004")
    tran0.writeAction("slorii X18 X18 8 38")
    tran0.writeAction("vmadd.i32 X19 X17 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
