from EFA_v2 import *
def slsubii_45():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4970717929612158702, 12, 1556]
    tran0.writeAction("movir X16 17659")
    tran0.writeAction("slorii X16 X16 12 2201")
    tran0.writeAction("slorii X16 X16 12 3833")
    tran0.writeAction("slorii X16 X16 12 810")
    tran0.writeAction("slorii X16 X16 12 1774")
    tran0.writeAction("slsubii X16 X17 12 1556")
    tran0.writeAction("yieldt")
    return efa
