from EFA_v2 import *
def modi_99():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8442557517192750960, 14809]
    tran0.writeAction("movir X16 29993")
    tran0.writeAction("slorii X16 X16 12 4053")
    tran0.writeAction("slorii X16 X16 12 1232")
    tran0.writeAction("slorii X16 X16 12 318")
    tran0.writeAction("slorii X16 X16 12 1904")
    tran0.writeAction("modi X16 X17 14809")
    tran0.writeAction("yieldt")
    return efa
