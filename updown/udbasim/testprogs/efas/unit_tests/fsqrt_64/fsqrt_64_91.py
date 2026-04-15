from EFA_v2 import *
def fsqrt_64_91():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [9736851742525384421]
    tran0.writeAction("movir X16 34592")
    tran0.writeAction("slorii X16 X16 12 1009")
    tran0.writeAction("slorii X16 X16 12 607")
    tran0.writeAction("slorii X16 X16 12 3558")
    tran0.writeAction("slorii X16 X16 12 1765")
    tran0.writeAction("fsqrt.64 X16 X17")
    tran0.writeAction("yieldt")
    return efa
