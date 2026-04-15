from EFA_v2 import *
def slsubii_62():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5240979462952338486, 3, 1475]
    tran0.writeAction("movir X16 18619")
    tran0.writeAction("slorii X16 X16 12 2864")
    tran0.writeAction("slorii X16 X16 12 3516")
    tran0.writeAction("slorii X16 X16 12 1604")
    tran0.writeAction("slorii X16 X16 12 1078")
    tran0.writeAction("slsubii X16 X17 3 1475")
    tran0.writeAction("yieldt")
    return efa
