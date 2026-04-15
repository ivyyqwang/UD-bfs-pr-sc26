from EFA_v2 import *
def fcnvt_64_b16_91():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6772109147803000569]
    tran0.writeAction("movir X16 24059")
    tran0.writeAction("slorii X16 X16 12 1494")
    tran0.writeAction("slorii X16 X16 12 966")
    tran0.writeAction("slorii X16 X16 12 3977")
    tran0.writeAction("slorii X16 X16 12 3833")
    tran0.writeAction("fcnvt.64.b16 X16 X16")
    tran0.writeAction("yieldt")
    return efa
