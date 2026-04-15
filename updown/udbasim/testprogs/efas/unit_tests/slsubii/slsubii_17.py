from EFA_v2 import *
def slsubii_17():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-9210024495724111595, 10, 1434]
    tran0.writeAction("movir X16 32815")
    tran0.writeAction("slorii X16 X16 12 1720")
    tran0.writeAction("slorii X16 X16 12 1175")
    tran0.writeAction("slorii X16 X16 12 2941")
    tran0.writeAction("slorii X16 X16 12 2325")
    tran0.writeAction("slsubii X16 X17 10 1434")
    tran0.writeAction("yieldt")
    return efa
