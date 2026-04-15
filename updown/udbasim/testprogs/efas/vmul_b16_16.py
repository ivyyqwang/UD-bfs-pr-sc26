from EFA_v2 import *
def vmul_b16_16():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [49314, 41207, 45393, 35326, 30898, 26734, 22506, 41341, 257, 15960, 38864, 44744, 8]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 2207")
    tran0.writeAction("slorii X19 X19 4 14")
    tran0.writeAction("slorii X19 X19 12 2837")
    tran0.writeAction("slorii X19 X19 4 1")
    tran0.writeAction("slorii X19 X19 12 2575")
    tran0.writeAction("slorii X19 X19 4 7")
    tran0.writeAction("slorii X19 X19 12 3082")
    tran0.writeAction("slorii X19 X19 4 2")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 2583")
    tran0.writeAction("slorii X17 X17 4 13")
    tran0.writeAction("slorii X17 X17 12 1406")
    tran0.writeAction("slorii X17 X17 4 10")
    tran0.writeAction("slorii X17 X17 12 1670")
    tran0.writeAction("slorii X17 X17 4 14")
    tran0.writeAction("slorii X17 X17 12 1931")
    tran0.writeAction("slorii X17 X17 4 2")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2796")
    tran0.writeAction("slorii X18 X18 4 8")
    tran0.writeAction("slorii X18 X18 12 2429")
    tran0.writeAction("slorii X18 X18 4 0")
    tran0.writeAction("slorii X18 X18 12 997")
    tran0.writeAction("slorii X18 X18 4 8")
    tran0.writeAction("slorii X18 X18 12 16")
    tran0.writeAction("slorii X18 X18 4 1")
    tran0.writeAction("vmul.b16 X19 X17 X18 8 ")
    tran0.writeAction("yieldt")
    return efa
