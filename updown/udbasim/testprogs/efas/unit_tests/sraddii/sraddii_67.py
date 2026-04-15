from EFA_v2 import *
def sraddii_67():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4518580275198847304, 2, 338]
    tran0.writeAction("movir X16 16053")
    tran0.writeAction("slorii X16 X16 12 909")
    tran0.writeAction("slorii X16 X16 12 480")
    tran0.writeAction("slorii X16 X16 12 1286")
    tran0.writeAction("slorii X16 X16 12 2376")
    tran0.writeAction("sraddii X16 X17 2 338")
    tran0.writeAction("yieldt")
    return efa
