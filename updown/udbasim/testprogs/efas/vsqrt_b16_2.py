from EFA_v2 import *
def vsqrt_b16_2():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [59866, 33283, 8142, 31639, 54463, 28178, 43214, 57988, 13]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 1977")
    tran0.writeAction("slorii X19 X19 4 7")
    tran0.writeAction("slorii X19 X19 12 508")
    tran0.writeAction("slorii X19 X19 4 14")
    tran0.writeAction("slorii X19 X19 12 2080")
    tran0.writeAction("slorii X19 X19 4 3")
    tran0.writeAction("slorii X19 X19 12 3741")
    tran0.writeAction("slorii X19 X19 4 10")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 3624")
    tran0.writeAction("slorii X18 X18 4 4")
    tran0.writeAction("slorii X18 X18 12 2700")
    tran0.writeAction("slorii X18 X18 4 14")
    tran0.writeAction("slorii X18 X18 12 1761")
    tran0.writeAction("slorii X18 X18 4 2")
    tran0.writeAction("slorii X18 X18 12 3403")
    tran0.writeAction("slorii X18 X18 4 15")
    tran0.writeAction("vsqrt.b16 X19 X18 13 ")
    tran0.writeAction("yieldt")
    return efa
