from EFA_v2 import *
def vadd_i32_4():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1228115079, 428262781, -941799282, 1272714150, 1326184716, -66192336, 2]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 408")
    tran0.writeAction("slorii X19 X19 12 1733")
    tran0.writeAction("slorii X19 X19 8 125")
    tran0.writeAction("slorii X19 X19 12 1171")
    tran0.writeAction("slorii X19 X19 12 908")
    tran0.writeAction("slorii X19 X19 8 135")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 1213")
    tran0.writeAction("slorii X17 X17 12 3091")
    tran0.writeAction("slorii X17 X17 8 166")
    tran0.writeAction("slorii X17 X17 12 3197")
    tran0.writeAction("slorii X17 X17 12 3400")
    tran0.writeAction("slorii X17 X17 8 142")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 4032")
    tran0.writeAction("slorii X18 X18 12 3580")
    tran0.writeAction("slorii X18 X18 8 48")
    tran0.writeAction("slorii X18 X18 12 1264")
    tran0.writeAction("slorii X18 X18 12 3065")
    tran0.writeAction("slorii X18 X18 8 12")
    tran0.writeAction("vadd.i32 X19 X17 X18 2 ")
    tran0.writeAction("yieldt")
    return efa
