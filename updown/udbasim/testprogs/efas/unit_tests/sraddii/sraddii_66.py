from EFA_v2 import *
def sraddii_66():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-7716991031416762711, 9, 52]
    tran0.writeAction("movir X16 38119")
    tran0.writeAction("slorii X16 X16 12 3032")
    tran0.writeAction("slorii X16 X16 12 2837")
    tran0.writeAction("slorii X16 X16 12 2164")
    tran0.writeAction("slorii X16 X16 12 3753")
    tran0.writeAction("sraddii X16 X17 9 52")
    tran0.writeAction("yieldt")
    return efa
