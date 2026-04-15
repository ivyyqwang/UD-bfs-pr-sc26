from EFA_v2 import *
def vmul_b16_13():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [40317, 25970, 14535, 63388, 465, 26604, 34270, 1140, 17468, 52517, 56445, 53008, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3961")
    tran0.writeAction("slorii X19 X19 4 12")
    tran0.writeAction("slorii X19 X19 12 908")
    tran0.writeAction("slorii X19 X19 4 7")
    tran0.writeAction("slorii X19 X19 12 1623")
    tran0.writeAction("slorii X19 X19 4 2")
    tran0.writeAction("slorii X19 X19 12 2519")
    tran0.writeAction("slorii X19 X19 4 13")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 71")
    tran0.writeAction("slorii X17 X17 4 4")
    tran0.writeAction("slorii X17 X17 12 2141")
    tran0.writeAction("slorii X17 X17 4 14")
    tran0.writeAction("slorii X17 X17 12 1662")
    tran0.writeAction("slorii X17 X17 4 12")
    tran0.writeAction("slorii X17 X17 12 29")
    tran0.writeAction("slorii X17 X17 4 1")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 3313")
    tran0.writeAction("slorii X18 X18 4 0")
    tran0.writeAction("slorii X18 X18 12 3527")
    tran0.writeAction("slorii X18 X18 4 13")
    tran0.writeAction("slorii X18 X18 12 3282")
    tran0.writeAction("slorii X18 X18 4 5")
    tran0.writeAction("slorii X18 X18 12 1091")
    tran0.writeAction("slorii X18 X18 4 12")
    tran0.writeAction("vmul.b16 X19 X17 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
