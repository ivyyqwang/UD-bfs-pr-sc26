from EFA_v2 import *
def sladdii_84():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6435178287603354215, 12, 1937]
    tran0.writeAction("movir X16 22862")
    tran0.writeAction("slorii X16 X16 12 1416")
    tran0.writeAction("slorii X16 X16 12 3770")
    tran0.writeAction("slorii X16 X16 12 3704")
    tran0.writeAction("slorii X16 X16 12 2663")
    tran0.writeAction("sladdii X16 X17 12 1937")
    tran0.writeAction("yieldt")
    return efa
