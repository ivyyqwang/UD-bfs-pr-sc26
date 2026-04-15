from EFA_v2 import *
def fcnvt_i64_64_66():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-4231382534994726985]
    tran0.writeAction("movir X16 50503")
    tran0.writeAction("slorii X16 X16 12 448")
    tran0.writeAction("slorii X16 X16 12 212")
    tran0.writeAction("slorii X16 X16 12 3470")
    tran0.writeAction("slorii X16 X16 12 4023")
    tran0.writeAction("fcnvt.i64.64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
