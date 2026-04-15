from EFA_v2 import *
def vgt_i32_16():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [270537411, 649717661, 522944198, -1016143843, 269706216, -1194224958, 1]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 619")
    tran0.writeAction("slorii X19 X19 12 2535")
    tran0.writeAction("slorii X19 X19 8 157")
    tran0.writeAction("slorii X19 X19 12 258")
    tran0.writeAction("slorii X19 X19 12 18")
    tran0.writeAction("slorii X19 X19 8 195")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 3126")
    tran0.writeAction("slorii X17 X17 12 3808")
    tran0.writeAction("slorii X17 X17 8 29")
    tran0.writeAction("slorii X17 X17 12 498")
    tran0.writeAction("slorii X17 X17 12 2942")
    tran0.writeAction("slorii X17 X17 8 198")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2957")
    tran0.writeAction("slorii X18 X18 12 402")
    tran0.writeAction("slorii X18 X18 8 194")
    tran0.writeAction("slorii X18 X18 12 257")
    tran0.writeAction("slorii X18 X18 12 867")
    tran0.writeAction("slorii X18 X18 8 232")
    tran0.writeAction("vgt.i32 X19 X17 X18 1 ")
    tran0.writeAction("yieldt")
    return efa
