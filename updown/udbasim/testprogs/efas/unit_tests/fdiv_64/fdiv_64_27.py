from EFA_v2 import *
def fdiv_64_27():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4510315519317584108, 7268840107963680815]
    tran0.writeAction("movir X16 16023")
    tran0.writeAction("slorii X16 X16 12 3521")
    tran0.writeAction("slorii X16 X16 12 369")
    tran0.writeAction("slorii X16 X16 12 3506")
    tran0.writeAction("slorii X16 X16 12 2284")
    tran0.writeAction("movir X17 25824")
    tran0.writeAction("slorii X17 X17 12 441")
    tran0.writeAction("slorii X17 X17 12 244")
    tran0.writeAction("slorii X17 X17 12 1176")
    tran0.writeAction("slorii X17 X17 12 2095")
    tran0.writeAction("fdiv.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
