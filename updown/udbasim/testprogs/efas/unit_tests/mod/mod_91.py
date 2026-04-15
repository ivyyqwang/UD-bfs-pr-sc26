from EFA_v2 import *
def mod_91():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-4565064602692776926, 1436674626992752599]
    tran0.writeAction("movir X16 49317")
    tran0.writeAction("slorii X16 X16 12 2590")
    tran0.writeAction("slorii X16 X16 12 3643")
    tran0.writeAction("slorii X16 X16 12 3224")
    tran0.writeAction("slorii X16 X16 12 3106")
    tran0.writeAction("movir X17 5104")
    tran0.writeAction("slorii X17 X17 12 383")
    tran0.writeAction("slorii X17 X17 12 1567")
    tran0.writeAction("slorii X17 X17 12 2948")
    tran0.writeAction("slorii X17 X17 12 2007")
    tran0.writeAction("mod X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
