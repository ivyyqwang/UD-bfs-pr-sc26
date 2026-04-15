from EFA_v2 import *
def srsubii_76():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [446822590002537789, 2, 1224]
    tran0.writeAction("movir X16 1587")
    tran0.writeAction("slorii X16 X16 12 1772")
    tran0.writeAction("slorii X16 X16 12 1850")
    tran0.writeAction("slorii X16 X16 12 2954")
    tran0.writeAction("slorii X16 X16 12 1341")
    tran0.writeAction("srsubii X16 X17 2 1224")
    tran0.writeAction("yieldt")
    return efa
