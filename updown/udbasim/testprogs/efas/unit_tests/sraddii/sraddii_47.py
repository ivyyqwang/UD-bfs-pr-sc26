from EFA_v2 import *
def sraddii_47():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-6017176494680075776, 15, 122]
    tran0.writeAction("movir X16 44158")
    tran0.writeAction("slorii X16 X16 12 2845")
    tran0.writeAction("slorii X16 X16 12 3011")
    tran0.writeAction("slorii X16 X16 12 3129")
    tran0.writeAction("slorii X16 X16 12 512")
    tran0.writeAction("sraddii X16 X17 15 122")
    tran0.writeAction("yieldt")
    return efa
