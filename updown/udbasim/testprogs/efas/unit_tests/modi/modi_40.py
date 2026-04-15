from EFA_v2 import *
def modi_40():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-2066975101800749599, 18672]
    tran0.writeAction("movir X16 58192")
    tran0.writeAction("slorii X16 X16 12 2577")
    tran0.writeAction("slorii X16 X16 12 2209")
    tran0.writeAction("slorii X16 X16 12 2414")
    tran0.writeAction("slorii X16 X16 12 1505")
    tran0.writeAction("modi X16 X17 18672")
    tran0.writeAction("yieldt")
    return efa
