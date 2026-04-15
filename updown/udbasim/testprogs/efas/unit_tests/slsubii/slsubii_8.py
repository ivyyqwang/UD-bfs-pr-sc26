from EFA_v2 import *
def slsubii_8():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5606045258955641206, 10, 1975]
    tran0.writeAction("movir X16 19916")
    tran0.writeAction("slorii X16 X16 12 2759")
    tran0.writeAction("slorii X16 X16 12 1534")
    tran0.writeAction("slorii X16 X16 12 3333")
    tran0.writeAction("slorii X16 X16 12 374")
    tran0.writeAction("slsubii X16 X17 10 1975")
    tran0.writeAction("yieldt")
    return efa
