from EFA_v2 import *
def vadd_b16_10():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [29331, 62740, 49119, 64836, 23438, 34256, 43263, 26341, 41469, 33352, 39507, 46601, 15]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 4052")
    tran0.writeAction("slorii X19 X19 4 4")
    tran0.writeAction("slorii X19 X19 12 3069")
    tran0.writeAction("slorii X19 X19 4 15")
    tran0.writeAction("slorii X19 X19 12 3921")
    tran0.writeAction("slorii X19 X19 4 4")
    tran0.writeAction("slorii X19 X19 12 1833")
    tran0.writeAction("slorii X19 X19 4 3")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 1646")
    tran0.writeAction("slorii X17 X17 4 5")
    tran0.writeAction("slorii X17 X17 12 2703")
    tran0.writeAction("slorii X17 X17 4 15")
    tran0.writeAction("slorii X17 X17 12 2141")
    tran0.writeAction("slorii X17 X17 4 0")
    tran0.writeAction("slorii X17 X17 12 1464")
    tran0.writeAction("slorii X17 X17 4 14")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2912")
    tran0.writeAction("slorii X18 X18 4 9")
    tran0.writeAction("slorii X18 X18 12 2469")
    tran0.writeAction("slorii X18 X18 4 3")
    tran0.writeAction("slorii X18 X18 12 2084")
    tran0.writeAction("slorii X18 X18 4 8")
    tran0.writeAction("slorii X18 X18 12 2591")
    tran0.writeAction("slorii X18 X18 4 13")
    tran0.writeAction("vadd.b16 X19 X17 X18 15 ")
    tran0.writeAction("yieldt")
    return efa
