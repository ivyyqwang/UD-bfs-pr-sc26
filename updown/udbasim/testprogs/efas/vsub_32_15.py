from EFA_v2 import *
def vsub_32_15():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2099146389, 657424814, 1342568757, 161205975, 4180438468, 3121344078, 2]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 626")
    tran0.writeAction("slorii X19 X19 12 3969")
    tran0.writeAction("slorii X19 X19 8 174")
    tran0.writeAction("slorii X19 X19 12 2001")
    tran0.writeAction("slorii X19 X19 12 3694")
    tran0.writeAction("slorii X19 X19 8 149")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 153")
    tran0.writeAction("slorii X17 X17 12 3022")
    tran0.writeAction("slorii X17 X17 8 215")
    tran0.writeAction("slorii X17 X17 12 1280")
    tran0.writeAction("slorii X17 X17 12 1529")
    tran0.writeAction("slorii X17 X17 8 53")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2976")
    tran0.writeAction("slorii X18 X18 12 3054")
    tran0.writeAction("slorii X18 X18 8 78")
    tran0.writeAction("slorii X18 X18 12 3986")
    tran0.writeAction("slorii X18 X18 12 3181")
    tran0.writeAction("slorii X18 X18 8 196")
    tran0.writeAction("vsub.32 X19 X17 X18 2 ")
    tran0.writeAction("yieldt")
    return efa
