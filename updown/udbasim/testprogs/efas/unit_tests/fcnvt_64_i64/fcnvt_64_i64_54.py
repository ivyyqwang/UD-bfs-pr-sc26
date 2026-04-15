from EFA_v2 import *
def fcnvt_64_i64_54():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2667094589900962444]
    tran0.writeAction("movir X16 9475")
    tran0.writeAction("slorii X16 X16 12 1734")
    tran0.writeAction("slorii X16 X16 12 1549")
    tran0.writeAction("slorii X16 X16 12 1691")
    tran0.writeAction("slorii X16 X16 12 2700")
    tran0.writeAction("fcnvt.64.i64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
