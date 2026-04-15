from EFA_v2 import *
def fcnvt_64_i64_74():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4780844248918245795]
    tran0.writeAction("movir X16 16984")
    tran0.writeAction("slorii X16 X16 12 3976")
    tran0.writeAction("slorii X16 X16 12 943")
    tran0.writeAction("slorii X16 X16 12 988")
    tran0.writeAction("slorii X16 X16 12 419")
    tran0.writeAction("fcnvt.64.i64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
