from EFA_v2 import *
def sladdii_78():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [642425304996895093, 7, 1202]
    tran0.writeAction("movir X16 2282")
    tran0.writeAction("slorii X16 X16 12 1446")
    tran0.writeAction("slorii X16 X16 12 2371")
    tran0.writeAction("slorii X16 X16 12 253")
    tran0.writeAction("slorii X16 X16 12 2421")
    tran0.writeAction("sladdii X16 X17 7 1202")
    tran0.writeAction("yieldt")
    return efa
