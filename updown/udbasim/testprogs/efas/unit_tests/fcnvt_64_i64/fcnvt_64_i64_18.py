from EFA_v2 import *
def fcnvt_64_i64_18():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [526070599109917430]
    tran0.writeAction("movir X16 1868")
    tran0.writeAction("slorii X16 X16 12 4006")
    tran0.writeAction("slorii X16 X16 12 3122")
    tran0.writeAction("slorii X16 X16 12 2963")
    tran0.writeAction("slorii X16 X16 12 2806")
    tran0.writeAction("fcnvt.64.i64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
