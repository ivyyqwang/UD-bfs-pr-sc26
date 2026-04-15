from EFA_v2 import *
def hash_11():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-2976489815084337134, 8350448635770873936]
    tran0.writeAction("movir X16 54961")
    tran0.writeAction("slorii X16 X16 12 1572")
    tran0.writeAction("slorii X16 X16 12 2182")
    tran0.writeAction("slorii X16 X16 12 1351")
    tran0.writeAction("slorii X16 X16 12 2066")
    tran0.writeAction("movir X17 29666")
    tran0.writeAction("slorii X17 X17 12 3084")
    tran0.writeAction("slorii X17 X17 12 2730")
    tran0.writeAction("slorii X17 X17 12 1098")
    tran0.writeAction("slorii X17 X17 12 2128")
    tran0.writeAction("hash X16 X17")
    tran0.writeAction("yieldt")
    return efa
