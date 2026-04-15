from EFA_v2 import *
def modi_1():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-508681089868188339, -1823]
    tran0.writeAction("movir X16 63728")
    tran0.writeAction("slorii X16 X16 12 3283")
    tran0.writeAction("slorii X16 X16 12 3694")
    tran0.writeAction("slorii X16 X16 12 1835")
    tran0.writeAction("slorii X16 X16 12 1357")
    tran0.writeAction("modi X16 X17 -1823")
    tran0.writeAction("yieldt")
    return efa
