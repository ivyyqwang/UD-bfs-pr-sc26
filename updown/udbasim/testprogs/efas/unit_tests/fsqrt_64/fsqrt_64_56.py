from EFA_v2 import *
def fsqrt_64_56():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1866372111077219292]
    tran0.writeAction("movir X16 6630")
    tran0.writeAction("slorii X16 X16 12 2808")
    tran0.writeAction("slorii X16 X16 12 3051")
    tran0.writeAction("slorii X16 X16 12 1857")
    tran0.writeAction("slorii X16 X16 12 3036")
    tran0.writeAction("fsqrt.64 X16 X17")
    tran0.writeAction("yieldt")
    return efa
