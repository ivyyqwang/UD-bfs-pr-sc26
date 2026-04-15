from EFA_v2 import *
def vgt_i32_19():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [648578580, 701075262, 1984231305, 835753202, 2112370243, 322371900, 2]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 668")
    tran0.writeAction("slorii X19 X19 12 2447")
    tran0.writeAction("slorii X19 X19 8 62")
    tran0.writeAction("slorii X19 X19 12 618")
    tran0.writeAction("slorii X19 X19 12 2182")
    tran0.writeAction("slorii X19 X19 8 20")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 797")
    tran0.writeAction("slorii X17 X17 12 148")
    tran0.writeAction("slorii X17 X17 8 242")
    tran0.writeAction("slorii X17 X17 12 1892")
    tran0.writeAction("slorii X17 X17 12 1271")
    tran0.writeAction("slorii X17 X17 8 137")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 307")
    tran0.writeAction("slorii X18 X18 12 1793")
    tran0.writeAction("slorii X18 X18 8 60")
    tran0.writeAction("slorii X18 X18 12 2014")
    tran0.writeAction("slorii X18 X18 12 2102")
    tran0.writeAction("slorii X18 X18 8 67")
    tran0.writeAction("vgt.i32 X19 X17 X18 2 ")
    tran0.writeAction("yieldt")
    return efa
