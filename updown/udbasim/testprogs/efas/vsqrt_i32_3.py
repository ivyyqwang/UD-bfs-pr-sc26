from EFA_v2 import *
def vsqrt_i32_3():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1833342556, 2138579189, 350039491, 1946147491, 0]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 2039")
    tran0.writeAction("slorii X19 X19 12 2080")
    tran0.writeAction("slorii X19 X19 8 245")
    tran0.writeAction("slorii X19 X19 12 1748")
    tran0.writeAction("slorii X19 X19 12 1686")
    tran0.writeAction("slorii X19 X19 8 92")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1855")
    tran0.writeAction("slorii X18 X18 12 4058")
    tran0.writeAction("slorii X18 X18 8 163")
    tran0.writeAction("slorii X18 X18 12 333")
    tran0.writeAction("slorii X18 X18 12 3373")
    tran0.writeAction("slorii X18 X18 8 195")
    tran0.writeAction("vsqrt.i32 X19 X18 0 ")
    tran0.writeAction("yieldt")
    return efa
