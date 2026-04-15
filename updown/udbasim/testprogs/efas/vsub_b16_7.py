from EFA_v2 import *
def vsub_b16_7():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [24670, 9471, 43899, 61766, 1115, 50549, 39750, 53990, 54957, 54752, 6157, 57466, 15]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3860")
    tran0.writeAction("slorii X19 X19 4 6")
    tran0.writeAction("slorii X19 X19 12 2743")
    tran0.writeAction("slorii X19 X19 4 11")
    tran0.writeAction("slorii X19 X19 12 591")
    tran0.writeAction("slorii X19 X19 4 15")
    tran0.writeAction("slorii X19 X19 12 1541")
    tran0.writeAction("slorii X19 X19 4 14")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 3374")
    tran0.writeAction("slorii X17 X17 4 6")
    tran0.writeAction("slorii X17 X17 12 2484")
    tran0.writeAction("slorii X17 X17 4 6")
    tran0.writeAction("slorii X17 X17 12 3159")
    tran0.writeAction("slorii X17 X17 4 5")
    tran0.writeAction("slorii X17 X17 12 69")
    tran0.writeAction("slorii X17 X17 4 11")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 3591")
    tran0.writeAction("slorii X18 X18 4 10")
    tran0.writeAction("slorii X18 X18 12 384")
    tran0.writeAction("slorii X18 X18 4 13")
    tran0.writeAction("slorii X18 X18 12 3422")
    tran0.writeAction("slorii X18 X18 4 0")
    tran0.writeAction("slorii X18 X18 12 3434")
    tran0.writeAction("slorii X18 X18 4 13")
    tran0.writeAction("vsub.b16 X19 X17 X18 15 ")
    tran0.writeAction("yieldt")
    return efa
