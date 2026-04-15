from EFA_v2 import *
def fcnvt_64_i64_11():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [13853959552802589237]
    tran0.writeAction("movir X16 49219")
    tran0.writeAction("slorii X16 X16 12 620")
    tran0.writeAction("slorii X16 X16 12 4053")
    tran0.writeAction("slorii X16 X16 12 1752")
    tran0.writeAction("slorii X16 X16 12 2613")
    tran0.writeAction("fcnvt.64.i64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
