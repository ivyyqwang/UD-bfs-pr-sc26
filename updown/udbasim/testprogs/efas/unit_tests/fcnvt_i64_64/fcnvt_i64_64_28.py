from EFA_v2 import *
def fcnvt_i64_64_28():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-5309893816559659591]
    tran0.writeAction("movir X16 46671")
    tran0.writeAction("slorii X16 X16 12 1915")
    tran0.writeAction("slorii X16 X16 12 1268")
    tran0.writeAction("slorii X16 X16 12 3761")
    tran0.writeAction("slorii X16 X16 12 1465")
    tran0.writeAction("fcnvt.i64.64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
