from EFA_v2 import *
def divi_80():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7810132399427187256, -2872]
    tran0.writeAction("movir X16 27747")
    tran0.writeAction("slorii X16 X16 12 672")
    tran0.writeAction("slorii X16 X16 12 2452")
    tran0.writeAction("slorii X16 X16 12 2567")
    tran0.writeAction("slorii X16 X16 12 568")
    tran0.writeAction("divi X16 X17 -2872")
    tran0.writeAction("yieldt")
    return efa
