from EFA_v2 import *
def fcnvt_64_32_79():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [10536920294401658462]
    tran0.writeAction("movir X16 37434")
    tran0.writeAction("slorii X16 X16 12 2706")
    tran0.writeAction("slorii X16 X16 12 3654")
    tran0.writeAction("slorii X16 X16 12 1700")
    tran0.writeAction("slorii X16 X16 12 3678")
    tran0.writeAction("fcnvt.64.32 X16 X16")
    tran0.writeAction("yieldt")
    return efa
