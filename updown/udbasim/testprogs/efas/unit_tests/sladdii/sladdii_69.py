from EFA_v2 import *
def sladdii_69():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4805094307111428828, 11, 1056]
    tran0.writeAction("movir X16 17071")
    tran0.writeAction("slorii X16 X16 12 509")
    tran0.writeAction("slorii X16 X16 12 87")
    tran0.writeAction("slorii X16 X16 12 2574")
    tran0.writeAction("slorii X16 X16 12 732")
    tran0.writeAction("sladdii X16 X17 11 1056")
    tran0.writeAction("yieldt")
    return efa
