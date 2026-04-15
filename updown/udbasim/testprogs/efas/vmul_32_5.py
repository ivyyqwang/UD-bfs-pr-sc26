from EFA_v2 import *
def vmul_32_5():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2814677037, 1978808304, 3569005733, 717979363, 1137103416, 3054161929, 1]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 1887")
    tran0.writeAction("slorii X19 X19 12 567")
    tran0.writeAction("slorii X19 X19 8 240")
    tran0.writeAction("slorii X19 X19 12 2684")
    tran0.writeAction("slorii X19 X19 12 1168")
    tran0.writeAction("slorii X19 X19 8 45")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 684")
    tran0.writeAction("slorii X17 X17 12 2942")
    tran0.writeAction("slorii X17 X17 8 227")
    tran0.writeAction("slorii X17 X17 12 3403")
    tran0.writeAction("slorii X17 X17 12 2740")
    tran0.writeAction("slorii X17 X17 8 165")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2912")
    tran0.writeAction("slorii X18 X18 12 2768")
    tran0.writeAction("slorii X18 X18 8 9")
    tran0.writeAction("slorii X18 X18 12 1084")
    tran0.writeAction("slorii X18 X18 12 1746")
    tran0.writeAction("slorii X18 X18 8 56")
    tran0.writeAction("vmul.32 X19 X17 X18 1 ")
    tran0.writeAction("yieldt")
    return efa
