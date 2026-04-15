from EFA_v2 import *
def vmadd_b16_15():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [61439, 33817, 17054, 64879, 27778, 12973, 16869, 54794, 16640, 8903, 61073, 54467, 9]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 4054")
    tran0.writeAction("slorii X19 X19 4 15")
    tran0.writeAction("slorii X19 X19 12 1065")
    tran0.writeAction("slorii X19 X19 4 14")
    tran0.writeAction("slorii X19 X19 12 2113")
    tran0.writeAction("slorii X19 X19 4 9")
    tran0.writeAction("slorii X19 X19 12 3839")
    tran0.writeAction("slorii X19 X19 4 15")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 3424")
    tran0.writeAction("slorii X17 X17 4 10")
    tran0.writeAction("slorii X17 X17 12 1054")
    tran0.writeAction("slorii X17 X17 4 5")
    tran0.writeAction("slorii X17 X17 12 810")
    tran0.writeAction("slorii X17 X17 4 13")
    tran0.writeAction("slorii X17 X17 12 1736")
    tran0.writeAction("slorii X17 X17 4 2")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 3404")
    tran0.writeAction("slorii X18 X18 4 3")
    tran0.writeAction("slorii X18 X18 12 3817")
    tran0.writeAction("slorii X18 X18 4 1")
    tran0.writeAction("slorii X18 X18 12 556")
    tran0.writeAction("slorii X18 X18 4 7")
    tran0.writeAction("slorii X18 X18 12 1040")
    tran0.writeAction("slorii X18 X18 4 0")
    tran0.writeAction("vmadd.b16 X19 X17 X18 9 ")
    tran0.writeAction("yieldt")
    return efa
