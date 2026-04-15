from EFA_v2 import *
def modi_60():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-8452452758042785105, -19896]
    tran0.writeAction("movir X16 35506")
    tran0.writeAction("slorii X16 X16 12 3503")
    tran0.writeAction("slorii X16 X16 12 4068")
    tran0.writeAction("slorii X16 X16 12 364")
    tran0.writeAction("slorii X16 X16 12 2735")
    tran0.writeAction("modi X16 X17 -19896")
    tran0.writeAction("yieldt")
    return efa
