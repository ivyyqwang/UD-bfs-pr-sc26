from EFA_v2 import *
def addi_18():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-2334663335707320270, 2883]
    tran0.writeAction("movir X16 57241")
    tran0.writeAction("slorii X16 X16 12 2497")
    tran0.writeAction("slorii X16 X16 12 213")
    tran0.writeAction("slorii X16 X16 12 150")
    tran0.writeAction("slorii X16 X16 12 50")
    tran0.writeAction("addi X16 X17 2883")
    tran0.writeAction("yieldt")
    return efa
