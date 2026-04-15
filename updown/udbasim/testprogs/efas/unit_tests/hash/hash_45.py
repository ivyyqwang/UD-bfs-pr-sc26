from EFA_v2 import *
def hash_45():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4756897353326091137, -5003222303485985722]
    tran0.writeAction("movir X16 16899")
    tran0.writeAction("slorii X16 X16 12 3663")
    tran0.writeAction("slorii X16 X16 12 145")
    tran0.writeAction("slorii X16 X16 12 4085")
    tran0.writeAction("slorii X16 X16 12 2945")
    tran0.writeAction("movir X17 47760")
    tran0.writeAction("slorii X17 X17 12 4029")
    tran0.writeAction("slorii X17 X17 12 700")
    tran0.writeAction("slorii X17 X17 12 1663")
    tran0.writeAction("slorii X17 X17 12 3142")
    tran0.writeAction("hash X16 X17")
    tran0.writeAction("yieldt")
    return efa
