from EFA_v2 import *
def vmul_i32_19():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1855299938, 1689531657, -403546699, 2062351607, 1370147616, 1855622228, 1]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 1611")
    tran0.writeAction("slorii X19 X19 12 1077")
    tran0.writeAction("slorii X19 X19 8 9")
    tran0.writeAction("slorii X19 X19 12 1769")
    tran0.writeAction("slorii X19 X19 12 1441")
    tran0.writeAction("slorii X19 X19 8 98")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 1966")
    tran0.writeAction("slorii X17 X17 12 3324")
    tran0.writeAction("slorii X17 X17 8 247")
    tran0.writeAction("slorii X17 X17 12 3711")
    tran0.writeAction("slorii X17 X17 12 605")
    tran0.writeAction("slorii X17 X17 8 181")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1769")
    tran0.writeAction("slorii X18 X18 12 2700")
    tran0.writeAction("slorii X18 X18 8 84")
    tran0.writeAction("slorii X18 X18 12 1306")
    tran0.writeAction("slorii X18 X18 12 2763")
    tran0.writeAction("slorii X18 X18 8 32")
    tran0.writeAction("vmul.i32 X19 X17 X18 1 ")
    tran0.writeAction("yieldt")
    return efa
