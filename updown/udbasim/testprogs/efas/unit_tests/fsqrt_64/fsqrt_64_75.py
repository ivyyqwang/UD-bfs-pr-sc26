from EFA_v2 import *
def fsqrt_64_75():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [16451414658382523939]
    tran0.writeAction("movir X16 58447")
    tran0.writeAction("slorii X16 X16 12 679")
    tran0.writeAction("slorii X16 X16 12 2029")
    tran0.writeAction("slorii X16 X16 12 2230")
    tran0.writeAction("slorii X16 X16 12 3619")
    tran0.writeAction("fsqrt.64 X16 X17")
    tran0.writeAction("yieldt")
    return efa
