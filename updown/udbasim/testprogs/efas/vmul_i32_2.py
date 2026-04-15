from EFA_v2 import *
def vmul_i32_2():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1511415054, 1026720001, -1130000179, 588311224, -107267879, -1598491999, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 979")
    tran0.writeAction("slorii X19 X19 12 641")
    tran0.writeAction("slorii X19 X19 8 1")
    tran0.writeAction("slorii X19 X19 12 2654")
    tran0.writeAction("slorii X19 X19 12 2466")
    tran0.writeAction("slorii X19 X19 8 242")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 561")
    tran0.writeAction("slorii X17 X17 12 234")
    tran0.writeAction("slorii X17 X17 8 184")
    tran0.writeAction("slorii X17 X17 12 3018")
    tran0.writeAction("slorii X17 X17 12 1424")
    tran0.writeAction("slorii X17 X17 8 205")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2571")
    tran0.writeAction("slorii X18 X18 12 2290")
    tran0.writeAction("slorii X18 X18 8 161")
    tran0.writeAction("slorii X18 X18 12 3993")
    tran0.writeAction("slorii X18 X18 12 2872")
    tran0.writeAction("slorii X18 X18 8 217")
    tran0.writeAction("vmul.i32 X19 X17 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
