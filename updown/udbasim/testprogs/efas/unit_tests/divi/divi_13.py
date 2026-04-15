from EFA_v2 import *
def divi_13():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-2220359684757361358, -7025]
    tran0.writeAction("movir X16 57647")
    tran0.writeAction("slorii X16 X16 12 2858")
    tran0.writeAction("slorii X16 X16 12 372")
    tran0.writeAction("slorii X16 X16 12 1798")
    tran0.writeAction("slorii X16 X16 12 3378")
    tran0.writeAction("divi X16 X17 -7025")
    tran0.writeAction("yieldt")
    return efa
