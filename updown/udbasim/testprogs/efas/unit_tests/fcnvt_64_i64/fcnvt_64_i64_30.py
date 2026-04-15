from EFA_v2 import *
def fcnvt_64_i64_30():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [17386812116990020936]
    tran0.writeAction("movir X16 61770")
    tran0.writeAction("slorii X16 X16 12 1496")
    tran0.writeAction("slorii X16 X16 12 73")
    tran0.writeAction("slorii X16 X16 12 2652")
    tran0.writeAction("slorii X16 X16 12 3400")
    tran0.writeAction("fcnvt.64.i64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
