from EFA_v2 import *
def div_8():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-7510964032595778387, 4360011971106184414]
    tran0.writeAction("movir X16 38851")
    tran0.writeAction("slorii X16 X16 12 2848")
    tran0.writeAction("slorii X16 X16 12 468")
    tran0.writeAction("slorii X16 X16 12 1610")
    tran0.writeAction("slorii X16 X16 12 1197")
    tran0.writeAction("movir X17 15489")
    tran0.writeAction("slorii X17 X17 12 3580")
    tran0.writeAction("slorii X17 X17 12 2450")
    tran0.writeAction("slorii X17 X17 12 961")
    tran0.writeAction("slorii X17 X17 12 3294")
    tran0.writeAction("div X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
