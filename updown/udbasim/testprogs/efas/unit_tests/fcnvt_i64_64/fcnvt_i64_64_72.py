from EFA_v2 import *
def fcnvt_i64_64_72():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-7886228056774951454]
    tran0.writeAction("movir X16 37518")
    tran0.writeAction("slorii X16 X16 12 2005")
    tran0.writeAction("slorii X16 X16 12 3466")
    tran0.writeAction("slorii X16 X16 12 859")
    tran0.writeAction("slorii X16 X16 12 3554")
    tran0.writeAction("fcnvt.i64.64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
