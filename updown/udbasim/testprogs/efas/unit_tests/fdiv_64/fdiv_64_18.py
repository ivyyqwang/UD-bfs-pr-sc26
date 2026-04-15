from EFA_v2 import *
def fdiv_64_18():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3251689110861086446, 3968701818637341423]
    tran0.writeAction("movir X16 11552")
    tran0.writeAction("slorii X16 X16 12 1312")
    tran0.writeAction("slorii X16 X16 12 1188")
    tran0.writeAction("slorii X16 X16 12 3607")
    tran0.writeAction("slorii X16 X16 12 3822")
    tran0.writeAction("movir X17 14099")
    tran0.writeAction("slorii X17 X17 12 2708")
    tran0.writeAction("slorii X17 X17 12 1767")
    tran0.writeAction("slorii X17 X17 12 1333")
    tran0.writeAction("slorii X17 X17 12 751")
    tran0.writeAction("fdiv.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
