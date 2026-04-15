from EFA_v2 import *
def fdiv_64_37():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8582278972154486711, 14320694347626636777]
    tran0.writeAction("movir X16 30490")
    tran0.writeAction("slorii X16 X16 12 1556")
    tran0.writeAction("slorii X16 X16 12 282")
    tran0.writeAction("slorii X16 X16 12 2345")
    tran0.writeAction("slorii X16 X16 12 4023")
    tran0.writeAction("movir X17 50877")
    tran0.writeAction("slorii X17 X17 12 1338")
    tran0.writeAction("slorii X17 X17 12 647")
    tran0.writeAction("slorii X17 X17 12 942")
    tran0.writeAction("slorii X17 X17 12 1513")
    tran0.writeAction("fdiv.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
