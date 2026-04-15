from EFA_v2 import *
def vsqrt_i32_6():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [714320187, 437917766, 347547273, 1927719963, 0]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 417")
    tran0.writeAction("slorii X19 X19 12 2584")
    tran0.writeAction("slorii X19 X19 8 70")
    tran0.writeAction("slorii X19 X19 12 681")
    tran0.writeAction("slorii X19 X19 12 937")
    tran0.writeAction("slorii X19 X19 8 59")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1838")
    tran0.writeAction("slorii X18 X18 12 1708")
    tran0.writeAction("slorii X18 X18 8 27")
    tran0.writeAction("slorii X18 X18 12 331")
    tran0.writeAction("slorii X18 X18 12 1830")
    tran0.writeAction("slorii X18 X18 8 137")
    tran0.writeAction("vsqrt.i32 X19 X18 0 ")
    tran0.writeAction("yieldt")
    return efa
