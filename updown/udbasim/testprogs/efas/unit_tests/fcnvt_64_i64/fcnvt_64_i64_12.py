from EFA_v2 import *
def fcnvt_64_i64_12():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8560125272641783388]
    tran0.writeAction("movir X16 30411")
    tran0.writeAction("slorii X16 X16 12 2761")
    tran0.writeAction("slorii X16 X16 12 1276")
    tran0.writeAction("slorii X16 X16 12 2692")
    tran0.writeAction("slorii X16 X16 12 1628")
    tran0.writeAction("fcnvt.64.i64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
