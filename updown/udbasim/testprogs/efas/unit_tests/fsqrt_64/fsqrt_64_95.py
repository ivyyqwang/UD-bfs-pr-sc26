from EFA_v2 import *
def fsqrt_64_95():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [13295899261290245190]
    tran0.writeAction("movir X16 47236")
    tran0.writeAction("slorii X16 X16 12 2142")
    tran0.writeAction("slorii X16 X16 12 3830")
    tran0.writeAction("slorii X16 X16 12 2390")
    tran0.writeAction("slorii X16 X16 12 3142")
    tran0.writeAction("fsqrt.64 X16 X17")
    tran0.writeAction("yieldt")
    return efa
