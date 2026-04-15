from EFA_v2 import *
def vmadd_b16_1():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [22141, 34242, 55482, 59766, 1240, 46125, 8959, 58513, 17789, 9440, 9359, 4861, 10]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3735")
    tran0.writeAction("slorii X19 X19 4 6")
    tran0.writeAction("slorii X19 X19 12 3467")
    tran0.writeAction("slorii X19 X19 4 10")
    tran0.writeAction("slorii X19 X19 12 2140")
    tran0.writeAction("slorii X19 X19 4 2")
    tran0.writeAction("slorii X19 X19 12 1383")
    tran0.writeAction("slorii X19 X19 4 13")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 3657")
    tran0.writeAction("slorii X17 X17 4 1")
    tran0.writeAction("slorii X17 X17 12 559")
    tran0.writeAction("slorii X17 X17 4 15")
    tran0.writeAction("slorii X17 X17 12 2882")
    tran0.writeAction("slorii X17 X17 4 13")
    tran0.writeAction("slorii X17 X17 12 77")
    tran0.writeAction("slorii X17 X17 4 8")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 303")
    tran0.writeAction("slorii X18 X18 4 13")
    tran0.writeAction("slorii X18 X18 12 584")
    tran0.writeAction("slorii X18 X18 4 15")
    tran0.writeAction("slorii X18 X18 12 590")
    tran0.writeAction("slorii X18 X18 4 0")
    tran0.writeAction("slorii X18 X18 12 1111")
    tran0.writeAction("slorii X18 X18 4 13")
    tran0.writeAction("vmadd.b16 X19 X17 X18 10 ")
    tran0.writeAction("yieldt")
    return efa
