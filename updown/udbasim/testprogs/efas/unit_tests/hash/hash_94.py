from EFA_v2 import *
def hash_94():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-3766531350328670516, -1833548495700956525]
    tran0.writeAction("movir X16 52154")
    tran0.writeAction("slorii X16 X16 12 2427")
    tran0.writeAction("slorii X16 X16 12 348")
    tran0.writeAction("slorii X16 X16 12 1176")
    tran0.writeAction("slorii X16 X16 12 1740")
    tran0.writeAction("movir X17 59021")
    tran0.writeAction("slorii X17 X17 12 3797")
    tran0.writeAction("slorii X17 X17 12 2963")
    tran0.writeAction("slorii X17 X17 12 1198")
    tran0.writeAction("slorii X17 X17 12 2707")
    tran0.writeAction("hash X16 X17")
    tran0.writeAction("yieldt")
    return efa
