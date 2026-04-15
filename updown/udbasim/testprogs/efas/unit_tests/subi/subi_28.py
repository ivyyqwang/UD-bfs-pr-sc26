from EFA_v2 import *
def subi_28():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-284498786279568598, 12619]
    tran0.writeAction("movir X16 64525")
    tran0.writeAction("slorii X16 X16 12 1053")
    tran0.writeAction("slorii X16 X16 12 3192")
    tran0.writeAction("slorii X16 X16 12 3180")
    tran0.writeAction("slorii X16 X16 12 2858")
    tran0.writeAction("subi X16 X17 12619")
    tran0.writeAction("yieldt")
    return efa
