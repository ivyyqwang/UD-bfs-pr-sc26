from EFA_v2 import *
def modi_42():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4991715488289288813, 8234]
    tran0.writeAction("movir X16 17734")
    tran0.writeAction("slorii X16 X16 12 556")
    tran0.writeAction("slorii X16 X16 12 2579")
    tran0.writeAction("slorii X16 X16 12 1223")
    tran0.writeAction("slorii X16 X16 12 621")
    tran0.writeAction("modi X16 X17 8234")
    tran0.writeAction("yieldt")
    return efa
