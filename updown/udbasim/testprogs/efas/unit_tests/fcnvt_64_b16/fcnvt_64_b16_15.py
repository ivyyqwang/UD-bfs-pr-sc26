from EFA_v2 import *
def fcnvt_64_b16_15():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3382246462766516495]
    tran0.writeAction("movir X16 12016")
    tran0.writeAction("slorii X16 X16 12 627")
    tran0.writeAction("slorii X16 X16 12 3308")
    tran0.writeAction("slorii X16 X16 12 80")
    tran0.writeAction("slorii X16 X16 12 2319")
    tran0.writeAction("fcnvt.64.b16 X16 X16")
    tran0.writeAction("yieldt")
    return efa
