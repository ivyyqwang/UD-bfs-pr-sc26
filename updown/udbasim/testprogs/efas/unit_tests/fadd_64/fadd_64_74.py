from EFA_v2 import *
def fadd_64_74():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [10867937169079889709, 11484430137198677889]
    tran0.writeAction("movir X16 38610")
    tran0.writeAction("slorii X16 X16 12 2740")
    tran0.writeAction("slorii X16 X16 12 1604")
    tran0.writeAction("slorii X16 X16 12 1110")
    tran0.writeAction("slorii X16 X16 12 3885")
    tran0.writeAction("movir X17 40800")
    tran0.writeAction("slorii X17 X17 12 3653")
    tran0.writeAction("slorii X17 X17 12 3287")
    tran0.writeAction("slorii X17 X17 12 2120")
    tran0.writeAction("slorii X17 X17 12 3969")
    tran0.writeAction("fadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
