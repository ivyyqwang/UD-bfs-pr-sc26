from EFA_v2 import *
def vmadd_b16_5():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [61203, 11287, 13068, 54089, 41792, 19422, 61559, 25633, 4571, 42480, 16616, 15095, 1]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3380")
    tran0.writeAction("slorii X19 X19 4 9")
    tran0.writeAction("slorii X19 X19 12 816")
    tran0.writeAction("slorii X19 X19 4 12")
    tran0.writeAction("slorii X19 X19 12 705")
    tran0.writeAction("slorii X19 X19 4 7")
    tran0.writeAction("slorii X19 X19 12 3825")
    tran0.writeAction("slorii X19 X19 4 3")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 1602")
    tran0.writeAction("slorii X17 X17 4 1")
    tran0.writeAction("slorii X17 X17 12 3847")
    tran0.writeAction("slorii X17 X17 4 7")
    tran0.writeAction("slorii X17 X17 12 1213")
    tran0.writeAction("slorii X17 X17 4 14")
    tran0.writeAction("slorii X17 X17 12 2612")
    tran0.writeAction("slorii X17 X17 4 0")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 943")
    tran0.writeAction("slorii X18 X18 4 7")
    tran0.writeAction("slorii X18 X18 12 1038")
    tran0.writeAction("slorii X18 X18 4 8")
    tran0.writeAction("slorii X18 X18 12 2655")
    tran0.writeAction("slorii X18 X18 4 0")
    tran0.writeAction("slorii X18 X18 12 285")
    tran0.writeAction("slorii X18 X18 4 11")
    tran0.writeAction("vmadd.b16 X19 X17 X18 1 ")
    tran0.writeAction("yieldt")
    return efa
