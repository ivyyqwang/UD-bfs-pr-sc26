from EFA_v2 import *
def fcnvt_i64_64_54():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-4855956353656718627]
    tran0.writeAction("movir X16 48284")
    tran0.writeAction("slorii X16 X16 12 726")
    tran0.writeAction("slorii X16 X16 12 3231")
    tran0.writeAction("slorii X16 X16 12 2007")
    tran0.writeAction("slorii X16 X16 12 2781")
    tran0.writeAction("fcnvt.i64.64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
