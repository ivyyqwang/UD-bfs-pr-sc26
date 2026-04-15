from EFA_v2 import *
def vdiv_b16_5():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [57634, 7701, 58275, 10894, 10506, 51731, 47686, 41277, 19624, 55529, 17545, 31512, 6]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 680")
    tran0.writeAction("slorii X19 X19 4 14")
    tran0.writeAction("slorii X19 X19 12 3642")
    tran0.writeAction("slorii X19 X19 4 3")
    tran0.writeAction("slorii X19 X19 12 481")
    tran0.writeAction("slorii X19 X19 4 5")
    tran0.writeAction("slorii X19 X19 12 3602")
    tran0.writeAction("slorii X19 X19 4 2")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 2579")
    tran0.writeAction("slorii X17 X17 4 13")
    tran0.writeAction("slorii X17 X17 12 2980")
    tran0.writeAction("slorii X17 X17 4 6")
    tran0.writeAction("slorii X17 X17 12 3233")
    tran0.writeAction("slorii X17 X17 4 3")
    tran0.writeAction("slorii X17 X17 12 656")
    tran0.writeAction("slorii X17 X17 4 10")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1969")
    tran0.writeAction("slorii X18 X18 4 8")
    tran0.writeAction("slorii X18 X18 12 1096")
    tran0.writeAction("slorii X18 X18 4 9")
    tran0.writeAction("slorii X18 X18 12 3470")
    tran0.writeAction("slorii X18 X18 4 9")
    tran0.writeAction("slorii X18 X18 12 1226")
    tran0.writeAction("slorii X18 X18 4 8")
    tran0.writeAction("vdiv.b16 X19 X17 X18 6 ")
    tran0.writeAction("yieldt")
    return efa
