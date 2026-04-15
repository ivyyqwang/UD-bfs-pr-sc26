from EFA_v2 import *
def modi_5():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [9135156443757938790, -9444]
    tran0.writeAction("movir X16 32454")
    tran0.writeAction("slorii X16 X16 12 2438")
    tran0.writeAction("slorii X16 X16 12 685")
    tran0.writeAction("slorii X16 X16 12 3328")
    tran0.writeAction("slorii X16 X16 12 2150")
    tran0.writeAction("modi X16 X17 -9444")
    tran0.writeAction("yieldt")
    return efa
