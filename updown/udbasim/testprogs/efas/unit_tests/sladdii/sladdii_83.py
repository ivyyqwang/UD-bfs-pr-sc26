from EFA_v2 import *
def sladdii_83():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4147726503494463253, 12, 2044]
    tran0.writeAction("movir X16 14735")
    tran0.writeAction("slorii X16 X16 12 2804")
    tran0.writeAction("slorii X16 X16 12 1922")
    tran0.writeAction("slorii X16 X16 12 1066")
    tran0.writeAction("slorii X16 X16 12 3861")
    tran0.writeAction("sladdii X16 X17 12 2044")
    tran0.writeAction("yieldt")
    return efa
