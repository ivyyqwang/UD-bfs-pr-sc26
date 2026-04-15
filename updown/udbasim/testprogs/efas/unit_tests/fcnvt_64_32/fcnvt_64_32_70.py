from EFA_v2 import *
def fcnvt_64_32_70():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [15986700946774955862]
    tran0.writeAction("movir X16 56796")
    tran0.writeAction("slorii X16 X16 12 700")
    tran0.writeAction("slorii X16 X16 12 3926")
    tran0.writeAction("slorii X16 X16 12 3777")
    tran0.writeAction("slorii X16 X16 12 1878")
    tran0.writeAction("fcnvt.64.32 X16 X16")
    tran0.writeAction("yieldt")
    return efa
