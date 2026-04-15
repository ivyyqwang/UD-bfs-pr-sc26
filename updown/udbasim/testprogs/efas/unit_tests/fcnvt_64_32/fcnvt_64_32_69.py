from EFA_v2 import *
def fcnvt_64_32_69():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [17676132339534384900]
    tran0.writeAction("movir X16 62798")
    tran0.writeAction("slorii X16 X16 12 971")
    tran0.writeAction("slorii X16 X16 12 1516")
    tran0.writeAction("slorii X16 X16 12 3036")
    tran0.writeAction("slorii X16 X16 12 3844")
    tran0.writeAction("fcnvt.64.32 X16 X16")
    tran0.writeAction("yieldt")
    return efa
