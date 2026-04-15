from EFA_v2 import *
def add_45():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1737346686978128844, -3204304560934169635]
    tran0.writeAction("movir X16 59363")
    tran0.writeAction("slorii X16 X16 12 2886")
    tran0.writeAction("slorii X16 X16 12 1182")
    tran0.writeAction("slorii X16 X16 12 3960")
    tran0.writeAction("slorii X16 X16 12 1076")
    tran0.writeAction("movir X17 54152")
    tran0.writeAction("slorii X17 X17 12 95")
    tran0.writeAction("slorii X17 X17 12 2717")
    tran0.writeAction("slorii X17 X17 12 1453")
    tran0.writeAction("slorii X17 X17 12 989")
    tran0.writeAction("add X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
