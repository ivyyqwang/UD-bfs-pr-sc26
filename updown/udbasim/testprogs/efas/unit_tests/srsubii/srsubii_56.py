from EFA_v2 import *
def srsubii_56():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1023011349750715735, 4, 1960]
    tran0.writeAction("movir X16 3634")
    tran0.writeAction("slorii X16 X16 12 1910")
    tran0.writeAction("slorii X16 X16 12 1799")
    tran0.writeAction("slorii X16 X16 12 345")
    tran0.writeAction("slorii X16 X16 12 1367")
    tran0.writeAction("srsubii X16 X17 4 1960")
    tran0.writeAction("yieldt")
    return efa
