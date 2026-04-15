from EFA_v2 import *
def add_7():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8072888400759001488, 4791481038884785060]
    tran0.writeAction("movir X16 28680")
    tran0.writeAction("slorii X16 X16 12 2707")
    tran0.writeAction("slorii X16 X16 12 2686")
    tran0.writeAction("slorii X16 X16 12 2505")
    tran0.writeAction("slorii X16 X16 12 400")
    tran0.writeAction("movir X17 17022")
    tran0.writeAction("slorii X17 X17 12 3113")
    tran0.writeAction("slorii X17 X17 12 3670")
    tran0.writeAction("slorii X17 X17 12 3060")
    tran0.writeAction("slorii X17 X17 12 2980")
    tran0.writeAction("add X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
