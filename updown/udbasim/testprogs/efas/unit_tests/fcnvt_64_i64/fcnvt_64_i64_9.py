from EFA_v2 import *
def fcnvt_64_i64_9():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [13058678144643358831]
    tran0.writeAction("movir X16 46393")
    tran0.writeAction("slorii X16 X16 12 3049")
    tran0.writeAction("slorii X16 X16 12 1455")
    tran0.writeAction("slorii X16 X16 12 2558")
    tran0.writeAction("slorii X16 X16 12 111")
    tran0.writeAction("fcnvt.64.i64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
