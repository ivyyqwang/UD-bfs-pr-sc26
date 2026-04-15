from EFA_v2 import *
def vadd_32_16():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2159644729, 18211893, 2550466961, 1906011495, 170756404, 641263535, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 17")
    tran0.writeAction("slorii X19 X19 12 1508")
    tran0.writeAction("slorii X19 X19 8 53")
    tran0.writeAction("slorii X19 X19 12 2059")
    tran0.writeAction("slorii X19 X19 12 2448")
    tran0.writeAction("slorii X19 X19 8 57")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 1817")
    tran0.writeAction("slorii X17 X17 12 2925")
    tran0.writeAction("slorii X17 X17 8 103")
    tran0.writeAction("slorii X17 X17 12 2432")
    tran0.writeAction("slorii X17 X17 12 1289")
    tran0.writeAction("slorii X17 X17 8 145")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 611")
    tran0.writeAction("slorii X18 X18 12 2279")
    tran0.writeAction("slorii X18 X18 8 175")
    tran0.writeAction("slorii X18 X18 12 162")
    tran0.writeAction("slorii X18 X18 12 3465")
    tran0.writeAction("slorii X18 X18 8 52")
    tran0.writeAction("vadd.32 X19 X17 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
