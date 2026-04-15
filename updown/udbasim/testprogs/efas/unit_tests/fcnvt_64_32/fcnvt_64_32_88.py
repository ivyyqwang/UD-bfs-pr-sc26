from EFA_v2 import *
def fcnvt_64_32_88():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3096103760051841489]
    tran0.writeAction("movir X16 10999")
    tran0.writeAction("slorii X16 X16 12 2335")
    tran0.writeAction("slorii X16 X16 12 1861")
    tran0.writeAction("slorii X16 X16 12 2626")
    tran0.writeAction("slorii X16 X16 12 2513")
    tran0.writeAction("fcnvt.64.32 X16 X16")
    tran0.writeAction("yieldt")
    return efa
