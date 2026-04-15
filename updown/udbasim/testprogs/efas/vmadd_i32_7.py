from EFA_v2 import *
def vmadd_i32_7():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [661509936, 417440737, 1698356781, -1111317007, 978407305, -1859966709, 2]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 398")
    tran0.writeAction("slorii X19 X19 12 419")
    tran0.writeAction("slorii X19 X19 8 225")
    tran0.writeAction("slorii X19 X19 12 630")
    tran0.writeAction("slorii X19 X19 12 3543")
    tran0.writeAction("slorii X19 X19 8 48")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 3036")
    tran0.writeAction("slorii X17 X17 12 677")
    tran0.writeAction("slorii X17 X17 8 241")
    tran0.writeAction("slorii X17 X17 12 1619")
    tran0.writeAction("slorii X17 X17 12 2782")
    tran0.writeAction("slorii X17 X17 8 45")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2322")
    tran0.writeAction("slorii X18 X18 12 809")
    tran0.writeAction("slorii X18 X18 8 11")
    tran0.writeAction("slorii X18 X18 12 933")
    tran0.writeAction("slorii X18 X18 12 335")
    tran0.writeAction("slorii X18 X18 8 137")
    tran0.writeAction("vmadd.i32 X19 X17 X18 2 ")
    tran0.writeAction("yieldt")
    return efa
