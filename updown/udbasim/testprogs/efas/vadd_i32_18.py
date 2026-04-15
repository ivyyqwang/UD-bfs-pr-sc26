from EFA_v2 import *
def vadd_i32_18():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1710643128, -1572387352, 847754819, 1658306579, 597193602, 1586361263, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 2596")
    tran0.writeAction("slorii X19 X19 12 1861")
    tran0.writeAction("slorii X19 X19 8 232")
    tran0.writeAction("slorii X19 X19 12 2464")
    tran0.writeAction("slorii X19 X19 12 2472")
    tran0.writeAction("slorii X19 X19 8 72")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 1581")
    tran0.writeAction("slorii X17 X17 12 1984")
    tran0.writeAction("slorii X17 X17 8 19")
    tran0.writeAction("slorii X17 X17 12 808")
    tran0.writeAction("slorii X17 X17 12 1974")
    tran0.writeAction("slorii X17 X17 8 67")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1512")
    tran0.writeAction("slorii X18 X18 12 3571")
    tran0.writeAction("slorii X18 X18 8 175")
    tran0.writeAction("slorii X18 X18 12 569")
    tran0.writeAction("slorii X18 X18 12 2163")
    tran0.writeAction("slorii X18 X18 8 130")
    tran0.writeAction("vadd.i32 X19 X17 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
