from EFA_v2 import *
def fcnvt_64_32_45():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [931618956145094231]
    tran0.writeAction("movir X16 3309")
    tran0.writeAction("slorii X16 X16 12 3176")
    tran0.writeAction("slorii X16 X16 12 307")
    tran0.writeAction("slorii X16 X16 12 198")
    tran0.writeAction("slorii X16 X16 12 3671")
    tran0.writeAction("fcnvt.64.32 X16 X16")
    tran0.writeAction("yieldt")
    return efa
