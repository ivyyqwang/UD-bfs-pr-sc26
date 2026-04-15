from EFA_v2 import *
def fcnvt_64_b16_3():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [876121865711293580]
    tran0.writeAction("movir X16 3112")
    tran0.writeAction("slorii X16 X16 12 2499")
    tran0.writeAction("slorii X16 X16 12 489")
    tran0.writeAction("slorii X16 X16 12 2761")
    tran0.writeAction("slorii X16 X16 12 1164")
    tran0.writeAction("fcnvt.64.b16 X16 X16")
    tran0.writeAction("yieldt")
    return efa
