from EFA_v2 import *
def fcnvt_64_i64_4():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [18441470306663256122]
    tran0.writeAction("movir X16 65517")
    tran0.writeAction("slorii X16 X16 12 1080")
    tran0.writeAction("slorii X16 X16 12 2412")
    tran0.writeAction("slorii X16 X16 12 2365")
    tran0.writeAction("slorii X16 X16 12 58")
    tran0.writeAction("fcnvt.64.i64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
