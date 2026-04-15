from EFA_v2 import *
def fdiv_64_35():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1523945829680257382, 14796214738509128849]
    tran0.writeAction("movir X16 5414")
    tran0.writeAction("slorii X16 X16 12 586")
    tran0.writeAction("slorii X16 X16 12 2155")
    tran0.writeAction("slorii X16 X16 12 121")
    tran0.writeAction("slorii X16 X16 12 2406")
    tran0.writeAction("movir X17 52566")
    tran0.writeAction("slorii X17 X17 12 2926")
    tran0.writeAction("slorii X17 X17 12 2357")
    tran0.writeAction("slorii X17 X17 12 966")
    tran0.writeAction("slorii X17 X17 12 1169")
    tran0.writeAction("fdiv.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
