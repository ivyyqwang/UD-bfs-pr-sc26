from EFA_v2 import *
def fcnvt_64_32_35():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2483868941655368010]
    tran0.writeAction("movir X16 8824")
    tran0.writeAction("slorii X16 X16 12 1946")
    tran0.writeAction("slorii X16 X16 12 1135")
    tran0.writeAction("slorii X16 X16 12 4070")
    tran0.writeAction("slorii X16 X16 12 330")
    tran0.writeAction("fcnvt.64.32 X16 X16")
    tran0.writeAction("yieldt")
    return efa
