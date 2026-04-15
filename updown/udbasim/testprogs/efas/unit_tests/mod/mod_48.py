from EFA_v2 import *
def mod_48():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-678563810351833790, -8738943316214275180]
    tran0.writeAction("movir X16 63125")
    tran0.writeAction("slorii X16 X16 12 1052")
    tran0.writeAction("slorii X16 X16 12 3910")
    tran0.writeAction("slorii X16 X16 12 2225")
    tran0.writeAction("slorii X16 X16 12 3394")
    tran0.writeAction("movir X17 34489")
    tran0.writeAction("slorii X17 X17 12 149")
    tran0.writeAction("slorii X17 X17 12 2772")
    tran0.writeAction("slorii X17 X17 12 3170")
    tran0.writeAction("slorii X17 X17 12 916")
    tran0.writeAction("mod X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
