from EFA_v2 import *
def fcnvt_i64_64_27():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8037888238188316099]
    tran0.writeAction("movir X16 28556")
    tran0.writeAction("slorii X16 X16 12 1292")
    tran0.writeAction("slorii X16 X16 12 1053")
    tran0.writeAction("slorii X16 X16 12 2068")
    tran0.writeAction("slorii X16 X16 12 1475")
    tran0.writeAction("fcnvt.i64.64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
