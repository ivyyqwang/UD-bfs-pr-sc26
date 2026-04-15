from EFA_v2 import *
def srsubii_49():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-7658919244607157721, 11, 368]
    tran0.writeAction("movir X16 38326")
    tran0.writeAction("slorii X16 X16 12 216")
    tran0.writeAction("slorii X16 X16 12 1685")
    tran0.writeAction("slorii X16 X16 12 3224")
    tran0.writeAction("slorii X16 X16 12 2599")
    tran0.writeAction("srsubii X16 X17 11 368")
    tran0.writeAction("yieldt")
    return efa
