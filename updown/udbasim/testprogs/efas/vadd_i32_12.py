from EFA_v2 import *
def vadd_i32_12():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-2077725124, -1092316794, -1012803979, -1807542922, -1712756095, 805061072, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3054")
    tran0.writeAction("slorii X19 X19 12 1169")
    tran0.writeAction("slorii X19 X19 8 134")
    tran0.writeAction("slorii X19 X19 12 2114")
    tran0.writeAction("slorii X19 X19 12 2158")
    tran0.writeAction("slorii X19 X19 8 60")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 2372")
    tran0.writeAction("slorii X17 X17 12 789")
    tran0.writeAction("slorii X17 X17 8 118")
    tran0.writeAction("slorii X17 X17 12 3130")
    tran0.writeAction("slorii X17 X17 12 470")
    tran0.writeAction("slorii X17 X17 8 117")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 767")
    tran0.writeAction("slorii X18 X18 12 3137")
    tran0.writeAction("slorii X18 X18 8 208")
    tran0.writeAction("slorii X18 X18 12 2462")
    tran0.writeAction("slorii X18 X18 12 2410")
    tran0.writeAction("slorii X18 X18 8 129")
    tran0.writeAction("vadd.i32 X19 X17 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
