from EFA_v2 import *
def hash_39():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3149839568727438624, 5332155855647640978]
    tran0.writeAction("movir X16 11190")
    tran0.writeAction("slorii X16 X16 12 1958")
    tran0.writeAction("slorii X16 X16 12 1585")
    tran0.writeAction("slorii X16 X16 12 1919")
    tran0.writeAction("slorii X16 X16 12 1312")
    tran0.writeAction("movir X17 18943")
    tran0.writeAction("slorii X17 X17 12 2551")
    tran0.writeAction("slorii X17 X17 12 4078")
    tran0.writeAction("slorii X17 X17 12 3672")
    tran0.writeAction("slorii X17 X17 12 3474")
    tran0.writeAction("hash X16 X17")
    tran0.writeAction("yieldt")
    return efa
