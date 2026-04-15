from EFA_v2 import *
def slsubii_70():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6079053720043143665, 2, 2013]
    tran0.writeAction("movir X16 21597")
    tran0.writeAction("slorii X16 X16 12 562")
    tran0.writeAction("slorii X16 X16 12 1649")
    tran0.writeAction("slorii X16 X16 12 2820")
    tran0.writeAction("slorii X16 X16 12 497")
    tran0.writeAction("slsubii X16 X17 2 2013")
    tran0.writeAction("yieldt")
    return efa
