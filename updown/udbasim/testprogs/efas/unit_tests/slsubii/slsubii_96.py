from EFA_v2 import *
def slsubii_96():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-293272796867720035, 0, 748]
    tran0.writeAction("movir X16 64494")
    tran0.writeAction("slorii X16 X16 12 351")
    tran0.writeAction("slorii X16 X16 12 496")
    tran0.writeAction("slorii X16 X16 12 1696")
    tran0.writeAction("slorii X16 X16 12 3229")
    tran0.writeAction("slsubii X16 X17 0 748")
    tran0.writeAction("yieldt")
    return efa
