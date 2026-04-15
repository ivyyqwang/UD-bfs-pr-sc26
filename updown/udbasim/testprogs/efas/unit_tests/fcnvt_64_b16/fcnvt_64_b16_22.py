from EFA_v2 import *
def fcnvt_64_b16_22():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [17362486384710241070]
    tran0.writeAction("movir X16 61683")
    tran0.writeAction("slorii X16 X16 12 3862")
    tran0.writeAction("slorii X16 X16 12 98")
    tran0.writeAction("slorii X16 X16 12 860")
    tran0.writeAction("slorii X16 X16 12 2862")
    tran0.writeAction("fcnvt.64.b16 X16 X16")
    tran0.writeAction("yieldt")
    return efa
