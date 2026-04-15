from EFA_v2 import *
def sraddii_76():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-7011067572075624741, 0, 1214]
    tran0.writeAction("movir X16 40627")
    tran0.writeAction("slorii X16 X16 12 2803")
    tran0.writeAction("slorii X16 X16 12 126")
    tran0.writeAction("slorii X16 X16 12 704")
    tran0.writeAction("slorii X16 X16 12 1755")
    tran0.writeAction("sraddii X16 X17 0 1214")
    tran0.writeAction("yieldt")
    return efa
