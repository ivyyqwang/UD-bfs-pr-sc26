from EFA_v2 import *
def slsubii_3():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6733343452291657255, 10, 1660]
    tran0.writeAction("movir X16 23921")
    tran0.writeAction("slorii X16 X16 12 2627")
    tran0.writeAction("slorii X16 X16 12 496")
    tran0.writeAction("slorii X16 X16 12 2238")
    tran0.writeAction("slorii X16 X16 12 3623")
    tran0.writeAction("slsubii X16 X17 10 1660")
    tran0.writeAction("yieldt")
    return efa
