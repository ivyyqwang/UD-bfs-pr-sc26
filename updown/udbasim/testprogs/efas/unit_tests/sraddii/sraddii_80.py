from EFA_v2 import *
def sraddii_80():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-7783457693238901101, 15, 95]
    tran0.writeAction("movir X16 37883")
    tran0.writeAction("slorii X16 X16 12 2471")
    tran0.writeAction("slorii X16 X16 12 1902")
    tran0.writeAction("slorii X16 X16 12 876")
    tran0.writeAction("slorii X16 X16 12 1683")
    tran0.writeAction("sraddii X16 X17 15 95")
    tran0.writeAction("yieldt")
    return efa
