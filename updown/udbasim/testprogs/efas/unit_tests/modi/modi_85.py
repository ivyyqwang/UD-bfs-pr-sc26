from EFA_v2 import *
def modi_85():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6499511545573350210, 952]
    tran0.writeAction("movir X16 23090")
    tran0.writeAction("slorii X16 X16 12 3701")
    tran0.writeAction("slorii X16 X16 12 151")
    tran0.writeAction("slorii X16 X16 12 1841")
    tran0.writeAction("slorii X16 X16 12 2882")
    tran0.writeAction("modi X16 X17 952")
    tran0.writeAction("yieldt")
    return efa
