from EFA_v2 import *
def sraddii_35():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-8148075419706395172, 1, 51]
    tran0.writeAction("movir X16 36588")
    tran0.writeAction("slorii X16 X16 12 905")
    tran0.writeAction("slorii X16 X16 12 893")
    tran0.writeAction("slorii X16 X16 12 1263")
    tran0.writeAction("slorii X16 X16 12 1500")
    tran0.writeAction("sraddii X16 X17 1 51")
    tran0.writeAction("yieldt")
    return efa
