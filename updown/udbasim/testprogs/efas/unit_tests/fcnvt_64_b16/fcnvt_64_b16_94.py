from EFA_v2 import *
def fcnvt_64_b16_94():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [16725820811478778041]
    tran0.writeAction("movir X16 59422")
    tran0.writeAction("slorii X16 X16 12 214")
    tran0.writeAction("slorii X16 X16 12 2349")
    tran0.writeAction("slorii X16 X16 12 116")
    tran0.writeAction("slorii X16 X16 12 185")
    tran0.writeAction("fcnvt.64.b16 X16 X16")
    tran0.writeAction("yieldt")
    return efa
