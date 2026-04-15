from EFA_v2 import *
def fcnvt_64_i64_99():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [11576467486559336882]
    tran0.writeAction("movir X16 41127")
    tran0.writeAction("slorii X16 X16 12 3581")
    tran0.writeAction("slorii X16 X16 12 2082")
    tran0.writeAction("slorii X16 X16 12 935")
    tran0.writeAction("slorii X16 X16 12 2482")
    tran0.writeAction("fcnvt.64.i64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
