from EFA_v2 import *
def muli_21():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4274790200057205236, -20263]
    tran0.writeAction("movir X16 15187")
    tran0.writeAction("slorii X16 X16 12 432")
    tran0.writeAction("slorii X16 X16 12 2499")
    tran0.writeAction("slorii X16 X16 12 2993")
    tran0.writeAction("slorii X16 X16 12 500")
    tran0.writeAction("muli X16 X17 -20263")
    tran0.writeAction("yieldt")
    return efa
