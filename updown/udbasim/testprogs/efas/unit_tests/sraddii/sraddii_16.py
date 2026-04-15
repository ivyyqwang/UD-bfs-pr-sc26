from EFA_v2 import *
def sraddii_16():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1548229403683698201, 8, 566]
    tran0.writeAction("movir X16 5500")
    tran0.writeAction("slorii X16 X16 12 1703")
    tran0.writeAction("slorii X16 X16 12 149")
    tran0.writeAction("slorii X16 X16 12 1563")
    tran0.writeAction("slorii X16 X16 12 1561")
    tran0.writeAction("sraddii X16 X17 8 566")
    tran0.writeAction("yieldt")
    return efa
