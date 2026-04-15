from EFA_v2 import *
def slsubii_7():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-7011523136606404787, 15, 1257]
    tran0.writeAction("movir X16 40626")
    tran0.writeAction("slorii X16 X16 12 269")
    tran0.writeAction("slorii X16 X16 12 2844")
    tran0.writeAction("slorii X16 X16 12 583")
    tran0.writeAction("slorii X16 X16 12 3917")
    tran0.writeAction("slsubii X16 X17 15 1257")
    tran0.writeAction("yieldt")
    return efa
