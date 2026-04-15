from EFA_v2 import *
def fdiv_64_24():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [14744420920230874035, 8120233638853676172]
    tran0.writeAction("movir X16 52382")
    tran0.writeAction("slorii X16 X16 12 2891")
    tran0.writeAction("slorii X16 X16 12 1321")
    tran0.writeAction("slorii X16 X16 12 816")
    tran0.writeAction("slorii X16 X16 12 2995")
    tran0.writeAction("movir X17 28848")
    tran0.writeAction("slorii X17 X17 12 3543")
    tran0.writeAction("slorii X17 X17 12 2241")
    tran0.writeAction("slorii X17 X17 12 208")
    tran0.writeAction("slorii X17 X17 12 3212")
    tran0.writeAction("fdiv.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
