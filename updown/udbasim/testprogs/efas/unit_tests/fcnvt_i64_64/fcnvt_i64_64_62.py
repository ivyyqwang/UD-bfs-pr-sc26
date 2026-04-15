from EFA_v2 import *
def fcnvt_i64_64_62():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7856702033862220620]
    tran0.writeAction("movir X16 27912")
    tran0.writeAction("slorii X16 X16 12 2509")
    tran0.writeAction("slorii X16 X16 12 3978")
    tran0.writeAction("slorii X16 X16 12 1829")
    tran0.writeAction("slorii X16 X16 12 2892")
    tran0.writeAction("fcnvt.i64.64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
