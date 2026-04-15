from EFA_v2 import *
def fcnvt_64_32_60():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7287220546410576745]
    tran0.writeAction("movir X16 25889")
    tran0.writeAction("slorii X16 X16 12 1671")
    tran0.writeAction("slorii X16 X16 12 2628")
    tran0.writeAction("slorii X16 X16 12 2991")
    tran0.writeAction("slorii X16 X16 12 2921")
    tran0.writeAction("fcnvt.64.32 X16 X16")
    tran0.writeAction("yieldt")
    return efa
