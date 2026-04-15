from EFA_v2 import *
def vgt_b16_5():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [20315, 43687, 52250, 14966, 51684, 22752, 4509, 26287, 33088, 52442, 53089, 27403, 1]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 935")
    tran0.writeAction("slorii X19 X19 4 6")
    tran0.writeAction("slorii X19 X19 12 3265")
    tran0.writeAction("slorii X19 X19 4 10")
    tran0.writeAction("slorii X19 X19 12 2730")
    tran0.writeAction("slorii X19 X19 4 7")
    tran0.writeAction("slorii X19 X19 12 1269")
    tran0.writeAction("slorii X19 X19 4 11")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 1642")
    tran0.writeAction("slorii X17 X17 4 15")
    tran0.writeAction("slorii X17 X17 12 281")
    tran0.writeAction("slorii X17 X17 4 13")
    tran0.writeAction("slorii X17 X17 12 1422")
    tran0.writeAction("slorii X17 X17 4 0")
    tran0.writeAction("slorii X17 X17 12 3230")
    tran0.writeAction("slorii X17 X17 4 4")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1712")
    tran0.writeAction("slorii X18 X18 4 11")
    tran0.writeAction("slorii X18 X18 12 3318")
    tran0.writeAction("slorii X18 X18 4 1")
    tran0.writeAction("slorii X18 X18 12 3277")
    tran0.writeAction("slorii X18 X18 4 10")
    tran0.writeAction("slorii X18 X18 12 2068")
    tran0.writeAction("slorii X18 X18 4 0")
    tran0.writeAction("vgt.b16 X19 X17 X18 1 ")
    tran0.writeAction("yieldt")
    return efa
