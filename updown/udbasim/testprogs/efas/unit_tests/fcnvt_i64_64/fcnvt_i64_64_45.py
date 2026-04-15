from EFA_v2 import *
def fcnvt_i64_64_45():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3766410207652529553]
    tran0.writeAction("movir X16 13380")
    tran0.writeAction("slorii X16 X16 12 4002")
    tran0.writeAction("slorii X16 X16 12 233")
    tran0.writeAction("slorii X16 X16 12 2188")
    tran0.writeAction("slorii X16 X16 12 1425")
    tran0.writeAction("fcnvt.i64.64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
