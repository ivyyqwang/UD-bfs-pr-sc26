from EFA_v2 import *
def fsqrt_64_1():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [13810493415693490391]
    tran0.writeAction("movir X16 49064")
    tran0.writeAction("slorii X16 X16 12 2985")
    tran0.writeAction("slorii X16 X16 12 1831")
    tran0.writeAction("slorii X16 X16 12 1153")
    tran0.writeAction("slorii X16 X16 12 2263")
    tran0.writeAction("fsqrt.64 X16 X17")
    tran0.writeAction("yieldt")
    return efa
