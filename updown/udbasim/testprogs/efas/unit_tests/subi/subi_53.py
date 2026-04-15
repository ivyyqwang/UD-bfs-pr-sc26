from EFA_v2 import *
def subi_53():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1112119372218230400, -31988]
    tran0.writeAction("movir X16 3951")
    tran0.writeAction("slorii X16 X16 12 170")
    tran0.writeAction("slorii X16 X16 12 3392")
    tran0.writeAction("slorii X16 X16 12 3678")
    tran0.writeAction("slorii X16 X16 12 1664")
    tran0.writeAction("subi X16 X17 -31988")
    tran0.writeAction("yieldt")
    return efa
