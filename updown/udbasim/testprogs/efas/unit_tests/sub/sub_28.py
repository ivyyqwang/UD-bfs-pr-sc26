from EFA_v2 import *
def sub_28():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [9047801043750428274, -806588789201023034]
    tran0.writeAction("movir X16 32144")
    tran0.writeAction("slorii X16 X16 12 1009")
    tran0.writeAction("slorii X16 X16 12 3243")
    tran0.writeAction("slorii X16 X16 12 625")
    tran0.writeAction("slorii X16 X16 12 3698")
    tran0.writeAction("movir X17 62670")
    tran0.writeAction("slorii X17 X17 12 1724")
    tran0.writeAction("slorii X17 X17 12 1291")
    tran0.writeAction("slorii X17 X17 12 3524")
    tran0.writeAction("slorii X17 X17 12 4038")
    tran0.writeAction("sub X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
