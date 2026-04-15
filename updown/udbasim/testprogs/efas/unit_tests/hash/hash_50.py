from EFA_v2 import *
def hash_50():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-871388192805404201, -4859672068982346646]
    tran0.writeAction("movir X16 62440")
    tran0.writeAction("slorii X16 X16 12 848")
    tran0.writeAction("slorii X16 X16 12 3634")
    tran0.writeAction("slorii X16 X16 12 1492")
    tran0.writeAction("slorii X16 X16 12 471")
    tran0.writeAction("movir X17 48270")
    tran0.writeAction("slorii X17 X17 12 4000")
    tran0.writeAction("slorii X17 X17 12 59")
    tran0.writeAction("slorii X17 X17 12 1718")
    tran0.writeAction("slorii X17 X17 12 3178")
    tran0.writeAction("hash X16 X17")
    tran0.writeAction("yieldt")
    return efa
