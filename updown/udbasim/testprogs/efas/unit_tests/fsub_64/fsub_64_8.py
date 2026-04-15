from EFA_v2 import *
def fsub_64_8():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [13253030876318171930, 13553808655529216277]
    tran0.writeAction("movir X16 47084")
    tran0.writeAction("slorii X16 X16 12 917")
    tran0.writeAction("slorii X16 X16 12 3404")
    tran0.writeAction("slorii X16 X16 12 936")
    tran0.writeAction("slorii X16 X16 12 794")
    tran0.writeAction("movir X17 48152")
    tran0.writeAction("slorii X17 X17 12 3282")
    tran0.writeAction("slorii X17 X17 12 2362")
    tran0.writeAction("slorii X17 X17 12 1776")
    tran0.writeAction("slorii X17 X17 12 2325")
    tran0.writeAction("fsub.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
