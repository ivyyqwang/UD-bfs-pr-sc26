from EFA_v2 import *
def fcnvt_i64_64_77():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [732743145134104695]
    tran0.writeAction("movir X16 2603")
    tran0.writeAction("slorii X16 X16 12 928")
    tran0.writeAction("slorii X16 X16 12 541")
    tran0.writeAction("slorii X16 X16 12 1314")
    tran0.writeAction("slorii X16 X16 12 119")
    tran0.writeAction("fcnvt.i64.64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
