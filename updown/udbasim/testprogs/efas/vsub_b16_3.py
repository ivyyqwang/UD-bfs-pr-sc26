from EFA_v2 import *
def vsub_b16_3():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4980, 56970, 26153, 46341, 54942, 31033, 40955, 64057, 50906, 51450, 23678, 40297, 2]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 2896")
    tran0.writeAction("slorii X19 X19 4 5")
    tran0.writeAction("slorii X19 X19 12 1634")
    tran0.writeAction("slorii X19 X19 4 9")
    tran0.writeAction("slorii X19 X19 12 3560")
    tran0.writeAction("slorii X19 X19 4 10")
    tran0.writeAction("slorii X19 X19 12 311")
    tran0.writeAction("slorii X19 X19 4 4")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 4003")
    tran0.writeAction("slorii X17 X17 4 9")
    tran0.writeAction("slorii X17 X17 12 2559")
    tran0.writeAction("slorii X17 X17 4 11")
    tran0.writeAction("slorii X17 X17 12 1939")
    tran0.writeAction("slorii X17 X17 4 9")
    tran0.writeAction("slorii X17 X17 12 3433")
    tran0.writeAction("slorii X17 X17 4 14")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2518")
    tran0.writeAction("slorii X18 X18 4 9")
    tran0.writeAction("slorii X18 X18 12 1479")
    tran0.writeAction("slorii X18 X18 4 14")
    tran0.writeAction("slorii X18 X18 12 3215")
    tran0.writeAction("slorii X18 X18 4 10")
    tran0.writeAction("slorii X18 X18 12 3181")
    tran0.writeAction("slorii X18 X18 4 10")
    tran0.writeAction("vsub.b16 X19 X17 X18 2 ")
    tran0.writeAction("yieldt")
    return efa
