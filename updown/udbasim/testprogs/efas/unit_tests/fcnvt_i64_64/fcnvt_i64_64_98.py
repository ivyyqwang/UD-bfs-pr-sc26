from EFA_v2 import *
def fcnvt_i64_64_98():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-6820940487950524245]
    tran0.writeAction("movir X16 41303")
    tran0.writeAction("slorii X16 X16 12 620")
    tran0.writeAction("slorii X16 X16 12 989")
    tran0.writeAction("slorii X16 X16 12 2578")
    tran0.writeAction("slorii X16 X16 12 171")
    tran0.writeAction("fcnvt.i64.64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
