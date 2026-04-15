from EFA_v2 import *
def fcnvt_i64_64_73():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5993326530352228377]
    tran0.writeAction("movir X16 21292")
    tran0.writeAction("slorii X16 X16 12 2347")
    tran0.writeAction("slorii X16 X16 12 2480")
    tran0.writeAction("slorii X16 X16 12 2330")
    tran0.writeAction("slorii X16 X16 12 2073")
    tran0.writeAction("fcnvt.i64.64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
