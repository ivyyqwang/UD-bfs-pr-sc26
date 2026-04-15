from EFA_v2 import *
def vmul_32_0():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2566667081, 2477967257, 2690055988, 215531545, 1840917199, 2352833992, 1]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 2363")
    tran0.writeAction("slorii X19 X19 12 711")
    tran0.writeAction("slorii X19 X19 8 153")
    tran0.writeAction("slorii X19 X19 12 2447")
    tran0.writeAction("slorii X19 X19 12 3131")
    tran0.writeAction("slorii X19 X19 8 73")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 205")
    tran0.writeAction("slorii X17 X17 12 2240")
    tran0.writeAction("slorii X17 X17 8 25")
    tran0.writeAction("slorii X17 X17 12 2565")
    tran0.writeAction("slorii X17 X17 12 1791")
    tran0.writeAction("slorii X17 X17 8 52")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2243")
    tran0.writeAction("slorii X18 X18 12 3429")
    tran0.writeAction("slorii X18 X18 8 200")
    tran0.writeAction("slorii X18 X18 12 1755")
    tran0.writeAction("slorii X18 X18 12 2602")
    tran0.writeAction("slorii X18 X18 8 207")
    tran0.writeAction("vmul.32 X19 X17 X18 1 ")
    tran0.writeAction("yieldt")
    return efa
