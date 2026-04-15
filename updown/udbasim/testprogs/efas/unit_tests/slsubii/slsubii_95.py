from EFA_v2 import *
def slsubii_95():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1719602467896182705, 4, 60]
    tran0.writeAction("movir X16 59426")
    tran0.writeAction("slorii X16 X16 12 3050")
    tran0.writeAction("slorii X16 X16 12 2706")
    tran0.writeAction("slorii X16 X16 12 667")
    tran0.writeAction("slorii X16 X16 12 2127")
    tran0.writeAction("slsubii X16 X17 4 60")
    tran0.writeAction("yieldt")
    return efa
