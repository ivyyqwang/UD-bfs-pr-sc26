from EFA_v2 import *
def add_66():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-424256324239702801, -7233301293014333224]
    tran0.writeAction("movir X16 64028")
    tran0.writeAction("slorii X16 X16 12 3025")
    tran0.writeAction("slorii X16 X16 12 3827")
    tran0.writeAction("slorii X16 X16 12 4012")
    tran0.writeAction("slorii X16 X16 12 1263")
    tran0.writeAction("movir X17 39838")
    tran0.writeAction("slorii X17 X17 12 620")
    tran0.writeAction("slorii X17 X17 12 3124")
    tran0.writeAction("slorii X17 X17 12 2076")
    tran0.writeAction("slorii X17 X17 12 2264")
    tran0.writeAction("add X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
