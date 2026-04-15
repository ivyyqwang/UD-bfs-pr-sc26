from EFA_v2 import *
def modi_0():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4122569774314865950, -17851]
    tran0.writeAction("movir X16 14646")
    tran0.writeAction("slorii X16 X16 12 1269")
    tran0.writeAction("slorii X16 X16 12 3599")
    tran0.writeAction("slorii X16 X16 12 3276")
    tran0.writeAction("slorii X16 X16 12 1310")
    tran0.writeAction("modi X16 X17 -17851")
    tran0.writeAction("yieldt")
    return efa
