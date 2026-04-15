from EFA_v2 import *
def hash_55():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-8660075320748474922, 1761137503298096062]
    tran0.writeAction("movir X16 34769")
    tran0.writeAction("slorii X16 X16 12 950")
    tran0.writeAction("slorii X16 X16 12 250")
    tran0.writeAction("slorii X16 X16 12 2703")
    tran0.writeAction("slorii X16 X16 12 3542")
    tran0.writeAction("movir X17 6256")
    tran0.writeAction("slorii X17 X17 12 3347")
    tran0.writeAction("slorii X17 X17 12 2676")
    tran0.writeAction("slorii X17 X17 12 2872")
    tran0.writeAction("slorii X17 X17 12 3006")
    tran0.writeAction("hash X16 X17")
    tran0.writeAction("yieldt")
    return efa
