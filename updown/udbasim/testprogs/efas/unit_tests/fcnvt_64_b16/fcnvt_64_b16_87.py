from EFA_v2 import *
def fcnvt_64_b16_87():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [10626811252350444611]
    tran0.writeAction("movir X16 37754")
    tran0.writeAction("slorii X16 X16 12 72")
    tran0.writeAction("slorii X16 X16 12 2015")
    tran0.writeAction("slorii X16 X16 12 1934")
    tran0.writeAction("slorii X16 X16 12 1091")
    tran0.writeAction("fcnvt.64.b16 X16 X16")
    tran0.writeAction("yieldt")
    return efa
