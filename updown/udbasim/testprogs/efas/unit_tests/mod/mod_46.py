from EFA_v2 import *
def mod_46():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6371533294290961098, 9102977436083608575]
    tran0.writeAction("movir X16 22636")
    tran0.writeAction("slorii X16 X16 12 956")
    tran0.writeAction("slorii X16 X16 12 1528")
    tran0.writeAction("slorii X16 X16 12 3224")
    tran0.writeAction("slorii X16 X16 12 714")
    tran0.writeAction("movir X17 32340")
    tran0.writeAction("slorii X17 X17 12 1115")
    tran0.writeAction("slorii X17 X17 12 3996")
    tran0.writeAction("slorii X17 X17 12 653")
    tran0.writeAction("slorii X17 X17 12 3071")
    tran0.writeAction("mod X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
