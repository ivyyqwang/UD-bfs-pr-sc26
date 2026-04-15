from EFA_v2 import *
def fcnvt_64_i64_91():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5632686080085935403]
    tran0.writeAction("movir X16 20011")
    tran0.writeAction("slorii X16 X16 12 1314")
    tran0.writeAction("slorii X16 X16 12 1414")
    tran0.writeAction("slorii X16 X16 12 3316")
    tran0.writeAction("slorii X16 X16 12 1323")
    tran0.writeAction("fcnvt.64.i64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
