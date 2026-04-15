from EFA_v2 import *
def slsubii_6():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1807380919110464163, 15, 934]
    tran0.writeAction("movir X16 59114")
    tran0.writeAction("slorii X16 X16 12 3658")
    tran0.writeAction("slorii X16 X16 12 326")
    tran0.writeAction("slorii X16 X16 12 2464")
    tran0.writeAction("slorii X16 X16 12 3421")
    tran0.writeAction("slsubii X16 X17 15 934")
    tran0.writeAction("yieldt")
    return efa
