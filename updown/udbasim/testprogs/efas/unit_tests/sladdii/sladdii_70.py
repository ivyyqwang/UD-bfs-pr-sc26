from EFA_v2 import *
def sladdii_70():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-7357035910193273248, 5, 1257]
    tran0.writeAction("movir X16 39398")
    tran0.writeAction("slorii X16 X16 12 2285")
    tran0.writeAction("slorii X16 X16 12 421")
    tran0.writeAction("slorii X16 X16 12 562")
    tran0.writeAction("slorii X16 X16 12 1632")
    tran0.writeAction("sladdii X16 X17 5 1257")
    tran0.writeAction("yieldt")
    return efa
