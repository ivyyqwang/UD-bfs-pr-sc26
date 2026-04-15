from EFA_v2 import *
def vmul_i32_13():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1384965588, -384418643, 1980138753, -1088529230, -2123302539, 749917858, 1]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3729")
    tran0.writeAction("slorii X19 X19 12 1596")
    tran0.writeAction("slorii X19 X19 8 173")
    tran0.writeAction("slorii X19 X19 12 2775")
    tran0.writeAction("slorii X19 X19 12 794")
    tran0.writeAction("slorii X19 X19 8 44")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 3057")
    tran0.writeAction("slorii X17 X17 12 3676")
    tran0.writeAction("slorii X17 X17 8 178")
    tran0.writeAction("slorii X17 X17 12 1888")
    tran0.writeAction("slorii X17 X17 12 1669")
    tran0.writeAction("slorii X17 X17 8 1")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 715")
    tran0.writeAction("slorii X18 X18 12 726")
    tran0.writeAction("slorii X18 X18 8 162")
    tran0.writeAction("slorii X18 X18 12 2071")
    tran0.writeAction("slorii X18 X18 12 249")
    tran0.writeAction("slorii X18 X18 8 117")
    tran0.writeAction("vmul.i32 X19 X17 X18 1 ")
    tran0.writeAction("yieldt")
    return efa
