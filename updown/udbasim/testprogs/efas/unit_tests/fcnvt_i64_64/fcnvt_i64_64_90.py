from EFA_v2 import *
def fcnvt_i64_64_90():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4791495943691717921]
    tran0.writeAction("movir X16 17022")
    tran0.writeAction("slorii X16 X16 12 3330")
    tran0.writeAction("slorii X16 X16 12 3234")
    tran0.writeAction("slorii X16 X16 12 1924")
    tran0.writeAction("slorii X16 X16 12 3361")
    tran0.writeAction("fcnvt.i64.64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
