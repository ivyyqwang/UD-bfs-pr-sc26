from EFA_v2 import *
def vmadd_32_4():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2428980963, 2172197538, 2226530831, 3605559777, 875751938, 2126625514, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 2071")
    tran0.writeAction("slorii X19 X19 12 2330")
    tran0.writeAction("slorii X19 X19 8 162")
    tran0.writeAction("slorii X19 X19 12 2316")
    tran0.writeAction("slorii X19 X19 12 1870")
    tran0.writeAction("slorii X19 X19 8 227")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 3438")
    tran0.writeAction("slorii X17 X17 12 2169")
    tran0.writeAction("slorii X17 X17 8 225")
    tran0.writeAction("slorii X17 X17 12 2123")
    tran0.writeAction("slorii X17 X17 12 1578")
    tran0.writeAction("slorii X17 X17 8 15")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2028")
    tran0.writeAction("slorii X18 X18 12 442")
    tran0.writeAction("slorii X18 X18 8 234")
    tran0.writeAction("slorii X18 X18 12 835")
    tran0.writeAction("slorii X18 X18 12 746")
    tran0.writeAction("slorii X18 X18 8 2")
    tran0.writeAction("vmadd.32 X19 X17 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
