from EFA_v2 import *
def hash_53():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1085866875945053289, -606853868723231018]
    tran0.writeAction("movir X16 61678")
    tran0.writeAction("slorii X16 X16 12 925")
    tran0.writeAction("slorii X16 X16 12 1113")
    tran0.writeAction("slorii X16 X16 12 3817")
    tran0.writeAction("slorii X16 X16 12 919")
    tran0.writeAction("movir X17 63380")
    tran0.writeAction("slorii X17 X17 12 89")
    tran0.writeAction("slorii X17 X17 12 3876")
    tran0.writeAction("slorii X17 X17 12 738")
    tran0.writeAction("slorii X17 X17 12 1750")
    tran0.writeAction("hash X16 X17")
    tran0.writeAction("yieldt")
    return efa
