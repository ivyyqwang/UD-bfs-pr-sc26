from EFA_v2 import *
def vsub_b16_10():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [27927, 51195, 26891, 25190, 37434, 7036, 4268, 31103, 23823, 53828, 4734, 30558, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 1574")
    tran0.writeAction("slorii X19 X19 4 6")
    tran0.writeAction("slorii X19 X19 12 1680")
    tran0.writeAction("slorii X19 X19 4 11")
    tran0.writeAction("slorii X19 X19 12 3199")
    tran0.writeAction("slorii X19 X19 4 11")
    tran0.writeAction("slorii X19 X19 12 1745")
    tran0.writeAction("slorii X19 X19 4 7")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 1943")
    tran0.writeAction("slorii X17 X17 4 15")
    tran0.writeAction("slorii X17 X17 12 266")
    tran0.writeAction("slorii X17 X17 4 12")
    tran0.writeAction("slorii X17 X17 12 439")
    tran0.writeAction("slorii X17 X17 4 12")
    tran0.writeAction("slorii X17 X17 12 2339")
    tran0.writeAction("slorii X17 X17 4 10")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1909")
    tran0.writeAction("slorii X18 X18 4 14")
    tran0.writeAction("slorii X18 X18 12 295")
    tran0.writeAction("slorii X18 X18 4 14")
    tran0.writeAction("slorii X18 X18 12 3364")
    tran0.writeAction("slorii X18 X18 4 4")
    tran0.writeAction("slorii X18 X18 12 1488")
    tran0.writeAction("slorii X18 X18 4 15")
    tran0.writeAction("vsub.b16 X19 X17 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
