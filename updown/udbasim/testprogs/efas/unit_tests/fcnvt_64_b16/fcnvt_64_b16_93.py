from EFA_v2 import *
def fcnvt_64_b16_93():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8836893778670707880]
    tran0.writeAction("movir X16 31394")
    tran0.writeAction("slorii X16 X16 12 3905")
    tran0.writeAction("slorii X16 X16 12 611")
    tran0.writeAction("slorii X16 X16 12 2158")
    tran0.writeAction("slorii X16 X16 12 1192")
    tran0.writeAction("fcnvt.64.b16 X16 X16")
    tran0.writeAction("yieldt")
    return efa
