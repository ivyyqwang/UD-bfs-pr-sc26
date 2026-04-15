from EFA_v2 import *
def modi_47():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2591275429611489020, 24880]
    tran0.writeAction("movir X16 9206")
    tran0.writeAction("slorii X16 X16 12 244")
    tran0.writeAction("slorii X16 X16 12 1577")
    tran0.writeAction("slorii X16 X16 12 780")
    tran0.writeAction("slorii X16 X16 12 1788")
    tran0.writeAction("modi X16 X17 24880")
    tran0.writeAction("yieldt")
    return efa
