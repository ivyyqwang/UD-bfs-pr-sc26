from EFA_v2 import *
def fcnvt_64_b16_98():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [15474609115665089379]
    tran0.writeAction("movir X16 54976")
    tran0.writeAction("slorii X16 X16 12 3504")
    tran0.writeAction("slorii X16 X16 12 177")
    tran0.writeAction("slorii X16 X16 12 980")
    tran0.writeAction("slorii X16 X16 12 867")
    tran0.writeAction("fcnvt.64.b16 X16 X16")
    tran0.writeAction("yieldt")
    return efa
