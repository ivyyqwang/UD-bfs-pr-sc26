from EFA_v2 import *
def slsubii_71():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6348946824761311267, 15, 1733]
    tran0.writeAction("movir X16 22555")
    tran0.writeAction("slorii X16 X16 12 4055")
    tran0.writeAction("slorii X16 X16 12 4027")
    tran0.writeAction("slorii X16 X16 12 3040")
    tran0.writeAction("slorii X16 X16 12 35")
    tran0.writeAction("slsubii X16 X17 15 1733")
    tran0.writeAction("yieldt")
    return efa
