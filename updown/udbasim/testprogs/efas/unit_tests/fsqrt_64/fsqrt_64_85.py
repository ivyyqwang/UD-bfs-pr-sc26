from EFA_v2 import *
def fsqrt_64_85():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [10429691881552274130]
    tran0.writeAction("movir X16 37053")
    tran0.writeAction("slorii X16 X16 12 2904")
    tran0.writeAction("slorii X16 X16 12 484")
    tran0.writeAction("slorii X16 X16 12 2862")
    tran0.writeAction("slorii X16 X16 12 722")
    tran0.writeAction("fsqrt.64 X16 X17")
    tran0.writeAction("yieldt")
    return efa
