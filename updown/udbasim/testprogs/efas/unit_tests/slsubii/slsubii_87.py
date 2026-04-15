from EFA_v2 import *
def slsubii_87():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-5810991060463238092, 4, 674]
    tran0.writeAction("movir X16 44891")
    tran0.writeAction("slorii X16 X16 12 870")
    tran0.writeAction("slorii X16 X16 12 2848")
    tran0.writeAction("slorii X16 X16 12 484")
    tran0.writeAction("slorii X16 X16 12 1076")
    tran0.writeAction("slsubii X16 X17 4 674")
    tran0.writeAction("yieldt")
    return efa
