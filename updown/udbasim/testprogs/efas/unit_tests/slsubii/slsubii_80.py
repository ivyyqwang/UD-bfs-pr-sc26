from EFA_v2 import *
def slsubii_80():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5912918950221909798, 4, 365]
    tran0.writeAction("movir X16 21006")
    tran0.writeAction("slorii X16 X16 12 3719")
    tran0.writeAction("slorii X16 X16 12 1293")
    tran0.writeAction("slorii X16 X16 12 2672")
    tran0.writeAction("slorii X16 X16 12 3878")
    tran0.writeAction("slsubii X16 X17 4 365")
    tran0.writeAction("yieldt")
    return efa
