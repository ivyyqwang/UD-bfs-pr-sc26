from EFA_v2 import *
def vdiv_32_19():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [490289524, 2788612687, 1734503775, 1178141238, 767388649, 1079682618, 1]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 2659")
    tran0.writeAction("slorii X19 X19 12 1754")
    tran0.writeAction("slorii X19 X19 8 79")
    tran0.writeAction("slorii X19 X19 12 467")
    tran0.writeAction("slorii X19 X19 12 2361")
    tran0.writeAction("slorii X19 X19 8 116")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 1123")
    tran0.writeAction("slorii X17 X17 12 2306")
    tran0.writeAction("slorii X17 X17 8 54")
    tran0.writeAction("slorii X17 X17 12 1654")
    tran0.writeAction("slorii X17 X17 12 621")
    tran0.writeAction("slorii X17 X17 8 95")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1029")
    tran0.writeAction("slorii X18 X18 12 2726")
    tran0.writeAction("slorii X18 X18 8 58")
    tran0.writeAction("slorii X18 X18 12 731")
    tran0.writeAction("slorii X18 X18 12 3435")
    tran0.writeAction("slorii X18 X18 8 233")
    tran0.writeAction("vdiv.32 X19 X17 X18 1 ")
    tran0.writeAction("yieldt")
    return efa
