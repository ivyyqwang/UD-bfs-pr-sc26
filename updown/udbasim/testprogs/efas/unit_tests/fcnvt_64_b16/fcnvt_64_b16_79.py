from EFA_v2 import *
def fcnvt_64_b16_79():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8561511518795304900]
    tran0.writeAction("movir X16 30416")
    tran0.writeAction("slorii X16 X16 12 2453")
    tran0.writeAction("slorii X16 X16 12 3474")
    tran0.writeAction("slorii X16 X16 12 856")
    tran0.writeAction("slorii X16 X16 12 4036")
    tran0.writeAction("fcnvt.64.b16 X16 X16")
    tran0.writeAction("yieldt")
    return efa
