from EFA_v2 import *
def fadd_64_27():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [10584813609700018128, 16293544193514833737]
    tran0.writeAction("movir X16 37604")
    tran0.writeAction("slorii X16 X16 12 3326")
    tran0.writeAction("slorii X16 X16 12 1459")
    tran0.writeAction("slorii X16 X16 12 3644")
    tran0.writeAction("slorii X16 X16 12 2000")
    tran0.writeAction("movir X17 57886")
    tran0.writeAction("slorii X17 X17 12 1217")
    tran0.writeAction("slorii X17 X17 12 3578")
    tran0.writeAction("slorii X17 X17 12 2376")
    tran0.writeAction("slorii X17 X17 12 1865")
    tran0.writeAction("fadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
