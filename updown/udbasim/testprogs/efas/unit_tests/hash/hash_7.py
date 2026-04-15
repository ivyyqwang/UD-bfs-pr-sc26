from EFA_v2 import *
def hash_7():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [426096704647837703, -1038854624402496499]
    tran0.writeAction("movir X16 1513")
    tran0.writeAction("slorii X16 X16 12 3275")
    tran0.writeAction("slorii X16 X16 12 512")
    tran0.writeAction("slorii X16 X16 12 2043")
    tran0.writeAction("slorii X16 X16 12 2055")
    tran0.writeAction("movir X17 61845")
    tran0.writeAction("slorii X17 X17 12 1011")
    tran0.writeAction("slorii X17 X17 12 2339")
    tran0.writeAction("slorii X17 X17 12 890")
    tran0.writeAction("slorii X17 X17 12 1037")
    tran0.writeAction("hash X16 X17")
    tran0.writeAction("yieldt")
    return efa
