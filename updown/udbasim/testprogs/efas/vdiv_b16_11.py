from EFA_v2 import *
def vdiv_b16_11():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [15193, 27642, 56235, 259, 41045, 12614, 37497, 6053, 41073, 35313, 42528, 43647, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 16")
    tran0.writeAction("slorii X19 X19 4 3")
    tran0.writeAction("slorii X19 X19 12 3514")
    tran0.writeAction("slorii X19 X19 4 11")
    tran0.writeAction("slorii X19 X19 12 1727")
    tran0.writeAction("slorii X19 X19 4 10")
    tran0.writeAction("slorii X19 X19 12 949")
    tran0.writeAction("slorii X19 X19 4 9")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 378")
    tran0.writeAction("slorii X17 X17 4 5")
    tran0.writeAction("slorii X17 X17 12 2343")
    tran0.writeAction("slorii X17 X17 4 9")
    tran0.writeAction("slorii X17 X17 12 788")
    tran0.writeAction("slorii X17 X17 4 6")
    tran0.writeAction("slorii X17 X17 12 2565")
    tran0.writeAction("slorii X17 X17 4 5")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2727")
    tran0.writeAction("slorii X18 X18 4 15")
    tran0.writeAction("slorii X18 X18 12 2658")
    tran0.writeAction("slorii X18 X18 4 0")
    tran0.writeAction("slorii X18 X18 12 2207")
    tran0.writeAction("slorii X18 X18 4 1")
    tran0.writeAction("slorii X18 X18 12 2567")
    tran0.writeAction("slorii X18 X18 4 1")
    tran0.writeAction("vdiv.b16 X19 X17 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
