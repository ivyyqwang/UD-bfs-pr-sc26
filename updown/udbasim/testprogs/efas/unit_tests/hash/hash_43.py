from EFA_v2 import *
def hash_43():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-5750955659518548460, 6933033854768220389]
    tran0.writeAction("movir X16 45104")
    tran0.writeAction("slorii X16 X16 12 2052")
    tran0.writeAction("slorii X16 X16 12 3115")
    tran0.writeAction("slorii X16 X16 12 1534")
    tran0.writeAction("slorii X16 X16 12 1556")
    tran0.writeAction("movir X17 24631")
    tran0.writeAction("slorii X17 X17 12 344")
    tran0.writeAction("slorii X17 X17 12 3809")
    tran0.writeAction("slorii X17 X17 12 888")
    tran0.writeAction("slorii X17 X17 12 2277")
    tran0.writeAction("hash X16 X17")
    tran0.writeAction("yieldt")
    return efa
