from EFA_v2 import *
def fcnvt_64_32_11():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [625816556336718357]
    tran0.writeAction("movir X16 2223")
    tran0.writeAction("slorii X16 X16 12 1421")
    tran0.writeAction("slorii X16 X16 12 1951")
    tran0.writeAction("slorii X16 X16 12 34")
    tran0.writeAction("slorii X16 X16 12 533")
    tran0.writeAction("fcnvt.64.32 X16 X16")
    tran0.writeAction("yieldt")
    return efa
