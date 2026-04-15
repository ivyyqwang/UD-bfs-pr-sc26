from EFA_v2 import *
def mod_3():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5281279685044503950, -3673992139839961903]
    tran0.writeAction("movir X16 18762")
    tran0.writeAction("slorii X16 X16 12 3582")
    tran0.writeAction("slorii X16 X16 12 1122")
    tran0.writeAction("slorii X16 X16 12 2312")
    tran0.writeAction("slorii X16 X16 12 1422")
    tran0.writeAction("movir X17 52483")
    tran0.writeAction("slorii X17 X17 12 1465")
    tran0.writeAction("slorii X17 X17 12 3405")
    tran0.writeAction("slorii X17 X17 12 1072")
    tran0.writeAction("slorii X17 X17 12 1233")
    tran0.writeAction("mod X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
