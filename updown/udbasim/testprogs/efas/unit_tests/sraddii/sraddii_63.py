from EFA_v2 import *
def sraddii_63():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-3573502805665691607, 3, 1842]
    tran0.writeAction("movir X16 52840")
    tran0.writeAction("slorii X16 X16 12 1506")
    tran0.writeAction("slorii X16 X16 12 424")
    tran0.writeAction("slorii X16 X16 12 1780")
    tran0.writeAction("slorii X16 X16 12 2089")
    tran0.writeAction("sraddii X16 X17 3 1842")
    tran0.writeAction("yieldt")
    return efa
