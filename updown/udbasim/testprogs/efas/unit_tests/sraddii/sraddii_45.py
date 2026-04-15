from EFA_v2 import *
def sraddii_45():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6152772458847493264, 2, 1510]
    tran0.writeAction("movir X16 21859")
    tran0.writeAction("slorii X16 X16 12 159")
    tran0.writeAction("slorii X16 X16 12 985")
    tran0.writeAction("slorii X16 X16 12 1685")
    tran0.writeAction("slorii X16 X16 12 3216")
    tran0.writeAction("sraddii X16 X17 2 1510")
    tran0.writeAction("yieldt")
    return efa
