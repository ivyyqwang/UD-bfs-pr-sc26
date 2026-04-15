from EFA_v2 import *
def fadd_64_90():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4433939254342750674, 17021110978265420392]
    tran0.writeAction("movir X16 15752")
    tran0.writeAction("slorii X16 X16 12 2116")
    tran0.writeAction("slorii X16 X16 12 642")
    tran0.writeAction("slorii X16 X16 12 3113")
    tran0.writeAction("slorii X16 X16 12 466")
    tran0.writeAction("movir X17 60471")
    tran0.writeAction("slorii X17 X17 12 548")
    tran0.writeAction("slorii X17 X17 12 198")
    tran0.writeAction("slorii X17 X17 12 49")
    tran0.writeAction("slorii X17 X17 12 616")
    tran0.writeAction("fadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
