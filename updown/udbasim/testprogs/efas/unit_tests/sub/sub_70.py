from EFA_v2 import *
def sub_70():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6934937925643546174, -7473512754172524133]
    tran0.writeAction("movir X16 24637")
    tran0.writeAction("slorii X16 X16 12 3476")
    tran0.writeAction("slorii X16 X16 12 3309")
    tran0.writeAction("slorii X16 X16 12 1506")
    tran0.writeAction("slorii X16 X16 12 3646")
    tran0.writeAction("movir X17 38984")
    tran0.writeAction("slorii X17 X17 12 3067")
    tran0.writeAction("slorii X17 X17 12 3863")
    tran0.writeAction("slorii X17 X17 12 800")
    tran0.writeAction("slorii X17 X17 12 2459")
    tran0.writeAction("sub X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
