from EFA_v2 import *
def hash_8():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3202066693242419448, -3949919018193675827]
    tran0.writeAction("movir X16 11376")
    tran0.writeAction("slorii X16 X16 12 107")
    tran0.writeAction("slorii X16 X16 12 309")
    tran0.writeAction("slorii X16 X16 12 3375")
    tran0.writeAction("slorii X16 X16 12 2296")
    tran0.writeAction("movir X17 51503")
    tran0.writeAction("slorii X17 X17 12 281")
    tran0.writeAction("slorii X17 X17 12 1181")
    tran0.writeAction("slorii X17 X17 12 25")
    tran0.writeAction("slorii X17 X17 12 2509")
    tran0.writeAction("hash X16 X17")
    tran0.writeAction("yieldt")
    return efa
