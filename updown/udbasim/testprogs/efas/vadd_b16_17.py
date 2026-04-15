from EFA_v2 import *
def vadd_b16_17():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [10482, 62700, 35982, 53805, 43573, 25954, 43651, 10306, 25527, 14261, 41923, 35216, 9]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3362")
    tran0.writeAction("slorii X19 X19 4 13")
    tran0.writeAction("slorii X19 X19 12 2248")
    tran0.writeAction("slorii X19 X19 4 14")
    tran0.writeAction("slorii X19 X19 12 3918")
    tran0.writeAction("slorii X19 X19 4 12")
    tran0.writeAction("slorii X19 X19 12 655")
    tran0.writeAction("slorii X19 X19 4 2")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 644")
    tran0.writeAction("slorii X17 X17 4 2")
    tran0.writeAction("slorii X17 X17 12 2728")
    tran0.writeAction("slorii X17 X17 4 3")
    tran0.writeAction("slorii X17 X17 12 1622")
    tran0.writeAction("slorii X17 X17 4 2")
    tran0.writeAction("slorii X17 X17 12 2723")
    tran0.writeAction("slorii X17 X17 4 5")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2201")
    tran0.writeAction("slorii X18 X18 4 0")
    tran0.writeAction("slorii X18 X18 12 2620")
    tran0.writeAction("slorii X18 X18 4 3")
    tran0.writeAction("slorii X18 X18 12 891")
    tran0.writeAction("slorii X18 X18 4 5")
    tran0.writeAction("slorii X18 X18 12 1595")
    tran0.writeAction("slorii X18 X18 4 7")
    tran0.writeAction("vadd.b16 X19 X17 X18 9 ")
    tran0.writeAction("yieldt")
    return efa
