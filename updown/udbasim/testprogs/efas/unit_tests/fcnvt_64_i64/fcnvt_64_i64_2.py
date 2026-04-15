from EFA_v2 import *
def fcnvt_64_i64_2():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2926509926436862134]
    tran0.writeAction("movir X16 10397")
    tran0.writeAction("slorii X16 X16 12 212")
    tran0.writeAction("slorii X16 X16 12 1492")
    tran0.writeAction("slorii X16 X16 12 3783")
    tran0.writeAction("slorii X16 X16 12 2230")
    tran0.writeAction("fcnvt.64.i64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
