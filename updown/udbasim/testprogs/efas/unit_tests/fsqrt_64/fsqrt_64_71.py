from EFA_v2 import *
def fsqrt_64_71():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [16777527555784783266]
    tran0.writeAction("movir X16 59605")
    tran0.writeAction("slorii X16 X16 12 3078")
    tran0.writeAction("slorii X16 X16 12 3003")
    tran0.writeAction("slorii X16 X16 12 3603")
    tran0.writeAction("slorii X16 X16 12 1442")
    tran0.writeAction("fsqrt.64 X16 X17")
    tran0.writeAction("yieldt")
    return efa
