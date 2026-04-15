from EFA_v2 import *
def hash_78():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-3523506027413459080, -7116988543408165386]
    tran0.writeAction("movir X16 53017")
    tran0.writeAction("slorii X16 X16 12 4062")
    tran0.writeAction("slorii X16 X16 12 4024")
    tran0.writeAction("slorii X16 X16 12 298")
    tran0.writeAction("slorii X16 X16 12 3960")
    tran0.writeAction("movir X17 40251")
    tran0.writeAction("slorii X17 X17 12 1546")
    tran0.writeAction("slorii X17 X17 12 143")
    tran0.writeAction("slorii X17 X17 12 2586")
    tran0.writeAction("slorii X17 X17 12 3574")
    tran0.writeAction("hash X16 X17")
    tran0.writeAction("yieldt")
    return efa
