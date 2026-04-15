from EFA_v2 import *
def fcnvt_64_i64_89():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5145106861179756852]
    tran0.writeAction("movir X16 18279")
    tran0.writeAction("slorii X16 X16 12 374")
    tran0.writeAction("slorii X16 X16 12 3624")
    tran0.writeAction("slorii X16 X16 12 182")
    tran0.writeAction("slorii X16 X16 12 308")
    tran0.writeAction("fcnvt.64.i64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
