from EFA_v2 import *
def fsqrt_64_11():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [13533415360036192709]
    tran0.writeAction("movir X16 48080")
    tran0.writeAction("slorii X16 X16 12 1433")
    tran0.writeAction("slorii X16 X16 12 284")
    tran0.writeAction("slorii X16 X16 12 3164")
    tran0.writeAction("slorii X16 X16 12 453")
    tran0.writeAction("fsqrt.64 X16 X17")
    tran0.writeAction("yieldt")
    return efa
