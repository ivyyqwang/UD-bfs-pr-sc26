from EFA_v2 import *
def fadd_32_41():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1889542100, 2472005498]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 112")
    tran0.writeAction("slorii X16 X16 12 2561")
    tran0.writeAction("slorii X16 X16 12 4052")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 147")
    tran0.writeAction("slorii X17 X17 12 1404")
    tran0.writeAction("slorii X17 X17 12 3962")
    tran0.writeAction("fadd.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
