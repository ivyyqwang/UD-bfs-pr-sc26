from EFA_v2 import *
def vmul_32_3():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1233886427, 3748396131, 118272845, 3802145463, 1600654044, 748138264, 2]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3574")
    tran0.writeAction("slorii X19 X19 12 3068")
    tran0.writeAction("slorii X19 X19 8 99")
    tran0.writeAction("slorii X19 X19 12 1176")
    tran0.writeAction("slorii X19 X19 12 2972")
    tran0.writeAction("slorii X19 X19 8 219")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 3626")
    tran0.writeAction("slorii X17 X17 12 34")
    tran0.writeAction("slorii X17 X17 8 183")
    tran0.writeAction("slorii X17 X17 12 112")
    tran0.writeAction("slorii X17 X17 12 3251")
    tran0.writeAction("slorii X17 X17 8 77")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 713")
    tran0.writeAction("slorii X18 X18 12 1967")
    tran0.writeAction("slorii X18 X18 8 24")
    tran0.writeAction("slorii X18 X18 12 1526")
    tran0.writeAction("slorii X18 X18 12 2058")
    tran0.writeAction("slorii X18 X18 8 220")
    tran0.writeAction("vmul.32 X19 X17 X18 2 ")
    tran0.writeAction("yieldt")
    return efa
