from EFA_v2 import *
def vsqrt_32_5():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [881139790, 3460238275, 214273028, 3604456766, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3299")
    tran0.writeAction("slorii X19 X19 12 3851")
    tran0.writeAction("slorii X19 X19 8 195")
    tran0.writeAction("slorii X19 X19 12 840")
    tran0.writeAction("slorii X19 X19 12 1312")
    tran0.writeAction("slorii X19 X19 8 78")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 3437")
    tran0.writeAction("slorii X18 X18 12 1957")
    tran0.writeAction("slorii X18 X18 8 62")
    tran0.writeAction("slorii X18 X18 12 204")
    tran0.writeAction("slorii X18 X18 12 1420")
    tran0.writeAction("slorii X18 X18 8 4")
    tran0.writeAction("vsqrt.32 X19 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
