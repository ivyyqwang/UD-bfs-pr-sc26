from EFA_v2 import *
def divi_71():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-8097421171162075412, -2370]
    tran0.writeAction("movir X16 36768")
    tran0.writeAction("slorii X16 X16 12 741")
    tran0.writeAction("slorii X16 X16 12 2248")
    tran0.writeAction("slorii X16 X16 12 642")
    tran0.writeAction("slorii X16 X16 12 3820")
    tran0.writeAction("divi X16 X17 -2370")
    tran0.writeAction("yieldt")
    return efa
