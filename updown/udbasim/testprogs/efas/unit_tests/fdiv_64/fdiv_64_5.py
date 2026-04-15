from EFA_v2 import *
def fdiv_64_5():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [10150077757724381041, 10576364691798752649]
    tran0.writeAction("movir X16 36060")
    tran0.writeAction("slorii X16 X16 12 1311")
    tran0.writeAction("slorii X16 X16 12 375")
    tran0.writeAction("slorii X16 X16 12 3092")
    tran0.writeAction("slorii X16 X16 12 3953")
    tran0.writeAction("movir X17 37574")
    tran0.writeAction("slorii X17 X17 12 3258")
    tran0.writeAction("slorii X17 X17 12 1717")
    tran0.writeAction("slorii X17 X17 12 2655")
    tran0.writeAction("slorii X17 X17 12 3465")
    tran0.writeAction("fdiv.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
