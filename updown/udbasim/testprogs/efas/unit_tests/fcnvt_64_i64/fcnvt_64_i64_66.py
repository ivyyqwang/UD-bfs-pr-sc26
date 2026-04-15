from EFA_v2 import *
def fcnvt_64_i64_66():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5864858697413535266]
    tran0.writeAction("movir X16 20836")
    tran0.writeAction("slorii X16 X16 12 670")
    tran0.writeAction("slorii X16 X16 12 2421")
    tran0.writeAction("slorii X16 X16 12 794")
    tran0.writeAction("slorii X16 X16 12 1570")
    tran0.writeAction("fcnvt.64.i64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
