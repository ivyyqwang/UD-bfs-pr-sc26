from EFA_v2 import *
def divi_75():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-7509546811606031318, -8035]
    tran0.writeAction("movir X16 38856")
    tran0.writeAction("slorii X16 X16 12 2991")
    tran0.writeAction("slorii X16 X16 12 1614")
    tran0.writeAction("slorii X16 X16 12 226")
    tran0.writeAction("slorii X16 X16 12 1066")
    tran0.writeAction("divi X16 X17 -8035")
    tran0.writeAction("yieldt")
    return efa
