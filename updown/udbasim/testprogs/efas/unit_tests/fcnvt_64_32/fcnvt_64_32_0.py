from EFA_v2 import *
def fcnvt_64_32_0():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2875592872181427260]
    tran0.writeAction("movir X16 10216")
    tran0.writeAction("slorii X16 X16 12 647")
    tran0.writeAction("slorii X16 X16 12 2897")
    tran0.writeAction("slorii X16 X16 12 78")
    tran0.writeAction("slorii X16 X16 12 3132")
    tran0.writeAction("fcnvt.64.32 X16 X16")
    tran0.writeAction("yieldt")
    return efa
