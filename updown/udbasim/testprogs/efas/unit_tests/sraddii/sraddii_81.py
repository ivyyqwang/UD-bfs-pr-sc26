from EFA_v2 import *
def sraddii_81():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-3023888397711591621, 11, 1657]
    tran0.writeAction("movir X16 54792")
    tran0.writeAction("slorii X16 X16 12 4056")
    tran0.writeAction("slorii X16 X16 12 1541")
    tran0.writeAction("slorii X16 X16 12 3995")
    tran0.writeAction("slorii X16 X16 12 1851")
    tran0.writeAction("sraddii X16 X17 11 1657")
    tran0.writeAction("yieldt")
    return efa
