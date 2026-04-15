from EFA_v2 import *
def hash_23():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-8195191185272329136, 8268216224577024898]
    tran0.writeAction("movir X16 36420")
    tran0.writeAction("slorii X16 X16 12 3408")
    tran0.writeAction("slorii X16 X16 12 2423")
    tran0.writeAction("slorii X16 X16 12 1762")
    tran0.writeAction("slorii X16 X16 12 3152")
    tran0.writeAction("movir X17 29374")
    tran0.writeAction("slorii X17 X17 12 2477")
    tran0.writeAction("slorii X17 X17 12 2416")
    tran0.writeAction("slorii X17 X17 12 143")
    tran0.writeAction("slorii X17 X17 12 898")
    tran0.writeAction("hash X16 X17")
    tran0.writeAction("yieldt")
    return efa
