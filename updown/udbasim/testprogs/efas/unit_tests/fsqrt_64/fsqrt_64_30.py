from EFA_v2 import *
def fsqrt_64_30():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [553045544942292147]
    tran0.writeAction("movir X16 1964")
    tran0.writeAction("slorii X16 X16 12 3327")
    tran0.writeAction("slorii X16 X16 12 3634")
    tran0.writeAction("slorii X16 X16 12 3676")
    tran0.writeAction("slorii X16 X16 12 3251")
    tran0.writeAction("fsqrt.64 X16 X17")
    tran0.writeAction("yieldt")
    return efa
