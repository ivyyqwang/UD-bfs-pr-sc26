from EFA_v2 import *
def divi_2():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-2469699590211284592, -31860]
    tran0.writeAction("movir X16 56761")
    tran0.writeAction("slorii X16 X16 12 3540")
    tran0.writeAction("slorii X16 X16 12 3783")
    tran0.writeAction("slorii X16 X16 12 2165")
    tran0.writeAction("slorii X16 X16 12 400")
    tran0.writeAction("divi X16 X17 -31860")
    tran0.writeAction("yieldt")
    return efa
