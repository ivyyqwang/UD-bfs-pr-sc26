from EFA_v2 import *
def fcnvt_64_b16_32():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7195069426292650064]
    tran0.writeAction("movir X16 25562")
    tran0.writeAction("slorii X16 X16 12 88")
    tran0.writeAction("slorii X16 X16 12 1448")
    tran0.writeAction("slorii X16 X16 12 1831")
    tran0.writeAction("slorii X16 X16 12 80")
    tran0.writeAction("fcnvt.64.b16 X16 X16")
    tran0.writeAction("yieldt")
    return efa
