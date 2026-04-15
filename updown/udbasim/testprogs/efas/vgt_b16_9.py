from EFA_v2 import *
def vgt_b16_9():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [60800, 28835, 13618, 1423, 572, 14694, 57128, 11645, 63353, 18906, 26521, 11157, 2]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 88")
    tran0.writeAction("slorii X19 X19 4 15")
    tran0.writeAction("slorii X19 X19 12 851")
    tran0.writeAction("slorii X19 X19 4 2")
    tran0.writeAction("slorii X19 X19 12 1802")
    tran0.writeAction("slorii X19 X19 4 3")
    tran0.writeAction("slorii X19 X19 12 3800")
    tran0.writeAction("slorii X19 X19 4 0")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 727")
    tran0.writeAction("slorii X17 X17 4 13")
    tran0.writeAction("slorii X17 X17 12 3570")
    tran0.writeAction("slorii X17 X17 4 8")
    tran0.writeAction("slorii X17 X17 12 918")
    tran0.writeAction("slorii X17 X17 4 6")
    tran0.writeAction("slorii X17 X17 12 35")
    tran0.writeAction("slorii X17 X17 4 12")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 697")
    tran0.writeAction("slorii X18 X18 4 5")
    tran0.writeAction("slorii X18 X18 12 1657")
    tran0.writeAction("slorii X18 X18 4 9")
    tran0.writeAction("slorii X18 X18 12 1181")
    tran0.writeAction("slorii X18 X18 4 10")
    tran0.writeAction("slorii X18 X18 12 3959")
    tran0.writeAction("slorii X18 X18 4 9")
    tran0.writeAction("vgt.b16 X19 X17 X18 2 ")
    tran0.writeAction("yieldt")
    return efa
