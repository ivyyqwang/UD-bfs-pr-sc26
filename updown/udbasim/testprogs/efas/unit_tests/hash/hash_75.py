from EFA_v2 import *
def hash_75():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7490761560191511731, -9205359120782117311]
    tran0.writeAction("movir X16 26612")
    tran0.writeAction("slorii X16 X16 12 2175")
    tran0.writeAction("slorii X16 X16 12 900")
    tran0.writeAction("slorii X16 X16 12 1498")
    tran0.writeAction("slorii X16 X16 12 3251")
    tran0.writeAction("movir X17 32831")
    tran0.writeAction("slorii X17 X17 12 4074")
    tran0.writeAction("slorii X17 X17 12 1751")
    tran0.writeAction("slorii X17 X17 12 3603")
    tran0.writeAction("slorii X17 X17 12 1601")
    tran0.writeAction("hash X16 X17")
    tran0.writeAction("yieldt")
    return efa
