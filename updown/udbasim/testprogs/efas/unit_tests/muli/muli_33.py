from EFA_v2 import *
def muli_33():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6182840083703072245, 27804]
    tran0.writeAction("movir X16 21965")
    tran0.writeAction("slorii X16 X16 12 3524")
    tran0.writeAction("slorii X16 X16 12 3148")
    tran0.writeAction("slorii X16 X16 12 688")
    tran0.writeAction("slorii X16 X16 12 1525")
    tran0.writeAction("muli X16 X17 27804")
    tran0.writeAction("yieldt")
    return efa
