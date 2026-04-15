from EFA_v2 import *
def add_92():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7294010118832369191, 4251168824070052413]
    tran0.writeAction("movir X16 25913")
    tran0.writeAction("slorii X16 X16 12 2168")
    tran0.writeAction("slorii X16 X16 12 3785")
    tran0.writeAction("slorii X16 X16 12 442")
    tran0.writeAction("slorii X16 X16 12 3623")
    tran0.writeAction("movir X17 15103")
    tran0.writeAction("slorii X17 X17 12 760")
    tran0.writeAction("slorii X17 X17 12 1430")
    tran0.writeAction("slorii X17 X17 12 3729")
    tran0.writeAction("slorii X17 X17 12 2621")
    tran0.writeAction("add X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
