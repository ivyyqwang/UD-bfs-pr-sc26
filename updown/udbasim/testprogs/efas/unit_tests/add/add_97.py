from EFA_v2 import *
def add_97():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1538435291153569381, -550099147912864771]
    tran0.writeAction("movir X16 5465")
    tran0.writeAction("slorii X16 X16 12 2539")
    tran0.writeAction("slorii X16 X16 12 3855")
    tran0.writeAction("slorii X16 X16 12 545")
    tran0.writeAction("slorii X16 X16 12 1637")
    tran0.writeAction("movir X17 63581")
    tran0.writeAction("slorii X17 X17 12 2683")
    tran0.writeAction("slorii X17 X17 12 3409")
    tran0.writeAction("slorii X17 X17 12 1673")
    tran0.writeAction("slorii X17 X17 12 3069")
    tran0.writeAction("add X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
