from EFA_v2 import *
def sub_49():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6177617415892542949, 6680111326812466523]
    tran0.writeAction("movir X16 21947")
    tran0.writeAction("slorii X16 X16 12 1252")
    tran0.writeAction("slorii X16 X16 12 3888")
    tran0.writeAction("slorii X16 X16 12 2218")
    tran0.writeAction("slorii X16 X16 12 1509")
    tran0.writeAction("movir X17 23732")
    tran0.writeAction("slorii X17 X17 12 2141")
    tran0.writeAction("slorii X17 X17 12 3046")
    tran0.writeAction("slorii X17 X17 12 2950")
    tran0.writeAction("slorii X17 X17 12 3419")
    tran0.writeAction("sub X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
