from EFA_v2 import *
def fsqrt_64_35():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [14787701283791609036]
    tran0.writeAction("movir X16 52536")
    tran0.writeAction("slorii X16 X16 12 1919")
    tran0.writeAction("slorii X16 X16 12 2064")
    tran0.writeAction("slorii X16 X16 12 4041")
    tran0.writeAction("slorii X16 X16 12 3276")
    tran0.writeAction("fsqrt.64 X16 X17")
    tran0.writeAction("yieldt")
    return efa
