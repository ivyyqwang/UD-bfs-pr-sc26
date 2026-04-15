from EFA_v2 import *
def vadd_b16_0():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [11708, 57619, 7443, 59719, 14282, 56643, 2407, 39992, 65283, 54474, 34779, 40000, 7]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3732")
    tran0.writeAction("slorii X19 X19 4 7")
    tran0.writeAction("slorii X19 X19 12 465")
    tran0.writeAction("slorii X19 X19 4 3")
    tran0.writeAction("slorii X19 X19 12 3601")
    tran0.writeAction("slorii X19 X19 4 3")
    tran0.writeAction("slorii X19 X19 12 731")
    tran0.writeAction("slorii X19 X19 4 12")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 2499")
    tran0.writeAction("slorii X17 X17 4 8")
    tran0.writeAction("slorii X17 X17 12 150")
    tran0.writeAction("slorii X17 X17 4 7")
    tran0.writeAction("slorii X17 X17 12 3540")
    tran0.writeAction("slorii X17 X17 4 3")
    tran0.writeAction("slorii X17 X17 12 892")
    tran0.writeAction("slorii X17 X17 4 10")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2500")
    tran0.writeAction("slorii X18 X18 4 0")
    tran0.writeAction("slorii X18 X18 12 2173")
    tran0.writeAction("slorii X18 X18 4 11")
    tran0.writeAction("slorii X18 X18 12 3404")
    tran0.writeAction("slorii X18 X18 4 10")
    tran0.writeAction("slorii X18 X18 12 4080")
    tran0.writeAction("slorii X18 X18 4 3")
    tran0.writeAction("vadd.b16 X19 X17 X18 7 ")
    tran0.writeAction("yieldt")
    return efa
