from EFA_v2 import *
def slsubii_53():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-7530886389149376660, 0, 252]
    tran0.writeAction("movir X16 38780")
    tran0.writeAction("slorii X16 X16 12 3755")
    tran0.writeAction("slorii X16 X16 12 2746")
    tran0.writeAction("slorii X16 X16 12 3797")
    tran0.writeAction("slorii X16 X16 12 3948")
    tran0.writeAction("slsubii X16 X17 0 252")
    tran0.writeAction("yieldt")
    return efa
