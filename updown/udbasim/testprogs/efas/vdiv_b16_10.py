from EFA_v2 import *
def vdiv_b16_10():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [25099, 60653, 25376, 53112, 16044, 31071, 4212, 2573, 47220, 41900, 32565, 3795, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3319")
    tran0.writeAction("slorii X19 X19 4 8")
    tran0.writeAction("slorii X19 X19 12 1586")
    tran0.writeAction("slorii X19 X19 4 0")
    tran0.writeAction("slorii X19 X19 12 3790")
    tran0.writeAction("slorii X19 X19 4 13")
    tran0.writeAction("slorii X19 X19 12 1568")
    tran0.writeAction("slorii X19 X19 4 11")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 160")
    tran0.writeAction("slorii X17 X17 4 13")
    tran0.writeAction("slorii X17 X17 12 263")
    tran0.writeAction("slorii X17 X17 4 4")
    tran0.writeAction("slorii X17 X17 12 1941")
    tran0.writeAction("slorii X17 X17 4 15")
    tran0.writeAction("slorii X17 X17 12 1002")
    tran0.writeAction("slorii X17 X17 4 12")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 237")
    tran0.writeAction("slorii X18 X18 4 3")
    tran0.writeAction("slorii X18 X18 12 2035")
    tran0.writeAction("slorii X18 X18 4 5")
    tran0.writeAction("slorii X18 X18 12 2618")
    tran0.writeAction("slorii X18 X18 4 12")
    tran0.writeAction("slorii X18 X18 12 2951")
    tran0.writeAction("slorii X18 X18 4 4")
    tran0.writeAction("vdiv.b16 X19 X17 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
