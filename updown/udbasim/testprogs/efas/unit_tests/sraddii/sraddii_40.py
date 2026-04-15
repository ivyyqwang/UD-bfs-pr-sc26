from EFA_v2 import *
def sraddii_40():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4898406359658162431, 3, 984]
    tran0.writeAction("movir X16 17402")
    tran0.writeAction("slorii X16 X16 12 2602")
    tran0.writeAction("slorii X16 X16 12 408")
    tran0.writeAction("slorii X16 X16 12 3846")
    tran0.writeAction("slorii X16 X16 12 2303")
    tran0.writeAction("sraddii X16 X17 3 984")
    tran0.writeAction("yieldt")
    return efa
