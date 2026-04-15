from EFA_v2 import *
def muli_97():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-6892820920167099918, -25336]
    tran0.writeAction("movir X16 41047")
    tran0.writeAction("slorii X16 X16 12 3198")
    tran0.writeAction("slorii X16 X16 12 1169")
    tran0.writeAction("slorii X16 X16 12 241")
    tran0.writeAction("slorii X16 X16 12 498")
    tran0.writeAction("muli X16 X17 -25336")
    tran0.writeAction("yieldt")
    return efa
