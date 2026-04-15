from EFA_v2 import *
def vmul_i32_3():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [514274271, 635242776, 799183772, 1884872719, -892262585, -171380774, 1]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 605")
    tran0.writeAction("slorii X19 X19 12 3337")
    tran0.writeAction("slorii X19 X19 8 24")
    tran0.writeAction("slorii X19 X19 12 490")
    tran0.writeAction("slorii X19 X19 12 1843")
    tran0.writeAction("slorii X19 X19 8 223")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 1797")
    tran0.writeAction("slorii X17 X17 12 2272")
    tran0.writeAction("slorii X17 X17 8 15")
    tran0.writeAction("slorii X17 X17 12 762")
    tran0.writeAction("slorii X17 X17 12 659")
    tran0.writeAction("slorii X17 X17 8 156")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 3932")
    tran0.writeAction("slorii X18 X18 12 2287")
    tran0.writeAction("slorii X18 X18 8 218")
    tran0.writeAction("slorii X18 X18 12 3245")
    tran0.writeAction("slorii X18 X18 12 295")
    tran0.writeAction("slorii X18 X18 8 71")
    tran0.writeAction("vmul.i32 X19 X17 X18 1 ")
    tran0.writeAction("yieldt")
    return efa
