from EFA_v2 import *
def muli_79():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6552460297314082438, -8813]
    tran0.writeAction("movir X16 23279")
    tran0.writeAction("slorii X16 X16 12 62")
    tran0.writeAction("slorii X16 X16 12 3210")
    tran0.writeAction("slorii X16 X16 12 1049")
    tran0.writeAction("slorii X16 X16 12 3718")
    tran0.writeAction("muli X16 X17 -8813")
    tran0.writeAction("yieldt")
    return efa
