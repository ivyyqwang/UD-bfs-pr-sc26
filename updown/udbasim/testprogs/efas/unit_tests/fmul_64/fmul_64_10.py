from EFA_v2 import *
def fmul_64_10():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4045422644534516065, 5802090506667964707]
    tran0.writeAction("movir X16 14372")
    tran0.writeAction("slorii X16 X16 12 935")
    tran0.writeAction("slorii X16 X16 12 1581")
    tran0.writeAction("slorii X16 X16 12 3281")
    tran0.writeAction("slorii X16 X16 12 2401")
    tran0.writeAction("movir X17 20613")
    tran0.writeAction("slorii X17 X17 12 681")
    tran0.writeAction("slorii X17 X17 12 820")
    tran0.writeAction("slorii X17 X17 12 2499")
    tran0.writeAction("slorii X17 X17 12 2339")
    tran0.writeAction("fmul.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
