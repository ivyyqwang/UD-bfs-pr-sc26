from EFA_v2 import *
def slsubii_40():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6169883742109473653, 4, 1982]
    tran0.writeAction("movir X16 21919")
    tran0.writeAction("slorii X16 X16 12 3401")
    tran0.writeAction("slorii X16 X16 12 753")
    tran0.writeAction("slorii X16 X16 12 3657")
    tran0.writeAction("slorii X16 X16 12 2933")
    tran0.writeAction("slsubii X16 X17 4 1982")
    tran0.writeAction("yieldt")
    return efa
