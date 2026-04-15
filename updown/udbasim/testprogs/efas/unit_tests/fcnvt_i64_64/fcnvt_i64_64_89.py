from EFA_v2 import *
def fcnvt_i64_64_89():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8199974603598529213]
    tran0.writeAction("movir X16 29132")
    tran0.writeAction("slorii X16 X16 12 663")
    tran0.writeAction("slorii X16 X16 12 1254")
    tran0.writeAction("slorii X16 X16 12 2928")
    tran0.writeAction("slorii X16 X16 12 701")
    tran0.writeAction("fcnvt.i64.64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
