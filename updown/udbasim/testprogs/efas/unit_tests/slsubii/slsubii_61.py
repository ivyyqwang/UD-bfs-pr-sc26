from EFA_v2 import *
def slsubii_61():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-4019057378222729916, 10, 1414]
    tran0.writeAction("movir X16 51257")
    tran0.writeAction("slorii X16 X16 12 1801")
    tran0.writeAction("slorii X16 X16 12 3007")
    tran0.writeAction("slorii X16 X16 12 497")
    tran0.writeAction("slorii X16 X16 12 1348")
    tran0.writeAction("slsubii X16 X17 10 1414")
    tran0.writeAction("yieldt")
    return efa
