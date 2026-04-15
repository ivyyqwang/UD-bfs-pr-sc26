from EFA_v2 import *
def hash_66():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1570237054194179230, 5681351881689767314]
    tran0.writeAction("movir X16 5578")
    tran0.writeAction("slorii X16 X16 12 2468")
    tran0.writeAction("slorii X16 X16 12 2052")
    tran0.writeAction("slorii X16 X16 12 1637")
    tran0.writeAction("slorii X16 X16 12 3230")
    tran0.writeAction("movir X17 20184")
    tran0.writeAction("slorii X17 X17 12 886")
    tran0.writeAction("slorii X17 X17 12 3952")
    tran0.writeAction("slorii X17 X17 12 473")
    tran0.writeAction("slorii X17 X17 12 3474")
    tran0.writeAction("hash X16 X17")
    tran0.writeAction("yieldt")
    return efa
