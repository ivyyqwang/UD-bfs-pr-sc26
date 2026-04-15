from EFA_v2 import *
def vsqrt_i32_8():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [544395907, -313145631, -1847019084, -1992837779, 0]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3797")
    tran0.writeAction("slorii X19 X19 12 1478")
    tran0.writeAction("slorii X19 X19 8 225")
    tran0.writeAction("slorii X19 X19 12 519")
    tran0.writeAction("slorii X19 X19 12 722")
    tran0.writeAction("slorii X19 X19 8 131")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2195")
    tran0.writeAction("slorii X18 X18 12 1973")
    tran0.writeAction("slorii X18 X18 8 109")
    tran0.writeAction("slorii X18 X18 12 2334")
    tran0.writeAction("slorii X18 X18 12 2233")
    tran0.writeAction("slorii X18 X18 8 180")
    tran0.writeAction("vsqrt.i32 X19 X18 0 ")
    tran0.writeAction("yieldt")
    return efa
