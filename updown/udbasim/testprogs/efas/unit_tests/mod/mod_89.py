from EFA_v2 import *
def mod_89():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8519148047737256166, -8108509761142973555]
    tran0.writeAction("movir X16 30266")
    tran0.writeAction("slorii X16 X16 12 384")
    tran0.writeAction("slorii X16 X16 12 854")
    tran0.writeAction("slorii X16 X16 12 1399")
    tran0.writeAction("slorii X16 X16 12 2278")
    tran0.writeAction("movir X17 36728")
    tran0.writeAction("slorii X17 X17 12 3221")
    tran0.writeAction("slorii X17 X17 12 1341")
    tran0.writeAction("slorii X17 X17 12 1169")
    tran0.writeAction("slorii X17 X17 12 2957")
    tran0.writeAction("mod X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
