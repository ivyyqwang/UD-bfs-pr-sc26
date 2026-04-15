from EFA_v2 import *
def addi_73():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1564865451346723085, -20403]
    tran0.writeAction("movir X16 5559")
    tran0.writeAction("slorii X16 X16 12 2125")
    tran0.writeAction("slorii X16 X16 12 1604")
    tran0.writeAction("slorii X16 X16 12 3288")
    tran0.writeAction("slorii X16 X16 12 269")
    tran0.writeAction("addi X16 X17 -20403")
    tran0.writeAction("yieldt")
    return efa
