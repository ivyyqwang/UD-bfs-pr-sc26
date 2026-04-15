from EFA_v2 import *
def fcnvt_64_b16_57():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [9688577732688527629]
    tran0.writeAction("movir X16 34420")
    tran0.writeAction("slorii X16 X16 12 3041")
    tran0.writeAction("slorii X16 X16 12 3479")
    tran0.writeAction("slorii X16 X16 12 2700")
    tran0.writeAction("slorii X16 X16 12 269")
    tran0.writeAction("fcnvt.64.b16 X16 X16")
    tran0.writeAction("yieldt")
    return efa
