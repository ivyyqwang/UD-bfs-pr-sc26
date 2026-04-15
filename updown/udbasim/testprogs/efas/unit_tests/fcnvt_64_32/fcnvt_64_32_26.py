from EFA_v2 import *
def fcnvt_64_32_26():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [10922347481672452360]
    tran0.writeAction("movir X16 38803")
    tran0.writeAction("slorii X16 X16 12 3986")
    tran0.writeAction("slorii X16 X16 12 2654")
    tran0.writeAction("slorii X16 X16 12 1920")
    tran0.writeAction("slorii X16 X16 12 2312")
    tran0.writeAction("fcnvt.64.32 X16 X16")
    tran0.writeAction("yieldt")
    return efa
