from EFA_v2 import *
def fcnvt_64_b16_48():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4098456025080953681]
    tran0.writeAction("movir X16 14560")
    tran0.writeAction("slorii X16 X16 12 2624")
    tran0.writeAction("slorii X16 X16 12 2638")
    tran0.writeAction("slorii X16 X16 12 2087")
    tran0.writeAction("slorii X16 X16 12 2897")
    tran0.writeAction("fcnvt.64.b16 X16 X16")
    tran0.writeAction("yieldt")
    return efa
