from EFA_v2 import *
def add_46():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-7327960270302429396, -6692678701054093799]
    tran0.writeAction("movir X16 39501")
    tran0.writeAction("slorii X16 X16 12 3503")
    tran0.writeAction("slorii X16 X16 12 1432")
    tran0.writeAction("slorii X16 X16 12 1835")
    tran0.writeAction("slorii X16 X16 12 3884")
    tran0.writeAction("movir X17 41758")
    tran0.writeAction("slorii X17 X17 12 3394")
    tran0.writeAction("slorii X17 X17 12 3651")
    tran0.writeAction("slorii X17 X17 12 3473")
    tran0.writeAction("slorii X17 X17 12 1561")
    tran0.writeAction("add X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
