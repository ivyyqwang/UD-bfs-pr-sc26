from EFA_v2 import *
def fcnvt_i64_64_51():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2156680069624334318]
    tran0.writeAction("movir X16 7662")
    tran0.writeAction("slorii X16 X16 12 273")
    tran0.writeAction("slorii X16 X16 12 2244")
    tran0.writeAction("slorii X16 X16 12 504")
    tran0.writeAction("slorii X16 X16 12 2030")
    tran0.writeAction("fcnvt.i64.64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
