from EFA_v2 import *
def sladdii_57():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6423161150946776002, 14, 500]
    tran0.writeAction("movir X16 22819")
    tran0.writeAction("slorii X16 X16 12 2672")
    tran0.writeAction("slorii X16 X16 12 2321")
    tran0.writeAction("slorii X16 X16 12 1113")
    tran0.writeAction("slorii X16 X16 12 962")
    tran0.writeAction("sladdii X16 X17 14 500")
    tran0.writeAction("yieldt")
    return efa
