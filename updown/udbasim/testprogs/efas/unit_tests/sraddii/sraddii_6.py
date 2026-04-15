from EFA_v2 import *
def sraddii_6():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [245436409492966847, 15, 1416]
    tran0.writeAction("movir X16 871")
    tran0.writeAction("slorii X16 X16 12 3953")
    tran0.writeAction("slorii X16 X16 12 3378")
    tran0.writeAction("slorii X16 X16 12 3176")
    tran0.writeAction("slorii X16 X16 12 3519")
    tran0.writeAction("sraddii X16 X17 15 1416")
    tran0.writeAction("yieldt")
    return efa
