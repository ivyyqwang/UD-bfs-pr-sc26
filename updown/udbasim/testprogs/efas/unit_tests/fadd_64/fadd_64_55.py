from EFA_v2 import *
def fadd_64_55():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [16457568148036794347, 13681996844334450361]
    tran0.writeAction("movir X16 58469")
    tran0.writeAction("slorii X16 X16 12 112")
    tran0.writeAction("slorii X16 X16 12 2274")
    tran0.writeAction("slorii X16 X16 12 2115")
    tran0.writeAction("slorii X16 X16 12 2027")
    tran0.writeAction("movir X17 48608")
    tran0.writeAction("slorii X17 X17 12 890")
    tran0.writeAction("slorii X17 X17 12 956")
    tran0.writeAction("slorii X17 X17 12 2336")
    tran0.writeAction("slorii X17 X17 12 1721")
    tran0.writeAction("fadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
