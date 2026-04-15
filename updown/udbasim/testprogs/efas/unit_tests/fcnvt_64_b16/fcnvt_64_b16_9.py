from EFA_v2 import *
def fcnvt_64_b16_9():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5537833817055780340]
    tran0.writeAction("movir X16 19674")
    tran0.writeAction("slorii X16 X16 12 1384")
    tran0.writeAction("slorii X16 X16 12 1042")
    tran0.writeAction("slorii X16 X16 12 3093")
    tran0.writeAction("slorii X16 X16 12 3572")
    tran0.writeAction("fcnvt.64.b16 X16 X16")
    tran0.writeAction("yieldt")
    return efa
