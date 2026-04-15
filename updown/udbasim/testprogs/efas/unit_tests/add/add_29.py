from EFA_v2 import *
def add_29():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5759089850437612187, 6168619170455667511]
    tran0.writeAction("movir X16 20460")
    tran0.writeAction("slorii X16 X16 12 1627")
    tran0.writeAction("slorii X16 X16 12 1212")
    tran0.writeAction("slorii X16 X16 12 3651")
    tran0.writeAction("slorii X16 X16 12 667")
    tran0.writeAction("movir X17 21915")
    tran0.writeAction("slorii X17 X17 12 1383")
    tran0.writeAction("slorii X17 X17 12 1001")
    tran0.writeAction("slorii X17 X17 12 2764")
    tran0.writeAction("slorii X17 X17 12 823")
    tran0.writeAction("add X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
