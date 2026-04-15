from EFA_v2 import *
def vgt_i32_6():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-663205008, -483791032, 121101836, -798070691, -278528829, 1542447893, 1]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3634")
    tran0.writeAction("slorii X19 X19 12 2543")
    tran0.writeAction("slorii X19 X19 8 72")
    tran0.writeAction("slorii X19 X19 12 3463")
    tran0.writeAction("slorii X19 X19 12 2123")
    tran0.writeAction("slorii X19 X19 8 112")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 3334")
    tran0.writeAction("slorii X17 X17 12 3688")
    tran0.writeAction("slorii X17 X17 8 93")
    tran0.writeAction("slorii X17 X17 12 115")
    tran0.writeAction("slorii X17 X17 12 2014")
    tran0.writeAction("slorii X17 X17 8 12")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1470")
    tran0.writeAction("slorii X18 X18 12 4067")
    tran0.writeAction("slorii X18 X18 8 21")
    tran0.writeAction("slorii X18 X18 12 3830")
    tran0.writeAction("slorii X18 X18 12 1532")
    tran0.writeAction("slorii X18 X18 8 195")
    tran0.writeAction("vgt.i32 X19 X17 X18 1 ")
    tran0.writeAction("yieldt")
    return efa
