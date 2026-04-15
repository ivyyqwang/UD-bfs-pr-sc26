from EFA_v2 import *
def vgt_32_18():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2085705789, 892537964, 212987141, 2004067153, 3868459449, 4064663109, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 851")
    tran0.writeAction("slorii X19 X19 12 780")
    tran0.writeAction("slorii X19 X19 8 108")
    tran0.writeAction("slorii X19 X19 12 1989")
    tran0.writeAction("slorii X19 X19 12 344")
    tran0.writeAction("slorii X19 X19 8 61")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 1911")
    tran0.writeAction("slorii X17 X17 12 931")
    tran0.writeAction("slorii X17 X17 8 81")
    tran0.writeAction("slorii X17 X17 12 203")
    tran0.writeAction("slorii X17 X17 12 493")
    tran0.writeAction("slorii X17 X17 8 5")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 3876")
    tran0.writeAction("slorii X18 X18 12 1494")
    tran0.writeAction("slorii X18 X18 8 69")
    tran0.writeAction("slorii X18 X18 12 3689")
    tran0.writeAction("slorii X18 X18 12 1025")
    tran0.writeAction("slorii X18 X18 8 185")
    tran0.writeAction("vgt.32 X19 X17 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
