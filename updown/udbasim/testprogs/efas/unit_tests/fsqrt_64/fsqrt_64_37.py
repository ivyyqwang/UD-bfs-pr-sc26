from EFA_v2 import *
def fsqrt_64_37():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [9105514314317953505]
    tran0.writeAction("movir X16 32349")
    tran0.writeAction("slorii X16 X16 12 1168")
    tran0.writeAction("slorii X16 X16 12 1690")
    tran0.writeAction("slorii X16 X16 12 639")
    tran0.writeAction("slorii X16 X16 12 2529")
    tran0.writeAction("fsqrt.64 X16 X17")
    tran0.writeAction("yieldt")
    return efa
