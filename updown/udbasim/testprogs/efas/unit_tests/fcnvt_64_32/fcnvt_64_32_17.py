from EFA_v2 import *
def fcnvt_64_32_17():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4178832161624159368]
    tran0.writeAction("movir X16 14846")
    tran0.writeAction("slorii X16 X16 12 795")
    tran0.writeAction("slorii X16 X16 12 1513")
    tran0.writeAction("slorii X16 X16 12 2399")
    tran0.writeAction("slorii X16 X16 12 1160")
    tran0.writeAction("fcnvt.64.32 X16 X16")
    tran0.writeAction("yieldt")
    return efa
