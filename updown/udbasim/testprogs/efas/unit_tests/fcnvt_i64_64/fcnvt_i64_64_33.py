from EFA_v2 import *
def fcnvt_i64_64_33():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8951975353244705638]
    tran0.writeAction("movir X16 31803")
    tran0.writeAction("slorii X16 X16 12 3298")
    tran0.writeAction("slorii X16 X16 12 1912")
    tran0.writeAction("slorii X16 X16 12 830")
    tran0.writeAction("slorii X16 X16 12 870")
    tran0.writeAction("fcnvt.i64.64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
