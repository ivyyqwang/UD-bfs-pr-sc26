from EFA_v2 import *
def sladdii_93():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-6320757731619351959, 8, 1981]
    tran0.writeAction("movir X16 43080")
    tran0.writeAction("slorii X16 X16 12 645")
    tran0.writeAction("slorii X16 X16 12 1271")
    tran0.writeAction("slorii X16 X16 12 2149")
    tran0.writeAction("slorii X16 X16 12 617")
    tran0.writeAction("sladdii X16 X17 8 1981")
    tran0.writeAction("yieldt")
    return efa
