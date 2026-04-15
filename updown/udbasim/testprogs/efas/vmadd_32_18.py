from EFA_v2 import *
def vmadd_32_18():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1782752161, 1362827903, 3760810470, 3524286227, 4016933974, 3604911990, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 1299")
    tran0.writeAction("slorii X19 X19 12 2842")
    tran0.writeAction("slorii X19 X19 8 127")
    tran0.writeAction("slorii X19 X19 12 1700")
    tran0.writeAction("slorii X19 X19 12 675")
    tran0.writeAction("slorii X19 X19 8 161")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 3361")
    tran0.writeAction("slorii X17 X17 12 87")
    tran0.writeAction("slorii X17 X17 8 19")
    tran0.writeAction("slorii X17 X17 12 3586")
    tran0.writeAction("slorii X17 X17 12 2409")
    tran0.writeAction("slorii X17 X17 8 230")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 3437")
    tran0.writeAction("slorii X18 X18 12 3735")
    tran0.writeAction("slorii X18 X18 8 118")
    tran0.writeAction("slorii X18 X18 12 3830")
    tran0.writeAction("slorii X18 X18 12 3468")
    tran0.writeAction("slorii X18 X18 8 86")
    tran0.writeAction("vmadd.32 X19 X17 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
