from EFA_v2 import *
def fcnvt_64_b16_76():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3390320864624981623]
    tran0.writeAction("movir X16 12044")
    tran0.writeAction("slorii X16 X16 12 3437")
    tran0.writeAction("slorii X16 X16 12 3354")
    tran0.writeAction("slorii X16 X16 12 2323")
    tran0.writeAction("slorii X16 X16 12 1655")
    tran0.writeAction("fcnvt.64.b16 X16 X16")
    tran0.writeAction("yieldt")
    return efa
