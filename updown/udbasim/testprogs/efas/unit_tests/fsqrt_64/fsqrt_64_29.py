from EFA_v2 import *
def fsqrt_64_29():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [15860431408267241857]
    tran0.writeAction("movir X16 56347")
    tran0.writeAction("slorii X16 X16 12 2341")
    tran0.writeAction("slorii X16 X16 12 1386")
    tran0.writeAction("slorii X16 X16 12 890")
    tran0.writeAction("slorii X16 X16 12 2433")
    tran0.writeAction("fsqrt.64 X16 X17")
    tran0.writeAction("yieldt")
    return efa
