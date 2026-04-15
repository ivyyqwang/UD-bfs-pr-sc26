from EFA_v2 import *
def vsub_b16_0():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [44518, 40671, 61732, 56158, 26296, 64275, 46121, 51761, 56363, 39054, 13531, 43481, 13]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3509")
    tran0.writeAction("slorii X19 X19 4 14")
    tran0.writeAction("slorii X19 X19 12 3858")
    tran0.writeAction("slorii X19 X19 4 4")
    tran0.writeAction("slorii X19 X19 12 2541")
    tran0.writeAction("slorii X19 X19 4 15")
    tran0.writeAction("slorii X19 X19 12 2782")
    tran0.writeAction("slorii X19 X19 4 6")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 3235")
    tran0.writeAction("slorii X17 X17 4 1")
    tran0.writeAction("slorii X17 X17 12 2882")
    tran0.writeAction("slorii X17 X17 4 9")
    tran0.writeAction("slorii X17 X17 12 4017")
    tran0.writeAction("slorii X17 X17 4 3")
    tran0.writeAction("slorii X17 X17 12 1643")
    tran0.writeAction("slorii X17 X17 4 8")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2717")
    tran0.writeAction("slorii X18 X18 4 9")
    tran0.writeAction("slorii X18 X18 12 845")
    tran0.writeAction("slorii X18 X18 4 11")
    tran0.writeAction("slorii X18 X18 12 2440")
    tran0.writeAction("slorii X18 X18 4 14")
    tran0.writeAction("slorii X18 X18 12 3522")
    tran0.writeAction("slorii X18 X18 4 11")
    tran0.writeAction("vsub.b16 X19 X17 X18 13 ")
    tran0.writeAction("yieldt")
    return efa
