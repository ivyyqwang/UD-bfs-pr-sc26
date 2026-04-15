from EFA_v2 import *
def slsubii_5():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-3926330023695612312, 6, 1310]
    tran0.writeAction("movir X16 51586")
    tran0.writeAction("slorii X16 X16 12 3578")
    tran0.writeAction("slorii X16 X16 12 1378")
    tran0.writeAction("slorii X16 X16 12 2752")
    tran0.writeAction("slorii X16 X16 12 1640")
    tran0.writeAction("slsubii X16 X17 6 1310")
    tran0.writeAction("yieldt")
    return efa
