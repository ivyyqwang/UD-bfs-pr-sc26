from EFA_v2 import *
def vgt_b16_17():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [26012, 44272, 15372, 3838, 1512, 43113, 39354, 33300, 21574, 53338, 62804, 63692, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 239")
    tran0.writeAction("slorii X19 X19 4 14")
    tran0.writeAction("slorii X19 X19 12 960")
    tran0.writeAction("slorii X19 X19 4 12")
    tran0.writeAction("slorii X19 X19 12 2767")
    tran0.writeAction("slorii X19 X19 4 0")
    tran0.writeAction("slorii X19 X19 12 1625")
    tran0.writeAction("slorii X19 X19 4 12")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 2081")
    tran0.writeAction("slorii X17 X17 4 4")
    tran0.writeAction("slorii X17 X17 12 2459")
    tran0.writeAction("slorii X17 X17 4 10")
    tran0.writeAction("slorii X17 X17 12 2694")
    tran0.writeAction("slorii X17 X17 4 9")
    tran0.writeAction("slorii X17 X17 12 94")
    tran0.writeAction("slorii X17 X17 4 8")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 3980")
    tran0.writeAction("slorii X18 X18 4 12")
    tran0.writeAction("slorii X18 X18 12 3925")
    tran0.writeAction("slorii X18 X18 4 4")
    tran0.writeAction("slorii X18 X18 12 3333")
    tran0.writeAction("slorii X18 X18 4 10")
    tran0.writeAction("slorii X18 X18 12 1348")
    tran0.writeAction("slorii X18 X18 4 6")
    tran0.writeAction("vgt.b16 X19 X17 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
