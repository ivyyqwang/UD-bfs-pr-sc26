from EFA_v2 import *
def fcnvt_64_i64_59():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [570811870148690827]
    tran0.writeAction("movir X16 2027")
    tran0.writeAction("slorii X16 X16 12 3813")
    tran0.writeAction("slorii X16 X16 12 3873")
    tran0.writeAction("slorii X16 X16 12 3232")
    tran0.writeAction("slorii X16 X16 12 907")
    tran0.writeAction("fcnvt.64.i64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
