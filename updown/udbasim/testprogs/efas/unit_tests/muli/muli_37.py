from EFA_v2 import *
def muli_37():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1428642409071125264, 15416]
    tran0.writeAction("movir X16 5075")
    tran0.writeAction("slorii X16 X16 12 2283")
    tran0.writeAction("slorii X16 X16 12 935")
    tran0.writeAction("slorii X16 X16 12 3042")
    tran0.writeAction("slorii X16 X16 12 784")
    tran0.writeAction("muli X16 X17 15416")
    tran0.writeAction("yieldt")
    return efa
