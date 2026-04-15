from EFA_v2 import *
def vgt_b16_14():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [10346, 2169, 42453, 53625, 56729, 55175, 36454, 60865, 39412, 61872, 19880, 37254, 2]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3351")
    tran0.writeAction("slorii X19 X19 4 9")
    tran0.writeAction("slorii X19 X19 12 2653")
    tran0.writeAction("slorii X19 X19 4 5")
    tran0.writeAction("slorii X19 X19 12 135")
    tran0.writeAction("slorii X19 X19 4 9")
    tran0.writeAction("slorii X19 X19 12 646")
    tran0.writeAction("slorii X19 X19 4 10")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 3804")
    tran0.writeAction("slorii X17 X17 4 1")
    tran0.writeAction("slorii X17 X17 12 2278")
    tran0.writeAction("slorii X17 X17 4 6")
    tran0.writeAction("slorii X17 X17 12 3448")
    tran0.writeAction("slorii X17 X17 4 7")
    tran0.writeAction("slorii X17 X17 12 3545")
    tran0.writeAction("slorii X17 X17 4 9")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2328")
    tran0.writeAction("slorii X18 X18 4 6")
    tran0.writeAction("slorii X18 X18 12 1242")
    tran0.writeAction("slorii X18 X18 4 8")
    tran0.writeAction("slorii X18 X18 12 3867")
    tran0.writeAction("slorii X18 X18 4 0")
    tran0.writeAction("slorii X18 X18 12 2463")
    tran0.writeAction("slorii X18 X18 4 4")
    tran0.writeAction("vgt.b16 X19 X17 X18 2 ")
    tran0.writeAction("yieldt")
    return efa
