from EFA_v2 import *
def add_94():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [852375700527308918, -3449843940193375040]
    tran0.writeAction("movir X16 3028")
    tran0.writeAction("slorii X16 X16 12 1010")
    tran0.writeAction("slorii X16 X16 12 3837")
    tran0.writeAction("slorii X16 X16 12 430")
    tran0.writeAction("slorii X16 X16 12 118")
    tran0.writeAction("movir X17 53279")
    tran0.writeAction("slorii X17 X17 12 2835")
    tran0.writeAction("slorii X17 X17 12 1766")
    tran0.writeAction("slorii X17 X17 12 982")
    tran0.writeAction("slorii X17 X17 12 3264")
    tran0.writeAction("add X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
