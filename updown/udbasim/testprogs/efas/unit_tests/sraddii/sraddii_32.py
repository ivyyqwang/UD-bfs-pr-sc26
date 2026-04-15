from EFA_v2 import *
def sraddii_32():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4962346992131004852, 9, 1762]
    tran0.writeAction("movir X16 17629")
    tran0.writeAction("slorii X16 X16 12 3268")
    tran0.writeAction("slorii X16 X16 12 3126")
    tran0.writeAction("slorii X16 X16 12 805")
    tran0.writeAction("slorii X16 X16 12 2484")
    tran0.writeAction("sraddii X16 X17 9 1762")
    tran0.writeAction("yieldt")
    return efa
