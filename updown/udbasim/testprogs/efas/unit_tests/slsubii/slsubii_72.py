from EFA_v2 import *
def slsubii_72():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1408700361220487685, 15, 1106]
    tran0.writeAction("movir X16 5004")
    tran0.writeAction("slorii X16 X16 12 2904")
    tran0.writeAction("slorii X16 X16 12 977")
    tran0.writeAction("slorii X16 X16 12 2095")
    tran0.writeAction("slorii X16 X16 12 2565")
    tran0.writeAction("slsubii X16 X17 15 1106")
    tran0.writeAction("yieldt")
    return efa
