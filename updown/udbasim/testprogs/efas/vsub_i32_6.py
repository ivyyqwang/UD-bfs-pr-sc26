from EFA_v2 import *
def vsub_i32_6():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-890955351, -428664861, 1147991785, 1857670951, -1578869895, -1056120190, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3687")
    tran0.writeAction("slorii X19 X19 12 791")
    tran0.writeAction("slorii X19 X19 8 227")
    tran0.writeAction("slorii X19 X19 12 3246")
    tran0.writeAction("slorii X19 X19 12 1305")
    tran0.writeAction("slorii X19 X19 8 169")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 1771")
    tran0.writeAction("slorii X17 X17 12 2511")
    tran0.writeAction("slorii X17 X17 8 39")
    tran0.writeAction("slorii X17 X17 12 1094")
    tran0.writeAction("slorii X17 X17 12 3318")
    tran0.writeAction("slorii X17 X17 8 233")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 3088")
    tran0.writeAction("slorii X18 X18 12 3298")
    tran0.writeAction("slorii X18 X18 8 130")
    tran0.writeAction("slorii X18 X18 12 2590")
    tran0.writeAction("slorii X18 X18 12 1115")
    tran0.writeAction("slorii X18 X18 8 121")
    tran0.writeAction("vsub.i32 X19 X17 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
