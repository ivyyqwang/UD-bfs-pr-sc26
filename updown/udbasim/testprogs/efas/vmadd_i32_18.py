from EFA_v2 import *
def vmadd_i32_18():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1453716947, 264476760, 1702836976, 1656614420, 1186806221, 1754226450, 1]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 252")
    tran0.writeAction("slorii X19 X19 12 920")
    tran0.writeAction("slorii X19 X19 8 88")
    tran0.writeAction("slorii X19 X19 12 2709")
    tran0.writeAction("slorii X19 X19 12 2570")
    tran0.writeAction("slorii X19 X19 8 45")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 1579")
    tran0.writeAction("slorii X17 X17 12 3566")
    tran0.writeAction("slorii X17 X17 8 20")
    tran0.writeAction("slorii X17 X17 12 1623")
    tran0.writeAction("slorii X17 X17 12 3898")
    tran0.writeAction("slorii X17 X17 8 240")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1672")
    tran0.writeAction("slorii X18 X18 12 3935")
    tran0.writeAction("slorii X18 X18 8 18")
    tran0.writeAction("slorii X18 X18 12 1131")
    tran0.writeAction("slorii X18 X18 12 3385")
    tran0.writeAction("slorii X18 X18 8 205")
    tran0.writeAction("vmadd.i32 X19 X17 X18 1 ")
    tran0.writeAction("yieldt")
    return efa
