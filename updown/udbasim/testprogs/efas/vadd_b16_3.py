from EFA_v2 import *
def vadd_b16_3():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7847, 48490, 38704, 5824, 27026, 28121, 5544, 11790, 25201, 2003, 52582, 60689, 4]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 364")
    tran0.writeAction("slorii X19 X19 4 0")
    tran0.writeAction("slorii X19 X19 12 2419")
    tran0.writeAction("slorii X19 X19 4 0")
    tran0.writeAction("slorii X19 X19 12 3030")
    tran0.writeAction("slorii X19 X19 4 10")
    tran0.writeAction("slorii X19 X19 12 490")
    tran0.writeAction("slorii X19 X19 4 7")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 736")
    tran0.writeAction("slorii X17 X17 4 14")
    tran0.writeAction("slorii X17 X17 12 346")
    tran0.writeAction("slorii X17 X17 4 8")
    tran0.writeAction("slorii X17 X17 12 1757")
    tran0.writeAction("slorii X17 X17 4 9")
    tran0.writeAction("slorii X17 X17 12 1689")
    tran0.writeAction("slorii X17 X17 4 2")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 3793")
    tran0.writeAction("slorii X18 X18 4 1")
    tran0.writeAction("slorii X18 X18 12 3286")
    tran0.writeAction("slorii X18 X18 4 6")
    tran0.writeAction("slorii X18 X18 12 125")
    tran0.writeAction("slorii X18 X18 4 3")
    tran0.writeAction("slorii X18 X18 12 1575")
    tran0.writeAction("slorii X18 X18 4 1")
    tran0.writeAction("vadd.b16 X19 X17 X18 4 ")
    tran0.writeAction("yieldt")
    return efa
