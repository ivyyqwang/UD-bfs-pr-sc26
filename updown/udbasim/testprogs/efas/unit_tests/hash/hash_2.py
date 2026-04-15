from EFA_v2 import *
def hash_2():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5254615230980312373, -5056698563261581626]
    tran0.writeAction("movir X16 18668")
    tran0.writeAction("slorii X16 X16 12 587")
    tran0.writeAction("slorii X16 X16 12 1633")
    tran0.writeAction("slorii X16 X16 12 3844")
    tran0.writeAction("slorii X16 X16 12 3381")
    tran0.writeAction("movir X17 47570")
    tran0.writeAction("slorii X17 X17 12 4087")
    tran0.writeAction("slorii X17 X17 12 704")
    tran0.writeAction("slorii X17 X17 12 2315")
    tran0.writeAction("slorii X17 X17 12 1734")
    tran0.writeAction("hash X16 X17")
    tran0.writeAction("yieldt")
    return efa
