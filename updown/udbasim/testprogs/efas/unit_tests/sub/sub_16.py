from EFA_v2 import *
def sub_16():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6637979863911832499, 6273572087703276443]
    tran0.writeAction("movir X16 23582")
    tran0.writeAction("slorii X16 X16 12 3448")
    tran0.writeAction("slorii X16 X16 12 1094")
    tran0.writeAction("slorii X16 X16 12 2705")
    tran0.writeAction("slorii X16 X16 12 2995")
    tran0.writeAction("movir X17 22288")
    tran0.writeAction("slorii X17 X17 12 841")
    tran0.writeAction("slorii X17 X17 12 816")
    tran0.writeAction("slorii X17 X17 12 1472")
    tran0.writeAction("slorii X17 X17 12 2971")
    tran0.writeAction("sub X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
