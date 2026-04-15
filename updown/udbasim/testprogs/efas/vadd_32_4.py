from EFA_v2 import *
def vadd_32_4():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3088425684, 1590594831, 1436263442, 793349056, 656436008, 2215787184, 2]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 1516")
    tran0.writeAction("slorii X19 X19 12 3725")
    tran0.writeAction("slorii X19 X19 8 15")
    tran0.writeAction("slorii X19 X19 12 2945")
    tran0.writeAction("slorii X19 X19 12 1442")
    tran0.writeAction("slorii X19 X19 8 212")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 756")
    tran0.writeAction("slorii X17 X17 12 2443")
    tran0.writeAction("slorii X17 X17 8 192")
    tran0.writeAction("slorii X17 X17 12 1369")
    tran0.writeAction("slorii X17 X17 12 2980")
    tran0.writeAction("slorii X17 X17 8 18")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2113")
    tran0.writeAction("slorii X18 X18 12 570")
    tran0.writeAction("slorii X18 X18 8 176")
    tran0.writeAction("slorii X18 X18 12 626")
    tran0.writeAction("slorii X18 X18 12 107")
    tran0.writeAction("slorii X18 X18 8 40")
    tran0.writeAction("vadd.32 X19 X17 X18 2 ")
    tran0.writeAction("yieldt")
    return efa
