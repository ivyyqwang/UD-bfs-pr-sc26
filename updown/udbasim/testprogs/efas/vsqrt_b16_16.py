from EFA_v2 import *
def vsqrt_b16_16():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [55878, 22728, 25140, 12086, 65037, 39624, 28322, 48114, 7]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 755")
    tran0.writeAction("slorii X19 X19 4 6")
    tran0.writeAction("slorii X19 X19 12 1571")
    tran0.writeAction("slorii X19 X19 4 4")
    tran0.writeAction("slorii X19 X19 12 1420")
    tran0.writeAction("slorii X19 X19 4 8")
    tran0.writeAction("slorii X19 X19 12 3492")
    tran0.writeAction("slorii X19 X19 4 6")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 3007")
    tran0.writeAction("slorii X18 X18 4 2")
    tran0.writeAction("slorii X18 X18 12 1770")
    tran0.writeAction("slorii X18 X18 4 2")
    tran0.writeAction("slorii X18 X18 12 2476")
    tran0.writeAction("slorii X18 X18 4 8")
    tran0.writeAction("slorii X18 X18 12 4064")
    tran0.writeAction("slorii X18 X18 4 13")
    tran0.writeAction("vsqrt.b16 X19 X18 7 ")
    tran0.writeAction("yieldt")
    return efa
