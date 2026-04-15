from EFA_v2 import *
def fsqrt_64_82():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [11890065272522359370]
    tran0.writeAction("movir X16 42241")
    tran0.writeAction("slorii X16 X16 12 4085")
    tran0.writeAction("slorii X16 X16 12 3708")
    tran0.writeAction("slorii X16 X16 12 3700")
    tran0.writeAction("slorii X16 X16 12 586")
    tran0.writeAction("fsqrt.64 X16 X17")
    tran0.writeAction("yieldt")
    return efa
