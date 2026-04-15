from EFA_v2 import *
def divi_88():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-508527611161479710, 22218]
    tran0.writeAction("movir X16 63729")
    tran0.writeAction("slorii X16 X16 12 1421")
    tran0.writeAction("slorii X16 X16 12 1274")
    tran0.writeAction("slorii X16 X16 12 991")
    tran0.writeAction("slorii X16 X16 12 1506")
    tran0.writeAction("divi X16 X17 22218")
    tran0.writeAction("yieldt")
    return efa
