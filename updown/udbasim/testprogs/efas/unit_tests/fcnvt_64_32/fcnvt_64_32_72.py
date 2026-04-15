from EFA_v2 import *
def fcnvt_64_32_72():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2799388354579462896]
    tran0.writeAction("movir X16 9945")
    tran0.writeAction("slorii X16 X16 12 1742")
    tran0.writeAction("slorii X16 X16 12 111")
    tran0.writeAction("slorii X16 X16 12 303")
    tran0.writeAction("slorii X16 X16 12 2800")
    tran0.writeAction("fcnvt.64.32 X16 X16")
    tran0.writeAction("yieldt")
    return efa
