from EFA_v2 import *
def vmul_i32_16():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1049632821, 391421424, -507019495, 1598089137, 1489295643, 469982531, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 373")
    tran0.writeAction("slorii X19 X19 12 1181")
    tran0.writeAction("slorii X19 X19 8 240")
    tran0.writeAction("slorii X19 X19 12 3094")
    tran0.writeAction("slorii X19 X19 12 4063")
    tran0.writeAction("slorii X19 X19 8 203")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 1524")
    tran0.writeAction("slorii X17 X17 12 231")
    tran0.writeAction("slorii X17 X17 8 177")
    tran0.writeAction("slorii X17 X17 12 3612")
    tran0.writeAction("slorii X17 X17 12 1919")
    tran0.writeAction("slorii X17 X17 8 25")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 448")
    tran0.writeAction("slorii X18 X18 12 861")
    tran0.writeAction("slorii X18 X18 8 67")
    tran0.writeAction("slorii X18 X18 12 1420")
    tran0.writeAction("slorii X18 X18 12 1241")
    tran0.writeAction("slorii X18 X18 8 27")
    tran0.writeAction("vmul.i32 X19 X17 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
