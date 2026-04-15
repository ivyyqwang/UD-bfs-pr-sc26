from EFA_v2 import *
def sraddii_72():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3578690254696046025, 6, 1163]
    tran0.writeAction("movir X16 12714")
    tran0.writeAction("slorii X16 X16 12 253")
    tran0.writeAction("slorii X16 X16 12 880")
    tran0.writeAction("slorii X16 X16 12 1269")
    tran0.writeAction("slorii X16 X16 12 3529")
    tran0.writeAction("sraddii X16 X17 6 1163")
    tran0.writeAction("yieldt")
    return efa
