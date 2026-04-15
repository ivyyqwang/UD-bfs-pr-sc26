from EFA_v2 import *
def fcnvt_i64_64_67():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-5049443023780736049]
    tran0.writeAction("movir X16 47596")
    tran0.writeAction("slorii X16 X16 12 3173")
    tran0.writeAction("slorii X16 X16 12 685")
    tran0.writeAction("slorii X16 X16 12 3993")
    tran0.writeAction("slorii X16 X16 12 975")
    tran0.writeAction("fcnvt.i64.64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
