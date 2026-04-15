from EFA_v2 import *
def modi_52():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4222514530758228573, 12611]
    tran0.writeAction("movir X16 15001")
    tran0.writeAction("slorii X16 X16 12 1577")
    tran0.writeAction("slorii X16 X16 12 2056")
    tran0.writeAction("slorii X16 X16 12 3151")
    tran0.writeAction("slorii X16 X16 12 2653")
    tran0.writeAction("modi X16 X17 12611")
    tran0.writeAction("yieldt")
    return efa
