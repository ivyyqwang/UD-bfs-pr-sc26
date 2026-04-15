from EFA_v2 import *
def mod_40():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8503433373279063366, -8431532929667566501]
    tran0.writeAction("movir X16 30210")
    tran0.writeAction("slorii X16 X16 12 1081")
    tran0.writeAction("slorii X16 X16 12 2449")
    tran0.writeAction("slorii X16 X16 12 2048")
    tran0.writeAction("slorii X16 X16 12 3398")
    tran0.writeAction("movir X17 35581")
    tran0.writeAction("slorii X17 X17 12 727")
    tran0.writeAction("slorii X17 X17 12 2303")
    tran0.writeAction("slorii X17 X17 12 639")
    tran0.writeAction("slorii X17 X17 12 1115")
    tran0.writeAction("mod X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
