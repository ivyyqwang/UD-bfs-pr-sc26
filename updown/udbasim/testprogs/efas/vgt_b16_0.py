from EFA_v2 import *
def vgt_b16_0():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [14161, 21171, 22022, 61251, 59472, 39993, 50571, 39166, 58150, 40861, 54480, 3252, 1]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3828")
    tran0.writeAction("slorii X19 X19 4 3")
    tran0.writeAction("slorii X19 X19 12 1376")
    tran0.writeAction("slorii X19 X19 4 6")
    tran0.writeAction("slorii X19 X19 12 1323")
    tran0.writeAction("slorii X19 X19 4 3")
    tran0.writeAction("slorii X19 X19 12 885")
    tran0.writeAction("slorii X19 X19 4 1")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 2447")
    tran0.writeAction("slorii X17 X17 4 14")
    tran0.writeAction("slorii X17 X17 12 3160")
    tran0.writeAction("slorii X17 X17 4 11")
    tran0.writeAction("slorii X17 X17 12 2499")
    tran0.writeAction("slorii X17 X17 4 9")
    tran0.writeAction("slorii X17 X17 12 3717")
    tran0.writeAction("slorii X17 X17 4 0")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 203")
    tran0.writeAction("slorii X18 X18 4 4")
    tran0.writeAction("slorii X18 X18 12 3405")
    tran0.writeAction("slorii X18 X18 4 0")
    tran0.writeAction("slorii X18 X18 12 2553")
    tran0.writeAction("slorii X18 X18 4 13")
    tran0.writeAction("slorii X18 X18 12 3634")
    tran0.writeAction("slorii X18 X18 4 6")
    tran0.writeAction("vgt.b16 X19 X17 X18 1 ")
    tran0.writeAction("yieldt")
    return efa
