from EFA_v2 import *
def add_81():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4404781323324716857, 4651244800559349230]
    tran0.writeAction("movir X16 15648")
    tran0.writeAction("slorii X16 X16 12 3796")
    tran0.writeAction("slorii X16 X16 12 1706")
    tran0.writeAction("slorii X16 X16 12 183")
    tran0.writeAction("slorii X16 X16 12 1849")
    tran0.writeAction("movir X17 16524")
    tran0.writeAction("slorii X17 X17 12 2216")
    tran0.writeAction("slorii X17 X17 12 180")
    tran0.writeAction("slorii X17 X17 12 2959")
    tran0.writeAction("slorii X17 X17 12 3566")
    tran0.writeAction("add X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
