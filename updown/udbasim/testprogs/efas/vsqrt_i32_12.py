from EFA_v2 import *
def vsqrt_i32_12():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1016028374, -1805106726, -631662287, -770141621, 0]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 2374")
    tran0.writeAction("slorii X19 X19 12 2113")
    tran0.writeAction("slorii X19 X19 8 218")
    tran0.writeAction("slorii X19 X19 12 968")
    tran0.writeAction("slorii X19 X19 12 3932")
    tran0.writeAction("slorii X19 X19 8 214")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 3361")
    tran0.writeAction("slorii X18 X18 12 2194")
    tran0.writeAction("slorii X18 X18 8 75")
    tran0.writeAction("slorii X18 X18 12 3493")
    tran0.writeAction("slorii X18 X18 12 2457")
    tran0.writeAction("slorii X18 X18 8 49")
    tran0.writeAction("vsqrt.i32 X19 X18 0 ")
    tran0.writeAction("yieldt")
    return efa
