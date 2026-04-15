from EFA_v2 import *
def fcnvt_64_b16_88():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3727179187737938214]
    tran0.writeAction("movir X16 13241")
    tran0.writeAction("slorii X16 X16 12 2459")
    tran0.writeAction("slorii X16 X16 12 2379")
    tran0.writeAction("slorii X16 X16 12 1428")
    tran0.writeAction("slorii X16 X16 12 2342")
    tran0.writeAction("fcnvt.64.b16 X16 X16")
    tran0.writeAction("yieldt")
    return efa
