from EFA_v2 import *
def fcnvt_64_i64_41():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [9684576113249882000]
    tran0.writeAction("movir X16 34406")
    tran0.writeAction("slorii X16 X16 12 2154")
    tran0.writeAction("slorii X16 X16 12 2550")
    tran0.writeAction("slorii X16 X16 12 2016")
    tran0.writeAction("slorii X16 X16 12 3984")
    tran0.writeAction("fcnvt.64.i64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
