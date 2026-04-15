from EFA_v2 import *
def fcnvt_64_32_73():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [15136491227645125134]
    tran0.writeAction("movir X16 53775")
    tran0.writeAction("slorii X16 X16 12 2537")
    tran0.writeAction("slorii X16 X16 12 817")
    tran0.writeAction("slorii X16 X16 12 2474")
    tran0.writeAction("slorii X16 X16 12 526")
    tran0.writeAction("fcnvt.64.32 X16 X16")
    tran0.writeAction("yieldt")
    return efa
