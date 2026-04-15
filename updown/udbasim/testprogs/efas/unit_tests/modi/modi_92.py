from EFA_v2 import *
def modi_92():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-8309642913895777559, 26106]
    tran0.writeAction("movir X16 36014")
    tran0.writeAction("slorii X16 X16 12 892")
    tran0.writeAction("slorii X16 X16 12 3026")
    tran0.writeAction("slorii X16 X16 12 3687")
    tran0.writeAction("slorii X16 X16 12 2793")
    tran0.writeAction("modi X16 X17 26106")
    tran0.writeAction("yieldt")
    return efa
