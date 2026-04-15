from EFA_v2 import *
def fcnvt_i64_64_59():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6545941303084715399]
    tran0.writeAction("movir X16 23255")
    tran0.writeAction("slorii X16 X16 12 3502")
    tran0.writeAction("slorii X16 X16 12 3818")
    tran0.writeAction("slorii X16 X16 12 3776")
    tran0.writeAction("slorii X16 X16 12 3463")
    tran0.writeAction("fcnvt.i64.64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
