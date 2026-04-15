from EFA_v2 import *
def fcnvt_64_i64_13():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6482352586510210655]
    tran0.writeAction("movir X16 23029")
    tran0.writeAction("slorii X16 X16 12 3861")
    tran0.writeAction("slorii X16 X16 12 1307")
    tran0.writeAction("slorii X16 X16 12 3177")
    tran0.writeAction("slorii X16 X16 12 1631")
    tran0.writeAction("fcnvt.64.i64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
