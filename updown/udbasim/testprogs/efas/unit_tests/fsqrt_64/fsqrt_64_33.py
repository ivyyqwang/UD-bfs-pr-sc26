from EFA_v2 import *
def fsqrt_64_33():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [9304535541384726950]
    tran0.writeAction("movir X16 33056")
    tran0.writeAction("slorii X16 X16 12 1436")
    tran0.writeAction("slorii X16 X16 12 1792")
    tran0.writeAction("slorii X16 X16 12 956")
    tran0.writeAction("slorii X16 X16 12 2470")
    tran0.writeAction("fsqrt.64 X16 X17")
    tran0.writeAction("yieldt")
    return efa
