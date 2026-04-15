from EFA_v2 import *
def fcnvt_64_b16_38():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [16704447993798441644]
    tran0.writeAction("movir X16 59346")
    tran0.writeAction("slorii X16 X16 12 495")
    tran0.writeAction("slorii X16 X16 12 583")
    tran0.writeAction("slorii X16 X16 12 1403")
    tran0.writeAction("slorii X16 X16 12 2732")
    tran0.writeAction("fcnvt.64.b16 X16 X16")
    tran0.writeAction("yieldt")
    return efa
