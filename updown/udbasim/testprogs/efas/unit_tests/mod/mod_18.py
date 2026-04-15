from EFA_v2 import *
def mod_18():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1399580494234616200, -4701821858501116702]
    tran0.writeAction("movir X16 60563")
    tran0.writeAction("slorii X16 X16 12 2831")
    tran0.writeAction("slorii X16 X16 12 1198")
    tran0.writeAction("slorii X16 X16 12 2375")
    tran0.writeAction("slorii X16 X16 12 3704")
    tran0.writeAction("movir X17 48831")
    tran0.writeAction("slorii X17 X17 12 3166")
    tran0.writeAction("slorii X17 X17 12 3670")
    tran0.writeAction("slorii X17 X17 12 3579")
    tran0.writeAction("slorii X17 X17 12 3298")
    tran0.writeAction("mod X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
