from EFA_v2 import *
def fcnvt_64_b16_82():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [12737128220879058756]
    tran0.writeAction("movir X16 45251")
    tran0.writeAction("slorii X16 X16 12 1514")
    tran0.writeAction("slorii X16 X16 12 504")
    tran0.writeAction("slorii X16 X16 12 407")
    tran0.writeAction("slorii X16 X16 12 1860")
    tran0.writeAction("fcnvt.64.b16 X16 X16")
    tran0.writeAction("yieldt")
    return efa
