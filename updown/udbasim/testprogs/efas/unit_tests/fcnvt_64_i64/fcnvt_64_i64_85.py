from EFA_v2 import *
def fcnvt_64_i64_85():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3708929602198353875]
    tran0.writeAction("movir X16 13176")
    tran0.writeAction("slorii X16 X16 12 3133")
    tran0.writeAction("slorii X16 X16 12 651")
    tran0.writeAction("slorii X16 X16 12 3947")
    tran0.writeAction("slorii X16 X16 12 2003")
    tran0.writeAction("fcnvt.64.i64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
