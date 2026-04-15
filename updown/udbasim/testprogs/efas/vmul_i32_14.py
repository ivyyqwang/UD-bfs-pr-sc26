from EFA_v2 import *
def vmul_i32_14():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1371641189, -1442966887, 428182976, -68350335, 1246386395, -1525783024, 2]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 2719")
    tran0.writeAction("slorii X19 X19 12 3602")
    tran0.writeAction("slorii X19 X19 8 153")
    tran0.writeAction("slorii X19 X19 12 1308")
    tran0.writeAction("slorii X19 X19 12 405")
    tran0.writeAction("slorii X19 X19 8 101")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 4030")
    tran0.writeAction("slorii X17 X17 12 3342")
    tran0.writeAction("slorii X17 X17 8 129")
    tran0.writeAction("slorii X17 X17 12 408")
    tran0.writeAction("slorii X17 X17 12 1421")
    tran0.writeAction("slorii X17 X17 8 192")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2640")
    tran0.writeAction("slorii X18 X18 12 3686")
    tran0.writeAction("slorii X18 X18 8 16")
    tran0.writeAction("slorii X18 X18 12 1188")
    tran0.writeAction("slorii X18 X18 12 2648")
    tran0.writeAction("slorii X18 X18 8 219")
    tran0.writeAction("vmul.i32 X19 X17 X18 2 ")
    tran0.writeAction("yieldt")
    return efa
