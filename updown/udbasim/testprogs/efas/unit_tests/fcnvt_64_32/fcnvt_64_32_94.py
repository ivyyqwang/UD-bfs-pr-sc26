from EFA_v2 import *
def fcnvt_64_32_94():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3952303006603632865]
    tran0.writeAction("movir X16 14041")
    tran0.writeAction("slorii X16 X16 12 1642")
    tran0.writeAction("slorii X16 X16 12 1265")
    tran0.writeAction("slorii X16 X16 12 1302")
    tran0.writeAction("slorii X16 X16 12 225")
    tran0.writeAction("fcnvt.64.32 X16 X16")
    tran0.writeAction("yieldt")
    return efa
