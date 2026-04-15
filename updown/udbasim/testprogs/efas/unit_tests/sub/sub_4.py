from EFA_v2 import *
def sub_4():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [9017890459290266470, 5796810927878205533]
    tran0.writeAction("movir X16 32037")
    tran0.writeAction("slorii X16 X16 12 4025")
    tran0.writeAction("slorii X16 X16 12 2057")
    tran0.writeAction("slorii X16 X16 12 1558")
    tran0.writeAction("slorii X16 X16 12 2918")
    tran0.writeAction("movir X17 20594")
    tran0.writeAction("slorii X17 X17 12 1677")
    tran0.writeAction("slorii X17 X17 12 890")
    tran0.writeAction("slorii X17 X17 12 1159")
    tran0.writeAction("slorii X17 X17 12 93")
    tran0.writeAction("sub X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
