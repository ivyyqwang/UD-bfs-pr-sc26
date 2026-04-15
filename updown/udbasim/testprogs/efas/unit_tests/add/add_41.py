from EFA_v2 import *
def add_41():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7401201999410080379, 6521647528909796307]
    tran0.writeAction("movir X16 26294")
    tran0.writeAction("slorii X16 X16 12 1440")
    tran0.writeAction("slorii X16 X16 12 341")
    tran0.writeAction("slorii X16 X16 12 3066")
    tran0.writeAction("slorii X16 X16 12 2683")
    tran0.writeAction("movir X17 23169")
    tran0.writeAction("slorii X17 X17 12 2237")
    tran0.writeAction("slorii X17 X17 12 4054")
    tran0.writeAction("slorii X17 X17 12 3983")
    tran0.writeAction("slorii X17 X17 12 979")
    tran0.writeAction("add X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
