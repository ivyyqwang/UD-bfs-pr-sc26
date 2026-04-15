from EFA_v2 import *
def divi_6():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-8655564619722539655, -31083]
    tran0.writeAction("movir X16 34785")
    tran0.writeAction("slorii X16 X16 12 1053")
    tran0.writeAction("slorii X16 X16 12 1638")
    tran0.writeAction("slorii X16 X16 12 4091")
    tran0.writeAction("slorii X16 X16 12 3449")
    tran0.writeAction("divi X16 X17 -31083")
    tran0.writeAction("yieldt")
    return efa
