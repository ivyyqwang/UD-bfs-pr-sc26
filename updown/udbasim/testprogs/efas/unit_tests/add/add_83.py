from EFA_v2 import *
def add_83():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2398417710985470637, -8107216743936858675]
    tran0.writeAction("movir X16 8520")
    tran0.writeAction("slorii X16 X16 12 3651")
    tran0.writeAction("slorii X16 X16 12 870")
    tran0.writeAction("slorii X16 X16 12 1206")
    tran0.writeAction("slorii X16 X16 12 685")
    tran0.writeAction("movir X17 36733")
    tran0.writeAction("slorii X17 X17 12 1557")
    tran0.writeAction("slorii X17 X17 12 836")
    tran0.writeAction("slorii X17 X17 12 2230")
    tran0.writeAction("slorii X17 X17 12 1485")
    tran0.writeAction("add X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
