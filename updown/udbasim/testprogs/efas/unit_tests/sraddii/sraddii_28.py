from EFA_v2 import *
def sraddii_28():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-3263083122311413213, 14, 553]
    tran0.writeAction("movir X16 53943")
    tran0.writeAction("slorii X16 X16 12 819")
    tran0.writeAction("slorii X16 X16 12 86")
    tran0.writeAction("slorii X16 X16 12 228")
    tran0.writeAction("slorii X16 X16 12 547")
    tran0.writeAction("sraddii X16 X17 14 553")
    tran0.writeAction("yieldt")
    return efa
