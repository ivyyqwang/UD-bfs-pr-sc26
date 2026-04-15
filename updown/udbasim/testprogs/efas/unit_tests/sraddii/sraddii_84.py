from EFA_v2 import *
def sraddii_84():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3886827972395554169, 0, 480]
    tran0.writeAction("movir X16 13808")
    tran0.writeAction("slorii X16 X16 12 3223")
    tran0.writeAction("slorii X16 X16 12 661")
    tran0.writeAction("slorii X16 X16 12 2821")
    tran0.writeAction("slorii X16 X16 12 1401")
    tran0.writeAction("sraddii X16 X17 0 480")
    tran0.writeAction("yieldt")
    return efa
