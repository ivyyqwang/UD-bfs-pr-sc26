from EFA_v2 import *
def fcnvt_64_i64_44():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3938119180014317074]
    tran0.writeAction("movir X16 13991")
    tran0.writeAction("slorii X16 X16 12 40")
    tran0.writeAction("slorii X16 X16 12 1911")
    tran0.writeAction("slorii X16 X16 12 3710")
    tran0.writeAction("slorii X16 X16 12 3602")
    tran0.writeAction("fcnvt.64.i64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
