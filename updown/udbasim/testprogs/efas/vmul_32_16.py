from EFA_v2 import *
def vmul_32_16():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3255569030, 3882635649, 3945655910, 3308416842, 643996050, 2543758493, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3702")
    tran0.writeAction("slorii X19 X19 12 3153")
    tran0.writeAction("slorii X19 X19 8 129")
    tran0.writeAction("slorii X19 X19 12 3104")
    tran0.writeAction("slorii X19 X19 12 3082")
    tran0.writeAction("slorii X19 X19 8 134")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 3155")
    tran0.writeAction("slorii X17 X17 12 623")
    tran0.writeAction("slorii X17 X17 8 74")
    tran0.writeAction("slorii X17 X17 12 3762")
    tran0.writeAction("slorii X17 X17 12 3566")
    tran0.writeAction("slorii X17 X17 8 102")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2425")
    tran0.writeAction("slorii X18 X18 12 3756")
    tran0.writeAction("slorii X18 X18 8 157")
    tran0.writeAction("slorii X18 X18 12 614")
    tran0.writeAction("slorii X18 X18 12 665")
    tran0.writeAction("slorii X18 X18 8 146")
    tran0.writeAction("vmul.32 X19 X17 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
