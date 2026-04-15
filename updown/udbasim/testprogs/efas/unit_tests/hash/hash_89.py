from EFA_v2 import *
def hash_89():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-2073489944272948346, 1944970884476885574]
    tran0.writeAction("movir X16 58169")
    tran0.writeAction("slorii X16 X16 12 1982")
    tran0.writeAction("slorii X16 X16 12 426")
    tran0.writeAction("slorii X16 X16 12 1091")
    tran0.writeAction("slorii X16 X16 12 902")
    tran0.writeAction("movir X17 6909")
    tran0.writeAction("slorii X17 X17 12 3787")
    tran0.writeAction("slorii X17 X17 12 1771")
    tran0.writeAction("slorii X17 X17 12 2957")
    tran0.writeAction("slorii X17 X17 12 2630")
    tran0.writeAction("hash X16 X17")
    tran0.writeAction("yieldt")
    return efa
