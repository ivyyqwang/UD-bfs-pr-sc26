from EFA_v2 import *
def fsqrt_64_22():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [15288517804583829640]
    tran0.writeAction("movir X16 54315")
    tran0.writeAction("slorii X16 X16 12 2975")
    tran0.writeAction("slorii X16 X16 12 244")
    tran0.writeAction("slorii X16 X16 12 1860")
    tran0.writeAction("slorii X16 X16 12 136")
    tran0.writeAction("fsqrt.64 X16 X17")
    tran0.writeAction("yieldt")
    return efa
