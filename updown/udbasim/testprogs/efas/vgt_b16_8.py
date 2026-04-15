from EFA_v2 import *
def vgt_b16_8():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [16506, 20548, 6048, 6556, 15887, 64707, 14914, 11865, 10000, 10333, 46710, 33957, 2]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 409")
    tran0.writeAction("slorii X19 X19 4 12")
    tran0.writeAction("slorii X19 X19 12 378")
    tran0.writeAction("slorii X19 X19 4 0")
    tran0.writeAction("slorii X19 X19 12 1284")
    tran0.writeAction("slorii X19 X19 4 4")
    tran0.writeAction("slorii X19 X19 12 1031")
    tran0.writeAction("slorii X19 X19 4 10")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 741")
    tran0.writeAction("slorii X17 X17 4 9")
    tran0.writeAction("slorii X17 X17 12 932")
    tran0.writeAction("slorii X17 X17 4 2")
    tran0.writeAction("slorii X17 X17 12 4044")
    tran0.writeAction("slorii X17 X17 4 3")
    tran0.writeAction("slorii X17 X17 12 992")
    tran0.writeAction("slorii X17 X17 4 15")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2122")
    tran0.writeAction("slorii X18 X18 4 5")
    tran0.writeAction("slorii X18 X18 12 2919")
    tran0.writeAction("slorii X18 X18 4 6")
    tran0.writeAction("slorii X18 X18 12 645")
    tran0.writeAction("slorii X18 X18 4 13")
    tran0.writeAction("slorii X18 X18 12 625")
    tran0.writeAction("slorii X18 X18 4 0")
    tran0.writeAction("vgt.b16 X19 X17 X18 2 ")
    tran0.writeAction("yieldt")
    return efa
