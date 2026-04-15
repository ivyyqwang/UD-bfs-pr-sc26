from EFA_v2 import *
def fcnvt_64_32_92():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [13912933206329021420]
    tran0.writeAction("movir X16 49428")
    tran0.writeAction("slorii X16 X16 12 2736")
    tran0.writeAction("slorii X16 X16 12 2442")
    tran0.writeAction("slorii X16 X16 12 4005")
    tran0.writeAction("slorii X16 X16 12 1004")
    tran0.writeAction("fcnvt.64.32 X16 X16")
    tran0.writeAction("yieldt")
    return efa
