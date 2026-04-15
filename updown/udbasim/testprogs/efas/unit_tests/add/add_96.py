from EFA_v2 import *
def add_96():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-6828323046268650423, -3634363069604596341]
    tran0.writeAction("movir X16 41276")
    tran0.writeAction("slorii X16 X16 12 3781")
    tran0.writeAction("slorii X16 X16 12 3599")
    tran0.writeAction("slorii X16 X16 12 2227")
    tran0.writeAction("slorii X16 X16 12 3145")
    tran0.writeAction("movir X17 52624")
    tran0.writeAction("slorii X17 X17 12 608")
    tran0.writeAction("slorii X17 X17 12 2875")
    tran0.writeAction("slorii X17 X17 12 1719")
    tran0.writeAction("slorii X17 X17 12 1419")
    tran0.writeAction("add X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
