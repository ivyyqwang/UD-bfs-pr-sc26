from EFA_v2 import *
def fcnvt_32_b16_3():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1552225730]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 92")
    tran0.writeAction("slorii X16 X16 12 2129")
    tran0.writeAction("slorii X16 X16 12 1474")
    tran0.writeAction("fcnvt.32.b16 X16 X16")
    tran0.writeAction("yieldt")
    return efa
