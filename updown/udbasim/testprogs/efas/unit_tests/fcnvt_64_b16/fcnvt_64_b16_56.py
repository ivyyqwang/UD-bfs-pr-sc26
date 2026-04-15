from EFA_v2 import *
def fcnvt_64_b16_56():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2466079803586524999]
    tran0.writeAction("movir X16 8761")
    tran0.writeAction("slorii X16 X16 12 1128")
    tran0.writeAction("slorii X16 X16 12 1016")
    tran0.writeAction("slorii X16 X16 12 2211")
    tran0.writeAction("slorii X16 X16 12 1863")
    tran0.writeAction("fcnvt.64.b16 X16 X16")
    tran0.writeAction("yieldt")
    return efa
