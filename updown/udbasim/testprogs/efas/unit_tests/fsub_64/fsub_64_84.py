from EFA_v2 import *
def fsub_64_84():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [13885527863452761910, 15759815248084527162]
    tran0.writeAction("movir X16 49331")
    tran0.writeAction("slorii X16 X16 12 1248")
    tran0.writeAction("slorii X16 X16 12 1515")
    tran0.writeAction("slorii X16 X16 12 3647")
    tran0.writeAction("slorii X16 X16 12 3894")
    tran0.writeAction("movir X17 55990")
    tran0.writeAction("slorii X17 X17 12 455")
    tran0.writeAction("slorii X17 X17 12 2067")
    tran0.writeAction("slorii X17 X17 12 3534")
    tran0.writeAction("slorii X17 X17 12 2106")
    tran0.writeAction("fsub.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
