from EFA_v2 import *
def fcnvt_b16_64_37():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [47846]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 11")
    tran0.writeAction("slorii X16 X16 12 2790")
    tran0.writeAction("fcnvt.b16.64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
