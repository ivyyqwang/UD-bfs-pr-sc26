from EFA_v2 import *
def sladdii_50():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1900705176995901313, 3, 40]
    tran0.writeAction("movir X16 6752")
    tran0.writeAction("slorii X16 X16 12 2708")
    tran0.writeAction("slorii X16 X16 12 2497")
    tran0.writeAction("slorii X16 X16 12 2402")
    tran0.writeAction("slorii X16 X16 12 3969")
    tran0.writeAction("sladdii X16 X17 3 40")
    tran0.writeAction("yieldt")
    return efa
