from EFA_v2 import *
def slsubii_64():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-6231111198550951138, 7, 963]
    tran0.writeAction("movir X16 43398")
    tran0.writeAction("slorii X16 X16 12 2646")
    tran0.writeAction("slorii X16 X16 12 246")
    tran0.writeAction("slorii X16 X16 12 1687")
    tran0.writeAction("slorii X16 X16 12 2846")
    tran0.writeAction("slsubii X16 X17 7 963")
    tran0.writeAction("yieldt")
    return efa
