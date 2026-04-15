from EFA_v2 import *
def fcnvt_i64_64_34():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8682847099051921844]
    tran0.writeAction("movir X16 30847")
    tran0.writeAction("slorii X16 X16 12 2742")
    tran0.writeAction("slorii X16 X16 12 3794")
    tran0.writeAction("slorii X16 X16 12 85")
    tran0.writeAction("slorii X16 X16 12 436")
    tran0.writeAction("fcnvt.i64.64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
