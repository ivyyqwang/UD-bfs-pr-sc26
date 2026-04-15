from EFA_v2 import *
def vmadd_b16_13():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [14335, 64066, 60180, 46856, 17465, 30381, 56389, 10613, 56456, 20792, 60859, 22966, 5]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 2928")
    tran0.writeAction("slorii X19 X19 4 8")
    tran0.writeAction("slorii X19 X19 12 3761")
    tran0.writeAction("slorii X19 X19 4 4")
    tran0.writeAction("slorii X19 X19 12 4004")
    tran0.writeAction("slorii X19 X19 4 2")
    tran0.writeAction("slorii X19 X19 12 895")
    tran0.writeAction("slorii X19 X19 4 15")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 663")
    tran0.writeAction("slorii X17 X17 4 5")
    tran0.writeAction("slorii X17 X17 12 3524")
    tran0.writeAction("slorii X17 X17 4 5")
    tran0.writeAction("slorii X17 X17 12 1898")
    tran0.writeAction("slorii X17 X17 4 13")
    tran0.writeAction("slorii X17 X17 12 1091")
    tran0.writeAction("slorii X17 X17 4 9")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1435")
    tran0.writeAction("slorii X18 X18 4 6")
    tran0.writeAction("slorii X18 X18 12 3803")
    tran0.writeAction("slorii X18 X18 4 11")
    tran0.writeAction("slorii X18 X18 12 1299")
    tran0.writeAction("slorii X18 X18 4 8")
    tran0.writeAction("slorii X18 X18 12 3528")
    tran0.writeAction("slorii X18 X18 4 8")
    tran0.writeAction("vmadd.b16 X19 X17 X18 5 ")
    tran0.writeAction("yieldt")
    return efa
