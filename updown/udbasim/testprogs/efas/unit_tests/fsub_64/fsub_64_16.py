from EFA_v2 import *
def fsub_64_16():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [12985566933525041738, 3169316158507740572]
    tran0.writeAction("movir X16 46134")
    tran0.writeAction("slorii X16 X16 12 5")
    tran0.writeAction("slorii X16 X16 12 855")
    tran0.writeAction("slorii X16 X16 12 3353")
    tran0.writeAction("slorii X16 X16 12 586")
    tran0.writeAction("movir X17 11259")
    tran0.writeAction("slorii X17 X17 12 2756")
    tran0.writeAction("slorii X17 X17 12 288")
    tran0.writeAction("slorii X17 X17 12 3110")
    tran0.writeAction("slorii X17 X17 12 3484")
    tran0.writeAction("fsub.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
