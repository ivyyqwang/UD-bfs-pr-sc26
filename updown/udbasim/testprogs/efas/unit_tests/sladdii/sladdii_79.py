from EFA_v2 import *
def sladdii_79():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-4450692352936063998, 0, 719]
    tran0.writeAction("movir X16 49723")
    tran0.writeAction("slorii X16 X16 12 3950")
    tran0.writeAction("slorii X16 X16 12 706")
    tran0.writeAction("slorii X16 X16 12 2860")
    tran0.writeAction("slorii X16 X16 12 3074")
    tran0.writeAction("sladdii X16 X17 0 719")
    tran0.writeAction("yieldt")
    return efa
