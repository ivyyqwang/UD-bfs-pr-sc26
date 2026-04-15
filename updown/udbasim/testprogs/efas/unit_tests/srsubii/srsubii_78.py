from EFA_v2 import *
def srsubii_78():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2645611459440811624, 12, 1946]
    tran0.writeAction("movir X16 9399")
    tran0.writeAction("slorii X16 X16 12 409")
    tran0.writeAction("slorii X16 X16 12 2805")
    tran0.writeAction("slorii X16 X16 12 2753")
    tran0.writeAction("slorii X16 X16 12 3688")
    tran0.writeAction("srsubii X16 X17 12 1946")
    tran0.writeAction("yieldt")
    return efa
