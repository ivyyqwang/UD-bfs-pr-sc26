from EFA_v2 import *
def sraddii_39():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-737536652647638370, 9, 1640]
    tran0.writeAction("movir X16 62915")
    tran0.writeAction("slorii X16 X16 12 3045")
    tran0.writeAction("slorii X16 X16 12 626")
    tran0.writeAction("slorii X16 X16 12 437")
    tran0.writeAction("slorii X16 X16 12 2718")
    tran0.writeAction("sraddii X16 X17 9 1640")
    tran0.writeAction("yieldt")
    return efa
