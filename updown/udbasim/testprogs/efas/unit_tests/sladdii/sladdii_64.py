from EFA_v2 import *
def sladdii_64():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1420425554892222630, 14, 172]
    tran0.writeAction("movir X16 5046")
    tran0.writeAction("slorii X16 X16 12 1496")
    tran0.writeAction("slorii X16 X16 12 1077")
    tran0.writeAction("slorii X16 X16 12 975")
    tran0.writeAction("slorii X16 X16 12 166")
    tran0.writeAction("sladdii X16 X17 14 172")
    tran0.writeAction("yieldt")
    return efa
