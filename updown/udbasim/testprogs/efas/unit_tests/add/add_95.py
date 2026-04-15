from EFA_v2 import *
def add_95():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7309170325626187445, 3913803540004161240]
    tran0.writeAction("movir X16 25967")
    tran0.writeAction("slorii X16 X16 12 1594")
    tran0.writeAction("slorii X16 X16 12 3965")
    tran0.writeAction("slorii X16 X16 12 3174")
    tran0.writeAction("slorii X16 X16 12 3765")
    tran0.writeAction("movir X17 13904")
    tran0.writeAction("slorii X17 X17 12 2553")
    tran0.writeAction("slorii X17 X17 12 1370")
    tran0.writeAction("slorii X17 X17 12 2516")
    tran0.writeAction("slorii X17 X17 12 1752")
    tran0.writeAction("add X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
