from EFA_v2 import *
def fsqrt_64_74():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [16841066681903506772]
    tran0.writeAction("movir X16 59831")
    tran0.writeAction("slorii X16 X16 12 1998")
    tran0.writeAction("slorii X16 X16 12 2909")
    tran0.writeAction("slorii X16 X16 12 2150")
    tran0.writeAction("slorii X16 X16 12 1364")
    tran0.writeAction("fsqrt.64 X16 X17")
    tran0.writeAction("yieldt")
    return efa
