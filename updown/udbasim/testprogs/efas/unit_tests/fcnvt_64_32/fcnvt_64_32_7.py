from EFA_v2 import *
def fcnvt_64_32_7():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [18076461180295443214]
    tran0.writeAction("movir X16 64220")
    tran0.writeAction("slorii X16 X16 12 2010")
    tran0.writeAction("slorii X16 X16 12 2967")
    tran0.writeAction("slorii X16 X16 12 2655")
    tran0.writeAction("slorii X16 X16 12 782")
    tran0.writeAction("fcnvt.64.32 X16 X16")
    tran0.writeAction("yieldt")
    return efa
