from EFA_v2 import *
def sraddii_97():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1363164470921030571, 3, 388]
    tran0.writeAction("movir X16 60693")
    tran0.writeAction("slorii X16 X16 12 274")
    tran0.writeAction("slorii X16 X16 12 724")
    tran0.writeAction("slorii X16 X16 12 1305")
    tran0.writeAction("slorii X16 X16 12 1109")
    tran0.writeAction("sraddii X16 X17 3 388")
    tran0.writeAction("yieldt")
    return efa
