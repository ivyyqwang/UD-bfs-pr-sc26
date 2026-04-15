from EFA_v2 import *
def fsqrt_64_98():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [13136100769559841144]
    tran0.writeAction("movir X16 46668")
    tran0.writeAction("slorii X16 X16 12 3296")
    tran0.writeAction("slorii X16 X16 12 3399")
    tran0.writeAction("slorii X16 X16 12 1432")
    tran0.writeAction("slorii X16 X16 12 2424")
    tran0.writeAction("fsqrt.64 X16 X17")
    tran0.writeAction("yieldt")
    return efa
