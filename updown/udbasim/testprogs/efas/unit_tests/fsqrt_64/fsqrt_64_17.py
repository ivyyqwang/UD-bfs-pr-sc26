from EFA_v2 import *
def fsqrt_64_17():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [11535598816569979279]
    tran0.writeAction("movir X16 40982")
    tran0.writeAction("slorii X16 X16 12 2784")
    tran0.writeAction("slorii X16 X16 12 357")
    tran0.writeAction("slorii X16 X16 12 287")
    tran0.writeAction("slorii X16 X16 12 399")
    tran0.writeAction("fsqrt.64 X16 X17")
    tran0.writeAction("yieldt")
    return efa
