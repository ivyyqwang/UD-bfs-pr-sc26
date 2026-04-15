from EFA_v2 import *
def vadd_b16_12():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [25544, 61669, 52384, 43483, 58002, 31402, 28708, 62174, 43285, 37523, 3430, 42224, 8]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 2717")
    tran0.writeAction("slorii X19 X19 4 11")
    tran0.writeAction("slorii X19 X19 12 3274")
    tran0.writeAction("slorii X19 X19 4 0")
    tran0.writeAction("slorii X19 X19 12 3854")
    tran0.writeAction("slorii X19 X19 4 5")
    tran0.writeAction("slorii X19 X19 12 1596")
    tran0.writeAction("slorii X19 X19 4 8")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 3885")
    tran0.writeAction("slorii X17 X17 4 14")
    tran0.writeAction("slorii X17 X17 12 1794")
    tran0.writeAction("slorii X17 X17 4 4")
    tran0.writeAction("slorii X17 X17 12 1962")
    tran0.writeAction("slorii X17 X17 4 10")
    tran0.writeAction("slorii X17 X17 12 3625")
    tran0.writeAction("slorii X17 X17 4 2")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2639")
    tran0.writeAction("slorii X18 X18 4 0")
    tran0.writeAction("slorii X18 X18 12 214")
    tran0.writeAction("slorii X18 X18 4 6")
    tran0.writeAction("slorii X18 X18 12 2345")
    tran0.writeAction("slorii X18 X18 4 3")
    tran0.writeAction("slorii X18 X18 12 2705")
    tran0.writeAction("slorii X18 X18 4 5")
    tran0.writeAction("vadd.b16 X19 X17 X18 8 ")
    tran0.writeAction("yieldt")
    return efa
