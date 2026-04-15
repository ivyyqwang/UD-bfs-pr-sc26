from EFA_v2 import *
def modi_82():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-5241709729027340961, -12418]
    tran0.writeAction("movir X16 46913")
    tran0.writeAction("slorii X16 X16 12 2892")
    tran0.writeAction("slorii X16 X16 12 1521")
    tran0.writeAction("slorii X16 X16 12 2524")
    tran0.writeAction("slorii X16 X16 12 1375")
    tran0.writeAction("modi X16 X17 -12418")
    tran0.writeAction("yieldt")
    return efa
