from EFA_v2 import *
def fsqrt_64_42():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [16589331610589430870]
    tran0.writeAction("movir X16 58937")
    tran0.writeAction("slorii X16 X16 12 595")
    tran0.writeAction("slorii X16 X16 12 1198")
    tran0.writeAction("slorii X16 X16 12 1400")
    tran0.writeAction("slorii X16 X16 12 1110")
    tran0.writeAction("fsqrt.64 X16 X17")
    tran0.writeAction("yieldt")
    return efa
