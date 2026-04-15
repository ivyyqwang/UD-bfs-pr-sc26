from EFA_v2 import *
def fadd_64_81():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [16691919089309886553, 13850678776171952991]
    tran0.writeAction("movir X16 59301")
    tran0.writeAction("slorii X16 X16 12 2495")
    tran0.writeAction("slorii X16 X16 12 2401")
    tran0.writeAction("slorii X16 X16 12 3594")
    tran0.writeAction("slorii X16 X16 12 2137")
    tran0.writeAction("movir X17 49207")
    tran0.writeAction("slorii X17 X17 12 2031")
    tran0.writeAction("slorii X17 X17 12 1663")
    tran0.writeAction("slorii X17 X17 12 3159")
    tran0.writeAction("slorii X17 X17 12 2911")
    tran0.writeAction("fadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
