from EFA_v2 import *
def vsub_32_0():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2746966899, 2354627186, 4169338774, 856979768, 1024278763, 956545489, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 2245")
    tran0.writeAction("slorii X19 X19 12 2242")
    tran0.writeAction("slorii X19 X19 8 114")
    tran0.writeAction("slorii X19 X19 12 2619")
    tran0.writeAction("slorii X19 X19 12 2915")
    tran0.writeAction("slorii X19 X19 8 115")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 817")
    tran0.writeAction("slorii X17 X17 12 1145")
    tran0.writeAction("slorii X17 X17 8 56")
    tran0.writeAction("slorii X17 X17 12 3976")
    tran0.writeAction("slorii X17 X17 12 783")
    tran0.writeAction("slorii X17 X17 8 150")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 912")
    tran0.writeAction("slorii X18 X18 12 953")
    tran0.writeAction("slorii X18 X18 8 209")
    tran0.writeAction("slorii X18 X18 12 976")
    tran0.writeAction("slorii X18 X18 12 3392")
    tran0.writeAction("slorii X18 X18 8 235")
    tran0.writeAction("vsub.32 X19 X17 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
