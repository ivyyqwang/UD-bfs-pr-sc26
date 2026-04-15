from EFA_v2 import *
def sladdii_0():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-7215527534018050852, 7, 1974]
    tran0.writeAction("movir X16 39901")
    tran0.writeAction("slorii X16 X16 12 1214")
    tran0.writeAction("slorii X16 X16 12 4083")
    tran0.writeAction("slorii X16 X16 12 3292")
    tran0.writeAction("slorii X16 X16 12 1244")
    tran0.writeAction("sladdii X16 X17 7 1974")
    tran0.writeAction("yieldt")
    return efa
