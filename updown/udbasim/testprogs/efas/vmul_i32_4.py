from EFA_v2 import *
def vmul_i32_4():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1432573013, -1078686464, -423758575, 1875512605, -651361720, -1168542967, 2]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3067")
    tran0.writeAction("slorii X19 X19 12 1165")
    tran0.writeAction("slorii X19 X19 8 0")
    tran0.writeAction("slorii X19 X19 12 1366")
    tran0.writeAction("slorii X19 X19 12 852")
    tran0.writeAction("slorii X19 X19 8 85")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 1788")
    tran0.writeAction("slorii X17 X17 12 2573")
    tran0.writeAction("slorii X17 X17 8 29")
    tran0.writeAction("slorii X17 X17 12 3691")
    tran0.writeAction("slorii X17 X17 12 3573")
    tran0.writeAction("slorii X17 X17 8 17")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2981")
    tran0.writeAction("slorii X18 X18 12 2419")
    tran0.writeAction("slorii X18 X18 8 9")
    tran0.writeAction("slorii X18 X18 12 3474")
    tran0.writeAction("slorii X18 X18 12 3330")
    tran0.writeAction("slorii X18 X18 8 72")
    tran0.writeAction("vmul.i32 X19 X17 X18 2 ")
    tran0.writeAction("yieldt")
    return efa
