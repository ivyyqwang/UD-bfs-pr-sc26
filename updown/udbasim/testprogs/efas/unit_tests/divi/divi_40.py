from EFA_v2 import *
def divi_40():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-2327523169787336684, -28978]
    tran0.writeAction("movir X16 57266")
    tran0.writeAction("slorii X16 X16 12 4000")
    tran0.writeAction("slorii X16 X16 12 578")
    tran0.writeAction("slorii X16 X16 12 1370")
    tran0.writeAction("slorii X16 X16 12 2068")
    tran0.writeAction("divi X16 X17 -28978")
    tran0.writeAction("yieldt")
    return efa
