from EFA_v2 import *
def fcnvt_64_32_81():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [13789909479000682743]
    tran0.writeAction("movir X16 48991")
    tran0.writeAction("slorii X16 X16 12 2457")
    tran0.writeAction("slorii X16 X16 12 3052")
    tran0.writeAction("slorii X16 X16 12 2571")
    tran0.writeAction("slorii X16 X16 12 247")
    tran0.writeAction("fcnvt.64.32 X16 X16")
    tran0.writeAction("yieldt")
    return efa
