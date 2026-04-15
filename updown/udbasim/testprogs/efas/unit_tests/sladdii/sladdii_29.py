from EFA_v2 import *
def sladdii_29():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7032475688660928514, 3, 1121]
    tran0.writeAction("movir X16 24984")
    tran0.writeAction("slorii X16 X16 12 1526")
    tran0.writeAction("slorii X16 X16 12 274")
    tran0.writeAction("slorii X16 X16 12 840")
    tran0.writeAction("slorii X16 X16 12 2050")
    tran0.writeAction("sladdii X16 X17 3 1121")
    tran0.writeAction("yieldt")
    return efa
