from EFA_v2 import *
def modi_46():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-4198998483442883731, -14740]
    tran0.writeAction("movir X16 50618")
    tran0.writeAction("slorii X16 X16 12 658")
    tran0.writeAction("slorii X16 X16 12 101")
    tran0.writeAction("slorii X16 X16 12 4026")
    tran0.writeAction("slorii X16 X16 12 877")
    tran0.writeAction("modi X16 X17 -14740")
    tran0.writeAction("yieldt")
    return efa
