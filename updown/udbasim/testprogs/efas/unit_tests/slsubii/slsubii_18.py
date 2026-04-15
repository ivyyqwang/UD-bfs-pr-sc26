from EFA_v2 import *
def slsubii_18():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-3747517623619205775, 15, 393]
    tran0.writeAction("movir X16 52222")
    tran0.writeAction("slorii X16 X16 12 585")
    tran0.writeAction("slorii X16 X16 12 918")
    tran0.writeAction("slorii X16 X16 12 2708")
    tran0.writeAction("slorii X16 X16 12 1393")
    tran0.writeAction("slsubii X16 X17 15 393")
    tran0.writeAction("yieldt")
    return efa
