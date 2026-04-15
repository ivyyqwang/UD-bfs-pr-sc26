from EFA_v2 import *
def hash_65():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8151116113009420317, 2166870524242880776]
    tran0.writeAction("movir X16 28958")
    tran0.writeAction("slorii X16 X16 12 2382")
    tran0.writeAction("slorii X16 X16 12 2838")
    tran0.writeAction("slorii X16 X16 12 3642")
    tran0.writeAction("slorii X16 X16 12 2077")
    tran0.writeAction("movir X17 7698")
    tran0.writeAction("slorii X17 X17 12 1108")
    tran0.writeAction("slorii X17 X17 12 735")
    tran0.writeAction("slorii X17 X17 12 3118")
    tran0.writeAction("slorii X17 X17 12 2312")
    tran0.writeAction("hash X16 X17")
    tran0.writeAction("yieldt")
    return efa
