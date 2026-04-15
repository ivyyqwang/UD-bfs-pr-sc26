from EFA_v2 import *
def fcnvt_64_b16_37():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3962613399858671204]
    tran0.writeAction("movir X16 14078")
    tran0.writeAction("slorii X16 X16 12 126")
    tran0.writeAction("slorii X16 X16 12 1136")
    tran0.writeAction("slorii X16 X16 12 3190")
    tran0.writeAction("slorii X16 X16 12 3684")
    tran0.writeAction("fcnvt.64.b16 X16 X16")
    tran0.writeAction("yieldt")
    return efa
