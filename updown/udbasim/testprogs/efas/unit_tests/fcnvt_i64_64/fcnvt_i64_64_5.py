from EFA_v2 import *
def fcnvt_i64_64_5():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-5399381412851553518]
    tran0.writeAction("movir X16 46353")
    tran0.writeAction("slorii X16 X16 12 2227")
    tran0.writeAction("slorii X16 X16 12 1616")
    tran0.writeAction("slorii X16 X16 12 558")
    tran0.writeAction("slorii X16 X16 12 2834")
    tran0.writeAction("fcnvt.i64.64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
