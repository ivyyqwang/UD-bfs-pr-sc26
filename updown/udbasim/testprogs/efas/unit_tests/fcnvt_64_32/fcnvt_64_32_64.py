from EFA_v2 import *
def fcnvt_64_32_64():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [10529593116700226567]
    tran0.writeAction("movir X16 37408")
    tran0.writeAction("slorii X16 X16 12 2578")
    tran0.writeAction("slorii X16 X16 12 1734")
    tran0.writeAction("slorii X16 X16 12 1291")
    tran0.writeAction("slorii X16 X16 12 1031")
    tran0.writeAction("fcnvt.64.32 X16 X16")
    tran0.writeAction("yieldt")
    return efa
