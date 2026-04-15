from EFA_v2 import *
def vadd_i32_8():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1303985004, -807087198, 1727029444, 8101415, 1594452309, 914506330, 2]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3326")
    tran0.writeAction("slorii X19 X19 12 1235")
    tran0.writeAction("slorii X19 X19 8 162")
    tran0.writeAction("slorii X19 X19 12 2852")
    tran0.writeAction("slorii X19 X19 12 1732")
    tran0.writeAction("slorii X19 X19 8 148")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 7")
    tran0.writeAction("slorii X17 X17 12 2974")
    tran0.writeAction("slorii X17 X17 8 39")
    tran0.writeAction("slorii X17 X17 12 1647")
    tran0.writeAction("slorii X17 X17 12 96")
    tran0.writeAction("slorii X17 X17 8 196")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 872")
    tran0.writeAction("slorii X18 X18 12 578")
    tran0.writeAction("slorii X18 X18 8 90")
    tran0.writeAction("slorii X18 X18 12 1520")
    tran0.writeAction("slorii X18 X18 12 2409")
    tran0.writeAction("slorii X18 X18 8 85")
    tran0.writeAction("vadd.i32 X19 X17 X18 2 ")
    tran0.writeAction("yieldt")
    return efa
