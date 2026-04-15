from EFA_v2 import *
def modi_36():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7156871001947107242, 21009]
    tran0.writeAction("movir X16 25426")
    tran0.writeAction("slorii X16 X16 12 1284")
    tran0.writeAction("slorii X16 X16 12 494")
    tran0.writeAction("slorii X16 X16 12 1438")
    tran0.writeAction("slorii X16 X16 12 4010")
    tran0.writeAction("modi X16 X17 21009")
    tran0.writeAction("yieldt")
    return efa
