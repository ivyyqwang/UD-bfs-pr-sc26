from EFA_v2 import *
def vgt_b16_1():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [35162, 19202, 46608, 41134, 580, 45276, 44060, 31749, 1120, 25593, 35007, 54972, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 2570")
    tran0.writeAction("slorii X19 X19 4 14")
    tran0.writeAction("slorii X19 X19 12 2913")
    tran0.writeAction("slorii X19 X19 4 0")
    tran0.writeAction("slorii X19 X19 12 1200")
    tran0.writeAction("slorii X19 X19 4 2")
    tran0.writeAction("slorii X19 X19 12 2197")
    tran0.writeAction("slorii X19 X19 4 10")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 1984")
    tran0.writeAction("slorii X17 X17 4 5")
    tran0.writeAction("slorii X17 X17 12 2753")
    tran0.writeAction("slorii X17 X17 4 12")
    tran0.writeAction("slorii X17 X17 12 2829")
    tran0.writeAction("slorii X17 X17 4 12")
    tran0.writeAction("slorii X17 X17 12 36")
    tran0.writeAction("slorii X17 X17 4 4")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 3435")
    tran0.writeAction("slorii X18 X18 4 12")
    tran0.writeAction("slorii X18 X18 12 2187")
    tran0.writeAction("slorii X18 X18 4 15")
    tran0.writeAction("slorii X18 X18 12 1599")
    tran0.writeAction("slorii X18 X18 4 9")
    tran0.writeAction("slorii X18 X18 12 70")
    tran0.writeAction("slorii X18 X18 4 0")
    tran0.writeAction("vgt.b16 X19 X17 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
