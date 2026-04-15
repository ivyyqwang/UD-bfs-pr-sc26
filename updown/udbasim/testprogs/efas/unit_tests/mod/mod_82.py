from EFA_v2 import *
def mod_82():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4622351568602216674, 8888207117038692474]
    tran0.writeAction("movir X16 16421")
    tran0.writeAction("slorii X16 X16 12 3652")
    tran0.writeAction("slorii X16 X16 12 745")
    tran0.writeAction("slorii X16 X16 12 2067")
    tran0.writeAction("slorii X16 X16 12 2274")
    tran0.writeAction("movir X17 31577")
    tran0.writeAction("slorii X17 X17 12 1044")
    tran0.writeAction("slorii X17 X17 12 2045")
    tran0.writeAction("slorii X17 X17 12 778")
    tran0.writeAction("slorii X17 X17 12 2170")
    tran0.writeAction("mod X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
