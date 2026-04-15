from EFA_v2 import *
def sraddii_78():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-9002777311225980984, 5, 1956]
    tran0.writeAction("movir X16 33551")
    tran0.writeAction("slorii X16 X16 12 2907")
    tran0.writeAction("slorii X16 X16 12 3060")
    tran0.writeAction("slorii X16 X16 12 1757")
    tran0.writeAction("slorii X16 X16 12 1992")
    tran0.writeAction("sraddii X16 X17 5 1956")
    tran0.writeAction("yieldt")
    return efa
