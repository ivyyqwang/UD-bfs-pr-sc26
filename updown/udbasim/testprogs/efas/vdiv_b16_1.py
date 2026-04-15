from EFA_v2 import *
def vdiv_b16_1():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [9699, 4118, 44265, 1349, 50608, 7503, 15777, 7996, 14846, 49180, 47371, 26364, 8]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 84")
    tran0.writeAction("slorii X19 X19 4 5")
    tran0.writeAction("slorii X19 X19 12 2766")
    tran0.writeAction("slorii X19 X19 4 9")
    tran0.writeAction("slorii X19 X19 12 257")
    tran0.writeAction("slorii X19 X19 4 6")
    tran0.writeAction("slorii X19 X19 12 606")
    tran0.writeAction("slorii X19 X19 4 3")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 499")
    tran0.writeAction("slorii X17 X17 4 12")
    tran0.writeAction("slorii X17 X17 12 986")
    tran0.writeAction("slorii X17 X17 4 1")
    tran0.writeAction("slorii X17 X17 12 468")
    tran0.writeAction("slorii X17 X17 4 15")
    tran0.writeAction("slorii X17 X17 12 3163")
    tran0.writeAction("slorii X17 X17 4 0")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1647")
    tran0.writeAction("slorii X18 X18 4 12")
    tran0.writeAction("slorii X18 X18 12 2960")
    tran0.writeAction("slorii X18 X18 4 11")
    tran0.writeAction("slorii X18 X18 12 3073")
    tran0.writeAction("slorii X18 X18 4 12")
    tran0.writeAction("slorii X18 X18 12 927")
    tran0.writeAction("slorii X18 X18 4 14")
    tran0.writeAction("vdiv.b16 X19 X17 X18 8 ")
    tran0.writeAction("yieldt")
    return efa
