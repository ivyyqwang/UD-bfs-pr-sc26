from EFA_v2 import *
def fcnvt_i64_64_12():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4572280041979412797]
    tran0.writeAction("movir X16 16244")
    tran0.writeAction("slorii X16 X16 12 7")
    tran0.writeAction("slorii X16 X16 12 2339")
    tran0.writeAction("slorii X16 X16 12 3240")
    tran0.writeAction("slorii X16 X16 12 317")
    tran0.writeAction("fcnvt.i64.64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
