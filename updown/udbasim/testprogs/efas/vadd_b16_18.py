from EFA_v2 import *
def vadd_b16_18():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [47094, 29612, 34958, 2332, 47007, 41868, 44867, 27344, 30058, 45419, 33708, 5727, 11]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 145")
    tran0.writeAction("slorii X19 X19 4 12")
    tran0.writeAction("slorii X19 X19 12 2184")
    tran0.writeAction("slorii X19 X19 4 14")
    tran0.writeAction("slorii X19 X19 12 1850")
    tran0.writeAction("slorii X19 X19 4 12")
    tran0.writeAction("slorii X19 X19 12 2943")
    tran0.writeAction("slorii X19 X19 4 6")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 1709")
    tran0.writeAction("slorii X17 X17 4 0")
    tran0.writeAction("slorii X17 X17 12 2804")
    tran0.writeAction("slorii X17 X17 4 3")
    tran0.writeAction("slorii X17 X17 12 2616")
    tran0.writeAction("slorii X17 X17 4 12")
    tran0.writeAction("slorii X17 X17 12 2937")
    tran0.writeAction("slorii X17 X17 4 15")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 357")
    tran0.writeAction("slorii X18 X18 4 15")
    tran0.writeAction("slorii X18 X18 12 2106")
    tran0.writeAction("slorii X18 X18 4 12")
    tran0.writeAction("slorii X18 X18 12 2838")
    tran0.writeAction("slorii X18 X18 4 11")
    tran0.writeAction("slorii X18 X18 12 1878")
    tran0.writeAction("slorii X18 X18 4 10")
    tran0.writeAction("vadd.b16 X19 X17 X18 11 ")
    tran0.writeAction("yieldt")
    return efa
