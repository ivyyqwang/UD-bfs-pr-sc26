from EFA_v2 import *
def mod_71():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-5661966696672024312, 8465287820703791475]
    tran0.writeAction("movir X16 45420")
    tran0.writeAction("slorii X16 X16 12 2676")
    tran0.writeAction("slorii X16 X16 12 2474")
    tran0.writeAction("slorii X16 X16 12 3162")
    tran0.writeAction("slorii X16 X16 12 2312")
    tran0.writeAction("movir X17 30074")
    tran0.writeAction("slorii X17 X17 12 3046")
    tran0.writeAction("slorii X17 X17 12 3074")
    tran0.writeAction("slorii X17 X17 12 2007")
    tran0.writeAction("slorii X17 X17 12 2419")
    tran0.writeAction("mod X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
