from EFA_v2 import *
def slsubii_48():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7129151032117657124, 15, 1209]
    tran0.writeAction("movir X16 25327")
    tran0.writeAction("slorii X16 X16 12 3409")
    tran0.writeAction("slorii X16 X16 12 1923")
    tran0.writeAction("slorii X16 X16 12 1975")
    tran0.writeAction("slorii X16 X16 12 3620")
    tran0.writeAction("slsubii X16 X17 15 1209")
    tran0.writeAction("yieldt")
    return efa
