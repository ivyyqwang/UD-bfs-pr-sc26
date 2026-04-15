from EFA_v2 import *
def fcnvt_64_b16_59():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [11668150391819591730]
    tran0.writeAction("movir X16 41453")
    tran0.writeAction("slorii X16 X16 12 2447")
    tran0.writeAction("slorii X16 X16 12 1530")
    tran0.writeAction("slorii X16 X16 12 990")
    tran0.writeAction("slorii X16 X16 12 50")
    tran0.writeAction("fcnvt.64.b16 X16 X16")
    tran0.writeAction("yieldt")
    return efa
