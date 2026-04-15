from EFA_v2 import *
def subi_31():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-6233175844404273569, 18455]
    tran0.writeAction("movir X16 43391")
    tran0.writeAction("slorii X16 X16 12 1273")
    tran0.writeAction("slorii X16 X16 12 2083")
    tran0.writeAction("slorii X16 X16 12 3021")
    tran0.writeAction("slorii X16 X16 12 3679")
    tran0.writeAction("subi X16 X17 18455")
    tran0.writeAction("yieldt")
    return efa
