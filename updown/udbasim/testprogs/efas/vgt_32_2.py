from EFA_v2 import *
def vgt_32_2():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [811262713, 2225869027, 1410304040, 515873397, 670050862, 290866913, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 2122")
    tran0.writeAction("slorii X19 X19 12 3088")
    tran0.writeAction("slorii X19 X19 8 227")
    tran0.writeAction("slorii X19 X19 12 773")
    tran0.writeAction("slorii X19 X19 12 2786")
    tran0.writeAction("slorii X19 X19 8 249")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 491")
    tran0.writeAction("slorii X17 X17 12 3994")
    tran0.writeAction("slorii X17 X17 8 117")
    tran0.writeAction("slorii X17 X17 12 1344")
    tran0.writeAction("slorii X17 X17 12 3976")
    tran0.writeAction("slorii X17 X17 8 40")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 277")
    tran0.writeAction("slorii X18 X18 12 1606")
    tran0.writeAction("slorii X18 X18 8 225")
    tran0.writeAction("slorii X18 X18 12 639")
    tran0.writeAction("slorii X18 X18 12 42")
    tran0.writeAction("slorii X18 X18 8 46")
    tran0.writeAction("vgt.32 X19 X17 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
