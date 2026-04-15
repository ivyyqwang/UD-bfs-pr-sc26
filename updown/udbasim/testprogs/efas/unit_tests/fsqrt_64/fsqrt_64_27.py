from EFA_v2 import *
def fsqrt_64_27():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [9406938859080074874]
    tran0.writeAction("movir X16 33420")
    tran0.writeAction("slorii X16 X16 12 656")
    tran0.writeAction("slorii X16 X16 12 3423")
    tran0.writeAction("slorii X16 X16 12 1172")
    tran0.writeAction("slorii X16 X16 12 1658")
    tran0.writeAction("fsqrt.64 X16 X17")
    tran0.writeAction("yieldt")
    return efa
