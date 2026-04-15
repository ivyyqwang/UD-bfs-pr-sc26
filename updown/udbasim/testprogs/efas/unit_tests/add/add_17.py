from EFA_v2 import *
def add_17():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6983700898598008937, 3885293765110285491]
    tran0.writeAction("movir X16 24811")
    tran0.writeAction("slorii X16 X16 12 367")
    tran0.writeAction("slorii X16 X16 12 1870")
    tran0.writeAction("slorii X16 X16 12 2091")
    tran0.writeAction("slorii X16 X16 12 2153")
    tran0.writeAction("movir X17 13803")
    tran0.writeAction("slorii X17 X17 12 1377")
    tran0.writeAction("slorii X17 X17 12 2077")
    tran0.writeAction("slorii X17 X17 12 1796")
    tran0.writeAction("slorii X17 X17 12 1203")
    tran0.writeAction("add X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
