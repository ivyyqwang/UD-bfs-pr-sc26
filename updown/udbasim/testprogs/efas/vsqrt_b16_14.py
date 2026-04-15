from EFA_v2 import *
def vsqrt_b16_14():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [11874, 44730, 47417, 6099, 35974, 4385, 6083, 49915, 14]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 381")
    tran0.writeAction("slorii X19 X19 4 3")
    tran0.writeAction("slorii X19 X19 12 2963")
    tran0.writeAction("slorii X19 X19 4 9")
    tran0.writeAction("slorii X19 X19 12 2795")
    tran0.writeAction("slorii X19 X19 4 10")
    tran0.writeAction("slorii X19 X19 12 742")
    tran0.writeAction("slorii X19 X19 4 2")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 3119")
    tran0.writeAction("slorii X18 X18 4 11")
    tran0.writeAction("slorii X18 X18 12 380")
    tran0.writeAction("slorii X18 X18 4 3")
    tran0.writeAction("slorii X18 X18 12 274")
    tran0.writeAction("slorii X18 X18 4 1")
    tran0.writeAction("slorii X18 X18 12 2248")
    tran0.writeAction("slorii X18 X18 4 6")
    tran0.writeAction("vsqrt.b16 X19 X18 14 ")
    tran0.writeAction("yieldt")
    return efa
