from EFA_v2 import *
def fsqrt_64_14():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [9722375956988478498]
    tran0.writeAction("movir X16 34540")
    tran0.writeAction("slorii X16 X16 12 3350")
    tran0.writeAction("slorii X16 X16 12 3049")
    tran0.writeAction("slorii X16 X16 12 396")
    tran0.writeAction("slorii X16 X16 12 1058")
    tran0.writeAction("fsqrt.64 X16 X17")
    tran0.writeAction("yieldt")
    return efa
