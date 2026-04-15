from EFA_v2 import *
def divi_96():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-3978271300964780963, 25033]
    tran0.writeAction("movir X16 51402")
    tran0.writeAction("slorii X16 X16 12 1397")
    tran0.writeAction("slorii X16 X16 12 1117")
    tran0.writeAction("slorii X16 X16 12 3535")
    tran0.writeAction("slorii X16 X16 12 1117")
    tran0.writeAction("divi X16 X17 25033")
    tran0.writeAction("yieldt")
    return efa
