from EFA_v2 import *
def fcnvt_64_32_97():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6771541802628639123]
    tran0.writeAction("movir X16 24057")
    tran0.writeAction("slorii X16 X16 12 1430")
    tran0.writeAction("slorii X16 X16 12 1135")
    tran0.writeAction("slorii X16 X16 12 1590")
    tran0.writeAction("slorii X16 X16 12 2451")
    tran0.writeAction("fcnvt.64.32 X16 X16")
    tran0.writeAction("yieldt")
    return efa
