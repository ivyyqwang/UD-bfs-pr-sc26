from EFA_v2 import *
def vsub_b16_1():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [49851, 24690, 54057, 57426, 11222, 18401, 25083, 58053, 57865, 28897, 49266, 63759, 1]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3589")
    tran0.writeAction("slorii X19 X19 4 2")
    tran0.writeAction("slorii X19 X19 12 3378")
    tran0.writeAction("slorii X19 X19 4 9")
    tran0.writeAction("slorii X19 X19 12 1543")
    tran0.writeAction("slorii X19 X19 4 2")
    tran0.writeAction("slorii X19 X19 12 3115")
    tran0.writeAction("slorii X19 X19 4 11")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 3628")
    tran0.writeAction("slorii X17 X17 4 5")
    tran0.writeAction("slorii X17 X17 12 1567")
    tran0.writeAction("slorii X17 X17 4 11")
    tran0.writeAction("slorii X17 X17 12 1150")
    tran0.writeAction("slorii X17 X17 4 1")
    tran0.writeAction("slorii X17 X17 12 701")
    tran0.writeAction("slorii X17 X17 4 6")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 3984")
    tran0.writeAction("slorii X18 X18 4 15")
    tran0.writeAction("slorii X18 X18 12 3079")
    tran0.writeAction("slorii X18 X18 4 2")
    tran0.writeAction("slorii X18 X18 12 1806")
    tran0.writeAction("slorii X18 X18 4 1")
    tran0.writeAction("slorii X18 X18 12 3616")
    tran0.writeAction("slorii X18 X18 4 9")
    tran0.writeAction("vsub.b16 X19 X17 X18 1 ")
    tran0.writeAction("yieldt")
    return efa
