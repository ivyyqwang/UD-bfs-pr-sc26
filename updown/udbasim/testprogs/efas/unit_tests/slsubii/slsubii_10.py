from EFA_v2 import *
def slsubii_10():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7322806275042245092, 10, 421]
    tran0.writeAction("movir X16 26015")
    tran0.writeAction("slorii X16 X16 12 3416")
    tran0.writeAction("slorii X16 X16 12 606")
    tran0.writeAction("slorii X16 X16 12 3663")
    tran0.writeAction("slorii X16 X16 12 2532")
    tran0.writeAction("slsubii X16 X17 10 421")
    tran0.writeAction("yieldt")
    return efa
