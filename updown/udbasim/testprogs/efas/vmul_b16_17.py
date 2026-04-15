from EFA_v2 import *
def vmul_b16_17():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [10462, 57078, 63280, 23755, 1790, 17497, 22902, 7897, 28955, 27836, 29037, 10379, 7]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 1484")
    tran0.writeAction("slorii X19 X19 4 11")
    tran0.writeAction("slorii X19 X19 12 3955")
    tran0.writeAction("slorii X19 X19 4 0")
    tran0.writeAction("slorii X19 X19 12 3567")
    tran0.writeAction("slorii X19 X19 4 6")
    tran0.writeAction("slorii X19 X19 12 653")
    tran0.writeAction("slorii X19 X19 4 14")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 493")
    tran0.writeAction("slorii X17 X17 4 9")
    tran0.writeAction("slorii X17 X17 12 1431")
    tran0.writeAction("slorii X17 X17 4 6")
    tran0.writeAction("slorii X17 X17 12 1093")
    tran0.writeAction("slorii X17 X17 4 9")
    tran0.writeAction("slorii X17 X17 12 111")
    tran0.writeAction("slorii X17 X17 4 14")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 648")
    tran0.writeAction("slorii X18 X18 4 11")
    tran0.writeAction("slorii X18 X18 12 1814")
    tran0.writeAction("slorii X18 X18 4 13")
    tran0.writeAction("slorii X18 X18 12 1739")
    tran0.writeAction("slorii X18 X18 4 12")
    tran0.writeAction("slorii X18 X18 12 1809")
    tran0.writeAction("slorii X18 X18 4 11")
    tran0.writeAction("vmul.b16 X19 X17 X18 7 ")
    tran0.writeAction("yieldt")
    return efa
