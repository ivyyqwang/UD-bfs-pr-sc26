from EFA_v2 import *
def sraddii_29():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2120132062981280972, 9, 1429]
    tran0.writeAction("movir X16 7532")
    tran0.writeAction("slorii X16 X16 12 910")
    tran0.writeAction("slorii X16 X16 12 218")
    tran0.writeAction("slorii X16 X16 12 3749")
    tran0.writeAction("slorii X16 X16 12 1228")
    tran0.writeAction("sraddii X16 X17 9 1429")
    tran0.writeAction("yieldt")
    return efa
