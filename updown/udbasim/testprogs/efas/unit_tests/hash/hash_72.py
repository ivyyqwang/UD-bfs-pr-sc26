from EFA_v2 import *
def hash_72():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6761861233469544700, 2941743159178781579]
    tran0.writeAction("movir X16 24022")
    tran0.writeAction("slorii X16 X16 12 3919")
    tran0.writeAction("slorii X16 X16 12 1865")
    tran0.writeAction("slorii X16 X16 12 1789")
    tran0.writeAction("slorii X16 X16 12 2300")
    tran0.writeAction("movir X17 10451")
    tran0.writeAction("slorii X17 X17 12 701")
    tran0.writeAction("slorii X17 X17 12 311")
    tran0.writeAction("slorii X17 X17 12 1174")
    tran0.writeAction("slorii X17 X17 12 907")
    tran0.writeAction("hash X16 X17")
    tran0.writeAction("yieldt")
    return efa
