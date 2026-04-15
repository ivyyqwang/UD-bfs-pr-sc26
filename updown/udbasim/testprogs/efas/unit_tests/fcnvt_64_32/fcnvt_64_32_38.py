from EFA_v2 import *
def fcnvt_64_32_38():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [17299631504508429863]
    tran0.writeAction("movir X16 61460")
    tran0.writeAction("slorii X16 X16 12 2611")
    tran0.writeAction("slorii X16 X16 12 555")
    tran0.writeAction("slorii X16 X16 12 1562")
    tran0.writeAction("slorii X16 X16 12 1575")
    tran0.writeAction("fcnvt.64.32 X16 X16")
    tran0.writeAction("yieldt")
    return efa
