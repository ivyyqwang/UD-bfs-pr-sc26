from EFA_v2 import *
def vmadd_i32_19():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [571558794, -1324881531, -722175535, -433621600, 462365490, 2062796823, 2]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 2832")
    tran0.writeAction("slorii X19 X19 12 2025")
    tran0.writeAction("slorii X19 X19 8 133")
    tran0.writeAction("slorii X19 X19 12 545")
    tran0.writeAction("slorii X19 X19 12 331")
    tran0.writeAction("slorii X19 X19 8 138")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 3682")
    tran0.writeAction("slorii X17 X17 12 1909")
    tran0.writeAction("slorii X17 X17 8 160")
    tran0.writeAction("slorii X17 X17 12 3407")
    tran0.writeAction("slorii X17 X17 12 1145")
    tran0.writeAction("slorii X17 X17 8 209")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1967")
    tran0.writeAction("slorii X18 X18 12 968")
    tran0.writeAction("slorii X18 X18 8 23")
    tran0.writeAction("slorii X18 X18 12 440")
    tran0.writeAction("slorii X18 X18 12 3875")
    tran0.writeAction("slorii X18 X18 8 50")
    tran0.writeAction("vmadd.i32 X19 X17 X18 2 ")
    tran0.writeAction("yieldt")
    return efa
