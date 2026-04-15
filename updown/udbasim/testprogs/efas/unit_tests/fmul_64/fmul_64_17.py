from EFA_v2 import *
def fmul_64_17():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [39380538793849226, 5441092222874508991]
    tran0.writeAction("movir X16 139")
    tran0.writeAction("slorii X16 X16 12 3718")
    tran0.writeAction("slorii X16 X16 12 1073")
    tran0.writeAction("slorii X16 X16 12 3567")
    tran0.writeAction("slorii X16 X16 12 394")
    tran0.writeAction("movir X17 19330")
    tran0.writeAction("slorii X17 X17 12 2632")
    tran0.writeAction("slorii X17 X17 12 3182")
    tran0.writeAction("slorii X17 X17 12 2357")
    tran0.writeAction("slorii X17 X17 12 3775")
    tran0.writeAction("fmul.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
