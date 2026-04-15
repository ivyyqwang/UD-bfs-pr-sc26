from EFA_v2 import *
def vgt_32_19():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [974423914, 3776433065, 1390410733, 948212936, 2314211527, 1552812925, 2]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3601")
    tran0.writeAction("slorii X19 X19 12 1995")
    tran0.writeAction("slorii X19 X19 8 169")
    tran0.writeAction("slorii X19 X19 12 929")
    tran0.writeAction("slorii X19 X19 12 1159")
    tran0.writeAction("slorii X19 X19 8 106")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 904")
    tran0.writeAction("slorii X17 X17 12 1172")
    tran0.writeAction("slorii X17 X17 8 200")
    tran0.writeAction("slorii X17 X17 12 1325")
    tran0.writeAction("slorii X17 X17 12 4091")
    tran0.writeAction("slorii X17 X17 8 237")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1480")
    tran0.writeAction("slorii X18 X18 12 3595")
    tran0.writeAction("slorii X18 X18 8 125")
    tran0.writeAction("slorii X18 X18 12 2207")
    tran0.writeAction("slorii X18 X18 12 16")
    tran0.writeAction("slorii X18 X18 8 199")
    tran0.writeAction("vgt.32 X19 X17 X18 2 ")
    tran0.writeAction("yieldt")
    return efa
