from EFA_v2 import *
def vadd_32_19():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1118203622, 3745235233, 635433961, 612460685, 829320000, 2948657467, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3571")
    tran0.writeAction("slorii X19 X19 12 3009")
    tran0.writeAction("slorii X19 X19 8 33")
    tran0.writeAction("slorii X19 X19 12 1066")
    tran0.writeAction("slorii X19 X19 12 1646")
    tran0.writeAction("slorii X19 X19 8 230")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 584")
    tran0.writeAction("slorii X17 X17 12 360")
    tran0.writeAction("slorii X17 X17 8 141")
    tran0.writeAction("slorii X17 X17 12 605")
    tran0.writeAction("slorii X17 X17 12 4083")
    tran0.writeAction("slorii X17 X17 8 233")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2812")
    tran0.writeAction("slorii X18 X18 12 241")
    tran0.writeAction("slorii X18 X18 8 59")
    tran0.writeAction("slorii X18 X18 12 790")
    tran0.writeAction("slorii X18 X18 12 3691")
    tran0.writeAction("slorii X18 X18 8 64")
    tran0.writeAction("vadd.32 X19 X17 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
