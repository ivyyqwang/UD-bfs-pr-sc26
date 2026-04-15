from EFA_v2 import *
def fcnvt_64_32_71():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [12006985941971265827]
    tran0.writeAction("movir X16 42657")
    tran0.writeAction("slorii X16 X16 12 1569")
    tran0.writeAction("slorii X16 X16 12 2358")
    tran0.writeAction("slorii X16 X16 12 1254")
    tran0.writeAction("slorii X16 X16 12 2339")
    tran0.writeAction("fcnvt.64.32 X16 X16")
    tran0.writeAction("yieldt")
    return efa
