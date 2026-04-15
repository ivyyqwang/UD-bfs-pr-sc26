from EFA_v2 import *
def hash_87():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3770779273159690202, 3302779775298768136]
    tran0.writeAction("movir X16 13396")
    tran0.writeAction("slorii X16 X16 12 2044")
    tran0.writeAction("slorii X16 X16 12 1343")
    tran0.writeAction("slorii X16 X16 12 364")
    tran0.writeAction("slorii X16 X16 12 2010")
    tran0.writeAction("movir X17 11733")
    tran0.writeAction("slorii X17 X17 12 3403")
    tran0.writeAction("slorii X17 X17 12 1262")
    tran0.writeAction("slorii X17 X17 12 112")
    tran0.writeAction("slorii X17 X17 12 3336")
    tran0.writeAction("hash X16 X17")
    tran0.writeAction("yieldt")
    return efa
