from EFA_v2 import *
def fcnvt_64_b16_20():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [15609726778458166171]
    tran0.writeAction("movir X16 55456")
    tran0.writeAction("slorii X16 X16 12 3644")
    tran0.writeAction("slorii X16 X16 12 3350")
    tran0.writeAction("slorii X16 X16 12 3693")
    tran0.writeAction("slorii X16 X16 12 923")
    tran0.writeAction("fcnvt.64.b16 X16 X16")
    tran0.writeAction("yieldt")
    return efa
