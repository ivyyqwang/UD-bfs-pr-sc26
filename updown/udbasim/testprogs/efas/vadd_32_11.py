from EFA_v2 import *
def vadd_32_11():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3688916881, 1188002424, 923587314, 3650315695, 1078760591, 3936154216, 1]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 1132")
    tran0.writeAction("slorii X19 X19 12 3962")
    tran0.writeAction("slorii X19 X19 8 120")
    tran0.writeAction("slorii X19 X19 12 3518")
    tran0.writeAction("slorii X19 X19 12 103")
    tran0.writeAction("slorii X19 X19 8 145")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 3481")
    tran0.writeAction("slorii X17 X17 12 869")
    tran0.writeAction("slorii X17 X17 8 175")
    tran0.writeAction("slorii X17 X17 12 880")
    tran0.writeAction("slorii X17 X17 12 3282")
    tran0.writeAction("slorii X17 X17 8 242")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 3753")
    tran0.writeAction("slorii X18 X18 12 3314")
    tran0.writeAction("slorii X18 X18 8 104")
    tran0.writeAction("slorii X18 X18 12 1028")
    tran0.writeAction("slorii X18 X18 12 3220")
    tran0.writeAction("slorii X18 X18 8 143")
    tran0.writeAction("vadd.32 X19 X17 X18 1 ")
    tran0.writeAction("yieldt")
    return efa
