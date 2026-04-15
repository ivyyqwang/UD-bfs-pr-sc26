from EFA_v2 import *
def fcnvt_64_b16_26():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [12186748007805690366]
    tran0.writeAction("movir X16 43296")
    tran0.writeAction("slorii X16 X16 12 107")
    tran0.writeAction("slorii X16 X16 12 3764")
    tran0.writeAction("slorii X16 X16 12 1874")
    tran0.writeAction("slorii X16 X16 12 510")
    tran0.writeAction("fcnvt.64.b16 X16 X16")
    tran0.writeAction("yieldt")
    return efa
