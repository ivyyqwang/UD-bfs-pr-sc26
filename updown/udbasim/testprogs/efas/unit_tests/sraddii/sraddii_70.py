from EFA_v2 import *
def sraddii_70():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-3430039764125609295, 10, 123]
    tran0.writeAction("movir X16 53350")
    tran0.writeAction("slorii X16 X16 12 208")
    tran0.writeAction("slorii X16 X16 12 501")
    tran0.writeAction("slorii X16 X16 12 3393")
    tran0.writeAction("slorii X16 X16 12 689")
    tran0.writeAction("sraddii X16 X17 10 123")
    tran0.writeAction("yieldt")
    return efa
