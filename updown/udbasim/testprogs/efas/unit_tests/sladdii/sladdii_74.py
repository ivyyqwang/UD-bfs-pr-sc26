from EFA_v2 import *
def sladdii_74():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4801331152373540183, 15, 967]
    tran0.writeAction("movir X16 17057")
    tran0.writeAction("slorii X16 X16 12 3091")
    tran0.writeAction("slorii X16 X16 12 3738")
    tran0.writeAction("slorii X16 X16 12 990")
    tran0.writeAction("slorii X16 X16 12 1367")
    tran0.writeAction("sladdii X16 X17 15 967")
    tran0.writeAction("yieldt")
    return efa
