from EFA_v2 import *
def fcnvt_64_32_10():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [12404699133082178294]
    tran0.writeAction("movir X16 44070")
    tran0.writeAction("slorii X16 X16 12 1410")
    tran0.writeAction("slorii X16 X16 12 892")
    tran0.writeAction("slorii X16 X16 12 3929")
    tran0.writeAction("slorii X16 X16 12 758")
    tran0.writeAction("fcnvt.64.32 X16 X16")
    tran0.writeAction("yieldt")
    return efa
