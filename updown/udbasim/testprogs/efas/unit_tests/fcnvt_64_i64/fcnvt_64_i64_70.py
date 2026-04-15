from EFA_v2 import *
def fcnvt_64_i64_70():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [9091242157125609759]
    tran0.writeAction("movir X16 32298")
    tran0.writeAction("slorii X16 X16 12 2377")
    tran0.writeAction("slorii X16 X16 12 782")
    tran0.writeAction("slorii X16 X16 12 2162")
    tran0.writeAction("slorii X16 X16 12 2335")
    tran0.writeAction("fcnvt.64.i64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
