from EFA_v2 import *
def fcnvt_64_32_53():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1767940607085483471]
    tran0.writeAction("movir X16 6280")
    tran0.writeAction("slorii X16 X16 12 4041")
    tran0.writeAction("slorii X16 X16 12 3453")
    tran0.writeAction("slorii X16 X16 12 1305")
    tran0.writeAction("slorii X16 X16 12 1487")
    tran0.writeAction("fcnvt.64.32 X16 X16")
    tran0.writeAction("yieldt")
    return efa
