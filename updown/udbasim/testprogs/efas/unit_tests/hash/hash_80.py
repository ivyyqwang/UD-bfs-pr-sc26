from EFA_v2 import *
def hash_80():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-7033327611717872904, 1949764506605685733]
    tran0.writeAction("movir X16 40548")
    tran0.writeAction("slorii X16 X16 12 2460")
    tran0.writeAction("slorii X16 X16 12 3362")
    tran0.writeAction("slorii X16 X16 12 2497")
    tran0.writeAction("slorii X16 X16 12 760")
    tran0.writeAction("movir X17 6926")
    tran0.writeAction("slorii X17 X17 12 3911")
    tran0.writeAction("slorii X17 X17 12 3339")
    tran0.writeAction("slorii X17 X17 12 3672")
    tran0.writeAction("slorii X17 X17 12 3045")
    tran0.writeAction("hash X16 X17")
    tran0.writeAction("yieldt")
    return efa
