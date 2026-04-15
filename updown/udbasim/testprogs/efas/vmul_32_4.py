from EFA_v2 import *
def vmul_32_4():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1633002616, 3277427212, 1554210334, 1560250207, 3787665212, 1388401462, 1]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3125")
    tran0.writeAction("slorii X19 X19 12 2450")
    tran0.writeAction("slorii X19 X19 8 12")
    tran0.writeAction("slorii X19 X19 12 1557")
    tran0.writeAction("slorii X19 X19 12 1444")
    tran0.writeAction("slorii X19 X19 8 120")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 1487")
    tran0.writeAction("slorii X17 X17 12 3975")
    tran0.writeAction("slorii X17 X17 8 95")
    tran0.writeAction("slorii X17 X17 12 1482")
    tran0.writeAction("slorii X17 X17 12 862")
    tran0.writeAction("slorii X17 X17 8 30")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1324")
    tran0.writeAction("slorii X18 X18 12 339")
    tran0.writeAction("slorii X18 X18 8 54")
    tran0.writeAction("slorii X18 X18 12 3612")
    tran0.writeAction("slorii X18 X18 12 815")
    tran0.writeAction("slorii X18 X18 8 60")
    tran0.writeAction("vmul.32 X19 X17 X18 1 ")
    tran0.writeAction("yieldt")
    return efa
