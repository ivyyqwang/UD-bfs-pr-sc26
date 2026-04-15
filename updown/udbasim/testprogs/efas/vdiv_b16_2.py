from EFA_v2 import *
def vdiv_b16_2():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [36478, 40085, 49217, 53409, 63003, 22891, 11446, 37610, 22328, 44118, 64534, 32151, 4]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3338")
    tran0.writeAction("slorii X19 X19 4 1")
    tran0.writeAction("slorii X19 X19 12 3076")
    tran0.writeAction("slorii X19 X19 4 1")
    tran0.writeAction("slorii X19 X19 12 2505")
    tran0.writeAction("slorii X19 X19 4 5")
    tran0.writeAction("slorii X19 X19 12 2279")
    tran0.writeAction("slorii X19 X19 4 14")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 2350")
    tran0.writeAction("slorii X17 X17 4 10")
    tran0.writeAction("slorii X17 X17 12 715")
    tran0.writeAction("slorii X17 X17 4 6")
    tran0.writeAction("slorii X17 X17 12 1430")
    tran0.writeAction("slorii X17 X17 4 11")
    tran0.writeAction("slorii X17 X17 12 3937")
    tran0.writeAction("slorii X17 X17 4 11")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2009")
    tran0.writeAction("slorii X18 X18 4 7")
    tran0.writeAction("slorii X18 X18 12 4033")
    tran0.writeAction("slorii X18 X18 4 6")
    tran0.writeAction("slorii X18 X18 12 2757")
    tran0.writeAction("slorii X18 X18 4 6")
    tran0.writeAction("slorii X18 X18 12 1395")
    tran0.writeAction("slorii X18 X18 4 8")
    tran0.writeAction("vdiv.b16 X19 X17 X18 4 ")
    tran0.writeAction("yieldt")
    return efa
