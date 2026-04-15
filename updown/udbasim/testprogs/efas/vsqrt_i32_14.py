from EFA_v2 import *
def vsqrt_i32_14():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-451603382, 1545761473, 818025946, -34035375, 0]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 1474")
    tran0.writeAction("slorii X19 X19 12 626")
    tran0.writeAction("slorii X19 X19 8 193")
    tran0.writeAction("slorii X19 X19 12 3665")
    tran0.writeAction("slorii X19 X19 12 1300")
    tran0.writeAction("slorii X19 X19 8 74")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 4063")
    tran0.writeAction("slorii X18 X18 12 2217")
    tran0.writeAction("slorii X18 X18 8 81")
    tran0.writeAction("slorii X18 X18 12 780")
    tran0.writeAction("slorii X18 X18 12 533")
    tran0.writeAction("slorii X18 X18 8 218")
    tran0.writeAction("vsqrt.i32 X19 X18 0 ")
    tran0.writeAction("yieldt")
    return efa
