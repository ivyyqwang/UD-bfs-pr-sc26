from EFA_v2 import *
def divi_34():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7756984646028433129, -16836]
    tran0.writeAction("movir X16 27558")
    tran0.writeAction("slorii X16 X16 12 1414")
    tran0.writeAction("slorii X16 X16 12 4082")
    tran0.writeAction("slorii X16 X16 12 2801")
    tran0.writeAction("slorii X16 X16 12 1769")
    tran0.writeAction("divi X16 X17 -16836")
    tran0.writeAction("yieldt")
    return efa
