from EFA_v2 import *
def fdiv_64_32():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5592791000361166095, 279746064899869952]
    tran0.writeAction("movir X16 19869")
    tran0.writeAction("slorii X16 X16 12 2396")
    tran0.writeAction("slorii X16 X16 12 2159")
    tran0.writeAction("slorii X16 X16 12 2166")
    tran0.writeAction("slorii X16 X16 12 1295")
    tran0.writeAction("movir X17 993")
    tran0.writeAction("slorii X17 X17 12 3513")
    tran0.writeAction("slorii X17 X17 12 89")
    tran0.writeAction("slorii X17 X17 12 2744")
    tran0.writeAction("slorii X17 X17 12 3328")
    tran0.writeAction("fdiv.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
